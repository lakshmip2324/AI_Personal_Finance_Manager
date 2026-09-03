def report_agent(expense_data, budget_data, savings_data, advisor_data):

    report = {
        "income": expense_data["income"],
        "total_expenses": expense_data["expenses"],
        "savings": expense_data["savings"],
        "savings_percentage": savings_data["savings_percentage"],
        "budget_status": budget_data["status"],
        "budget_limit": budget_data["budget_limit"],
        "highest_category": expense_data["highest_category"],
        "highest_category_amount": expense_data["highest_amount"],
        "advice": advisor_data["advice"]
    }

    return report