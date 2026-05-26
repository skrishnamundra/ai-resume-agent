import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="resumes")

def store_resume(candidate_name, text, embedding):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[candidate_name]
    )

def search_resumes(job_description_embedding, top_k=5):
    results = collection.query(
        query_embeddings=[job_description_embedding],
        n_results=top_k
    )

    return results
