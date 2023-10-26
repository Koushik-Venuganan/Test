from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

app = FastAPI()


try:
    # MongoDB connection (without username and password)
    MONGO_URI = "mongodb://mongo:27017"  # Assuming "mongo" is the hostname
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["credentials"]
    users_collection = db["users"]

except:
    print("unable to make connection")

# Create a data model for the user
class User(BaseModel):
    username: str
    password: str

# Login route
@app.post("/login")
async def login(user: User):
    # Check if the user exists in the MongoDB collection
    user_doc = await users_collection.find_one({"user_id": user.username, "password": user.password})
    if user_doc:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Login failed")


# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
