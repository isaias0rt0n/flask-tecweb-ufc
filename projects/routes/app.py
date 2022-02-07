from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<h1>Hello! Flask!</h1>"

@app.route("/about")
def about():
  return "<h1>Sobre a TECWEB</h1>"

@app.route("/contact")
def contact():
  return "<h1>UFC -  SOBRAL</h1>"

# 127.0.0.1:5000/hello/seunome
@app.route("/hello", defaults={'nome': None}, methods={"POST", "GET"})
@app.route("/hello/<string:nome>")
def hello(nome):
  if nome:
    return f'Hello {nome}'
  else:
    return "Olá, mundo"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)