from course import Course
from courselist import CourseList

def main():
    my_courses = CourseList()
    with open("data.txt", "r") as file:
        for line in file:
            line_list = line.strip().split(",")
            new_course = Course(line_list[0], line_list[1], line_list[2], line_list[3])
            my_courses.insert(new_course)
    print(my_courses)

if __name__ == "__main__":
    main()