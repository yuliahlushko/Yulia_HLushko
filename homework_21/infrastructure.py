import requests
import json


url = "https://api.restful-api.dev/objects"
class Mac:
    def __init__(self, object_id, name, data=''):
        self.object_id = object_id
        self.name=name
        self.data = data


def get_all_objects():
    response = requests.get(f"{url}")
    return response


def get_an_object_by_id(object_id):
    response = requests.get(f"{url}/{object_id}")
    return response


def create_a_new_object(request_body):
    response = requests.post(f"{url}", json = request_body)
    return response


def update_an_object(obj_id, new_body):
    response = requests.put(f'{url}/{obj_id}',json = new_body)
    return response


def delete_an_object(obj_id):
    response = requests.delete(f'{url}/{obj_id}')
    return response

