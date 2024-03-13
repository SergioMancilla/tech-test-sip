# -*- coding: utf-8 -*-

import json

from applications.sip_students.modules.factory.StudentFactory import StudentFactory
from applications.sip_students.modules.repository.StudentRepository import StudentRepository

def index():
    ''' Return students form view '''
    return dict()

def attendance():
    ''' TODO register attendance '''
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

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
        student_repositoty.save(student)
        
        return response.json({'status': 'success', 'msg': 'The student has been saved successfully'})
    except TypeError:
        return response.json({'status': 'error', 'msg': 'The data provided is not in the correct format'})