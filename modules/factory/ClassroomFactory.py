from applications.sip_students.modules.factory.SingletonMeta import SingletonMeta
from applications.sip_students.modules.models.Classroom import Classroom

class ClassromFactory(metaclass = SingletonMeta):
    
    def __init__(self):
        self.cache = {}

    def new_classroom(self, data: dict) -> Classroom :
        ''' Create new Classroom instance '''

        # Cache implemented for duplicated instances of Classroom class
        key = tuple(sorted(data.items()))
        if key not in self.cache:
            self.cache[key] = Classroom(
                name = data['name'],
                description = data['description'],
                monitor = data['monitor']
            )
        
        return self.cache[key]