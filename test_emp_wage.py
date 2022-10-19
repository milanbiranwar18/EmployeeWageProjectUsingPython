import pytest

from emp_wage import Employee, Company, MultiCompanies


@pytest.fixture
def employee():
    return Employee(
        {"employee_name": "milan", "employee_wage": 10, "maximum_working_hrs": 12, "maximum_working_days": 26})


@pytest.fixture
def company():
    return Company("sunflag")


@pytest.fixture
def multi_comp():
    return MultiCompanies()


def test_calculate_emp_wage(employee, company):
    company.add_emp(employee)
    totalwage = employee.calculate_emp_wage()
    assert totalwage


def test_add_employee(employee, company):
    assert len(company.employee_dict) == 0
    company.add_emp(employee)
    assert len(company.employee_dict) == 1


def test_get_emp(employee, company):
    company.add_emp(employee)
    actual = company.get_emp(employee.name_of_emp)
    assert actual.name_of_emp == "milan"


def test_delete_emp(employee, company):
    company.add_emp(employee)
    company.delete_emp("milan")
    assert not company.get_emp("milan")


def test_multi_company_dict_length(company):
    comp = MultiCompanies()
    assert len(comp.company_dict) == 0
    comp.add_company(company)
    assert len(comp.company_dict) == 1


def test_company(company, multi_comp):
    multi_comp.add_company(company)
    assert company == multi_comp.get_company_object("sunflag")
    assert company != multi_comp.get_company_object("")


def test_remove_company_method(company, multi_comp):
    multi_comp.add_company(company)
    multi_comp.remove_company("sunflag")
    assert not multi_comp.get_company_object("sunflag")
