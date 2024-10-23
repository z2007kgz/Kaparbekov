
courses = {'Math': ['Alice', 'Bob'], 'History': ['Charlie']}

def add_student_to_course(course_name, student_name):
    if course_name in courses:
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]

def show_students_in_course(course_name):
    if course_name in courses:
        print(f"Студенты, записанные на курс {course_name}: {', '.join(courses[course_name])}")
    else:
        print(f"Курс {course_name} не найден.")

add_student_to_course('Math', 'David')
add_student_to_course('Science', 'Emily')

show_students_in_course('Math')
show_students_in_course('Science')
