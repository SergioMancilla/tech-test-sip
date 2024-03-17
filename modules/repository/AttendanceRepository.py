from gluon.dal import Field

from applications.sip_students.modules.repository.BaseRepository import BaseRepository

class AttendanceRepository(BaseRepository):
    ''' Class for register the students attendance '''
    
    __tablename__ = 'attendance'

    def __init__(self):
        BaseRepository.__init__(self)

        self.table = self.db.define_table(
            self.__tablename__,
            Field('student_id', self.get_students_model()),
            Field('subject_id', self.get_subjects_model()),
            Field('attended', 'boolean'),
            format='%(name)s'
        )

    def get_subjects_model(self):
        ''' Used for references classroom_id field '''
        return self.db.define_table('subjects')
    
    def get_students_model(self):
        ''' Used for references classroom_id field '''
        return self.db.define_table('students')
    
    def get_db_object(self):
        ''' Return database instance for classrooms '''
        return self.db[self.__tablename__]
    
    def get_attendance_list(self) -> list:
        ''' Return the full list for attendance. This allows to render the attendance by default values later '''
        table = self.get_db_object()
        registers = self.db(table).select()

        attendance_taken = []

        for register in registers:
            attendance_taken.append('attendance_%s_%s_%s' % (register.student_id, register.subject_id, register.attended))
            
        return attendance_taken
    
    def register_attendance(self, student_id: int, subject_id: int, attended: bool):
        ''' Store the attendance status of a student for a given subject '''

        self.db[self.__tablename__].update_or_insert(
            (self.db[self.__tablename__].student_id == student_id) &
            (self.db[self.__tablename__].subject_id == subject_id),
            student_id = student_id,
            subject_id = subject_id,
            attended = attended
        )
        

