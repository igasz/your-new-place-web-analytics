from pydantic import BaseModel

# schema for images
class ImageResponse(BaseModel):
    image_url: str
    is_main_photo: int

    class Config:
        from_attributes = True

# listing schema
class ListingResponse(BaseModel):
    listing_id: str
    price: float
    street_address: str
    bedrooms: float
    bathrooms: float
    living_area: float

    images: list[ImageResponse] = []

    # from sqlalchemy object
    class Config:
        from_attributes = True