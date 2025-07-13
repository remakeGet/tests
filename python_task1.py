import pytest
from main import analyze_mentors

# Тестовые данные
MENTORS = [
    ["Евгений Шмаргунов", "Олег Булыгин"],
    ["Филипп Воронов", "Анна Юшина"]
]

def analyze_mentors(mentors):
    # Собираем всех менторов в один список
    all_mentors = []
    for mentor_group in mentors:
        all_mentors.extend(mentor_group)
    
    # Извлекаем только имена
    names = [name.split()[0] for name in all_mentors]
    
    # Считаем частоту имен
    name_counts = {}
    for name in set(names):
        name_counts[name] = names.count(name)
    
    # Получаем топ-3 имен
    top_names = sorted(name_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Формируем результат
    result = {
        'all_mentors': all_mentors,
        'names': names,
        'unique_names': set(names),
        'name_counts': name_counts,
        'top_3': top_names,
        'top_3_formatted': f"{top_names[0][0]}: {top_names[0][1]} раз(а), "
                          f"{top_names[1][0]}: {top_names[1][1]} раз(а), "
                          f"{top_names[2][0]}: {top_names[2][1]} раз(а)"
    }
    return result

def test_analyze_mentors_structure():
    result = analyze_mentors(MENTORS)
    assert isinstance(result, dict)
    assert set(result.keys()) == {'all_mentors', 'names', 'unique_names', 
                                'name_counts', 'top_3', 'top_3_formatted'}

def test_all_mentors_collection():
    result = analyze_mentors(MENTORS)
    assert len(result['all_mentors']) == 4
    assert "Евгений Шмаргунов" in result['all_mentors']
    assert "Анна Юшина" in result['all_mentors']

def test_names_extraction():
    result = analyze_mentors(MENTORS)
    assert len(result['names']) == 4
    assert result['names'].count("Евгений") == 1
    assert result['names'].count("Анна") == 1

def test_unique_names():
    result = analyze_mentors(MENTORS)
    assert isinstance(result['unique_names'], set)
    assert len(result['unique_names']) == 4
    assert "Олег" in result['unique_names']

def test_name_counts():
    result = analyze_mentors(MENTORS)
    assert isinstance(result['name_counts'], dict)
    assert result['name_counts']["Евгений"] == 1
    assert result['name_counts']["Анна"] == 1

def test_top_3():
    result = analyze_mentors(MENTORS)
    assert len(result['top_3']) == 3
    assert all(isinstance(item, tuple) for item in result['top_3'])
    assert result['top_3'][0][1] >= result['top_3'][1][1]

def test_top_3_formatted():
    result = analyze_mentors(MENTORS)
    assert isinstance(result['top_3_formatted'], str)
    assert "раз(а)" in result['top_3_formatted']
    assert all(name in result['top_3_formatted'] 
              for name in [item[0] for item in result['top_3']])

@pytest.mark.parametrize("mentors_data,expected_names", [
    ([["Александр Беспоясов", "Александр Фитискин"]], ["Александр"]),
    ([["Дмитрий Демидов"], ["Олег Булыгин"]], ["Дмитрий", "Олег"]),
])
def test_with_parametrized_data(mentors_data, expected_names):
    result = analyze_mentors(mentors_data)
    assert all(name in result['names'] for name in expected_names)
