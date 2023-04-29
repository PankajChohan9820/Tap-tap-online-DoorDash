from order_1 import panda_express
from order_2 import chipotle_order
from order_3 import subway_order
from token_access import token
import sys, os, json, random, requests


def check_order_present(number):

    # Define the file name
    file_name = 'data.json'
    if not os.path.exists(file_name): return False
    # Check if the file exists
    # Read the data from the file
    with open(file_name, 'r') as f:
        data = json.load(f)

    if number in data.keys() and data[(number)] and len(data['order_ids'])>0:
        return data[number]
    return False

def read_json(external_delivery_id, order_no):

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
        data['1']=False
        data['2']=False
        data['3']=False

    # Update the data
    data['order_ids'].append(external_delivery_id)
    data[order_no]=True
    data[external_delivery_id]=order_no
    # Write the data to the file
    with open(file_name, 'w') as f:
        json.dump(data, f)



def create_delivery(final_order, order_no):
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
            read_json(final_order['external_delivery_id'],order_no)
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
        '1':panda_express,
        '2':chipotle_order,
        '3':subway_order,
    }
    arguments = sys.argv
    order_no = str(arguments[1])
    if not check_order_present(order_no): 
        create_delivery(orders[order_no], order_no)
    else:
        print('The previous order with order no '+order_no+' still on progress')
