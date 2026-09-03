# 💰 AI Personal Finance Manager

An AI-powered personal finance management application that analyzes transaction data, monitors budgets, evaluates savings, and provides personalized financial suggestions.

## 🚀 Features

- 📂 Upload transaction data through CSV
- 💰 Calculate income, expenses, and savings
- 📊 Analyze spending by category
- 💳 Set and monitor monthly budgets
- 🔎 Identify the highest spending category
- 🤖 Generate AI-powered financial advice using Llama 3.2
- 🧠 Manager Agent for intelligent decision-making
- 🔀 Conditional routing using LangGraph
- 📈 Interactive spending visualization
- 🌐 Streamlit web interface

## 🧠 Agentic AI Workflow

The application uses multiple specialized agents:

```text
User
  ↓
Streamlit Application
  ↓
Expense Analysis
  ↓
Manager Agent
  ↓
 ┌───────────────┬───────────────┐
 ↓               ↓               ↓
Budget Agent   Savings Agent   Advisor Agent
 └───────────────┴───────────────┘
                  ↓
            Advisor Agent
                  ↓
             Report Agent
                  ↓
               Result

The Manager Agent analyzes the financial situation and determines the appropriate route:

Over Budget → Budget Agent
Savings below 20% → Savings Agent
Otherwise → Advisor Agent
🛠️ Technologies Used
Python
LangGraph
LangChain
Ollama
Llama 3.2
Pandas
Streamlit
Plotly
CSV
📁 Project Structure
AI_Personal_Finance_Manager/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── agents/
│   ├── budget_agent.py
│   ├── savings_agent.py
│   ├── advisor_agent.py
│   ├── report_agent.py
│   └── manager_agent.py
│
├── graph/
│   └── finance_graph.py
│
├── tools/
│   └── expense_tools.py
│
├── data/
│   └── transactions.csv
│
├── database/
│
├── utils/
│   └── llm.py
│
└── test_*.py
⚙️ How to Run
1. Clone the repository
git clone https://github.com/lakshmip2324/AI_Personal_Finance_Manager.git
2. Create and activate the environment
conda create -n finance_agent python=3.11
conda activate finance_agent
3. Install dependencies
pip install -r requirements.txt
4. Install and run Ollama

Make sure Ollama is installed and the Llama 3.2 model is available.

ollama pull llama3.2
5. Run the application
streamlit run app.py

The application will open in your browser.

📄 CSV Format

The transaction CSV should contain the following columns:

id
date
description
category
amount
type

Example:

id,date,description,category,amount,type
1,2026-08-01,Salary,Salary,40000,Income
2,2026-08-02,House Rent,Rent,10000,Expense
3,2026-08-03,Groceries,Food,3000,Expense
📊 Example Analysis

For the sample transaction data:

Income: ₹40,000
Total Expenses: ₹23,249
Savings: ₹16,751
Savings Rate: 41.88%
Budget: ₹20,000
Budget Status: Over Budget
Highest Spending Category: Rent
Highest Category Amount: ₹10,000

The AI Advisor then generates practical suggestions based on the user's financial situation.

🔀 Conditional Decision Making

The Manager Agent uses financial conditions to determine which specialized agent should handle the main issue.

                    Manager Agent
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Over Budget    Low Savings    Good Savings
          ↓              ↓              ↓
    Budget Agent    Savings Agent   Advisor Agent

This demonstrates autonomous decision-making and conditional workflow orchestration using LangGraph.

🔮 Future Enhancements
SQLite-based transaction storage
Persistent financial memory
Automatic monthly reports
Expense forecasting
Goal-based savings planning
More advanced financial analytics
Improved dashboard visualizations
⚠️ Disclaimer

This application provides general financial insights based on the uploaded transaction data. It is not a substitute for professional financial advice.

👩‍💻 Author

Lakshmi P
