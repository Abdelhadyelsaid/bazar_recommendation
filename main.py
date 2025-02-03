from fastapi import FastAPI, HTTPException
from services.recommendation import get_recommendations
from models.product import Product
from firebase.firebase_client import get_products 


app = FastAPI()


@app.get("/recommendations/{product_id}", response_model=list[Product])
async def get_recommendations_api(product_id: str):
    """API endpoint to get recommended products."""
    try:
        recommendations = get_recommendations(product_id)
        return recommendations
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)