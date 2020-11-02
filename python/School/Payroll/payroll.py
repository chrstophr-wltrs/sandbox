class Classification:
    def __init__(self):
        pass

    def compute_pay(self):
        """
        An abstract method for inheritance purposes,
        computes and returns the pay for an employee.
        """
        pass

class Hourly(Classification):
    """
    The employee is paid hourly, using timecards and an hourly rate.
    """
    
    def __init__(self, hourly_rate = float, timecards = []):
        self.hourly_rate = hourly_rate
        self.timecards = timecards
    
    def add_timecard(self, hours = float):
        """
        Adds a day's work to the employee's timecard.
        """
        self.timecards.append(hours)
    
    def compute_pay(self):
        """
        Adds up unpaid hours, clears the timecard,
        then returns the amount to be paid.
        """
        unpaid_hours_worked = sum(self.timecards)
        self.timecards = []
        pay = round((self.hourly_rate * unpaid_hours_worked), 2)
        return pay

class Salaried(Classification):
    """
    The employee is paid based on salary.
    """

    def __init__(self, salary = float):
        self.salary = salary

    def compute_pay(self):
        """
        Salaried employee's are paid 1/24th
        of their salary each pay period.
        """
        pay = round((self.salary / 24), 2)
        return pay

class Commissioned(Salaried):
    """
    Employee is commissioned, and is therefore paid based
    both on their salary, and a commission of their sales.
    """
    def __init__(self, salary = float, commission_rate = float, receipts = []):
        """
        Employee has salary, commission rate, and
        receipts (list of floats), which is a record of their sales.
        """
        super().__init__(salary)
        if commission_rate >= 1:
            self.commission_rate = commission_rate / 100
        else:
            self.commission_rate = commission_rate
        self.receipts = receipts
    
    def add_receipt(self, sale):
        """
        Adds a sale (int) to the employee's record.
        sale should be an int or float.
        """
        self.receipts.append(sale)
    
    def remove_receipt(self, index = int):
        """
        Removes a sale from self.receipts at the
        specified index. index must always be an int.
        Will remove last entry, if no index is specified.
        """
        self.receipts.pop(index)
    
    def compute_pay(self):
        """
        Returns the calculated commission based on 
        unpaid receipts and commission rate plus 1/24th
        of the salary. Clears self.receipts.
        """
        unpaid_sales = sum(self.receipts)
        self.receipts = []
        commission = unpaid_sales * self.commission_rate
        salary_pay = self.salary / 24
        pay = round((salary_pay + commission), 2)
        return pay

class Employee:
    """
    An employee, contains all the contact information, and methods
    to change classification as well as issue payment.
    """
    def __init__(self, emp_id = str, first_name = str, last_name = str, address = str, city = str, state = str, zipcode = str, classification = int, salary = float, commission = float, hourly = float):
        """
        All values should be strings, except for classification (int)
        and salary, commission, and hourly, which should be floats.
        """
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.salary = salary
        self.commission = commission
        self.hourly = hourly        
        if classification in [1, '1']:
            self.classification = Salaried(self.salary)
        elif classification in [2, '2']:
            self.classification = Commissioned(self.salary, self.commission)
        elif classification in [3, '3']:
            self.classification = Hourly(self.hourly)
        else:
            self.classification = Classification()
    
    def make_hourly(self, rate=float):
        """
        Changes an employee's classification to hourly,
        and sets their hourly rate.
        """   
        self.classification = Hourly(rate)
    
    def 
