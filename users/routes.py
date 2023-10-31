from users.user import User
from flask import Blueprint, request, jsonify
from db import schemas

usr = User()
router = Blueprint('users', __name__)

@router.route("/create/record/", methods = ['POST'])
def create_record():
    data = schemas.user(**request.get_json())
    if len(data.phone)>10:                                          # validating the phone number
        return jsonify({'details':'Phone number should be of 10 digits'}), 400
    response = usr.record_user(email = data.email, phone = data.phone, name = data.name, password = data.password, issuperuser = data.issuperuser)
    return response

@router.route("/retrieve/record/", methods = ['GET'])
def retrieve_record():
    response = usr.retrieve_records()
    return response

@router.route("/retrieve/by/email/", methods = ['GET'])
def retrieve_record_by_email():
    email = request.args.get('email', default = None)
    if not email:
        return jsonify({ "detail": "Please provide email" }), 400
    response = usr.retrieve_records(email = email)
    return response

@router.route("/update/record/", methods = ['PATCH'])
def update_records():
    name = request.form.get('name', None)
    email = request.form.get('email',None)
    phone = request.form.get('phone',None)
    prevemail = request.form['prevemail']
    response = usr.update_records(prevemail = prevemail, name = name, email = email, phone = phone)
    return response

@router.route("/delete/record/", methods = ['DELETE'])
def del_record():
    email = request.form['email']
    if not email:
        return jsonify({ "detail": "Please provide email" }), 400
    response = usr.remove_record(email = email)
    return response