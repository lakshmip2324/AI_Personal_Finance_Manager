from agents.manager_agent import manager_agent
from tools.expense_tools import analyze_expenses
from agents.budget_agent import budget_agent
from agents.savings_agent import savings_agent


expense_data = analyze_expenses("data/transactions.csv")

budget_data = budget_agent(
    expense_data,
    budget_limit=20000
)

savings_data = savings_agent(
    expense_data
)

result = manager_agent(
    expense_data,
    budget_data,
    savings_data
)

print("\n===== AI MANAGER AGENT =====")
print(result["decision"])