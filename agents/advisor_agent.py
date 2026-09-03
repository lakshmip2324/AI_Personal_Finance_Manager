from utils.llm import llm


def advisor_agent(expense_data, budget_data, savings_data):

    income = expense_data["income"]
    expenses = expense_data["expenses"]
    savings = expense_data["savings"]
    highest_category = expense_data["highest_category"]
    highest_amount = expense_data["highest_amount"]

    budget_status = budget_data["status"]
    savings_percentage = savings_data["savings_percentage"]

    prompt = f"""
You are a personal finance advisor.

Analyze the following monthly financial information:

Income: ₹{income}
Total Expenses: ₹{expenses}
Savings: ₹{savings}
Savings Percentage: {savings_percentage}%
Budget Status: {budget_status}
Highest Spending Category: {highest_category}
Highest Category Amount: ₹{highest_amount}

Give 3 short and practical financial suggestions.
Focus on reducing unnecessary expenses, improving savings,
and managing the highest spending category.

Do not give investment advice.
Keep the response simple and easy to understand.
"""

    response = llm.invoke(prompt)

    return {
        "advice": response.content,
        "savings_percentage": savings_percentage,
        "highest_category": highest_category,
        "highest_amount": highest_amount
    }