from flask import Flask
from controllers.receipt_controllers import receipt_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(receipt_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
