from fastapi import FastAPI, HTTPException
import webbrowser
from services.recommendation import get_recommendations
from models.product import Product
from firebase.firebase_client import get_products  # This will initialize Firebase


app = FastAPI()

# Default product ID
DEFAULT_PRODUCT_ID = "GpdyzYCYEMcmpr02fTOV"

@app.get("/recommendations/{product_id}", response_model=list[Product])
async def get_recommendations_api(product_id: str):
    """API endpoint to get recommended products."""
    try:
        print(f"Received request for product: {product_id}")
        recommendations = get_recommendations(product_id)
        print(f"Recommendations: {recommendations}")
        return recommendations
    except ValueError as e:
        print(f"ValueError: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
def open_browser_with_recommendation(product_id: str):
    """Open the browser with a Firebase link containing the recommendation"""
    # Construct the Firebase URL
    firebase_url = f"http://localhost:8000/recommendations/{product_id}"
    
    # Open the URL in the default browser
    webbrowser.open(firebase_url)
import time

if __name__ == "__main__":
    import uvicorn
    # Optionally delay to let the server start
    uvicorn_config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(uvicorn_config)
    
    # Start the server in a separate thread
    import threading
    server_thread = threading.Thread(target=server.run)
    server_thread.start()
    
    # Wait a couple of seconds for the server to start
    time.sleep(2)
    open_browser_with_recommendation(DEFAULT_PRODUCT_ID)
