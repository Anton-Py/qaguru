"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework_8_python_part_3_oop.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @pytest.mark.parametrize(
        "quantity, expected_result",
        [
            pytest.param(1, True, id='Проверка, когда запрашиваемое количество меньше, чем доступное'),
            pytest.param(1000, True, id='Проверка, когда запрашиваемое количество равно доступному'),
            pytest.param(1500, False, id='Проверка, когда запрашиваемое количество больше, чем доступное')
        ]
    )
    def test_product_check_quantity(self, product, quantity, expected_result):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(quantity) == expected_result

    @pytest.mark.parametrize(
        "quantity, expected_result",
        [
            pytest.param(455, 545, id='quantity < product.quantity'),
            pytest.param(1000, 0, id='quantity == product.quantity')
        ]
    )
    def test_product_buy(self, product, quantity, expected_result):
        # TODO напишите проверки на метод buy

        product.buy(quantity)

        assert product.quantity == expected_result

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        quantity_trigger_exception = 1050

        with pytest.raises(ValueError):
            product.buy(quantity_trigger_exception)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    # проверка добавления продукта в корзину по кол-ву и названию
    def test_add_to_cart(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5 and product.name == "book"

    # проверка добавления нескольких продуктов в корзину
    def test_adding_multiple_products_to_cart(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products[product] == 10
        cart.add_product(product, 50)
        assert cart.products[product] == 60

    # проверка добавления другого продукта в корзину
    def test_checking_adding_another_product(self, cart, product):
        second_product = Product("milk", 50, "This is a milk", 500)
        cart.add_product(second_product, 10)

        assert cart.products[second_product] == 10
        assert second_product.name == "milk"

    # проверка удаления продуктов больше чем есть в корзине
    def test_removing_more_products_from_the_cart(self, cart, product):
        cart.add_product(product, 10)
        print(cart.products[product])
        cart.remove_product(product, 15)
        assert product.name not in cart.products

   # проверка удаления продуктов больше чем есть в корзине
    def test_removing_product_from_the_cart(self, cart, product):
        cart.add_product(product, 10)
        print(cart.products[product])
        cart.remove_product(product, 5)
        assert cart.products[product] == 5

    # удаление такого же числа продуктов из корзины
    def test_removing_same_number_of_products_from_cart(self, cart, product):
        cart.add_product(product, 33)
        cart.remove_product(product, 33)
        assert product not in cart.products

    # удаление продукта если не передали кол-во для удаления
    def test_removing_same_without_remove_count(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product, None)
        assert product not in cart.products

    # проверка очитски корзины
    def test_cert_clear(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        cart.clear()
        assert product not in cart.products

    # стоимость корзины с товарами
    def test_get_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    # покупка товаров к корзины
    def test_buy_products_in_cart(self, cart, product):
        cart.add_product(product, 10)
        assert cart.buy() is None
        assert product.quantity == 990
