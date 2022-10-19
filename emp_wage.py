import logging
import random

logging.basicConfig(filename="calculate_emp_wage.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Employee:

    def __init__(self, employee_parameters_dict):
        """
            Method for constructor
        """
        self.total_wage = 0
        self.total_emp_hrs = 0
        self.total_emp_days = 0
        self.name_of_emp = employee_parameters_dict.get("employee_name")
        self.emp_wage = employee_parameters_dict.get("employee_wage")
        self.max_working_hrs = employee_parameters_dict.get(
            "maximum_working_hrs")
        self.max_working_days = employee_parameters_dict.get(
            "maximum_working_days")

    def calculate_emp_wage(self):
        """
        Method for calculating employee wage, using while loop to calculate employee monthly wage including employee did part time, full time or absent
        :return:it will return total working hours and total employee wage
        """
        try:
            is_full_time = 1
            is_part_time = 2

            while self.total_emp_hrs < self.max_working_hrs and self.total_emp_days < self.max_working_days:

                emp_check = random.randrange(0, 3)
                if emp_check == is_full_time:
                    emp_hrs = 8
                    self.total_emp_days += 1
                elif emp_check == is_part_time:
                    emp_hrs = 4
                    self.total_emp_days += 1
                else:
                    emp_hrs = 0

                self.total_emp_hrs += emp_hrs
                self.total_wage += emp_hrs * self.emp_wage

        except Exception as e:
            logging.exception(e)


class Company:
    try:

        def __init__(self, company_name):
            self.company_name = company_name
            self.employee_dict = {}

        def add_emp(self, employee):
            """
            Function for adding the employee to the dictionary
            :param employee: using employee parameter as a object
            :return: will add employee to the dictionary
            """
            try:
                self.employee_dict.update(
                    {employee.name_of_emp: employee})
            except Exception as e:
                print(e)
                logging.exception(e)

        def get_emp(self, name_of_emp):
            """
            Function for get the employee from dictionary
            :param name_of_emp: using name_of_emp parameter as a object
            :return: return values of dictionary
            """
            return self.employee_dict.get(name_of_emp)
    except Exception as e:
        logging.error(e)

    def update_emp(self, employee, data_dict):
        """
        Method to update the employee information
        :param employee: using object for old information
        :param data_dict: using object for new information
        :return: will return updated employee information
        """
        try:
            employee.emp_wage = data_dict.get("update_wage")
            employee.max_working_hrs = data_dict.get(
                "update_working_hours")
            employee.max_working_days = data_dict.get(
                "update_working_days")

        except Exception as e:
            logging.exception(e)

    def delete_emp(self, name_of_emp):
        """
        Function for deleting the employee from the dictionary
        :param name_of_emp: using as a object to delete the employee
        :return: will delete the employee from dictionary
        """
        try:
            self.employee_dict.pop(name_of_emp, "Employee not found")
        except Exception as e:
            print(e)
            logging.exception(e)

    def display_employees(self):
        """
        Function for displaying dictionary
        :return: will return dictionary
        """
        try:
            print(
                " Employee Name \tEmployee Wage Per hrs \tTotal Working hours \tTotal working days")
            for key, value in self.employee_dict.items():
                print("\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t{}".format(value.name_of_emp, value.emp_wage,
                                                                    value.max_working_hrs, value.max_working_days))

        except ValueError:
            logging.error("Enter valid input")
        except Exception as e:
            logging.error(e)

    def display_employee_data(self, name_of_emp):
        """
        Function to dispay employee data
        :return: will return employee data
        """
        try:
            employee = self.get_emp(name_of_emp)
            if not employee:
                print("Employee not present")
            else:
                print("s.no\t\t\t\t\tDetails\t\t\t\t\t\t\t\t\tData")
                print("1.\t\t\tTotal employee wage for the month \t\t\t\t\t {}".format(
                    employee.total_wage))
                print("2.\t\t\tTotal days employee worked for the month \t\t\t {}".format(
                    employee.total_emp_days))
                print("3.\t\t\tTotal hours employee worked for the month \t\t\t {}".format(
                    employee.total_emp_hrs))
        except Exception as e:
            print(e)
            logging.exception(e)


class MultiCompanies:
    def __init__(self, ):
        self.company_dict = {}

    def add_company(self, company_object):
        """
        Function to add a company to company_dict dictionary
        """
        try:
            self.company_dict.update(
                {company_object.company_name: company_object})
        except Exception as e:
            print(e)
            logging.exception(e)

    def get_company_object(self, company_name):
        return self.company_dict.get(company_name)

    def display_company(self):
        """
        Function for displaying all the company stored in the dictionary
        """

        for company_name, company_object in self.company_dict.items():
            print(company_name)

    def remove_company(self, company_name):
        """
        Function to delete/remove a company from company_dict dictionary
        """
        self.company_dict.pop(company_name, "Company not present")


def add_employee():
    """
    Function for adding employee information
    :return: will add employee information in dictionary
    """
    try:
        company_name = input("Enter company name : ")
        company_object = multi_comp.get_company_object(company_name)
        if not company_object:
            company_object = Company(company_name)
            multi_comp.add_company(company_object)

        employee_name = input("Enter employee name : ")
        if employee_name == "":
            print("Please enter employee name")
            return
        employee_wage = int(input("Enter employee wage per hour : "))
        maximum_working_hrs = int(input("Enter employee work hours : "))
        maximum_working_days = int(input("Enter employee working days : "))

        emp_parameters = {"employee_name": employee_name, "employee_wage": employee_wage,
                          "maximum_working_hrs": maximum_working_hrs, "maximum_working_days": maximum_working_days}
        employee = Employee(emp_parameters)

        employee.calculate_emp_wage()

        company_object.add_emp(employee)

    except Exception as e:
        logging.exception(e)


def update_employee():
    """
    Function to update any employee data or information
    :return: will update data of employee
    """
    try:
        comp_name_to_update = input(
            "Enter company to update employee information : ")
        company_obj = multi_comp.get_company_object(
            comp_name_to_update)
        employee_name = input("Enter employee name to update his details : ")
        emp_object = company_obj.get_emp(employee_name)
        if not emp_object:
            print("Employee not present")
        else:
            update_wage = int(input("Enter new wage to update : "))

            update_working_hours = int(
                input("Enter new working hours to update : "))

            update_working_days = int(
                input("Enter new working days to update : "))

            company_obj.update_emp(emp_object, {
                "update_wage": update_wage,
                "update_working_hours": update_working_hours,
                "update_working_days": update_working_days})


    except Exception as e:
        logging.exception(e)


def display_employee():
    """
    Function to display specific employee information
    """
    try:
        company_name = input("Enter company to view employees : ")
        company_object = multi_comp.get_company_object(company_name)
        company_object.display_employees()

    except ValueError:
        logging.error("Enter valid input")
    except Exception as e:
        logging.error(e)


def display_employee_monthly_info():
    """
    Function to display employee monthly wage information
    """
    try:
        company_name = input("Enter company to view employee wage information : ")
        company_object = multi_comp.get_company_object(company_name)
        employee_name = input(
            "Enter name of the employee you want the wage information of : ")
        company_object.display_employee_data(employee_name)

    except ValueError:
        logging.error("Enter valid input")
    except Exception as e:
        logging.error(e)


def delete_employee():
    """
    Function for delete employee from dictionary
    :return: will delete the employee and his data from dictionary
    """
    try:
        company_name = input("Enter company to delete employees : ")
        company_object = multi_comp.get_company_object(company_name)
        employee_name = input("Enter employee name : ")
        company_object.delete_emp(employee_name)

    except ValueError:
        logging.error("Enter valid input")
    except Exception as e:
        logging.error(e)


def display_companies():
    """
    Function to display all companies
    """
    multi_comp.display_company()


def delete_company():
    """
    Function to delete a company from dictionary
    """
    try:
        company_name = input("Enter company name to delete : ")
        multi_comp.remove_company(company_name)
        company_object = multi_comp.get_company_object(company_name)
        if not company_object:
            print("There is no", company_name, "company, Enter correct one")

    except ValueError:
        logging.error("Enter valid input")
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    try:
        multi_comp = MultiCompanies()

        while True:
            print("Enter 1 to add employee")
            print("Enter 2 to update employee")
            print("Enter 3 to delete employee")
            print("Enter 4 to display companies")
            print("Enter 5 to display employee")
            print("Enter 6 to display employee monthly information")
            print("Enter 7 to delete company")
            print("Enter 0 to Exist")

            choice = int(input("Enter any number between 0-7"))

            options = {1: add_employee,
                       2: update_employee,
                       3: delete_employee,
                       4: display_companies,
                       5: display_employee,
                       6: display_employee_monthly_info,
                       7: delete_company}

            if choice == 0:
                break
            else:
                options.get(choice)()

    except ValueError:
        logging.error("Enter valid input")
    except Exception as e:
        logging.exception(e)
