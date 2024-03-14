from applications.sip_students.modules.repository.SubjectRepository import SubjectRepository

def index():
    subject_repository = SubjectRepository()
    form_model = subject_repository.get_model()

    grid = SQLFORM.grid(form_model, user_signature=False, orderby='name', sortable=True, paginate=10, csv=False)
    return dict(grid=grid)