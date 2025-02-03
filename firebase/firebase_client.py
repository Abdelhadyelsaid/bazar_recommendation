import firebase_admin
from firebase_admin import credentials, firestore


def initialize_firebase():

    if not firebase_admin._apps:  # Check if Firebase is already initialized
        cred = credentials.Certificate("thebazar-serviceAccount.json")
        firebase_admin.initialize_app(cred)
        print("Firebase initialized successfully!")
    else:
        print("Firebase already initialized.")

initialize_firebase()

def get_products():
    """Fetch all products from Firestore."""
    db = firestore.client()
    products_ref = db.collection("products")
    products = products_ref.stream()

    product_list = []
    for product in products:
        product_data = product.to_dict()
        product_data["id"] = product.id  # Include the document ID
        product_list.append(product_data)

    return product_list