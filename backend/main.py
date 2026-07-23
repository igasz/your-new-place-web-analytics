from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import get_db

# Initialize the FastAPI app
app = FastAPI(title="Your New Place API")

# first "endpoint" (a URL route)
@app.get("/")
def read_root():
    return {"message": "Your New Place API!"}

# fetching data from Oracle
@app.get("/listings")
def get_listings(db: Session = Depends(get_db)):
    # raw SQL query to get 5 properties
    query = text("""
        SELECT listing_id, price, street_address, bedrooms, bathrooms, living_area 
        FROM listings 
        FETCH FIRST 5 ROWS ONLY
    """)
    
    result = db.execute(query)
    
    # Format the SQL results into a clean dictionary list
    listings_data = []
    for row in result:
        listings_data.append({
            "id": row[0],
            "price": row[1],
            "address": row[2],
            "beds": row[3],
            "baths": row[4],
            "sqft": row[5]
        })
        
    return {"listings": listings_data}