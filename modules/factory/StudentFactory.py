from applications.sip_students.modules.models.Student import Student

class StudentFactory:
    @staticmethod
    def new_student(data: dict) -> Student :
        ''' Create new student instance '''
        return Student(
            name = data['name'],
            last_name = data['last_name'],
            birth_date = data['birth_date'],
            id_number = data['id_number'],
            phone = data['phone']
        )

