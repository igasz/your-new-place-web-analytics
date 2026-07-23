import { useState, useEffect } from 'react'

function App() {
  const [listings, setListings] = useState([])

  useEffect(() => {
    // Fetch data from backend
    fetch('http://localhost:8000/listings')
      .then(response => response.json())
      .then(data => setListings(data))
      .catch(error => console.error("Error fetching data:", error))
  }, [])

  return (<div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Your New Place</h1>
      <div style={{ display: 'grid', gap: '20px' }}>
        {listings && listings.length > 0 ? (
          listings.map(listing => (
            <div key={listing.listing_id} style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '8px' }}>

              {listing.images && listing.images.length > 0 && (
                <img 
                  src={listing.images[0].image_url} 
                  alt="House" 
                  style={{ width: '300px', height: '200px', objectFit: 'cover', borderRadius: '4px' }} 
                />
              )}
              <h2>${listing.price.toLocaleString()}</h2>
              <p><strong>{listing.street_address}</strong></p>
              <p>{listing.bedrooms} Beds | {listing.bathrooms} Baths | {listing.living_area} sqft</p>
            </div>
          ))
        ) : (
          <p>Loading houses...</p>
        )}
      </div>
    </div>
  )
}

export default App