from rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

question = "What is Retrieval Augmented Generation?"
response = rag.ask(question)

print("=" * 60)
print("QUESTION")
print(question)

print("\nANSWER")
print(response["answer"])

print("\nSOURCES")
for source in response["sources"]:
    print(f"- {source['source']} (Chunk {source['chunk']})")
print("=" * 60)