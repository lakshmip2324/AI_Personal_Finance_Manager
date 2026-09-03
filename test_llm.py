from utils.llm import llm


response = llm.invoke(
    "Give me one simple tip for managing monthly expenses."
)

print("AI Response:")
print(response.content)