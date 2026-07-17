-- USERS
CREATE TABLE users (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR2(100),
    last_name VARCHAR2(100),
    email VARCHAR2(255) UNIQUE NOT NULL,
    password_hash VARCHAR2(255),
    phone_number VARCHAR2(20),
    role VARCHAR2(20) DEFAULT 'User', -- 'User' / 'Agent'
    created_at DATE DEFAULT SYSDATE
);

-- LOCATIONS
CREATE TABLE locations (
    location_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    zipcode VARCHAR2(20) NOT NULL,
    city VARCHAR2(100),
    county VARCHAR2(100),
    state VARCHAR2(50),
    CONSTRAINT unique_location UNIQUE (zipcode, city)
);

-- LISTINGS - main properties
CREATE TABLE listings (
    listing_id VARCHAR2(100) PRIMARY KEY,
    location_id NUMBER NOT NULL,
    seller_id NUMBER NOT NULL,
    current_status VARCHAR2(50) DEFAULT 'Active', -- Active, Pending, Sold
    price NUMBER(15, 2),
    date_posted DATE,
    street_address VARCHAR2(255),
    bedrooms NUMBER(4, 1),
    bathrooms NUMBER(4, 1),
    living_area NUMBER,
    year_built NUMBER(4),
    home_type VARCHAR2(50),
    description CLOB,
    
    CONSTRAINT fk_listing_location FOREIGN KEY (location_id) REFERENCES locations(location_id),
    CONSTRAINT fk_listing_seller FOREIGN KEY (seller_id) REFERENCES users(user_id)
);

-- LISTING HISTORY
CREATE TABLE listing_history (
    history_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    listing_id VARCHAR2(100) NOT NULL,
    event_type VARCHAR2(100) NOT NULL, -- 'Listed', 'Price Drop', 'Sold'
    event_date DATE NOT NULL,
    price NUMBER(15, 2),
    buyer_id NUMBER,
    
    CONSTRAINT fk_history_listing FOREIGN KEY (listing_id) REFERENCES listings(listing_id),
    CONSTRAINT fk_history_buyer FOREIGN KEY (buyer_id) REFERENCES users(user_id)
);

-- LISTING IMAGES
CREATE TABLE listing_images (
    image_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    listing_id VARCHAR2(100) NOT NULL,
    image_url VARCHAR2(500) NOT NULL,
    is_main_photo NUMBER(1) DEFAULT 0,
    
    CONSTRAINT fk_image_listing FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);

-- SAVED LISTINGS
CREATE TABLE saved_listings (
    user_id NUMBER NOT NULL,
    listing_id VARCHAR2(100) NOT NULL,
    saved_at DATE DEFAULT SYSDATE,
    
    PRIMARY KEY (user_id, listing_id),
    CONSTRAINT fk_saved_user FOREIGN KEY (user_id) REFERENCES users(user_id),
    CONSTRAINT fk_saved_listing FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);