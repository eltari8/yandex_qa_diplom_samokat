import data

import configuration

import send_request

import requests

import pytest

#Тест 1: по номеру заказа можно получить информацию о заказе
def test_order_data_received():
    response = send_request.create_new_order(data.new_order_body)
    track = response.json()["track"]
    track_response = send_request.receive_order_information(track)
    assert track_response.status_code == 200
    print(track_response.status_code)