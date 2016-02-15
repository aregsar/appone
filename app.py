from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"

print app.url_map

if __name__ == "__main__":
    app.run('0.0.0.0',3000)