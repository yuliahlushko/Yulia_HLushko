import pytest
from homework_13.make_order import Order


@pytest.fixture
def create_order():
    yield Order()

# Гість може додадти замовлення
@pytest.mark.positive
def test_add_order_item(create_order):
    first_order = create_order
    first_order.add_item('Pizza')
    assert first_order.items == ['Pizza']

# Гість отримає помилку, якщо спробує додати страву не з меню
@pytest.mark.positive
def test_exception(create_order):
    with pytest.raises(Exception) as error_mes:
        second_order = create_order
        second_order.add_item('Cake')
    assert str(error_mes.value) == 'The dish is not in the menu'


# Гість може обрати будь-яку страву з меню
@pytest.mark.positive
@pytest.mark.parametrize('item, expected', [('Pizza', ['Pizza']), ('Pasta', ['Pasta']), ('Salad', ['Salad'])])
def test_select_any_possible_dish(create_order, item, expected):
    third_order = create_order
    third_order.add_item(item)
    assert third_order.items == expected

#Гість не може зробити пусте замовлення
@pytest.mark.negative
def test_add_order_item(create_order):
    with pytest.raises(Exception):
        first_order = create_order
        first_order.add_item('')

# Гість може додати в замовлення дві однакові страви
@pytest.mark.positive
@pytest.mark.parametrize('item, expected', [('Pizza', ['Pizza', 'Pizza']), ('Pasta', ['Pasta', 'Pasta']), ('Salad', ['Salad', 'Salad'])])
def test_select_any_possible_dish(create_order, item, expected):
    forth_order = create_order
    forth_order.add_item(item)
    forth_order.add_item(item)
    assert forth_order.items == expected


