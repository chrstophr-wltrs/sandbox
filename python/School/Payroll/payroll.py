PAY_LOGFILE = "paylog.txt"

employee_dict = {}
employees = []

class Classification:
    """An abstract class for an employee's classification."""
    def __init__(self):
        pass

    def compute_pay(self):
        """
        An abstract method for inheritance purposes,
        computes and returns the pay for an employee.
        """
        pass

    @staticmethod
    def parse_clas(class_id, sal = 0.0, comm = 0.0, hr = 0.0):
        """
        Returns Hourly, Salaried, or Commissioned depending on whether class_id = 1, 2, or 3

        Parameters:
            class_id (int/str): 1 = Salaried, 2 = Commissioned, 3 = Hourly
            sal (float/int): The employee's salary, if Salaried of Commissioned
            comm (float/int): The employee's commission rate, if Commissioned
            hr (float/int): The employee's hourly pay, if Hourly
        """
        if class_id in [1, '1']:
            return Salaried(sal)
        elif class_id in [2, '2']:
            return Commissioned(sal, comm)
        elif class_id in [3, '3']:
            return Hourly(hr)
        return Classification()

class Hourly(Classification):
    """
    The employee is paid hourly, using timecards and an hourly rate.

    Attributes:
        hourly_rate (float/int): Pay earned for an hour's work.
        timecards (list of float): Details each time the employee worked, and for how long.
    """
    
    def __init__(self, hourly_rate, timecards = []):
        self.hourly_rate = hourly_rate
        self.timecards = timecards
    
    def add_timecard(self, hours):
        """
        Adds a day's work to the employee's timecard.

        Parameters:
            hours (float/int): The number of hours the employee worked that day.
        """
        self.timecards.append(hours)
    
    def compute_pay(self):
        """Adds up unpaid hours from timecard, clears timecard, then returns the amount to be paid."""
        unpaid_hours_worked = sum(self.timecards)
        self.timecards = []
        pay = self.hourly_rate * unpaid_hours_worked
        return pay
    
    def __repr__(self):
        return "Hourly"

class Salaried(Classification):
    """
    The employee is paid based on salary.

    Attributes:
        salary (float): The money that would be earned after 1 yr of work.
    """

    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        """Salaried employee's are paid 1/24th of their salary each pay period."""
        pay = self.salary / 24
        return pay
    
    def __repr__(self):
        return "Salaried"

class Commissioned(Salaried):
    """
    The employee is commissioned, and is therefore paid based both on their salary, and a percentage commission of their sales.
    
    Inherits Salaried

    Attributes:
        salary (float): The money that would be earned after 1 yr of work.
        commission_rate (float): The percentage of each sale that is paid to the employee.
        receipts (list of float): A record of the sales for which the employee has not yet been paid.
    """

    def __init__(self, salary, commission_rate, receipts = []):
        """
        Constructs the Commissioned object classification for the employee has salary(float), commission rate(float), and receipts (list of floats), which is a record of their sales.

        Converts commission_rate to a percentage, if a number higher than 1 was passed as the commission_rate.

        Attributes:
            salary (float): The money that would be earned after 1 yr of work.
            commission_rate (float): The percentage of each sale that is paid to the employee.
            receipts (list of float)[optional]: A record of the sales for which the employee has not yet been paid.
        """
        super().__init__(salary)
        if commission_rate >= 1:
            self.commission_rate = commission_rate / 100
        else:
            self.commission_rate = commission_rate
        self.receipts = receipts
    
    def add_receipt(self, sale):
        """
        Adds a sale to the employee's record (receipts list).
        
        Parameters:
            sale (float/int): The amount of the sale.
        """
        self.receipts.append(sale)
    
    def remove_receipt(self, index):
        """
        Removes a sale from self.receipts at the specified index. Removes last entry, if no index is specified.

        Parameters:
            index (int): the index to remove
        """
        self.receipts.pop(index)
    
    def compute_pay(self):
        """
        Sums unpaid receipts, and calculates commission pay based on the employee's commission rate * unpaid sales.
        Calculates salary pay by dividing yearly salary by 24.
        Returns salary pay + commission pay.
        """
        unpaid_sales = sum(self.receipts)
        self.receipts = []
        commission = unpaid_sales * self.commission_rate
        salary_pay = super().compute_pay()
        pay = salary_pay + commission
        return pay
    
    def __repr__(self):
        return "Commissioned"

class Employee:
    """
    The employee class, which contains all the contact information, and methods to change classification as well as to issue payment.

    Attributes:
        emp_id (str): The employee id, used to look them up when necessary.
        first_name (str): Employee's first name.
        last_name (str): Employee's last name.
        full_name (str): Employee's first and last name, constructed from first_name and last_name.
        address (str): Employee's house number and the name of the street on which their house is located.
        city (str): Employee's city of residence.
        state (str): Employee's state of residence.
        zipcode (str): The state/postal code where the employee lives.
        full_address (str): The employee's full address, where they live, constructed from address, city, state, and zipcode.
        classification (Classification): Classification object, depends on whether the employee is paid hourly, is salaried, or is paid by commission.
        salary (float)[optional]: How much the employee is paid per year, if they are salaried or commissioned.
        commission (float)[optional]: The percentage which the employee earns, based on the sales they make, if they are commissioned. Automatically converted to a percentage, if a value greater than 1 is provided.
        hourly (float)[optional]: The employee's hourly pay rate, if they're an hourly employee.
    """

    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, clas = 1, salary = 0.0, commission = 0.0, hourly = 0.0):
        """
        Constructs the Employee object. Parameter labels are REQUIRED.
        Also constructs full_name and full_address
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
        self.classification = Classification.parse_clas(clas, salary, commission, hourly)
    
    def make_hourly(self, rate):
        """
        Changes an employee's classification to hourly, and sets their hourly rate.

        Parameters:
            rate (float): The amount the employee would earn after working 1 hour.
        """   
        self.classification = Hourly(rate)
        print(f"{self.full_name} is now an hourly employee, making ${rate}/hr.")
    
    def make_salaried(self, salary):
        """
        Changes an employee's classification to salaried, and sets their yearly salary.

        Parameters:
            salary (float): The amount the employee would earn after working 1 yr.
        """
        self.classification = Salaried(salary)
        print(f"{self.full_name} is now a salaried employee, making ${salary} a year.")

    def make_commissioned(self, salary, commission, receipts = []):
        """
        Changes an employee's classification to commissioned, sets their yearly salary, commission rate, and adds any receipts they might have.

        Parameters:
            salary (float): The amount the employee would earn after working 1 yr, excluding any sales.
            commission (float): The percentage of sales that is paid to the employee.
            receipts (list of float) [optional]: Any previous sales the employee has made.
        """
        self.classification = Commissioned(salary, commission, receipts)
        print(f"{self.full_name} is now a commissioend employee, making ${salary} a year, as well as earning {commission}% of sales.")
    
    def issue_payment(self):
        """Calculates and issues payment using the compute_pay() method, from the employee's classification object."""
        pay = round(self.classification.compute_pay(), 2)
        pay_string = (f"Mailing {pay} to {self.full_name} at {self.full_address}...")
        print(pay_string)
        with open(PAY_LOGFILE, 'a') as file:
            file.write(pay_string + "\n")
    
    def __repr__(self):
        return (f"{self.full_name}, {self.classification}")

def load_employees():
    """
    Opens 'employees.csv' and reads each line into an Employee object.
    
    Stores the employee object in employee_dict, with a key based on their emp_id.
    Stores the employee object in employees list, for iteration purposes.
    """
    print("Loading employees...")
    with open('employees.csv', 'r') as file:
        for line in file:
            line_list = line.strip().split(',')
            if line_list[0] == 'id':
                continue
            current_obj = Employee(emp_id = line_list[0], first_name = line_list[1], last_name = line_list[2], address = line_list[3], city = line_list[4], state = line_list[5], zipcode = line_list[6], clas = int(line_list[7]), salary = float(line_list[8]), commission = float(line_list[9]), hourly = float(line_list[10]))
            employee_dict[line_list[0]] = current_obj
            employees.append(current_obj)
    print("Loaded all employees from 'employees.csv'")

def find_employee_by_id(id):
    """
    Looks up the employee from employee_dict, given the id string.
    
    Parameters:
        id (str): the ID of the desired employee.
    """
    return employee_dict[id]

def process_timecards():
    """Reads in the timecard file.
    
    Looks up the employee by ID, given the first item of the line.
    Adds each of the remaining line items ([1:]) to the respective employee's timecard list.
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
    Reads in the receipts file.
    
    Looks up the employee by ID, given the first item of the line.
    Adds each of the remaining line items ([1:]) to the respective employee's receipts list.
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