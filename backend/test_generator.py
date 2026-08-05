from rag.retriever import retrieve_context
from rag.generator import generate_answer

question = "Which institutes are mentioned?"

context = retrieve_context(question)

answer = generate_answer(context, question)

print("\n===== AI ANSWER =====\n")
print(answer)