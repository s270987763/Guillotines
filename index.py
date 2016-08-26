from Core.bottle import route,run
@route('/')
def index():
    return "Hello World!"

run(host='localhost', port=8080)
