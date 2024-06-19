class Job:
    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def DTalk(self):
        output = f"{self.name}       Salary: {self.salary}    Worked {self.hoursWorked} hours"
        return output


class Doctor(Job):
    def __init__(self, experience):
        super().__init__("Doctor", "200k", "48")
        self.experience = experience

    def DTalk(self):
        base_output = super().DTalk()
        output = f"{base_output} Experience is {self.experience} years as a Doctor"
        print(output)


class Teacher(Job):
    def __init__(self, subject, position):
        super().__init__("Teacher", "88k", "48+")
        self.subject = subject
        self.position = position

    def DTalk(self):
        base_output = super().DTalk()
        output = f"{base_output} Subject: {self.subject}           Position: {self.position}"
        print(output)


class Lawyer(Job):
    def __init__(self):
        super().__init__("Lawyer", "100k", "40")

    def DTalk(self):
        output = super().DTalk()
        print(output)


teach = Teacher("Math", "Principal")
doc = Doctor(7)
lawyer = Lawyer()

lawyer.DTalk()
doc.DTalk()
teach.DTalk()
