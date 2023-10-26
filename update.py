import pymongo

# MongoDB connection parameters
mongo_uri = "mongodb://192.168.1.5:27017"  # Modify if necessary
database_name = "credentials"
collection_name = "users"

# Sample user data to be inserted
user_data = [
    {"user_id": "1", "password": "password1"},
    {"user_id": "2", "password": "password2"},
    {"user_id": "3", "password": "password3"},
]

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# Insert user data into the collection
result = collection.insert_many(user_data)

# Print the inserted IDs
print("Inserted IDs:", result.inserted_ids)
