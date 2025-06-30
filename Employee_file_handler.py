import csv

from employee import *

class EmployeeFileHandler:
    
    @staticmethod
    def read_csv_file(file_name):
        with open(file_name) as f:
            file=csv.DictReader(f)
            return (file)
        
    @classmethod
    def append_employees_in_list(cls,file_name):
       employees=cls.read_csv_file(file_name)
       for em in employees:
            name=em["name"]
            phone=em["phone"]
            bank_account=em["bank_account"]
            age=em["age"]
            job=em["job_title"]
            Id=em["id"]
            hours_worked=int(em["hours_worked"])
            hour_rate=int(em["hour_rate"])
            Employee(name,age,job,Id,phone,bank_account,hour_rate,hours_worked,from_file=True)
            
    @staticmethod
    def update_employees(file_name):
        with open(file_name,"w",newline="") as f:

            csv_file=csv.DictWriter(f,fieldnames=["name","age","job_title","id","phone","bank_account","hours_worked","hour_rate","net_salary"])
            employees=AllEmployees.list_all_employees()
            csv_file.writeheader()
            for emp in employees:
                employee={}
                net_salary=emp.calculate_net_salary()
                employee["name"]=emp.name
                employee["age"]=emp.age
                employee["job_title"]=emp.job
                employee["id"]=emp.id
                employee["phone"]=emp.phone
                employee["bank_account"]=emp.bank_account
                employee["net_salary"]=net_salary
                employee["hours_worked"]=emp.hours_work
                employee["hour_rate"]=emp.hour_rate 
                csv_file.writerow(employee)