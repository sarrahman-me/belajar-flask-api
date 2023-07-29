from flask import Flask, jsonify, request
from controllers.users import users_blueprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my simple API"


app.register_blueprint(users_blueprint)


if __name__ == "__main__":
    app.run(debug=True, port=5009)
