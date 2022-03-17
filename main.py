from flask import Flask
app = Flask('app')

@app.route('/')
def index():
  return '<h1>Minha primeira rota!</h1>'

if __name__ == ('__main__'):
  app.run(host='0.0.0.0', port=8080)