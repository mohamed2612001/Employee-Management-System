from All_employee import *

from employee import *

from Employee_file_handler import *

class Manager(Employee):    
    BONUS=500
    MINIMUM_HOURLY_RATE = 10
    
    MIN_LEVEL_TO_REJECT_EMPLOYEE = 3
    MIN_LEVEL_TO_DEACREASE_HOURLY_RATE = 2

    
    def __init__(self,*args,authority=1,**kwargs):
        super().__init__(*args,**kwargs)
        self.authority=authority
        
    def calculate_net_salary(self):
        return super().calculate_net_salary() + Manager.BONUS
    
    def check_authority(self,low_level_authority):
        if self.authority<low_level_authority:
            raise AuthourityLow("your authority doesnot allow you to do this action")
    
    def reject_employee(self,emp):
        try:
            self.check_authority(Manager.MIN_LEVEL_TO_REJECT_EMPLOYEE)
            employee=AllEmployees.get_employee_by_id(emp.id)
            AllEmployees.remove_employee(employee)
        except Exception as e:
            print(e)
            
    @staticmethod
    def is_hour_rate_bigger_than_ten(new_hour_rate):
        return  (new_hour_rate) > Manager.MINIMUM_HOURLY_RATE
    
    def reduce_hour_rate(self,emp,new_hour_rate):
        try:

            self.check_authority(Manager.MIN_LEVEL_TO_DEACREASE_HOURLY_RATE)
            employee=AllEmployees.get_employee_by_id(emp.id)
            if Manager.is_hour_rate_bigger_than_ten(new_hour_rate):
                employee.hour_rate=new_hour_rate
            else:
                employee.hour_rate = Manager.MINIMUM_HOURLY_RATE
                print(f"we change hour rate to {Manager.MINIMUM_HOURLY_RATE}$")        
        except Exception as e:
            print(e)
            
    def promotion_employee(self,emp,new_hour_rate):
        employee=AllEmployees.get_employee_by_id(emp.id)
        employee.hour_rate=new_hour_rate



