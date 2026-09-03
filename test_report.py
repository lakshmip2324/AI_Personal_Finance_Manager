from tools.expense_tools import analyze_expenses
from agents.budget_agent import budget_agent
from agents.savings_agent import savings_agent
from agents.advisor_agent import advisor_agent
from agents.report_agent import report_agent


# Analyze expenses
file_path = "data/transactions.csv"
expense_data = analyze_expenses(file_path)

# Run agents
budget_data = budget_agent(expense_data, budget_limit=20000)
savings_data = savings_agent(expense_data)

# Run AI advisor agent
advisor_data = advisor_agent(
    expense_data,
    budget_data,
    savings_data
)

# Generate report
report = report_agent(
    expense_data,
    budget_data,
    savings_data,
    advisor_data
)

print("\n===== AI PERSONAL FINANCE REPORT =====")

print("Income:", report["income"])
print("Total Expenses:", report["total_expenses"])
print("Savings:", report["savings"])
print("Savings Percentage:", report["savings_percentage"], "%")
print("Budget Status:", report["budget_status"])
print("Budget Limit:", report["budget_limit"])
print("Highest Spending Category:", report["highest_category"])
print("Highest Category Amount:", report["highest_category_amount"])

print("\n===== AI FINANCIAL ADVICE =====")
print(report["advice"])