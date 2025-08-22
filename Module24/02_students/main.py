from random import randint
from statistics import mean


class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def average_grade(self):
        return mean(self.grades)


def create_students():
    students_list = []
    for number in range(1, 11):
        print('\nСтудент {}:'.format(number))
        name = input('Фамилия Имя: ')
        group = randint(1, 5)
        grades = [randint(1, 5) for _ in range(5)]
        students_list.append(Student(name, group, grades))
    return students_list


def sort_students(students_list):
    return sorted(students_list, key=lambda student: student.average_grade())


def print_students(students_list):
    for student in students_list:
        print('\nФИ: {}\nНомер группы: {}\nОценки: {}\nСредний балл: {}'.format(
            student.name, student.group, student.grades, student.average_grade()))


students = create_students()
sorted_students = sort_students(students)
print('\nСписок студентов, отсортированный по среднему баллу:')
print_students(sorted_students)
