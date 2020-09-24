"""
Add three methods to the Student class that compare twoStudent objects.
One method (__eq__) should test for equality.
A second method (__lt__) should test for less than.
The third method (__ge__) should test for greater than or equal to.
In each case, the method returns the result of the comparison of the two students’ names.
Include a main function that tests all of the comparison operators.

Note: The program should output in the following format:

False: False
True: True
True: True
False: False
True: True
True: True
True: True
True: True
True: True
True: True
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    # Write method definitions here
    def __eq__(self, second):
        """Compare two student names for equality"""
        if self.getName() == second.getName():
            return True
        else:
            return False
    
    def __lt__(self, second):
        """Test if first name is less than second name"""
        if self.getName() < second.getName():
            return True
        else:
            return False
    
    def __ge__(self, second):
        """Test if first name is greater than second name"""
        if self.getName() >= second.getName():
            return True
        else:
            return False

def main():
    """A simple test."""
    ken = Student("Ken", 5)
    for i in range(1, 6):
        ken.setScore(i, 100)
    ken2 = Student("Ken", 7)
    for i in range(1, 8):
        ken2.setScore(i, 90)
    print(f"{ken.__eq__(ken2)}: {ken2.__eq__(ken)}")

if __name__ == "__main__":
    main()
