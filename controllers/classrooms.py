from applications.sip_students.modules.models.Classroom import Classroom

def index():
    classroom = Classroom()
    form_model = classroom.get_model()

    grid = SQLFORM.grid(form_model, user_signature=False, orderby='name', sortable=True, paginate=10)
    return dict(grid=grid)