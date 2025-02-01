#oops module
class Employee(object):
    #constructor 
    def __init__(self,empno,ename,salary=500):
        self.eno=empno #instance variables/properties
        self.name=ename 
        self.pay=salary
        self.__bonus=10000 #private instance property


    def showDetails(self): #instance method
        print('Empno',self.eno)
        print('Emp name',self.name)
        print('Salary',self.pay)
        print('total amount',self.pay+self.__bonus)

#------------------------------
if __name__=='__main__':
    e1=Employee(100,"shankar",40000)
    e1.showDetails()
    e1=Employee(101,"swamy",50000)
    e1.showDetails()