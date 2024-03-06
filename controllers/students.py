# -*- coding: utf-8 -*-

# request.get_vars and request.post_vars and request.vars
import json

def index():
    return dict()

def attendance():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

def save_student():
    if not request.env.request_method == 'POST': raise HTTP(403)
    post_vars = json.loads(request.body.read())
    return response.json({'status': 'success', 'msg': 'hello', 'body': post_vars['fullname']})