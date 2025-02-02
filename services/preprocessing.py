def preprocess_products(products):
    """Combine product name and description into a single text field."""
    processed_products = []
    for product in products:
        text = f"{product['name']} {product['description']}"
        processed_products.append({
            "id": product["id"],
            "name": product["name"],
            "description": product["description"],
            "mainImage": product["mainImage"],
            "price": product["price"],
            "text": text,
        })
    return processed_products