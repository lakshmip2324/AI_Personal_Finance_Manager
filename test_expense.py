from tools.expense_tools import analyze_expenses


file_path = "data/transactions.csv"

result = analyze_expenses(file_path)

print("Income:", result["income"])
print("Expenses:", result["expenses"])
print("Savings:", result["savings"])

print("\nSpending by Category:")

for category, amount in result["category_summary"].items():
    print(category, ":", amount)

print("\nHighest Spending Category:")
print(result["highest_category"], "-", result["highest_amount"])