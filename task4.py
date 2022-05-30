if __name__ == '__main__':
    print("Question 1")
    employees = {'emp1': {'name': 'Bille', 'salary': 7500},
                 'emp2': {'name': 'Israel', 'salary': 8005},
                 'emp3': {'name': 'Katherine', 'salary': 5010}
                 }
    total_salary = 0

    for value in employees.values():
        total_salary += value['salary']

    print("Total salary = ", total_salary)

    print("Question 2")

    subjects = {'Physics': 82, 'Math': 65, 'history': 40}
    key_min = min(subjects, key=subjects.get)
    print('The minimum key is ' + key_min)

