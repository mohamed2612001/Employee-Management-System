from All_employee import *

from finance import *

from Exceptions import *

class Employee:
    def __init__(self,name,age,job,id,phone,bank_account,hour_rate,hours_work,from_file=False):
        self.name=name
        self.age=age
        self.job=job
        self.id=id
        self.__phone=phone
        self.__bank_account=bank_account
        self.__hour_rate=hour_rate
        self.hours_work=hours_work
        if  not from_file:
            AllEmployees.nums_employees+=1
            AllEmployees.add_employee(self)
        
    @staticmethod
    def is_valid_phone(new_phone):
        return isinstance(new_phone,str) and len(new_phone)==13 and new_phone.startswith("+20")
    
    @property
    def hour_rate(self):
        return self.__hour_rate
    @hour_rate.setter
    def hour_rate(self,new_hour_rate):
        if new_hour_rate > 0:
            self.__hour_rate=new_hour_rate
        else:
            raise HourRateError("Hour Rate should be positive")
        
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,new_phone):
        if Employee.is_valid_phone(new_phone):
            self.__phone=new_phone
        else:
            raise PhoneError (f"this phone is wrong ")
    @property
    def bank_account(self):
        return self.__bank_account
    
    @bank_account.setter
    def bank_account(self,new_bank_account):
        self.__bank_account==new_bank_account

            
    def __str__(self):
        return f"his name is {self.name} works as {self.job}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} \
    name:{self.name} \
    job:{self.job}\
    phone:{self.__phone}\
    bank_account:{self.__bank_account}\
    hour_rate:{self.__hour_rate}\
    hours_work:{self.hours_work}"
    
    def gross_salary(self) :
        return self.__hour_rate *self.hours_work
    
    def calculate_net_salary(self):
       gross_salary=self.gross_salary()
       return Finance.calculate_net_salary(gross_salary)