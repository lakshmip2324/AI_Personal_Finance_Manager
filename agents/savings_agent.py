def savings_agent(expense_data):

    income = expense_data["income"]
    expenses = expense_data["expenses"]
    savings = expense_data["savings"]

    if income > 0:
        savings_percentage = (savings / income) * 100
    else:
        savings_percentage = 0

    if savings_percentage >= 30:
        advice = "Excellent! You are saving a good portion of your income."

    elif savings_percentage >= 20:
        advice = "Good savings. Try to increase your savings gradually."

    else:
        advice = "Your savings are low. Consider reducing unnecessary expenses."

    return {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "savings_percentage": round(savings_percentage, 2),
        "advice": advice
    }