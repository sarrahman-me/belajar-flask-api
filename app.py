from flask import Flask
from controllers.users import users_blueprint
from controllers.weathers import weather_blueprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my simple API"


app.register_blueprint(weather_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5009)
