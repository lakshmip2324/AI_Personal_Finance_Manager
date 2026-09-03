from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from tools.expense_tools import analyze_expenses
from agents.budget_agent import budget_agent
from agents.savings_agent import savings_agent
from agents.advisor_agent import advisor_agent
from agents.manager_agent import manager_agent
from agents.report_agent import report_agent


class FinanceState(TypedDict):
    file_path: str
    budget_limit: float
    expense_data: dict
    budget_data: dict
    savings_data: dict
    manager_data: dict
    advisor_data: dict
    report: dict


# Expense Analysis Node
def expense_node(state):

    expense_data = analyze_expenses(
        state["file_path"]
    )

    return {
        "expense_data": expense_data
    }


# Manager Agent Node
def manager_node(state):

    budget_data = budget_agent(
        state["expense_data"],
        budget_limit=state["budget_limit"]
    )

    savings_data = savings_agent(
        state["expense_data"]
    )

    manager_data = manager_agent(
        state["expense_data"],
        budget_data,
        savings_data
    )

    return {
        "budget_data": budget_data,
        "savings_data": savings_data,
        "manager_data": manager_data
    }


# Budget Agent Node
def budget_node(state):

    budget_data = budget_agent(
        state["expense_data"],
        budget_limit=state["budget_limit"]
    )

    return {
        "budget_data": budget_data
    }


# Savings Agent Node
def savings_node(state):

    savings_data = savings_agent(
        state["expense_data"]
    )

    return {
        "savings_data": savings_data
    }


# Advisor Agent Node
def advisor_node(state):

    advisor_data = advisor_agent(
        state["expense_data"],
        state["budget_data"],
        state["savings_data"]
    )

    return {
        "advisor_data": advisor_data
    }


# Report Agent Node
def report_node(state):

    report = report_agent(
        state["expense_data"],
        state["budget_data"],
        state["savings_data"],
        state["advisor_data"]
    )

    return {
        "report": report
    }


# Manager routing function
def route_manager(state):

    decision = state["manager_data"]["decision"]

    return decision


# Create graph
graph_builder = StateGraph(FinanceState)


# Add nodes
graph_builder.add_node(
    "expense_analysis",
    expense_node
)

graph_builder.add_node(
    "manager_agent",
    manager_node
)

graph_builder.add_node(
    "budget_agent",
    budget_node
)

graph_builder.add_node(
    "savings_agent",
    savings_node
)

graph_builder.add_node(
    "advisor_agent",
    advisor_node
)

graph_builder.add_node(
    "report_agent",
    report_node
)


# Start → Expense Analysis
graph_builder.add_edge(
    START,
    "expense_analysis"
)


# Expense Analysis → Manager
graph_builder.add_edge(
    "expense_analysis",
    "manager_agent"
)


# Manager → Conditional Route
graph_builder.add_conditional_edges(
    "manager_agent",
    route_manager,
    {
        "budget": "budget_agent",
        "savings": "savings_agent",
        "advisor": "advisor_agent"
    }
)


# Budget → Advisor
graph_builder.add_edge(
    "budget_agent",
    "advisor_agent"
)


# Savings → Advisor
graph_builder.add_edge(
    "savings_agent",
    "advisor_agent"
)


# Advisor → Report
graph_builder.add_edge(
    "advisor_agent",
    "report_agent"
)


# Report → End
graph_builder.add_edge(
    "report_agent",
    END
)


# Compile graph
finance_graph = graph_builder.compile()