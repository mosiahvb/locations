from flask import Flask, render_template, jsonify, request
from actions import look_up, add_item, delete, change_location


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('location.html') # this renders the html page you created

# Handles the get location request, returning the locations of the product selected
@app.route('/get-location', methods=['POST'])
def get_loc():
    input = request.get_json()
    product_num = input.get('product_number')
    location = look_up(product_num)
    
    return jsonify({'location': location})

@app.route('/update')
def updates_page():
    return render_template('updates.html') # Renders the updates page 

# Handles the adding a part to the database request 
@app.route('/add-part', methods=['POST'])
def addpart():
    inputs = request.get_json()
    product_num = inputs.get('product_number')
    product_loc = inputs.get('product_location')

    add_item(product_num, product_loc)
    verify = look_up(product_num)
    if not verify:
        return jsonify({"error": "Item was not saved."}), 500
    else:
        return jsonify({"message": "Item added successfully."}), 200


# Handles Making changes to location
@app.route('/change-location', methods=['POST'])
def changelocation():
    inputs = request.get_json()
    product_num = inputs.get('product_number')
    product_loc = inputs.get('product_location')
    product_new_loc = inputs.get('new_Location')
    
    result = change_location(product_num, product_loc, product_new_loc)
    if result == 1:
        return jsonify({"message": "Item Found and successfully Changed."}), 200
    else:
        return jsonify({"error": "Item not found."}), 500
    



# Handles the removing a product for the database
@app.route('/remove-part', methods=['POST'])
def removepart():
    inputs = request.get_json()
    product_num = inputs.get('product_number')
    product_loc = inputs.get('product_location')
    part = product_num.strip()
    location = product_loc.strip()
    result = delete(part, location)

    if result == 1:
        return jsonify({"message": "Item Found and successfully Deleted."}), 200
    else:
        return jsonify({"error": "Item not found to delete."}), 500





if __name__ == '__main__':
    app.run()
    # app.run(host='127.0.0.1', debug=True,) FOR TESTING