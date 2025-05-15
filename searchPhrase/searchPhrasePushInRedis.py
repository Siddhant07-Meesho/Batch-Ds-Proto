import random

import redis
from debug.searchPhrase import searchPhrase_pb2

eligible_sscat = [
    {
        "group_id":1007,
        "combined_sscat_name": "Blouses",
        "sscats_combined":[
            {
                "id": 1007,
                "name": "Blouses",
                "clp": 88636
            }
        ]
    },
    {
        "group_id":1093,
        "combined_sscat_name": "Jewellery Set",
        "sscats_combined":[
            {
                "id": 1093,
                "name": "Jewellery Set",
                "clp": 39043
            }
        ]
    }
]

# Sample data generator
def generate_sample_data(eligible_sscat):
    descriptions = [
        "Saree with yellow flower",
        "Kurti with red border",
        "Lehenga with silver design",
        "Salwar with gold thread",
        "Dupatta with green embroidery",
        "Top with blue polka dots"
    ]
    return [{"id": grp["group_id"], "sp": random.choice(descriptions)} for grp in eligible_sscat]



# Function : Store using Protocol Buffers (proto format)
def store_using_protobuf(redis_client, key, data):
    # Create SearchPhrases message
    search_phrases = searchPhrase_pb2.SearchPhrases()

    # Add groups to search_phrases
    for item in data:
        group = search_phrases.phrases.add()
        group.id = item['id']
        group.sp = item['sp']

    # Serialize the data to binary format
    serialized_data = search_phrases.SerializeToString()

    # Store in Redis
    redis_client.set(key, serialized_data)


def read_from_redis(redis_client, key):
    # Fetch raw binary data
    serialized_data = redis_client.get(key)

    # Parse it back into Protobuf object
    search_phrases = searchPhrase_pb2.SearchPhrases()
    search_phrases.ParseFromString(serialized_data)

    # Print parsed data
    for group in search_phrases.phrases:
        print(f"id: {group.id}, sp: {group.sp}")


# Example usage
if __name__ == "__main__":
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    sample_data = generate_sample_data(eligible_sscat)
    print(sample_data)
    purchasedCatalogId = 8767890
    purchasedSscatId = 1004

    key = f"SP:v1:{purchasedCatalogId}"

    # suppose 1004 has sscatMapping of above eligible_sscat

    # Store using Protobuf
    store_using_protobuf(r, key, sample_data)

    print("Data pushed")

    read_from_redis(r, key)
