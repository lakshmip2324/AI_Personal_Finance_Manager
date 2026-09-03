def manager_agent(expense_data, budget_data, savings_data):

    budget_status = budget_data["status"]
    savings_percentage = savings_data["savings_percentage"]

    if budget_status == "Over Budget":
        decision = "budget"

    elif savings_percentage < 20:
        decision = "savings"

    else:
        decision = "advisor"

    return {
        "decision": decision
    }