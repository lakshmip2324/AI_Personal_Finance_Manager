from graph.finance_graph import finance_graph


# Input state
initial_state = {
    "file_path": "data/transactions.csv",
    "budget_limit": 20000
}


# Run the complete agentic workflow
result = finance_graph.invoke(initial_state)

# Get final report
report = result["report"]

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