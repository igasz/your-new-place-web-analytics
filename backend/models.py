from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# model for images
class ListingImage(Base):
    __tablename__ = 'listing_images'
    image_url = Column(String, primary_key=True)

    listing_id = Column(String, ForeignKey('listings.listing_id'))
    is_main_photo = Column(Integer)

    listing = relationship("Listing", back_populates="images")

# listing model
class Listing(Base):
    __tablename__ = 'listings'

    listing_id = Column(String, primary_key=True)
    location_id = Column(Integer)
    seller_id = Column(Integer)
    price = Column(Float)
    date_posted = Column(DateTime)
    street_address = Column(String)
    bedrooms = Column(Float)
    bathrooms = Column(Float)
    living_area = Column(Float)
    year_built = Column(Integer)
    home_type = Column(String)
    description = Column(String)
    current_status = Column(String)

    images = relationship("ListingImage", back_populates="listing")