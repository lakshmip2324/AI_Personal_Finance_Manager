from tools.expense_tools import analyze_expenses
from agents.budget_agent import budget_agent


# Analyze expenses
file_path = "data/transactions.csv"
expense_data = analyze_expenses(file_path)

# Run budget agent
result = budget_agent(expense_data, budget_limit=20000)

print("Budget Status:", result["status"])
print("Budget Limit:", result["budget_limit"])
print("Total Expenses:", result["total_expenses"])
print("Savings:", result["savings"])
print("Highest Spending Category:", result["highest_category"])
print("Highest Category Amount:", result["highest_amount"])
print("Message:", result["message"])