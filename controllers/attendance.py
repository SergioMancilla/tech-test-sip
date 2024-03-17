import json

from applications.sip_students.modules.renderer.AttendanceRenderer import AttendanceRenderer
from applications.sip_students.modules.repository.AttendanceRepository import AttendanceRepository
from applications.sip_students.modules.utils.attendance_enum import AttendanceEnum

def index():
    attendance_renderer = AttendanceRenderer()
    attendance = attendance_renderer.render_attendance_component()
    return {'message': "hello from students.py", 'attendance_component': attendance}

def change_attendance_student():
    ''' Register or change the attendance for a student and a subject '''

    attendance_repository = AttendanceRepository()
    
    if not request.env.request_method == 'POST': raise HTTP(403)
    try:
        post_vars = json.loads(request.body.read())
        attendance_repository.register_attendance(
            student_id = post_vars['student_id'],
            subject_id = post_vars['subject_id'],
            attended = True if int(post_vars['attendance']) == AttendanceEnum.ATTENDED.value else False
        )
        return response.json({'status': 'success', 'msg': 'hello', 'data': post_vars})
    except TypeError:
        return response.json({'status': 'error', 'msg': 'The data provided is not in the correct format'})