def upload_file(f):
    print(f)
    with open('testapp/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
