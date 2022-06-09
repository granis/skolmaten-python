"""test_molskaten.py."""

from molskaten import Molskaten


def test_molskaten_list_result() -> None:
    mol = Molskaten("dalviksskolan")
    data = mol.getData()
    assert isinstance(data, list)  # nosec assert_used
