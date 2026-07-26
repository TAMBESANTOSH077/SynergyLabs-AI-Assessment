from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from rag.generator import Generator
from rag.citation import CitationFormatter

import traceback


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.generator = Generator()
        self.citation_formatter = CitationFormatter()

    def ask(self, question: str, top_k: int = 5):

        try:

            # -------------------------
            # Validate Input
            # -------------------------

            if not question or not question.strip():
                raise ValueError("Question cannot be empty.")

            if top_k <= 0:
                top_k = 5

            # -------------------------
            # Retrieve Documents
            # -------------------------

            results = self.retriever.retrieve(
                query=question,
                top_k=top_k
            )

            if not results:
                return {
                    "question": question,
                    "answer": "No documents were retrieved.",
                    "sources": []
                }

            documents = results.get("documents", [])
            metadatas = results.get("metadatas", [])

            if (
                not documents
                or len(documents) == 0
                or len(documents[0]) == 0
            ):
                return {
                    "question": question,
                    "answer": "I couldn't find any relevant information in the uploaded documents.",
                    "sources": []
                }

            docs = documents[0]
            metadata = metadatas[0] if metadatas else []

            # -------------------------
            # Build Prompt
            # -------------------------

            prompt = self.prompt_builder.build(
                question=question,
                documents=docs,
                metadatas=metadata
            )

            # -------------------------
            # Generate Answer
            # -------------------------

            answer = self.generator.generate(prompt)

            if not answer:
                answer = "The model could not generate an answer."

            # -------------------------
            # Format Citations
            # -------------------------

            try:
                sources = self.citation_formatter.format(metadata)
            except Exception:
                traceback.print_exc()
                sources = []

            # -------------------------
            # Final Response
            # -------------------------

            return {
                "question": question,
                "answer": answer,
                "sources": sources
            }

        except Exception as e:

            traceback.print_exc()

            return {
                "question": question,
                "answer": f"RAG Pipeline Error: {str(e)}",
                "sources": []
            }