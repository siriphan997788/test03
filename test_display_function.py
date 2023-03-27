from function import display_month
import pytest

@pytest.mark.parametrize('input_number,expected_result',[(1,"january"),(2,"february"),(3,"march"),(4,"april"),
(5,"may"),(6,"june"),(7,"july"),(8,"august"),(9,"september"),(10,"october"),(11,"november"),(12,"december"),
(0,"out of rang"),(13,"out of rang"),(-10,"out of rang"),(22,"out of rang"),(1.1,"input integer"),
(13.1,"out of rang"),("a","input integer"),("#","input integer"),(0.5,"out of rang"),(-1.5,"out of rang"),
(1.5,"input integer"),

])
@pytest.mark.display #pytest -m display
def test_display(input_number,expected_result):
    actual_result = display_month(input_number)
    assert expected_result == actual_result