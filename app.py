from flask import Flask, jsonify, request

# create a variable "app" as a flask object and we are calling it as "app"
app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'Dillan',
        'contact': u'647-384-6770', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Jyoti',
        'contact': u'416-906-0211', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    contact.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 


# where we are calling the function and what function we are calling
if __name__ == '__main__':
    app.run(debug=True)