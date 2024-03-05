def register_student(request):
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status': 'success', 'msg': 'hello', 'data': request})