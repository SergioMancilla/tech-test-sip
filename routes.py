#!/usr/bin/python
# -*- coding: utf-8 -*

BASE = '/api'

routes_in = (
    ('/sip_students/api/students/register', '/sip_students/controllers/students/register_student'),
)

routes_out = [(r'/*', None)]