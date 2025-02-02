from firebase.firebase_client import get_products
from services.preprocessing import preprocess_products
from utils.similarity import vectorize_products, recommend_products

def get_recommendations(product_id):
    """Get recommended products for a given product ID."""
    # Fetch products from Firebase
    products = get_products()

    # Preprocess products
    processed_products = preprocess_products(products)

    # Vectorize product text
    tfidf_matrix, _ = vectorize_products(processed_products)

    # Get recommendations
    recommendations = recommend_products(product_id, processed_products, tfidf_matrix, top_n=5)

    return recommendations