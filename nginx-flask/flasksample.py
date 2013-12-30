from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Check out Docker Recipes by The Rigorous Programmers at http://rigprog.com/docker-recipes/nginx-flask.html\n"

if __name__ == "__main__":
    app.run("0.0.0.0")
