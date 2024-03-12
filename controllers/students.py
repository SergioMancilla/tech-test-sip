# -*- coding: utf-8 -*-

# request.get_vars and request.post_vars and request.vars
# from applications.sip_students.modules.factory.StudentFactory import StudentFactory
import json

def index():
    return dict()

def attendance():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

def save_student():
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
        return response.json({'status': 'success', 'msg': 'hello'})
    except TypeError:
        return response.json({'status': 'error', 'msg': 'The data provided is not in the correct format'})