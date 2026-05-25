students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


print('Список пар «ID студента — возраст»:',
      [(index, value['age']) for index, value in students.items()])

print('Полный список интересов всех студентов:',
      list({interest for value in students.values() for interest in value['interests']}))

print('Общая длина всех фамилий студентов:',
      sum([len(students[id_s]['surname']) for id_s in students]))

