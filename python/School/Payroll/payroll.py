PAY_LOGFILE = "paylog.txt"

employee_dict = {}
employees = []

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
    
    def __init__(self, hourly_rate, timecards = []):
        self.hourly_rate = hourly_rate
        self.timecards = timecards
    
    def add_timecard(self, hours):
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
        pay = self.hourly_rate * unpaid_hours_worked
        return pay
    
    def __repr__(self):
        return "Hourly"

class Salaried(Classification):
    """
    The employee is paid based on salary.
    """

    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        """
        Salaried employee's are paid 1/24th
        of their salary each pay period.
        """
        pay = self.salary / 24
        return pay
    
    def __repr__(self):
        return "Salaried"

class Commissioned(Salaried):
    """
    Employee is commissioned, and is therefore paid based
    both on their salary, and a commission of their sales.
    """
    def __init__(self, salary, commission_rate, receipts = []):
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
    
    def remove_receipt(self, index):
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
        pay = salary_pay + commission
        return pay
    
    def __repr__(self):
        return "Commissioned"

class Employee:
    """
    An employee, contains all the contact information, and methods
    to change classification as well as issue payment.
    """
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification, salary, commission, hourly):
        """
        All values should be strings, except for classification (int)
        and salary, commission, and hourly, which should be floats.
        """
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.full_address = (f"{address} {city}, {state} {zipcode}").title()
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
    
    def make_hourly(self, rate):
        """
        Changes an employee's classification to hourly,
        and sets their hourly rate.
        """   
        self.classification = Hourly(rate)
        print(f"{self.full_name} is now an hourly employee, making ${rate}/hr.")
    
    def make_salaried(self, salary):
        """
        Changes an employee's classification to salaried,
        and sets their yearly salary.
        """
        self.classification = Salaried(salary)
        print(f"{self.full_name} is now a salaried employee, making ${salary} a year.")

    def make_commissioned(self, salary, commission, receipts = []):
        """
        Changes an employee's classification to commissioned,
        sets their yearly salary, commission rate, and adds any
        receipts they might have.
        """
        self.classification = Commissioned(salary, commission, receipts)
        print(f"{self.full_name} is now a commissioend employee, making ${salary} a year, as well as earning {commission}% of sales.")
    
    def issue_payment(self):
        """
        Calculates and issues payment using the compute_pay() method,
        from the employee's classification.
        """
        pay = round(self.classification.compute_pay(), 2)
        pay_string = (f"Mailing {pay} to {self.full_name} at {self.full_address}...")
        print(pay_string)
        with open(PAY_LOGFILE, 'a') as file:
            file.write(pay_string + "\n")
    
    def __repr__(self):
        return (f"{self.full_name}, {self.classification}")

def load_employees():
    """
    Opens 'employees.csv' and reads each line into
    an Employee object, then stores the object in the
    employees dictionary, with a key based on the
    employee ID.
    """
    print("Loading employees...")
    with open('employees.csv', 'r') as file:
        for line in file:
            line_list = line.strip().split(',')
            if line_list[0] == 'id':
                continue
            current_obj = Employee(line_list[0], line_list[1], line_list[2], line_list[3], line_list[4], line_list[5], line_list[6], line_list[7], float(line_list[8]), float(line_list[9]), float(line_list[10]))
            employee_dict[line_list[0]] = current_obj
            employees.append(current_obj)
    print("Loaded all employees from 'employees.csv'")

def find_employee_by_id(id):
    """
    Looks up the employee from the dictionary, given the id string.
    """
    return employee_dict[id]

def process_timecards():
    """
    Reads in the timecard file, and adds each of the hours
    to the respective employee.
    """
    print("Loading timecards from 'timecards.csv'...")
    with open('timecards.csv', 'r') as file:
        for line in file:
            line_list = line.strip().split(',')
            emp = find_employee_by_id(line_list[0])
            clas = emp.classification
            print(f"Adding hours for {emp.full_name}...")
            for item in line_list[1:]:
                clas.add_timecard(float(item))
    print("Processed timecards.")

def process_receipts():
    """
    Reads in the receipts file, and adds each of the sales
    to the respective employee.
    """
    print("Loading sales receipts from 'receipts.csv'...")
    with open('receipts.csv', 'r') as file:
        for line in file:
            line_list = line.strip().split(',')
            emp = find_employee_by_id(line_list[0])
            clas = emp.classification
            print(f"Adding sales for {emp.full_name}...")
            for item in line_list[1:]:
                clas.add_receipt(float(item))
    print("Processed sales receipts.")