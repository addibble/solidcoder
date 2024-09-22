from flask import Flask, request, jsonify
from flask_compress import Compress
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from itsdangerous import URLSafeTimedSerializer
import logging

from database.sqlalchemy_database import SQLAlchemyDatabase
from decorators.error_handler import handle_errors


def create_app(config_class=DevelopmentConfig):
    # Logging configuration
    logging.basicConfig(filename='app.log', level=logging.INFO)

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Database
    database = DatabaseFactory.create_database(app.config)

    if isinstance(database, SQLAlchemyDatabase):
        # Initialize SQLAlchemyDatabase with app
        database = SQLAlchemyDatabase(app)
        # Create database tables
        with app.app_context():
            database.db.create_all()
    else:
        # Handle APIDatabase initialization
        pass

    # Initialize extensions
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)

    # Initialize Repositories
    user_repository = UserRepository(database)
    product_repository = ProductRepository(database)
    order_repository = OrderRepository(database)

    # Initialize Services
    user_service = UserService(user_repository, bcrypt, login_manager)
    product_service = ProductService(product_repository)
    order_service = OrderService(order_repository, product_service)

    # Initialize extensions
    compress = Compress(app)
    cors = CORS(app)
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    # Login manager user loader
    @login_manager.user_loader
    @handle_errors
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Routes
    @app.route('/register', methods=['POST'])
    @handle_errors
    def register():
        data = request.get_json()
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], password=hashed_password, email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'})
    
    @app.route('/login', methods=['POST'])
    @handle_errors
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
    @handle_errors
    def logout():
        logout_user()
        return jsonify({'message': 'Logged out successfully'})
    
    @app.route('/products', methods=['GET'])
    @handle_errors
    def get_products():
        products = Product.query.all()
        output = []
        for product in products:
            product_data = {'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock}
            output.append(product_data)
        return jsonify({'products': output})
    
    @app.route('/product/<int:product_id>', methods=['GET'])
    @handle_errors
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

    @app.route('/inventory_report', methods=['GET'])
    def inventory_report():
        report = product_service.generate_inventory_report()
        return jsonify(report)

    @app.route('/process_bulk_orders', methods=['POST'])
    @login_required
    def process_bulk_orders_route():
        data = request.get_json()
        orders = data.get('orders', [])
        processed_orders, total_revenue = order_service.process_bulk_orders(current_user.id, orders)

        response = {
            'processed_orders': processed_orders,
            'total_revenue': total_revenue,
            'message': f"Processed {len(processed_orders)} orders."
        }

        return jsonify(response)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'message': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'message': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
