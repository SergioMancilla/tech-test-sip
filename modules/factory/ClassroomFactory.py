from applications.sip_students.modules.models.Classroom import Classroom

class ClassromFactory:
    @staticmethod
    def new_classroom(data: dict) -> Classroom :
        ''' Create new Classroom instance '''
        return Classroom(
            name = data['name'],
            description = data['description'],
            monitor = data['monitor']
        )