class Finance: 
    
    TAX_THRESHOLD=6000
    TAX_LOW = .1
    TAX_HIGH = .3
    HEALTH_INSURANCE_COST = 200
    RETIREMENT_CONTRIBUTION_RATE = .02
    
    @classmethod
    def calculate_tax(cls,salary):
        if(salary < cls.TAX_THRESHOLD):
           return salary * .1
        else:
           return salary * .3
       
    @classmethod
    def calculate_net_salary(cls, salary):
        tax = cls.calculate_tax(salary)
        health = salary * (cls.RETIREMENT_CONTRIBUTION_RATE)
        total_dedctions = tax + health + cls.HEALTH_INSURANCE_COST
        return (salary - total_dedctions)