class Course:
    """
    Nodes of a linked list

    Represents a computer science course at Some Univeristy

    Attributes:
        number(int): the course number, ex: 2300
        name(str): the course name, ex: "Web Programming"
        credit_hr(float): the credit hours the course contributes to a degree or certification
        grade(float): the grade the student has received in the course
        next(Course): the next course in the linked list
        prev(Course): the previous course in the linked list
    """

    def __init__(self, number:int = 0, name:str = "", credit_hr:float = 1, grade:float = 0.0):
        self.number = int(number)
        self.name = str(name)
        self.credit_hr = float(credit_hr)
        self.grade = float(grade)
        self.next = None
        self.prev = None

    def number(self):
        """retrieve Course Number as an integer"""
        return self.number

    def name(self):
        """retrieve Course Name as a string"""
        return self.name

    def credit_hr(self):
        """retrieve Credits as a floating-point number"""
        return self.credit_hr

    def grade(self):
        """retrieve Grade as a numeric value in range 4.0 – 0.0"""
        return round(self.grade, 1)

    def __str__(self):
        """returns a string representing a single Course"""
        return f"cs{self.number} {self.name} Grade:{self.grade:.1f} Credit Hours: {self.credit_hr:.1f}"