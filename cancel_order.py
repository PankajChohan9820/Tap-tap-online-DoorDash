import requests, os, json
from token_access import token
# Set up the API endpoint and headers



def preset_order_status(order_id):
    try:
        # Define the file name
        file_name = 'data.json'
        if not os.path.exists(file_name):return None
        
        with open(file_name, 'r') as f:
            data = json.load(f)

        if len(data['order_ids'])==0:return None

        external_delivery_id = data['order_ids'].pop()
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

def get_order_id():
    try:
        # Define the file name
        file_name = 'data.json'
        if not os.path.exists(file_name):return None
        
        with open(file_name, 'r') as f:
            data = json.load(f)

        if len(data['order_ids'])==0:return None

        order_id = data['order_ids'][-1]
        return order_id
    except Exception as e:
        print(str(e))
        return None

def cancel_order(order_id):
    try:
        if order_id is None:
            print('NO ORDER LEFT TO CANCEL')
            return
        url = 'https://openapi.doordash.com/drive/v2/deliveries/'+order_id+'/cancel'

        headers = {"Accept-Encoding": "application/json",
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"}

        # Send the DELETE request to cancel the order
        response = requests.put(url, headers=headers)

        # Check the status code of the response to confirm the cancellation was successful
        if response.status_code == 200:
            print("Order successfully cancelled")
            preset_order_status(order_id)
        else:
            print("Failed to cancel order. Status code:", response.status_code, response.text)
    except Exception as e:
        print(str(e))




if __name__=='__main__':

    order_id = get_order_id() # Replace with the actual order ID you want to cancel
    cancel_order(order_id)

