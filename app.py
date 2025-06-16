from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import json, os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

app = Flask(__name__)

client = MongoClient(MONGO_URI)
print(client.list_database_names())
db = client['mydb']
collection = db['submissions']

@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/')
def form():
    #return render_template('form.html')
    return render_template('todo.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        print("Received data:", data)
        if not data.get("name") or not data.get("email"):
            return jsonify({"error": "Name and Email are required!"}), 400
        collection.insert_one(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")

    if item_name and item_desc:
        collection.insert_one({
            "name": item_name,
            "description": item_desc
        })
        return "Data submitted successfully"
    else:
        return "Missing data", 400

@app.route('/success')
def success():
    return render_template('success.html')

    
if __name__ == '__main__':
    app.run(debug=True)