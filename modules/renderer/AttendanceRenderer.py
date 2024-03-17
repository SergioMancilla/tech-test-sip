from typing import List

from gluon.html import *
from pydal.objects import Row

from applications.sip_students.modules.repository.ClassroomRepository import ClassroomRepository
from applications.sip_students.modules.repository.StudentRepository import StudentRepository
from applications.sip_students.modules.repository.SubjectRepository import SubjectRepository
from applications.sip_students.modules.repository.AttendanceRepository import AttendanceRepository
from applications.sip_students.modules.utils.attendance_enum import AttendanceEnum

class AttendanceRenderer:
    ''' Class for attendance rendering '''

    def __init__(self):
        self.classroom_repository = ClassroomRepository()
        self.student_repository = StudentRepository()
        self.subject_repository = SubjectRepository()
        # Variable for render the current value options
        self.attendance_repository = AttendanceRepository()

    def render_attendance_component(self):
        ''' Return the render component for showing the students attendance '''

        classrooms = self.classroom_repository.get_all_classrooms()

        div_classrooms = self.render_all_classrooms(classrooms)
        
        return div_classrooms
    
    def render_all_classrooms(self, classrooms: list):
        ''' Render all classrooms with students '''
        classroom_elements = []

        for classroom in classrooms:
            p_classroom = self.render_classroom(classroom)
            classroom_elements.append(p_classroom)

        return DIV(*classroom_elements, _class='classrooms-container')
        
    def render_classroom(self, classroom: Row):
        ''' Render a specific classroom with all their students '''

        selected_attendance = self.attendance_repository.get_attendance_list()

        subjects = self.subject_repository.get_all_subjects()
        students =  self.student_repository.get_students_by_classroom(classroom.id)

        table = TABLE(
            THEAD(
                TR(
                    *[
                        TH('Student', _scope="col"),
                        *[TH(*subject.name) for subject in subjects]
                    ]
                )
            ),
            TBODY(
                *[TR(
                    *[
                        TH(student.name + ' ' + student.last_name, _scope="row"),
                        *[TD(
                            SELECT(
                                OPTION('Select attendance', _value='2', _selected='selected', _disabled='disabled'),
                                OPTION('Yes', _value=AttendanceEnum.ATTENDED.value),
                                OPTION("No", _value=AttendanceEnum.NOT_ATTENDED.value),
                                _value = '2',
                                value = self.get_selected_value(selected_attendance, student.id, subject.id),
                                _class = 'attendance_select',
                                _name = 'attendance_%i_%i' % (student.id, subject.id)
                            )
                        ) for subject in subjects]
                    ]
                ) for student in students]
            )
        , _class='table')
        return DIV(H2(classroom.name), table)
    
    def get_selected_value(self, attendance_list: list, student_id: int, subject_id: int):
        ''' Asign the default value to a select based in attendance status '''
        return (AttendanceEnum.ATTENDED.value if 'attendance_%i_%i_True' % (student_id, subject_id) in attendance_list else
                AttendanceEnum.NOT_ATTENDED.value if 'attendance_%i_%i_False' % (student_id, subject_id) in attendance_list else None)