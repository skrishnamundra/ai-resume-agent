from app.services.embedding_service import generate_embedding
from app.services.chroma_service import search_resumes

def rank_candidates(job_description):
    jd_embedding = generate_embedding(job_description)
    results = search_resumes(jd_embedding)
    return results
