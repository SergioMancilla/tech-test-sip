from applications.sip_students.modules.models.Classroom import Classroom

def index():
    classroom = Classroom()
    form_model = classroom.getModel()

    grid = SQLFORM.grid(form_model, user_signature=False)
    return dict(grid=grid)