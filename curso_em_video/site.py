from flask import Flask

app = Flask('flaskconftest')

@app.route('/')
def root():
    return 'Olá, Mundo '

app.run()