def budget_agent(expense_data, budget_limit=20000):

    expenses = expense_data["expenses"]
    savings = expense_data["savings"]
    highest_category = expense_data["highest_category"]
    highest_amount = expense_data["highest_amount"]

    if expenses > budget_limit:
        status = "Over Budget"
        message = (
            f"You have exceeded your monthly budget by "
            f"₹{expenses - budget_limit}."
        )

    else:
        status = "Within Budget"
        message = (
            f"You are within your monthly budget with "
            f"₹{budget_limit - expenses} remaining."
        )

    return {
        "status": status,
        "budget_limit": budget_limit,
        "total_expenses": expenses,
        "savings": savings,
        "highest_category": highest_category,
        "highest_amount": highest_amount,
        "message": message
    }