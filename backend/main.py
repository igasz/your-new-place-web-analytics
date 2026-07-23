from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

# Initialize the FastAPI app
app = FastAPI(title="Your New Place API")

# first "endpoint" (a URL route)
@app.get("/")
def read_root():
    return {"message": "Your New Place API!"}

# fetching data from Oracle
@app.get("/listings")
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(models.Listing).limit(5).all()
    
    return listings