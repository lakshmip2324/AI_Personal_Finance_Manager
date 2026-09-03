from tools.expense_tools import analyze_expenses
from agents.budget_agent import budget_agent
from agents.savings_agent import savings_agent
from agents.advisor_agent import advisor_agent


# Analyze expenses
file_path = "data/transactions.csv"
expense_data = analyze_expenses(file_path)

# Run budget agent
budget_data = budget_agent(expense_data, budget_limit=20000)

# Run savings agent
savings_data = savings_agent(expense_data)

# Run AI advisor agent
result = advisor_agent(
    expense_data,
    budget_data,
    savings_data
)

print("\n===== AI FINANCIAL ADVICE =====")
print(result["advice"])

print("\nSavings Percentage:", result["savings_percentage"], "%")
print("Highest Spending Category:", result["highest_category"])
print("Highest Category Amount:", result["highest_amount"])