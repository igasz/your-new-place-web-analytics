from pydantic import BaseModel

class ListingResponse(BaseModel):
    listing_id: str
    price: float
    street_address: str
    bedrooms: float
    bathrooms: float
    living_area: float

    # from sqlalchemy object
    class Config:
        from_attributes = True