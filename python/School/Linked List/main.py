from course import Course
from courselist import CourseList
import random
import math

def try_course_creation():
    # make sure that an empty course is correct
    c = Course()
    print(c.name())
    print(c.number())
    print(c.credit_hr())
    print(c.grade())
    print(c.next)

def try_course_creation_with_parameters():
    c = Course(1234, "Test Name", 3.0, 3.72)
    print(c.number())
    print(c.name())
    print(c.credit_hr())
    print(c.grade())
    print(c.next)

    print(Course("cat"))
    print(Course(1234, None))
    print(Course(1234, "Test Name", "cat"))
    print(Course(1234, "Test Name", 3.0, "cat"))
    print(Course(-1))
    print(Course(1234, "Test Name", -2.1))
    print(Course(1234, "Test Name", 0.0, -2.0))


def try_empty_courselist():
    cl = CourseList()
    print(cl.head)
    print(cl.size())
    print(cl.calculate_gpa())
    print(cl.calculate_gpa())
    print(cl.is_sorted())

def try_insert():
    random.seed(0)
    cl = CourseList()
    for _ in range(37):
        cl.insert(Course(random.randrange(1000, 7000), "test", 1.0, 2.0))

    print(cl.size())
    print(cl.is_sorted())

def try_remove():
    random.seed(0)
    cl = CourseList()
    courseNumbers = []
    for _ in range(37):
        courseNumbers.append(random.randrange(1000, 7000))
    for number in courseNumbers:
        cl.insert(Course(number, "test", 1.0, 2.0))

    course = cl.find(courseNumbers[0])
    print(course.number())
    course = cl.find(courseNumbers[10])
    print(course.number())
    course = cl.find(courseNumbers[36])
    print(course.number())

    for i in range(0, 30, 3):
        cl.remove(courseNumbers[i])

    print(cl.size())
    print(cl.is_sorted())

def try_remove_all():
    cl = CourseList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    cl.insert(Course(1800))
    print(cl.size())
    cl.remove_all(1200)
    print(cl.size())


def try_gpa():
    random.seed(0)
    cl = CourseList()
    total_credits = 0.0
    total_grade_points = 0.0
    for _ in range(10):
        credits = random.uniform(1.0, 5.0)
        grade = random.uniform(0.0, 4.0)
        total_credits += credits
        total_grade_points += credits * grade
        cl.insert(Course(1234, "Test", credits, grade))

    print(math.isclose(cl.calculate_gpa(), total_grade_points / total_credits))

def try_iterate_list():
    cl = CourseList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    totalCourses = 0
    for _ in cl:
        totalCourses += 1
    print(totalCourses)

def main():
    with open("data.txt", "r") as file:
        
        pass

if __name__ == "__main__":
    main()