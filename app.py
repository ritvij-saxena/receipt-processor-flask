from flask import Flask
from controllers.receipt_controller import receipt_bp
from controllers.user_controller import user_bp
app = Flask(__name__)

# Register blueprint
app.register_blueprint(receipt_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
