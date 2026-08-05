from rag.retriever import retrieve_context

context = retrieve_context("Which institutes are mentioned?")

print(context)