SYSTEM_PROMPT = """
You are an expert AI assistant specializing in Retrieval-Augmented Generation (RAG).

Instructions:

1. Answer ONLY using the provided context.
2. Never invent facts.
3. If the answer is not in the context, reply exactly:
"I do not have sufficient information in the provided context."
4. Keep answers concise.
5. Preserve technical terminology.

--------------------

Context

{context}

--------------------

Question

{question}

--------------------

Answer
"""


class PromptBuilder:

    MAX_CONTEXT = 12000

    def build(
        self,
        question: str,
        documents: list,
        metadatas: list
    ) -> str:

        if not question or not question.strip():
            raise ValueError("Question cannot be empty.")

        if not documents:
            raise ValueError("No retrieved documents found.")

        context_blocks = []

        for index, doc in enumerate(documents):

            meta = (
                metadatas[index]
                if index < len(metadatas)
                else {}
            )

            source = meta.get("source", "Unknown")
            chunk = meta.get("chunk", index)

            context_blocks.append(
                f"""
Document {index+1}
Source: {source}
Chunk: {chunk}

Content:
{doc.strip()}
"""
            )

        context = "\n".join(context_blocks)

        if len(context) > self.MAX_CONTEXT:
            context = context[:self.MAX_CONTEXT]

        return SYSTEM_PROMPT.format(
            context=context,
            question=question.strip()
        )