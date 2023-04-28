first_order = {
    "name": "John Smith",

    #Pickup Address
    "pickup_address": "5500 Campanile Dr, San Diego, CA 92182",
    "pickup_business_name": "Panda Express",
    "pickup_phone_number": "+1 619-594-7707",
    "pickup_instructions": "Ask for John at the counter",

    #Drop off Address
    "dropoff_address": "5678 Second St, San Diego, CA 92101",
    "dropoff_business_name": "John Smith",
    "dropoff_phone_number": "+1 619-234-5678",
    "dropoff_instructions": "Leave at the doorstep",
    "categories": [
        {
            "merchant_supplied_id": "1001",
            "name": "Entrees",
            "items": [
                {
                    "name": "Orange Chicken",
                    "quantity": 2,
                    "options": [
                        {
                            "name": "Steamed Rice",
                            "quantity": 2
                        },
                        {
                            "name": "Wok-Fried Vegetables",
                            "quantity": 2
                        }
                    ]
                }
            ],
            "special_instructions": "No peanuts please"
        }
    ],
    "payment": {
        "card": {
            "number": "4111111111111111",
            "expiry_month": "12",
            "expiry_year": "2024",
            "cvv": "123",
            "postal_code": "92101"
        }
    },
    "order_value": 2899
}
