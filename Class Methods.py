class Student:
    college = "KL University"
    # obj is an instance of a class so obj is not required
    # constructor is not required in class methods
    # decorator
    # class method,it contains cls argument
    @classmethod
    def set(cls):
        return cls.college

s1=Student()
s2=Student()
print(Student.set())


    
    