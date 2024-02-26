from flask import Flask,jsonify
from pymongo.mongo_client import MongoClient
from flask_cors import CORS
app = Flask(__name__)

uri = "mongodb+srv://chollada:i2kYflYG6WfAHetF@cluster0.kua1tuq.mongodb.net/retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["Products"]
collection = db["week10"]

CORS(app)
products=[
{"id":0,"name":"Notebook Acer Swift","price":45900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0147295/A0147295_s.jpg"},
{"id":1,"name":"Notebook Asus Vivo","price":19900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146010/A0146010_s.jpg"},
{"id":2,"name":"Notebook Lenovo Ideapad","price":32900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149009/A0149009_s.jpg"},
{"id":3,"name":"Notebook MSI Prestige","price":54900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149954/A0149954_s.jpg"},
{"id":4,"name":"Notebook DELL XPS","price":99900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146335/A0146335_s.jpg"},
{"id":5,"name":"Notebook HP Envy","price":46900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0145712/A0145712_s.jpg"}];

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products",methods=["GET"])
def get_all_products():
    return jsonify(products),200

@app.route("/products", methods=["POST"])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify({"message": "Product added successfully"}), 201

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    updated_product = request.get_json
    for i, product in enumerate(products):
        if product["id"] == product_id:
            products[i] = updated_product
            return jsonify({"message": f"Product with ID {product_id} updated successfully"}), 200
    return jsonify({"message": f"Product with ID {product_id} not found"}), 404

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    for i, product in enumerate(products):
        if product["id"] == product_id:
            del products[i]
            return jsonify({"message": f"Product with ID {product_id} deleted successfully"}), 200
    return jsonify({"message": f"Product with ID {product_id} not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)