from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI(title="Your New Place API")

# Create our first "endpoint" (a URL route)
@app.get("/")
def read_root():
    return {"message": "Your New Place API!"}

@app.get("/status")
def api_status():
    return {"status": "Online", "database_connected": False}