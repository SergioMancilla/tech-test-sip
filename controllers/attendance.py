from applications.sip_students.modules.renderer.AttendanceRenderer import AttendanceRenderer

def index():
    attendance_renderer = AttendanceRenderer()
    attendance = attendance_renderer.render_attendance_component()
    return {'message': "hello from students.py", 'attendance_component': attendance}