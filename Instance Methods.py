#instance
class Student:
    def __init__(self,m1,m2,m3): #it is a special argument
        self.m1=m1         #m1,m2,m3 are instance methods
        self.m2=m2
        self.m3=m3

        def set(self):
            m1=85

            def avg(self):     #instance method it contains self argument
                return(self.m1+self.m2+self.m3)/3

            s1=Student(84,97,99)
            s2=Student(96,85,82)
            s1.set()

            print(s1.avg())
            print(s2.avg())