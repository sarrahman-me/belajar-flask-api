import requests
import os
from flask import jsonify, Blueprint, request
from dotenv import load_dotenv

load_dotenv()

weather_blueprint = Blueprint('weathers', __name__)


@weather_blueprint.route('/weathers', methods=['GET'])
def get_weathers():
    # Dapatkan nilai query parameter 'location', default 'indonesia' jika tidak ada.
    location = request.args.get('location', 'indonesia')

    url = "https://weatherapi-com.p.rapidapi.com/astronomy.json"
    query_string = {"q": location}

    headers = {
        "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=query_string)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "status": 200,
            "message": "Berhasil mendapatkan data cuaca",
            "success": True,
            "data": data
        })
    else:
        return jsonify({
            "status": response.status_code,
            "message": "Gagal mendapatkan data cuaca",
            "success": False,
        })
