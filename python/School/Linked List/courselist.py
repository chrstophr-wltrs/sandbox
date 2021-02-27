from course import Course


class CourseList:
    """
    Linked list representing all of the courses for 1 student at a university

    NOTE: All uses of 'crnt' represent the current node being iterated upon.

    Attributes:
        head(Course): the first course of the list, completely empty except for the next pointer
    """

    def __init__(self):
        self.head = None
        self.n = None

    def insert(self, course_to_insert: Course = None):
        """
        insert the specified Course in Course number ascending order

        Parameters:
            course_to_insert(Course): the Course object you want to insert into the linked list
        """
        if self.head == None:
            self.head = Course()
        crnt = self.head
        course_no = course_to_insert.number()
        while crnt.next != None:
            if (course_no >= crnt.number()) and (course_no < crnt.next.number()):
                course_to_insert.next = crnt.next
                course_to_insert.prev = crnt
                crnt.next.prev = course_to_insert
                crnt.next = course_to_insert
                return self
            crnt = crnt.next
        crnt.next = course_to_insert
        course_to_insert.prev = crnt
        return self

    def remove(self, number: int):
        """
        remove the first occurrence of the specified Course

        Parameters:
            number(int): the course number for the Course you want to remove
        """
        crnt = self.head
        while crnt.next != None:
            if crnt.number() == number:
                old_next = crnt.next
                old_prev = crnt.prev
                old_prev.next = old_next
                old_next.prev = old_prev
                break
            crnt = crnt.next
        return self

    def remove_all(self, number: int):
        """
        removes ALL occurrences of the specified Course

        Parameters:
            number(int): the course number for the Course you want to remove
        """
        crnt = self.head
        while crnt.next != None:
            if crnt.number() == number:
                crnt.next.prev = crnt.prev
                crnt.prev.next = crnt.next
            crnt = crnt.next
        return self

    def find(self, number: int):
        """
        find the first occurrance of the specified course in the list or return -1

        Parameters:
            number(int): the course number for the Course you want to remove
        """
        crnt = self.head
        while crnt.next != None:
            if crnt.number() == number:
                return crnt
            crnt = crnt.next
        return -1

    def size(self):
        """return the number of items in the list"""
        if self.head == None:
            return 0
        crnt = self.head
        size = 0
        while crnt.next != None:
            size += 1
            crnt = crnt.next
        return size

    def calculate_gpa(self):
        """return the GPA using all courses in the list"""
        if self.head == None:
            return 0.0
        total_points = 0
        hrs = 0
        crnt = self.head
        while crnt != None:
            points = crnt.credit_hr() * crnt.grade()
            total_points += points
            hrs += crnt.credit_hr()
            crnt = crnt.next
        return total_points / hrs

    def is_sorted(self):
        """return True if the list is sorted by Course Number, False otherwise"""
        if self.head == None:
            return True
        crnt = self.head.next
        while crnt.next != None:
            if crnt.number() < crnt.prev.number():
                return False
            crnt = crnt.next
        return True

    def __str__(self):
        """returns a string with each Course’s data on a separate line"""
        list_str = f"Current List: ({self.size()})"
        crnt = self.head.next
        while crnt != None:
            list_str += f"\n{crnt.__str__()}"
            crnt = crnt.next
        return list_str

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
        if self.n.next == None:
            raise StopIteration
        self.n = self.n.next
        return self.n.prev
