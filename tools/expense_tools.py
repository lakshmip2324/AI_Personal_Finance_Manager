import pandas as pd


def analyze_expenses(file_path):

    # Load transaction data
    df = pd.read_csv(file_path)

    # Calculate income
    income = df[df["type"] == "Income"]["amount"].sum()

    # Calculate expenses
    expenses = df[df["type"] == "Expense"]["amount"].sum()

    # Calculate savings
    savings = income - expenses

    # Calculate spending by category
    expense_data = df[df["type"] == "Expense"]

    category_summary = (
        expense_data.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    # Find highest spending category
    if not category_summary.empty:
        highest_category = category_summary.index[0]
        highest_amount = category_summary.iloc[0]
    else:
        highest_category = "None"
        highest_amount = 0

    return {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "category_summary": category_summary.to_dict(),
        "highest_category": highest_category,
        "highest_amount": highest_amount
    }