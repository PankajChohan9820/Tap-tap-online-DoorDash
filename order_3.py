subway_order = {
    "name": "John Smith",

    #Pickup Address
    "pickup_address": "5500 Campanile Dr, San Diego, CA 92182",
    "pickup_business_name": "Subway",
    "pickup_phone_number": "+1 619-594-7356",
    "pickup_instructions": "Ask for John at the counter",

    #Dropoff Address
    "dropoff_address": "4560 Mission Gorge Pl Apt 305, San Diego, CA 92120",
    "dropoff_business_name": "John Smith",
    "dropoff_phone_number": "+18783481131",
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",
    "categories": [
        {
            "merchant_supplied_id": "10033",
            "name": "Sandwiches",
            "items": [
                {
                    "name": "Italian B.M.T.",
                    "quantity": 1,
                    "options": [
                        {"name": "Footlong", "quantity": 1},
                        {"name": "Cheddar Cheese", "quantity": 1},
                        {"name": "Lettuce", "quantity": 1},
                        {"name": "Tomato", "quantity": 1},
                        {"name": "Onion", "quantity": 1},
                        {"name": "Green Pepper", "quantity": 1},
                        {"name": "Oil & Vinegar", "quantity": 1}
                    ]
                }
            ],
            "special_instructions": "Extra Cheese"
        }
    ],

    #Payment details
    "payment": {
        "card": {
            "number": "4111111111111111",
            "expiry_month": "12",
            "expiry_year": "2024",
            "cvv": "123",
            "postal_code": "92101"
        }
    },
    "order_value": 899
}
