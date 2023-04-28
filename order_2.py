second_order = {
    "name": "Pankaj Chohan", # Add name field with a value
    # "external_delivery_id": "D-12667",

    #Pickup address
    "pickup_address": "5500 Campanile Dr, San Diego, CA 92182",
    "pickup_business_name": "Chipotle Mexican Grill",
    "pickup_phone_number": "+1 619-362-9973",
    "pickup_instructions": "Pick up name is Pankaj",

    #Drop off address
    "dropoff_address": "4560 Mission Gorge Pl Apt 305, San Diego, CA 92120",
    "dropoff_business_name": "Pankaj Chohan",
    "dropoff_phone_number": "+16505555555",
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",

    #Item details
    "categories": [
    {
      "merchant_supplied_id": "10033",
      "name": "Breakfast",
      "items": [
        {"name": "Barbacoa Bowl", 
        "quantity": 1, 
        "options": [{"name": "White Rice", "quantity": 1},
                    {"name": "Pinto Beans", "quantity": 1},
                    {"name": "Barbacoa", "quantity": 1},
                    {"name": "Mild Salsa", "quantity": 1},
                    {"name": "Cheese", "quantity": 1},
                    {"name": "Lettuce", "quantity": 1},
                    {"name": "Guacamole", "quantity": 1}
                    ]
        }],
      "special_instructions": "Extra Cheese"
    }
  ],
  #Payment details
    "payment": {
        "card": {
            "number": "4111111111111111",
            "expiry_month": "01",
            "expiry_year": "2023",
            "cvv": "123",
            "postal_code": "12345"
        }
    },
    "order_value": 1999
}
