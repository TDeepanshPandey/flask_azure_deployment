from flask import Flask, app
from flask import request

Books = []

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Books REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["PROPAGATE_EXCEPTIONS"] = True

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    @app.route('/books', methods=['GET'])
    def get_books():
        return {'books': Books}
    
    @app.route('/books', methods=['POST'])
    def add_book():
        book = request.get_json()
        Books.append(book["title"])
        return {'message': 'Book added successfully', 'books': Books}, 201
    
    return app
    
    
