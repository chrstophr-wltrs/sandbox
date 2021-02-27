from course import Course
from courselist import CourseList
from pylint import epylint as lint

def main():
    from pylint import epylint as lint
    import re
    
    (pylint_stdout, pylint_stderr) = lint.py_run('course.py', return_std=True)
    actual = pylint_stdout.getvalue()
    x = re.findall('at [0-9].[0-9]+', actual)[0]
    x = float(x.split()[-1])
    print(x)

if __name__ == "__main__":
    main()