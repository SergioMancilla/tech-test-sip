from typing import List

from gluon.html import *
from pydal.objects import Row

from applications.sip_students.modules.models.Classroom import Classroom
from applications.sip_students.modules.repository.ClassroomRepository import ClassroomRepository
from applications.sip_students.modules.repository.StudentRepository import StudentRepository

class AttendanceRenderer:
    ''' Class for attendance rendering '''

    def __init__(self):
        self.classroom_repository = ClassroomRepository()
        self.student_repository = StudentRepository()

    def render_attendance_component(self):
        ''' Return the render component for showing the students attendance '''

        classrooms = self.classroom_repository.get_all_classrooms()

        div_classrooms = self.render_all_classrooms(classrooms)
        
        return div_classrooms
    
    def render_all_classrooms(self, classrooms: list):
        ''' Render all classrooms with students '''
        classrooms = []
        for classroom in classrooms:
            p_classroom = self.render_classroom(classroom)
            classrooms.append(p_classroom)

        print(classrooms)

        return DIV(classrooms)
        
    def render_classroom(self, classroom: Row):
        ''' Render a specific classroom with all their students '''
        classroom_name = classroom.name
        return DIV(classroom_name)