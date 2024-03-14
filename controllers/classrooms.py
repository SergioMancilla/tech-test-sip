from applications.sip_students.modules.repository.ClassroomRepository import ClassroomRepository

def index():
    ''' Returns view for editing classrooms through SQLForm '''
    classroom_repository = ClassroomRepository()
    form_model = classroom_repository.get_model()
    grid = SQLFORM.grid(form_model, user_signature=False, orderby='name', sortable=True, paginate=10, csv=False)
    return dict(grid=grid)