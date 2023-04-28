from order_1 import first_order
from order_2 import second_order
from order_3 import third_order
from token_access import token
import sys, os, json, random, requests


def read_json(external_delivery_id):

    # Define the file name
    file_name = 'data.json'

    # Check if the file exists
    if os.path.exists(file_name):
        # Read the data from the file
        with open(file_name, 'r') as f:
            data = json.load(f)
    else:
        # Create an empty dictionary
        data = {}
        data['order_ids']=[]

    # Update the data
    data['order_ids'].append(external_delivery_id)

    # Write the data to the file
    with open(file_name, 'w') as f:
        json.dump(data, f)



def create_delivery(final_order):
    try:
        # Generate a random 5-digit number
        num_digits = random.randint(5,10)
        random_num = random.randint(10**(num_digits-1), 10**num_digits-1)
        final_order['external_delivery_id']= 'D-'+str(random_num)

        create_delivery = requests.post(endpoint, headers=headers, json=final_order) # Create POST request
        print(create_delivery.status_code)
        if create_delivery.status_code==200:
            print('YOUR ORDER IS CREATED SUCCESSFULLY')
            print('YOUR ORDER DETAILS IS')
            print(create_delivery.text)
            print(create_delivery.reason)
            read_json(final_order['external_delivery_id'])
        else:
            print('ERROR CREATING YOUR ORDER')
            print(create_delivery.reason)
            print(create_delivery.text)

    except Exception as e:
        print(str(e))




if __name__=='__main__':

    endpoint = "https://openapi.doordash.com/drive/v2/deliveries/"
    headers = {"Accept-Encoding": "application/json",
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"}

    orders = {
        '1':first_order,
        '2':second_order,
        '3':third_order,
    }
    arguments = sys.argv
    order_no = arguments[1]
    create_delivery(orders[str(order_no)])
