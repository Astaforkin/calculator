import pytest

from calculator import calculator

def test_fold():
    assert calculator('2 + 2') == 4

def test_no_signs():
        with pytest.raises(ValueError) as error:
            calculator('abracadabra')
        assert 'Выраженеие должно содержать хотя бы один знак (+-/*)' == error.value.args[0]



if __name__ == '__main__':
    pytest.main()