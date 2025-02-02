# Pre-requisites
1- Python 3.5 or higher

# Installation
1- Clone the repository


2- run the following command to install the dependencies
```pip install -r requirements.txt```

Note: ```set the variable value in .env  with the sercive.json path```

3- Run the following command to start the server
```python main.py```

4- How It Works

Fetch Products: The firebase_client.py module fetches products from Firestore.

Preprocess Data: The preprocessing.py module combines product names and descriptions into a single text field.

Vectorize Text: The similarity.py module uses TF-IDF to vectorize the text and calculate cosine similarity.

Recommend Products: The recommendation.py module orchestrates the recommendation process.

Expose API: The main.py file exposes the recommendation logic as a FastAPI endpoint.

