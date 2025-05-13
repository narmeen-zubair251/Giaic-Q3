class Employee:
    def __init__(self , name , salary , ssn):
         self.name = name
         self._salary = salary
         self.__ssn = ssn

emp = Employee("Ahmed" , 45000 , "123-45-6789")
print(emp.name)
print(emp._salary)
print(emp._Employee__ssn) #Correct way to access private variable