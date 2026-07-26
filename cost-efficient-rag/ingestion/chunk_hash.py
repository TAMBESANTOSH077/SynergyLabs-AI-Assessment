import hashlib


def generate_chunk_hash(

    source,

    chunk_index,

    chunk_text

):

    value = f"{source}_{chunk_index}_{chunk_text}"

    return hashlib.sha256(

        value.encode()

    ).hexdigest()