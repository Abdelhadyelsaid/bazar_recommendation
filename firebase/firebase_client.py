import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import base64
import json

# Load environment variables from .env file
load_dotenv()

def initialize_firebase():
    """Initialize Firebase Admin SDK using a base64-encoded JSON string."""
    if not firebase_admin._apps:  # Check if Firebase is already initialized
        # Get the base64-encoded JSON string from the environment variable
        cred_base64 = os.getenv("FIREBASE_CREDENTIALS_PATH")
        if not cred_base64:
            raise ValueError("FIREBASE_CREDENTIALS_PATH environment variable is not set.")

        try:
            # Decode the base64 string to a JSON string
            cred_json = base64.b64decode(cred_base64).decode("utf-8")
            
            # Convert the JSON string to a dictionary
            cred_dict = json.loads(cred_json)
            
            # Initialize Firebase
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            print("Firebase initialized successfully!")
        except (base64.binascii.Error, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to decode Firebase credentials: {str(e)}")
    else:
        print("Firebase already initialized.")

# Call the initialization function when the module is imported
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