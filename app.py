from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from itsdangerous import URLSafeTimedSerializer
import logging


def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['COMPRESS_ALGORITHM'] = 'gzip'
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    # Initialize extensions
    db = SQLAlchemy(app)
    compress = Compress(app)
    cors = CORS(app)
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    
    # Logging configuration
    logging.basicConfig(filename='app.log', level=logging.INFO)
    
    # User model
    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(150), unique=True, nullable=False)
        password = db.Column(db.String(150), nullable=False)
        email = db.Column(db.String(150), unique=True, nullable=False)
        
    # Product model
    class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        price = db.Column(db.Float, nullable=False)
        stock = db.Column(db.Integer, nullable=False)
    
    # Order model
    class Order(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, nullable=False)
        product_id = db.Column(db.Integer, nullable=False)
        quantity = db.Column(db.Integer, nullable=False)
        
    # Login manager user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Routes
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password, email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'})
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and bcrypt.check_password_hash(user.password, data['password']):
            login_user(user)
            return jsonify({'message': 'Logged in successfully'})
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return jsonify({'message': 'Logged out successfully'})
    
    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        output = []
        for product in products:
            product_data = {'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock}
            output.append(product_data)
        return jsonify({'products': output})
    
    @app.route('/product/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        product = Product.query.get_or_404(product_id)
        product_data = {'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock}
        return jsonify({'product': product_data})
    
    @app.route('/order', methods=['POST'])
    @login_required
    def create_order():
        data = request.get_json()
        new_order = Order(user_id=current_user.id, product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully'})
    
    @app.route('/orders', methods=['GET'])
    @login_required
    def get_orders():
        orders = Order.query.filter_by(user_id=current_user.id).all()
        output = []
        for order in orders:
            product = Product.query.get(order.product_id)
            order_data = {'order_id': order.id, 'product_name': product.name, 'quantity': order.quantity}
            output.append(order_data)
        return jsonify({'orders': output})
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'message': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'message': 'Internal server error'}), 500
    
    # Database initialization
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
