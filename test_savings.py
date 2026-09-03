from tools.expense_tools import analyze_expenses
from agents.savings_agent import savings_agent


# Analyze expenses
file_path = "data/transactions.csv"
expense_data = analyze_expenses(file_path)

# Run savings agent
result = savings_agent(expense_data)

print("Income:", result["income"])
print("Expenses:", result["expenses"])
print("Savings:", result["savings"])
print("Savings Percentage:", result["savings_percentage"], "%")
print("Advice:", result["advice"])