from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas

# Initialize the FastAPI app
app = FastAPI(title="Your New Place API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you'd put your exact frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# first "endpoint" (a URL route)
@app.get("/")
def read_root():
    return {"message": "Your New Place API!"}

# fetching data from Oracle
@app.get("/listings", response_model=list[schemas.ListingResponse])
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(models.Listing).limit(5).all()
    
    return listings