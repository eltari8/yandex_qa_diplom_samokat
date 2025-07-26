import requests

import data

import configuration


#запрос на создание заказа
def create_new_order(body):
    return requests.post(configuration.MAIN_URL + configuration.CREATE_ORDER_URL,json=body)
response = create_new_order(data.new_order_body)
track_number = response.json()["track"]
print(response.status_code)
print(track_number)

def receive_order_information(track):
    return requests.get(configuration.MAIN_URL + configuration.RECEVE_Order_Track_URL + "?t=" + str(track))
response_track = receive_order_information(track_number)
print(configuration.MAIN_URL + configuration.RECEVE_Order_Track_URL + "?t=" + str(track_number))
print(response_track.status_code)