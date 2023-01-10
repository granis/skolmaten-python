"""test_molskaten.py."""
from datetime import datetime

from molskaten import Lunch, Molskaten


def test_molskaten_list_result() -> None:
    mol = Molskaten("dalviksskolan")
    data = mol.getData()
    assert isinstance(data, list)  # nosec assert_used


def test_lunch() -> None:
    lunch = Lunch("Meatrolls", datetime(2022, 1, 1, 0, 0, 0))
    assert str(lunch) == "Lunch: 2022-01-01 @ Meatrolls"
    assert lunch.food == "Meatrolls"
