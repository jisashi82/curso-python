from webpersonal import app

@app.route('/')
def home():
    return 'pagina de inicio'