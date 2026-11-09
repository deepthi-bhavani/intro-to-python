class student:
    def __init__(self, name):
        self.name = name
        self.grades=[]

    def add_grade(self, grade):
        self.grades.append(grade)

    def compute_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

ana = student("Ana")
for g in[14,16,12]:
    ana.add_grade(g)
Ben=student("Ben")
print(ana.name,ana.compute_average())
print(Ben.name,Ben.compute_average())
