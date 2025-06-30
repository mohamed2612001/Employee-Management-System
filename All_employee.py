from Exceptions import *

class AllEmployees:
    nums_employees=0
    all_employees=[]
    
    @classmethod
    def  add_employee(cls,employee):
        if employee in cls.all_employees:
            print(f"we add this employee before")
        else :
            cls.all_employees.append(employee)
            cls.nums_employees+=1
            
    @classmethod
    def get_employee_by_id(cls,id):
        for emp in cls.all_employees:
            if emp.id==id:
                return emp
        raise EmployeeNotFound("this employee not found in our list")
    
    @classmethod
    def remove_employee(cls,emp):
        try:
            emp=cls.get_employee_by_id(emp.id)
            cls.all_employees=[ employee for employee in cls.all_employees if employee.id !=emp.id]
            cls.nums_employees-=1
        except Exception as e:
            print(e)

    @classmethod
    def list_all_employees(cls):
        return cls.all_employees