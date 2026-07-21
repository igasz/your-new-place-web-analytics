import pandas as pd
from sqlalchemy import create_engine
import random

def load_data_to_oracle():
    DB_URL = "oracle+oracledb://yourplace:Password123@localhost:1521/?service_name=FREEPDB1"
    engine = create_engine(DB_URL)


    # creating agents

    users_data = []

    users_data.append({
        'first_name': 'Lando',
        'last_name': 'Norris',
        'email': 'landonor@mail.com',
        'phone_number': '789 993 245',
        'role': 'Agent'
    })

    users_data.append({
        'first_name': 'Iga',
        'last_name': 'Sz',
        'email': 'igasz@mail.com',
        'phone_number': '788 023 212',
        'role': 'Agent'
    })

    users_data.append({
        'first_name': 'Carlos',
        'last_name': 'Sainz',
        'email': 'carlosai@mail.com',
        'phone_number': '345 012 298',
        'role': 'Agent'
    })

    users_df = pd.DataFrame(users_data)
    users_df.to_sql('users', engine, if_exists='append', index=False)

    db_users = pd.read_sql("SELECT user_id FROM users", engine)
    agent_ids = db_users['user_id'].tolist()
    print(f"Inserted {len(agent_ids)} agents.")


   # read csv

    df = pd.read_csv("clean_data.csv")
    # random 4k houses
    df = df.sample(n=4000, random_state=42).copy()
    print(f"dataset down to a random sample of {len(df)} listings.")

    df['zipcode'] = df['zipcode'].astype(str).str.replace(r'\.0$', '', regex=True)

    # inserting locations
    locations_df = df[['zipcode', 'city', 'county', 'state']].drop_duplicates(subset=['zipcode', 'city'])
    locations_df.to_sql('locations', engine, if_exists='append', index=False)

    db_locations = pd.read_sql("SELECT location_id, zipcode, city FROM locations", engine)


    # preparing data

    df = df.merge(db_locations, on=['zipcode', 'city'], how='inner')
    df['seller_id'] = [random.choice(agent_ids) for _ in range(len(df))]
    
    listings_df = df.rename(columns={
        'id': 'listing_id',
        'datePostedString': 'date_posted',
        'streetAddress': 'street_address',
        'livingArea': 'living_area',
        'yearBuilt': 'year_built',
        'homeType': 'home_type'
    })
    listings_df['date_posted'] = pd.to_datetime(listings_df['date_posted'])
    listings_df['current_status'] = 'Active'
    
    db_listing_columns = [
        'listing_id', 'location_id', 'seller_id', 'price', 'date_posted', 
        'street_address', 'bedrooms', 'bathrooms', 'living_area', 
        'year_built', 'home_type', 'description', 'current_status'
    ]
    listings_to_insert = listings_df[[col for col in db_listing_columns if col in listings_df.columns]]
    
    listings_to_insert.to_sql('listings', engine, if_exists='append', index=False)
    print(f"Inserted {len(listings_to_insert)} listings.")


    # listing history

    history_df = listings_df[['listing_id', 'date_posted', 'price']].copy()
    history_df = history_df.rename(columns={'date_posted': 'event_date'})
    history_df['event_type'] = 'Listed for sale'
    
    history_df.to_sql('listing_history', engine, if_exists='append', index=False)
    print("Inserted listing history.")


    # mock photos

    images_data = []
    
    for listing_id in listings_to_insert['listing_id']:
        # 1 main photo
        images_data.append({
            'listing_id': listing_id,
            'image_url': f"https://picsum.photos/seed/{listing_id}_main/800/600",
            'is_main_photo': 1
        })
        # 2 gallery photos
        for i in range(2):
            images_data.append({
                'listing_id': listing_id,
                'image_url': f"https://picsum.photos/seed/{listing_id}_{i}/800/600",
                'is_main_photo': 0
            })
            
    images_df = pd.DataFrame(images_data)

    images_df.to_sql('listing_images', engine, if_exists='append', index=False, chunksize=1000)
    print("Inserted mock photos")
    
    print("\ncompleted")

if __name__ == "__main__":
    load_data_to_oracle()