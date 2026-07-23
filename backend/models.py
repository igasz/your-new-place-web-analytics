from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

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