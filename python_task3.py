import pytest

# Исходные данные 
ORIGINAL_PHRASES = [
    "нажал кабан на баклажан",
    "дом как комод",
    "рвал дед лавр",
    "азот калий и лактоза",
    "а собака боса",
    "тонет енот",
    "карман мрак",
    "пуст суп"
]

EXPECTED_RESULT = [
    "нажал кабан на баклажан",
    "рвал дед лавр",
    "азот калий и лактоза",
    "а собака боса",
    "тонет енот",
    "пуст суп"
]

def solve(phrases: list):
    result = []
    for phrase in phrases:
        processed_phrase = phrase.replace(' ', '').lower()  
        if processed_phrase == processed_phrase[::-1]:
            result.append(phrase)
    return result

def test_original_data_solution():
    result = solve(ORIGINAL_PHRASES)
    assert result == EXPECTED_RESULT
    assert len(result) == 6
    assert "дом как комод" not in result
    assert "карман мрак" not in result

@pytest.mark.parametrize("phrase,expected", [
    ("топот", True),
    ("А роза упала на лапу Азора", True),
    ("не палиндром", False),
    ("12321", True),
    ("", True),  # Пустая строка считается палиндромом
    ("a", True),  # Один символ - палиндром
    ("ab", False),
    ("а ва", True),  # С пробелом
    ("Was it a car or a cat I saw", True),  # Английский, регистр
])
def test_individual_phrases(phrase, expected):
    result = solve([phrase])
    assert (phrase in result) == expected

def test_empty_input():
    assert solve([]) == []

def test_case_sensitivity():
    assert solve(["ТоПоТ"]) == ["ТоПоТ"]
    assert solve(["А роза упала на лапу Азора"]) == ["А роза упала на лапу Азора"]

def test_whitespace_handling():
    assert solve([" топ от "] * 3) == [" топ от "] * 3
    assert solve(["не палиндром"]) == []

def test_returned_order():
    phrases = ["топот", "не палиндром", "12321"]
    result = solve(phrases)
    assert result == ["топот", "12321"]  # Порядок сохраняется
