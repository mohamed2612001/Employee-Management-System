
class PhoneError(Exception):
    """check the length of number equal 13 , its type is str , and starts with +20"""
    pass

class HourRateError(Exception):
    """check the hour rate is bigger than Zero"""
    pass

class EmployeeNotFound(Exception):
    """is employee in list_all_employees"""
    pass

class AuthourityLow(Exception):
    pass