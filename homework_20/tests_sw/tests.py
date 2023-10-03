import pytest

from homework_20.infrastructure.people import People
from homework_20.infrastructure.test_data_planets import second_page_planets


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def test_luke_with_fixture(people_service, first_people1):
    response = people_service.get_people("1")
    actual_people = People(
        **response.json()
    )
    assert actual_people == first_people1


def test_get_first_planet(planet_service):
    response = planet_service.get_planet("1")
    assert response.json()['name'] == 'Tatooine'


def test_receive_planets_from_2_page(planet_service):
    response = planet_service.get_planets_from_second_page("2")
    assert response.json() == second_page_planets

