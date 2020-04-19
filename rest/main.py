from app import app
from rest.auth.auth_controller import auth

if __name__ == '__main__':
    app.register_blueprint(auth)
    app.run(host='0.0.0.0', port=8080, debug=True)
