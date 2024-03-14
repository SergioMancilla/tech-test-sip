from applications.sip_students.modules.factory.SingletonMeta import SingletonMeta
from applications.sip_students.modules.models.Subject import Subject

class SubjectFactry(metaclass = SingletonMeta):
    
    def __init__(self):
        self.cache = {}

    def new_subject(self, data: dict) -> Subject :
        ''' Create new Classroom instance '''

        # Cache implemented for duplicated instances of Subject class
        key = tuple(sorted(data.items()))
        if key not in self.cache:
            self.cache[key] = Subject(
                name = data['name'],
                description = data['description'],
            )
        
        return self.cache[key]