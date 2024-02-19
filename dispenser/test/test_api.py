"""File that will contain all unit tests for api.py"""

import json

import pytest

from dispenser.src.api import (
    is_product_available,
    is_product_expired,
    is_sufficient_change_available_for_transaction,
)


class TestIsProductAvailable:
    """populate later"""

    @pytest.fixture(scope="session")
    def setup_teardown(self):
        """populate later"""
        stock = None
        with open("./data/stock.json", encoding="utf8") as filepointer:
            stock = json.load(filepointer)
        yield stock

    def test_product_that_is_available_is_marked_as_available(
        self,
        setup_teardown,
    ):
        """populate later"""
        result = is_product_available(
            setup_teardown["available_units"],
            "Water",
        )  # Water is set to 20
        assert result is True

    def test_product_that_is_not_available_is_marked_as_not_available(
        self,
        setup_teardown,
    ):
        """populate later"""
        result = is_product_available(
            setup_teardown["available_units"],
            "Orange_Juice",
        )  # Orange_Juice is set to zero
        assert result is False


class TestIsProdcutExpired:
    """populate later"""

    @pytest.fixture(scope="session")
    def setup_teardown(self):
        """populate later"""
        stock = None
        with open("./data/stock.json", encoding="utf8") as filepointer:
            stock = json.load(filepointer)
        yield stock

    def test_product_that_is_expired_is_marked_as_expired(
        self,
        setup_teardown,
    ):
        """populate later"""
        result = is_product_expired(
            setup_teardown["is_expired"],
            "Coke",
        )  # Water is set to True
        assert result is True

    def test_product_that_is_not_expired_is_marked_as_not_expired(
        self,
        setup_teardown,
    ):
        """populate later"""
        result = is_product_expired(
            setup_teardown["is_expired"],
            "Water",
        )  # Water is set to false
        assert result is False


class TestIsSufficientChangeAvailableForTransaction:
    """populate later"""

    @pytest.fixture(scope="session")
    def setup_teardown(self):
        """populate later"""
        stock = None
        with open("./data/stock.json", encoding="utf8") as filepointer:
            stock = json.load(filepointer)
        yield stock

    def test_dispenser_has_sufficient_change_for_transaction(
        self,
        setup_teardown,
    ):
        """populate later"""
        result = is_sufficient_change_available_for_transaction(
            setup_teardown["is_expired"],
            setup_teardown["prices"],
            "Coke",
        )  # Water is set to True
        assert result is True

    def test_dispenser_does_not_have_sufficient_change_for_transaction(
        self,
        setup_teardown,
    ):
        """populate later"""
        result = is_sufficient_change_available_for_transaction(
            setup_teardown["is_expired"],
            setup_teardown["prices"],
            "Water",
        )  # Water is set to false
        assert result is False
