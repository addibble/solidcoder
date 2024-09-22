# decorators/error_handler.py

def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception("An error occurred")
            return jsonify({'message': 'Internal server error'}), 500
    return wrapper