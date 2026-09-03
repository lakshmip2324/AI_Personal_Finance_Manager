import streamlit as st
import pandas as pd
import tempfile

from graph.finance_graph import finance_graph


# Page configuration
st.set_page_config(
    page_title="AI Personal Finance Manager",
    page_icon="💰",
    layout="wide"
)


# Header
st.title("💰 AI Personal Finance Manager")
st.write(
    "Analyze your spending, track your budget, and receive "
    "AI-powered financial insights."
)

st.divider()


# Sidebar
st.sidebar.header("⚙️ Finance Settings")

budget_limit = st.sidebar.number_input(
    "Monthly Budget (₹)",
    min_value=0,
    value=20000,
    step=1000
)

st.sidebar.info(
    "Upload a CSV file containing your transaction details."
)


# File upload
uploaded_file = st.file_uploader(
    "📂 Upload Transactions CSV",
    type=["csv"]
)


if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Transaction Data")
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # Save temporary CSV
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    ) as temp_file:

        df.to_csv(
            temp_file.name,
            index=False
        )

        file_path = temp_file.name

    st.divider()

    # Analyze button
    if st.button(
        "🔍 Analyze My Finances",
        use_container_width=True
    ):

        with st.spinner(
            "🤖 AI is analyzing your finances..."
        ):

            result = finance_graph.invoke({
                "file_path": file_path,
                "budget_limit": budget_limit
            })

            report = result["report"]

        st.success(
            "✅ Financial analysis completed!"
        )

        # Financial summary
        st.subheader("📊 Financial Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Income",
            f"₹{report['income']:,.0f}"
        )

        col2.metric(
            "Total Expenses",
            f"₹{report['total_expenses']:,.0f}"
        )

        col3.metric(
            "Savings",
            f"₹{report['savings']:,.0f}"
        )

        col4.metric(
            "Savings Rate",
            f"{report['savings_percentage']}%"
        )

        st.divider()

        # Budget status
        st.subheader("💳 Budget Status")

        if report["budget_status"] == "Over Budget":

            st.error(
                f"⚠️ You are over your budget of "
                f"₹{report['budget_limit']:,.0f}."
            )

        else:

            st.success(
                f"✅ You are within your budget of "
                f"₹{report['budget_limit']:,.0f}."
            )

        # Highest spending category
        st.subheader("🔎 Highest Spending Category")

        st.info(
            f"**{report['highest_category']}** — "
            f"₹{report['highest_category_amount']:,.0f}"
        )

        # Spending chart
        st.subheader("📈 Spending by Category")

        expense_df = df[
            df["type"] == "Expense"
        ]

        category_summary = (
            expense_df
            .groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(category_summary)

        st.divider()

        # AI Advice
        st.subheader("🤖 AI Financial Advice")

        st.write(report["advice"])

else:

    st.info(
        "👆 Upload your transactions CSV file to begin."
    )