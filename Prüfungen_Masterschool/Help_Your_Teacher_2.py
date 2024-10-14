def get_grade(subject):
    """Get grade for a subject from 1-6. Handel false inputs"""
    while True:
        try:
            grade = float(input(f'Enter {subject} grade:'))
            if 1 <= grade <= 6:
                return grade
        except ValueError:
            print('Invalid input, please enter a positive numeric input.')


def get_number_of_students():
    """Get number of students to add Handel false inputs"""
    while True:
        try:
            number_of_students = int(input(f'Enter number of students:'))
            return number_of_students
        except ValueError:
            print('Invalid input, please enter a positive numeric input.')


def get_student_info():
    """Gather student Information and return them in a list of dictionarys"""
    list_of_students = []
    for _ in range(get_number_of_students()):
        student_name = input('Enter student name:')
        english_grade = get_grade("English")
        math_grade = get_grade("Math")
        student_info = {"name": student_name,
                        "english": english_grade,
                        "math": math_grade}
        list_of_students.append(student_info)
    return list_of_students


def print_student_info(list_of_students):
    """Calculate Student áverage and best grade and print out student Info"""
    print("Student Information:")
    for student in list_of_students:
        if student["english"] < student["math"]:
            best_grade = student["english"]
        else:
            best_grade = student["math"]
        average_grade = (student["english"] + student["math"]) / 2
        name = student["name"]
        print(f'Student: {name}, Best Grade: {best_grade}, Average Grade: {average_grade}')


def calculate_average_grades(list_of_students):
    """Calculates the average grades of the subjects and overall and returns it"""
    list_of_english_grades = []
    list_of_math_grades = []
    for students in list_of_students:
        list_of_english_grades.append(students['english'])
        list_of_math_grades.append(students['math'])
    average_grade_english = sum(list_of_english_grades) / len(list_of_english_grades)
    average_grade_math = sum(list_of_math_grades) / len(list_of_math_grades)
    average_grade_overall = (average_grade_english + average_grade_math) / 2
    return average_grade_english, average_grade_math, average_grade_overall


def print_average_grades_info(average_grades_info):
    """Prints the average grades of the subjects and overall"""
    average_grade_english, average_grade_math, average_grade_overall = average_grades_info
    print()
    print('Average grades per subject:')
    print(f'English: {average_grade_english}')
    print(f'Math: {average_grade_math}')
    print(f'Overall average grade across all subjects: {average_grade_overall}')
    print()


def grade_to_points(grade):
    """Transforms the grade into points"""
    if grade == 1:
        return 100
    elif grade == 2:
        return 85
    elif grade == 3:
        return 70
    elif grade == 4:
        return 60
    elif grade == 5:
        return 50
    elif grade == 6:
        return 30


def calculate_failing_grades(list_of_students):
    """Calculate the amount of failed subjects of students and put them with the name into a dictionary.
     Also calculate overall failed subjects. And return both """
    number_of_overall_failed_subjects = 0
    failed_students = {}
    for student in list_of_students:
        number_of_failed_subjects = 0
        points_english = grade_to_points(student['english'])
        points_math = grade_to_points(student["math"])
        student_name = student['name']
        if points_english < 55:
            number_of_failed_subjects += 1
            number_of_overall_failed_subjects += 1
        if points_math < 55:
            number_of_failed_subjects += 1
            number_of_overall_failed_subjects += 1
        if number_of_failed_subjects > 0:
            failed_students[student_name] = number_of_failed_subjects
    return failed_students, number_of_overall_failed_subjects


def print_failed_grades(failed_subjects_data):
    """Print data of failed students"""
    failed_students, number_of_overall_failed_subjects = failed_subjects_data
    print('Failing grades per student:')
    for student, amount_failed_subjects in failed_students.items():
        print(f'{student}: {amount_failed_subjects} failing grade(s)')
    print(f'Total number of failing grades across all students: {number_of_overall_failed_subjects}')


def main():
    list_of_students = get_student_info()
    print_student_info(list_of_students)
    print_average_grades_info(calculate_average_grades(list_of_students))
    print_failed_grades((calculate_failing_grades(list_of_students)))


if __name__ == "__main__":
    main()





