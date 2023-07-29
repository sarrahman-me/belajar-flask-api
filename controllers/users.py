from flask import Blueprint, jsonify, request

users_blueprint = Blueprint('users', __name__)

users = [
    {
        "id": 1,
        "nama": "rahman"
    },
    {
        "id": 2,
        "nama": "sarah"
    }
]

# ambil data users

@users_blueprint.route('/users', methods=["GET"])
def get_all_users():
    return jsonify({
        "status": 200,
        "success": True,
        "message": "Berhasil mengambil data users",
        "data": users
    })

# tambah data users


@users_blueprint.route('/users', methods=['POST'])
def tambah_users():
    data = request.get_json()

    if not data or "nama" not in data:
        return jsonify({
            "status": 400,
            "message": "Data dan Nama tidak boleh kosong",
            "success": False,
            "field": {
                "nama": "Nama tidak boleh kosong"
            }
        })

    new_user = {
        "id": len(users) + 1,
        "nama": data['nama']
    }

    users.append(new_user)
    return jsonify({
        "status": 201,
        "message": "Berhasil menambah data user",
        "success": True,
        "data": new_user
    })
