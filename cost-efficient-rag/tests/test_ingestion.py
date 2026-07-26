from ingestion.ingest_pipeline import IngestionPipeline

pipeline = IngestionPipeline()

chunks = pipeline.ingest("data/raw_documents/rag_pape.pdf")

print(f"Chunks Created: {len(chunks)}")