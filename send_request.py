import requests

import data

import configuration


#запрос на создание заказа
def create_new_order(body):
    return requests.post(configuration.MAIN_URL + configuration.CREATE_ORDER_URL,json=body)


def receive_order_information(track):
    return requests.get(configuration.MAIN_URL + configuration.RECEVE_Order_Track_URL + "?t=" + str(track))

