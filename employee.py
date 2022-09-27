"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly=0, contractHours=0, contractPay=0,comission=0,comissionTime=0,bonus=0):
        self.name = name
        self.monthly = monthly
        self.contractHours = contractHours
        self.contractPay = contractPay
        self.comission = comission
        self.comissionTime = comissionTime
        self.bonus = bonus

    def get_pay(self):
        return self.monthly + self.contractHours*self.contractPay + self.comission * self.comissionTime + self.bonus

    def __str__(self):
        part1 =""
        part2=""
        part3=""
        if self.monthly!=0:
            part1=str(self.name)+" works on a monthly salary of "+str(self.monthly)
        else:
            part1=self.name+" works on a contract of "+str(self.contractHours)+" hours at "+str(self.contractPay)+"/hour"
        if self.comission!=0:
            part2=" and receives a commission for "+str(self.comissionTime)+" contract(s) at "+str(self.comission)+"/contract"
        if self.bonus!=0:
            part3=" and receives a bonus commission of "+str(self.bonus)
        pay = self.get_pay()
        part4=".  Their total pay is " + str(pay) + "."
        return part1+part2+part3+part4


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contractHours=100, contractPay=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly=3000, comission=200, comissionTime=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contractHours=150, contractPay=25, comission=220, comissionTime=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contractHours=120, contractPay=30, bonus=600)
