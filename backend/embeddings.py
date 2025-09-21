from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight semantic model

def get_embedding(text):
    return model.encode([text])[0]

def semantic_similarity(text1, text2):
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    return cosine_similarity([emb1], [emb2])[0][0]
