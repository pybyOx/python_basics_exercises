def create_list_and_calculation_length(dictionary):
    return (list({interest for value in dictionary.values() for interest in value['interests']}),
            sum([len(dictionary[key]['surname']) for key in dictionary]))


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


print('Список пар «ID студента — возраст»:', [(index, value['age']) for index, value in students.items()])

interests_list, total_surname = create_list_and_calculation_length(students)

print('Полный список интересов всех студентов:', interests_list)
print('Общая длина всех фамилий студентов:', total_surname)
