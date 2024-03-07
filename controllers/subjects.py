from applications.sip_students.modules.models.Subject import Subject

def index():
    subject = Subject()
    form_model = subject.get_model()

    grid = SQLFORM.grid(form_model, user_signature=False, orderby='name', sortable=True, paginate=10)
    return dict(grid=grid)