# -*- coding: utf-8 -*-

import json

from applications.sip_students.modules.factory.StudentFactory import StudentFactory
from applications.sip_students.modules.repository.StudentRepository import StudentRepository

def index():
    ''' Return students form view '''
    return dict()

def edit_student():
    ''' Allows to edit a student, or asigning a course '''
    student_repository = StudentRepository()
    form_model = student_repository.get_model()

    grid = SQLFORM.grid(form_model, user_signature=False, orderby='name', sortable=True, paginate=10, csv=False, create=False)
    return dict(grid=grid)

def attendance():
    ''' TODO register attendance '''
    return dict()

def save_student():
    ''' Persist student into database '''
    if not request.env.request_method == 'POST': raise HTTP(403)
    try:
        post_vars = json.loads(request.body.read())
        student = StudentFactory.new_student(data = {
            'name': post_vars['fullname'],
            'last_name': post_vars['lastnames'],
            'birth_date': post_vars['birth_date'],
            'id_number': post_vars['id_number'],
            'phone': post_vars['phone']
        })

        student_repositoty = StudentRepository()
        op_status = student_repositoty.save(student)

        if('error' in op_status):
            return response.json({'status': 'error', 'msg': op_status['error']})
        
        return response.json({'status': 'success', 'msg': 'Student saved successfully'})
    except TypeError:
        return response.json({'status': 'error', 'msg': 'The data provided is not in the correct format'})