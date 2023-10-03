from homework_20.tests_sw.app import config
from requests import get, Response


class PeopleService:
    def __init__(self):
        self.__people_url = f"{config['host']}/people"

    def get_people(self, people_id:str) -> Response:
        return get(f"{self.__people_url}/{people_id}")