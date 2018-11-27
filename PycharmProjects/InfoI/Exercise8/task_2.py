class UniPerson:
    unipersons = []
    def __init__(self, name):
        self._name = name
        self.__inbox = []
        UniPerson.unipersons.append(name)

    def receive_email(self, text):
        self.__inbox.append(text)

    def read_emails(self):
        return self.__inbox
        UniPerson.__inbox = []

    def __str__(self):
        return "Name: %s" %(self._name)


class Student(UniPerson):
    start_years = {}
    def __init__(self, name, start_year, has_gratuated, ects):
        super().__init__(name)
        self.has_gratuated = has_gratuated
        self.__ects = ects
        self.start_year = start_year
        student_count = self.add_student()
        five_digit_number = self.get_five_digit_number(student_count)
        self.__legi_nr = "%s-%s" %(start_year, five_digit_number)


    def add_student(self):
        for key in Student.start_years.keys():
            if key == self.start_year:
                Student.start_years[key] +=1

    def get_five_digit_number(self, start_year):
        Student.start_year = start_year
        five_digit_number = str(Student.start_years[start_year]).zfill(5)
        return five_digit_number

    def __str__(self):
        return super().__str__()+", " +self.__legi_nr+ ", "+str(self.has_gratuated)+", "+str(self.__ects)

class Lecturer(UniPerson):
    def __init__(self, name, lecture_name):
        super.__init__(name)
        self.__lecture_name = lecture_name

    def __str__(self):
        return super().__str__()+", " + self.__lecture_name

class UniManagement(UniPerson):
    def __init__(self):
        self.__persons = []

    def add_person(self, person):
        if person in unipersons:
            self.__persons.append(person)
        else:
            pass

    def __str__(self):
        return self.__persons

    def list_persons(self):
        return UniManagement().__str__()

    def send_email(self,text):
        for person in self.__persons:
            self.__inbox.append(text)

    def count_alumni(self):
        alumni = 0
        for person in self.__persons:
            if Student.has_gratuated ==True:
                alumni += 1
        return alumni


if __name__ == '__main__':
    p1 = UniPerson("Hans Muster")
    assert p1.__str__() == "Name: Hans Muster"

    p1.receive_email("Email 1")
    p1.receive_email("Email 2")
    assert p1.read_emails() == ["Email 1", "Email 2"]
    #assert p1.read_emails() == []  # Because inbox was emptied after reading the first time

    s1 = Student("Student 1", 2017, False, 40)
    assert "Student 1" in s1.__str__()
    assert "2017-00000" in s1.__str__()
    assert "False" in s1.__str__()
    assert "40" in s1.__str__()

    s2 = Student("Student 2", 2017, True, 120)
    assert "Student 2" in s2.__str__()
    assert "2017-00001" in s2.__str__()
    assert "True" in s2.__str__()
    assert "120" in s2.__str__()

    s3 = Student("Student 3", 2016, True, 180)
    assert "Student 3" in s3.__str__()
    assert "2016-00000" in s3.__str__()
    assert "True" in s3.__str__()
    assert "180" in s3.__str__()

    mgmt = UniManagement()

    lecturer = Lecturer("Prof. Dr. Harald Gall", "Informatik 1")

    mgmt.add_person(s1)
    mgmt.add_person(s2)
    mgmt.add_person(s3)
    mgmt.add_person(lecturer)

    assert mgmt.count_alumni() == 2

    mgmt.send_email("This test email is sent to all university persons.")
    assert s1.read_emails() == ["This test email is sent to all university persons."]
    assert s2.read_emails() == ["This test email is sent to all university persons."]
    assert s3.read_emails() == ["This test email is sent to all university persons."]
    assert lecturer.read_emails() == ["This test email is sent to all university persons."]
