from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Hola Abimael! Tu app web está corriendo en Docker y desplegada por Jenkins.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
