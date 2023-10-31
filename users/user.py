from db import model
from flask import jsonify, Response, json
from flask_bcrypt import Bcrypt

db = model.db
bcrypt = Bcrypt(model.app)  # for hashing the password that is to be stored in database

# defining User class which has methods to add, delete, retrieve, update the data in the database
class User:
    # retrieving the record by either using unique identifier i.e. email or list of records without identifier
    def retrieve_records(self, email = None):
        record = []
        if email:
            records = model.user.query.filter(model.user.email == email).all()
            if not records:
                return jsonify({'detail':'Email is not recorded'}), 400
        if not email:
            records = model.user.query.all()
        for row in records:
            ls = {
                'id': row.id,
                'name': row.name,
                'email': row.email,
                'phone': row.phone
            }
            record.append(ls)
        return Response(
            json.dumps(record, ensure_ascii = False).encode('utf-8'),
            content_type = 'application/json; charset=utf-8'
            )


    def record_user(self, email, phone, name, password, issuperuser = False):
        try:
            query = model.user.query.filter(model.user.email == email).first()
            if query:
                return jsonify({'detail':'Record with email already exists'}), 409
            query = model.user.query.filter(model.user.phone == phone).first()
            if query:
                return jsonify({'detail':'Record with phone already exists' }), 409
            record = model.user(name = name, phone = phone, email = email, issuperuser = issuperuser)
            with model.app.app_context():
                db.session.add(record)
                db.session.commit()
                db.session.refresh(record)
            query = model.user.query.filter(model.user.email == email).first()
            if not query:
                return jsonify({'detail':'Records are not recorded. Please try again'}), 422
            credentials = model.login(id = query.id, password = bcrypt.generate_password_hash(password))
            with model.app.app_context():
                db.session.add(credentials)
                db.session.commit()
                db.session.refresh(credentials)
                return "Record added successfully"
        except Exception as e:
            return jsonify({'error':str(e)}),500


    def update_records(self, prevemail, name = None, email = None, phone = None):
        try:
            query = model.user.query.filter(model.user.email == prevemail).first()
            updates = {}
            if not query:
                return jsonify({'detail':'No record with such email exists'}), 400
            if name and query.name != name:
                updates['name'] = name
            if email and query.email != email:
                updates['email'] = email
            if phone and query.phone != phone:
                updates['phone'] = phone
            if not updates:
                return jsonify({'detail': "No data found to update" }), 400
            for key in updates:
                setattr(query,key,updates[key])
            db.session.commit()
            return "Updated the data successfully"
        except Exception as e:
            return jsonify({'error':str(e)})


    def remove_record(self, email):
        login_cred = model.login.query.join(model.user).filter(model.user.email == email).first()
        if not login_cred:
            return jsonify({'detail':'Email is not registered' }), 400
        db.session.delete(login_cred)
        db.session.commit()
        query = model.user.query.filter(model.user.email == email).first()
        if not query:
            return jsonify({'detail':'Email is not registered' }), 400
        db.session.delete(query)
        db.session.commit()
        return "Record deleted successfully"