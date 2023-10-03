from homework_20.tests_sw.app import config
from requests import get, Response


class PlanetService:
    def __init__(self):
        self.__planet_url = f"{config['host']}/planets"

    def get_planet(self, planet_id : str) -> Response:
        return get(f"{self.__planet_url}/{planet_id}")

    def get_planets_from_second_page(self,page_num)-> Response:
        return get(f"{self.__planet_url}/?page={page_num}")