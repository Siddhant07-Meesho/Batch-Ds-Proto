import redis
import json

# Initialize Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# List of eligible items

oldFormatData = [
    {
        "id": 1007,
        "name": "Blouses",
        "clp": 88636
    },
    {
        "id": 1093,
        "name": "Jewellery Set",
        "clp": 39043
    },
    {
        "id": 1094,
        "name": "Bangles & Bracelets",
        "clp": 176832
    },
    {
        "id": 1091,
        "name": "Earrings & Studs",
        "clp": 954
    }]

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
    },
    {
        "group_id":1094,
        "combined_sscat_name": "Bangles & Bracelets",
        "sscats_combined":[
            {
                "id": 1094,
                "name": "Bangles & Bracelets",
                "clp": 176832
            }
        ]
    },
    {
        "group_id":1091,
        "combined_sscat_name": "Earrings & Studs",
        "sscats_combined":[
            {
                "id": 1091,
                "name": "Earrings & Studs",
                "clp": 954
            }
        ]
    }
]




eligible_sscat_json = [json.dumps(item) for item in eligible_sscat]

# Loop to add data to Redis
for i in range(500, 550):
    key = "ES:v3:" + str(i)
    # Push all items at once
    redis_client.rpush(key, *eligible_sscat_json)  # Use unpacking to pass all items
    if i % 500 == 0:
        print(f"Set eligible sscats for 500 sscats")
