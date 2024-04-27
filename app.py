from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This time we'll assume this is our database, next time we'll use SQLite
product_list = [
    {
        "product_id": 1001,
        "product_name": "Laptop",
        "product_price": 999.99,
        "product_count": 50
    },
    {
        "product_id": 1002,
        "product_name": "Smartphone",
        "product_price": 599.99,
        "product_count": 100
    },
    {
        "product_id": 1003,
        "product_name": "Headphones",
        "product_price": 99.99,
        "product_count": 200
    }
]


# Retrieves a certain product:
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
    product = next((p for p in product_list if p['product_id'] == product_id), None)
    if product is None:
        error_response = jsonify({'error': 'Product not found'})
        return make_response(error_response, 404)
    return jsonify(product), 200


# Retrieves top 3 (by count) products:
@app.route('/products', methods=['GET'])
def get_products():
    response = sorted(product_list, key=lambda p: p['product_count'], reverse=True)[:3]
    return jsonify(response), 200


# Creates a new customer:
@app.route('/products/', methods=['POST'])
def create_product():
    required_attributes = ['product_name', 'product_price', 'product_count']
    product = request.json
    # Check if all the data required is sent:
    if all(att in product for att in required_attributes):
        # Check if there are any extra data in the request:
        if set(product.keys()) - set(required_attributes):
            error_response = jsonify({'error': 'Extra attributes found'})
            return make_response(error_response, 400)
        # If we're here everything is alright:
        product['product_id'] = 1000 + len(product_list)
        product_list.append(product)
        return jsonify(product['product_id']), 201
    # Else the client sent incomplete data:
    error_response = jsonify({'error': 'Missing required attributes'})
    return make_response(error_response, 400)


# main:
if __name__ == '__main__':
    # Running the API, on port 5000 (it's the
    # default, but this way you can change this):
    app.run(port=5000)
