from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize_products(processed_products):
    """Vectorize product text using TF-IDF."""
    texts = [product["text"] for product in processed_products]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix, vectorizer

def recommend_products(product_id, processed_products, tfidf_matrix, top_n=5):
    """Recommend similar products based on cosine similarity."""
    target_index = next(
        (index for index, product in enumerate(processed_products) if product["id"] == product_id),
        None,
    )
    if target_index is None:
        raise ValueError(f"Product with ID {product_id} not found.")

    cosine_sim = cosine_similarity(tfidf_matrix[target_index], tfidf_matrix)
    similar_indices = cosine_sim.argsort()[0][-top_n-1:-1][::-1]  # Exclude the product itself
    recommended_products = [processed_products[i] for i in similar_indices]

    return recommended_products