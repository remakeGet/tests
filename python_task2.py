import pytest
# Исходные данные из задачи
COURSES = [
    {"title": "Java-разработчик с нуля", "mentors": [], "duration": 14},
    {"title": "Fullstack-разработчик на Python", "mentors": [], "duration": 20},
    {"title": "Python-разработчик с нуля", "mentors": [], "duration": 12},
    {"title": "Frontend-разработчик с нуля", "mentors": [], "duration": 20}
]

def sort_courses_by_duration(courses_list):
    durations_dict = {}
    
    for id, course in enumerate(courses_list):
        duration = course["duration"]
        durations_dict.setdefault(duration, []).append(id)
    
    sorted_durations = dict(sorted(durations_dict.items()))
    
    sorted_courses = []
    for duration, ids in sorted_durations.items():
        for course_id in ids:
            course = courses_list[course_id]
            sorted_courses.append({
                "title": course["title"],
                "duration": course["duration"],
                "original_index": course_id,
                "formatted": f"{course['title']} - {course['duration']} месяцев"
            })
    
    return sorted_courses

def test_original_data_sorting():
    result = sort_courses_by_duration(COURSES)
    
    # Проверяем порядок курсов
    assert result[0]['title'] == "Python-разработчик с нуля"
    assert result[0]['duration'] == 12
    assert result[1]['title'] == "Java-разработчик с нуля"
    assert result[1]['duration'] == 14
    assert result[2]['duration'] == 20
    assert result[3]['duration'] == 20
    
    # Проверяем сохранение оригинальных индексов
    assert result[0]['original_index'] == 2
    assert result[1]['original_index'] == 0
    assert set([result[2]['original_index'], result[3]['original_index']}) == {1, 3}

def test_original_data_formatted_output():
    result = sort_courses_by_duration(COURSES)
    
    assert result[0]['formatted'] == "Python-разработчик с нуля - 12 месяцев"
    assert result[1]['formatted'] == "Java-разработчик с нуля - 14 месяцев"
    assert "Fullstack-разработчик на Python - 20 месяцев" in [c['formatted'] for c in result]
    assert "Frontend-разработчик с нуля - 20 месяцев" in [c['formatted'] for c in result]

def test_original_data_grouping():
    result = sort_courses_by_duration(COURSES)
    durations = [c['duration'] for c in result]
    
    assert durations == [12, 14, 20, 20]
    assert len([c for c in result if c['duration'] == 20]) == 2

@pytest.mark.parametrize("index,expected", [
    (0, {"title": "Python-разработчик с нуля", "duration": 12}),
    (1, {"title": "Java-разработчик с нуля", "duration": 14}),
])
def test_original_data_first_courses(index, expected):
    result = sort_courses_by_duration(COURSES)
    
    assert result[index]['title'] == expected['title']
    assert result[index]['duration'] == expected['duration']
