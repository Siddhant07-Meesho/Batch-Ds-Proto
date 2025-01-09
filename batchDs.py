import random
import redis
from BatchDsCatalogs_pb2 import _globals

# Retrieve the generated protobuf class from the _globals dictionary
BatchDsCatalogs = _globals["BatchDsCatalogs"]

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def generate_feed():
    """Generates a list of random catalog IDs."""
    return [random.randint(100000, 3482998) for _ in range(500)]

def populate_redis():
    """Populates Redis with catalog data."""
    for catalogId in range(1000000, 1300000):
        # BDC-> Batch Ds Catalogs
        redis_key = f"BDC:{catalogId}"
        feed = generate_feed()

        # Create a protobuf object and extend it with the generated feed
        batch_catalogs = BatchDsCatalogs()
        batch_catalogs.catalogs.extend(feed)

        # Serialize the protobuf object to bytes
        serialized_data = batch_catalogs.SerializeToString()

        # Store serialized data in Redis
        # break
        redis_client.set(redis_key, serialized_data)

        # Log progress every 10,000 catalogIds
        if catalogId % 10000 == 0:
            print(f"Populated 10000 keys, Current catalogId: {catalogId}")

    print("Data stored successfully in Redis.")

if __name__ == "__main__":
    populate_redis()
