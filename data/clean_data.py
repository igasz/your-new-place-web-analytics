import pandas as pd

def clean_data(filepath, output_path):
    df = pd.read_csv(filepath)
    initial_rows = len(df)
    
    # remove unnecessary columns
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        print("Removed the technical column 'Unnamed: 0'.")
        
    # Handle missing data (NaN)
    df = df.dropna(subset=['zipcode', 'streetAddress', 'datePostedString'])
    
    # drop duplicates
    df = df.drop_duplicates(subset=['id'])
    print("Removed duplicate listings.")

    # Fill missing descriptions and events with default text
    df['description'] = df['description'].fillna('No description')
    df['event'] = df['event'].fillna('Unknown')
    df['time'] = df['time'].fillna(0)
    print("Patched missing values.")

    # price anomalies
    # Remove free or cheap houses (below $10,000)
    df = df[df['price'] > 10000]
    
    # Date formatting
    df['datePostedString'] = pd.to_datetime(df['datePostedString'], errors='coerce')
    
    # Text normalization
    df['city'] = df['city'].str.title() 
    
    final_rows = len(df)
    print(f"\nSummary:")
    print(f"Initial row count: {initial_rows}")
    print(f"Final row count: {final_rows}")
    print(f"Removed {initial_rows - final_rows} invalid rows.")
    
    # Save the cleaned data to a new file
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")

if __name__ == "__main__":
    INPUT_FILE = "raw_data.csv"
    OUTPUT_FILE = "clean_data.csv" 
    
    # Fixed the function call to match the definition above
    clean_data(INPUT_FILE, OUTPUT_FILE)