import pytest
from src.keyboard import Keyboard


@pytest.fixture
def sample_items():
    kb1 = Keyboard("EPOMAKER TH80 Pro Keyboard", 10_000, 20)
    return kb1


@pytest.mark.classes
def test_keyboard(sample_items):
    kb1 = sample_items
    assert str(kb1) == "EPOMAKER TH80 Pro Keyboard"
    assert repr(kb1) == 'Keyboard("EPOMAKER TH80 Pro Keyboard", 10000, 20)'

    assert str(kb1.language) == "EN"

    kb1.change_lang()
    assert str(kb1.language) == "RU"

    kb1.change_lang()
    assert str(kb1.language) == "EN"

    with pytest.raises(AttributeError) as exc_info:
        kb1.language = 'CH'

    assert str(exc_info.value) == "property 'language' of 'Keyboard' object has no setter"


if __name__ == "__main__":
    pytest.main()
