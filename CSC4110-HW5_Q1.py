import random
from datetime import datetime, timedelta

# Simplified Data Collector Method
def generate_user_data_simple(n):
    user_records = {}
    for _ in range(n):
        user_id = f"user_{random.randint(1, 10000)}"
        user_data = {
            "username": f"user{random.randint(100, 999)}",
            "password": f"pass{random.randint(1000, 9999)}",
            "birthdate": (datetime.now() - timedelta(days=random.randint(18, 90) * 365)).date().isoformat(),
            "address": f"{random.randint(100, 999)} Main St, City{random.randint(1, 99)}",
            "socialSecurityNumber": f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}",
            "productPurchased": {
                "orderID": f"ID-{random.randint(100000, 999999)}",
                "webOrder": random.choice([True, False]),
                "productID": f"ID-{random.randint(100000, 999999)}",
                "quantity": random.randint(1, 10),
                "dateOfOrder": (datetime.now() - timedelta(days=random.randint(1, 365))).date().isoformat(),
                "region": random.choice(["California", "Texas", "New York", "Florida"])
            },
            "salesperson": f"Salesperson{random.randint(1, 10)}"
        }
        user_records[user_id] = user_data
    return user_records

# Generate user records
user_records_simple = generate_user_data_simple(100)

# Search Engine
def search_user_records_simple(user_records, **criteria):
    results = []
    for user_id, user_data in user_records.items():
        match = True
        for key, value in criteria.items():
            if key == "state":
                if user_data["productPurchased"]["region"] != value:
                    match = False
                    break
            elif key == "salesperson":
                if user_data["salesperson"] != value:
                    match = False
                    break
            else:
                if user_data.get(key) != value:
                    match = False
                    break
        if match:
            results.append((user_id, user_data))
    return results

# Example searches
example_state_search_simple = search_user_records_simple(user_records_simple, state="California")
example_salesperson_search_simple = search_user_records_simple(user_records_simple, salesperson=user_records_simple[next(iter(user_records_simple))]['salesperson'])

# Output the number of matches for demonstration
print(f"Users from California: {len(example_state_search_simple)}")
print(f"Users handled by a specific salesperson: {len(example_salesperson_search_simple)}")
