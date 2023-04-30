import sys, requests, os, json
from token_access import token


# status code 500 means the order is either cancelled or no more available
# status code 200 means the order has been delivered succesfully
# status code 300 means the order is still in progress.

def delete_order(external_delivery_id):
    try:
        # Define the file name
        file_name = 'data.json'
        if not os.path.exists(file_name):return None
        
        with open(file_name, 'r') as f:
            data = json.load(f)

        if len(data['order_ids'])==0:return None

        data['order_ids'].remove(external_delivery_id)
        if data[external_delivery_id] in data:
            data[data[external_delivery_id]]=False
        if external_delivery_id in data:
            del data[external_delivery_id]
        # Write the data to the file
        with open(file_name, 'w') as f:
            json.dump(data, f)
        return
    except Exception as e:
        print(str(e))
        return None


def check_order_present(number):

    # Define the file name
    file_name = 'data.json'
    if not os.path.exists(file_name): return None
    # Check if the file exists
    # Read the data from the file
    with open(file_name, 'r') as f:
        data = json.load(f)

    if number in data.keys() and data[str(number)] and len(data['order_ids'])>0:
        for key, val in data.items():
        # If the value matches the desired value, return the key
            if isinstance(val, str) and val == order_no:
                return key      
        return None
    return None


def order_status(order_id):
    try:
        get_delivery = requests.get(endpoint + order_id, headers=headers) # Create GET request
        if get_delivery.status_code==200:
            data = get_delivery.json()
            if "delivery_status" in data.keys() and data["delivery_status"]=="delivered":
                delete_order(order_id)
                return 200
            elif "delivery_status" in data.keys() and data["delivery_status"]=="cancelled":
                delete_order(order_id)
                return 500
            else:
                return 300
        else:
            return 500

    except Exception as e:
        print(str(e))
        return 500




if __name__=='__main__':
    endpoint = "https://openapi.doordash.com/drive/v2/deliveries/"
    headers = {"Accept-Encoding": "application/json",
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"}

    arguments = sys.argv
    order_no = str(arguments[1])
    order_id = check_order_present(order_no)
    if order_id is not None:
        print(order_status(order_id))
    else:
        print('500')
