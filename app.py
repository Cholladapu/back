from flask import Flask,jsonify,request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
app = Flask(__name__)
CORS(app)

uri = "mongodb+srv://chollada:i2kYflYG6WfAHetF@cluster0.kua1tuq.mongodb.net/retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["Product"]
collection = db["dataprod"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products",methods=["GET"])
def get_all_products():
    products = list(collection.find({}))
    product_list = []
    
    for product in products:
        product_data = {
            "ID" : str(product["_id"]),
            "Name" : product["name"],
            "Price" : product["price"],
            "IMG": product["img"]
        }
        product_list.append(product_data)
    return jsonify({"products": product_list})

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    
    existing_product = collection.find_one({"_id": data.get("_id")})
    if existing_product:
        return jsonify({"error": "Cannot add product"}),500
    
    new_product = {
        "_id" : data.get("_id"),
        "name" : data.get("name"),
        "price" : data.get("price"),
        "img" : data.get("img")
    }
    result = collection.insert_one(new_product)
    return jsonify({"product": new_product}), 200

@app.route("/products/<string:prod_id>", methods=["DELETE"])
def delete_student(prod_id):
    existing_student = collection.find_one({"_id": prod_id})

    if existing_student:
        collection.delete_one({"_id": prod_id})
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)