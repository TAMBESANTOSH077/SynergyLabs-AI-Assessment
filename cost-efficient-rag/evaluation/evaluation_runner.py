from rag.rag_pipeline import RAGPipeline
from evaluation.latency_metrics import measure_latency
from evaluation.answer_metrics import answer_length
from evaluation.retrieval_metrics import retrieved_chunks

rag = RAGPipeline()

question = "What is Retrieval Augmented Generation?"

response, latency = measure_latency(
    rag.ask,
    question
)

print("="*60)
print("Question :", question)
print("Latency :", latency, "seconds")
print("Answer Length :", answer_length(response["answer"]))
print("Retrieved Chunks :", retrieved_chunks(response["sources"]))
print("Sources :", response["sources"])
print("="*60)