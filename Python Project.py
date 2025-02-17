# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I21_ebm32jO685lJV_iMk_PkZ_7nprIk
"""

## **Project Title: Personal Expense Tracker**
### **1. User Input and Dat
import pandas as pd
import os

# File name for storing expenses
file_name = "/content/personal_expenses.csv"

# Initialize CSV file if it doesn't exist
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(file_name, index=False)

# Function to add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Rent): ")
    amount = input("Enter the amount: ")
    description = input("Enter a description: ")
    new_entry = {"Date": date, "Category": category, "Amount": float(amount), "Description": description}

    df = pd.read_csv(file_name)
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(file_name, index=False)
    print("Expense added successfully!")
#### **2. Expense Summary and Analysis**

# Function to generate summary and analysis
def expense_summary():
    df = pd.read_csv(file_name)

    # Group expenses by category and calculate total
    print("\nCategory-wise Expenses:")
    category_totals = df.groupby('Category')['Amount'].sum()
    print(category_totals)

    # Analyze monthly total expenses
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_totals = df.groupby('Month')['Amount'].sum()
    print("\nMonthly Total Expenses:")
    print(monthly_totals)

    # Average daily expense
    total_days = (df['Date'].max() - df['Date'].min()).days + 1
    total_expenses = df['Amount'].sum()
    average_daily_expense = total_expenses / total_days
    print(f"\nAverage Daily Expense: {round(average_daily_expense, 2)}")
#### **3. Visualization**
import matplotlib.pyplot as plt

# Function to visualize expenses
def visualize_expenses():
    df = pd.read_csv(file_name)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    # Pie chart: Expenses by category
    category_totals = df.groupby('Category')['Amount'].sum()
    category_totals.plot.pie(autopct='%1.1f%%', startangle=140, title="Category-wise Expenses")
    plt.show()

    # Bar chart: Monthly expenses
    monthly_totals = df.groupby('Month')['Amount'].sum()
    monthly_totals.plot.bar(color='skyblue', title="Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.xticks(rotation=45)
    plt.show()

    # Line graph: Daily expenses for a selected month
    selected_month = input("Enter a month to view daily expenses (e.g., 2024-01): ")
    daily_expenses = df[df['Date'].dt.to_period('M') == selected_month].groupby('Date')['Amount'].sum()
    daily_expenses.plot.line(marker='o', title=f"Daily Expenses for {selected_month}")
    plt.xlabel("Date")
    plt.ylabel("Expense")
    plt.grid()
    plt.show()
#### **4. Applying Functions and Logic**
# Function to delete an expense
def delete_expense():
    df = pd.read_csv(file_name)
    choice = input("Delete by (1) ID or (2) Description? Enter 1 or 2: ")
    if choice == "1":
        entry_id = int(input("Enter the ID of the entry to delete: "))
        if entry_id in df.index:
            print(f"Deleting entry:\n{df.iloc[entry_id]}")
            df = df.drop(index=entry_id).reset_index(drop=True)
        else:
            print("Invalid ID.")
    elif choice == "2":
        description = input("Enter a keyword from the description to delete: ")
        matches = df[df['Description'].str.contains(description, case=False)]
        if not matches.empty:
            print(f"Deleting entries matching '{description}':\n{matches}")
            df = df[~df['Description'].str.contains(description, case=False)].reset_index(drop=True)
        else:
            print("No matches found.")
    else:
        print("Invalid choice.")
    df.to_csv(file_name, index=False)
    print("Expense deleted successfully!")

#### **5. Advanced Features
import re

# Validate date input
def validate_date(date):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

# Handle invalid input
try:
    date = input("Enter a date (YYYY-MM-DD): ")
    validate_date(date)
    print("Date is valid!")
except ValueError as e:
    print(e)
#### **6. User Interaction**
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add a new expense")
        print("2. Delete an expense")
        print("3. View expense summaries")
        print("4. Visualize expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            delete_expense()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            visualize_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
#### **7. Using NumPy for Statistical Analysis**
import numpy as np

# Function to calculate statistical measures
def calculate_statistics():
    df = pd.read_csv(file_name)
    expenses = df['Amount'].values
    print("\nStatistics:")
    print(f"Highest Expense: {np.max(expenses)}")
    print(f"Lowest Expense: {np.min(expenses)}")
    print(f"Average Expense: {np.mean(expenses):.2f}")
    print(f"Total Expense: {np.sum(expenses)}")
if __name__ == "__main__":
    print("Welcome to Personal Expense Tracker!")
    main_menu()

