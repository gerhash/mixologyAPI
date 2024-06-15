from datas import *
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)


COCKTAILS_API_URL = 'http://localhost:5000/cocktails'

# Homepage to display all cocktails
@app.route('/', methods=['GET'])
def homepage():
    try:
        # Send a GET request to retrieve cocktails data from the external API
        response = requests.get(COCKTAILS_API_URL)
        response.raise_for_status()

        all_cocktails = response.json()


        # Render the homepage.html template with cocktails data and unique ingredients
        return render_template('homepage.html', cocktails=all_cocktails)

    except requests.exceptions.RequestException as e:
        # Handle connection or HTTP request errors
        print(f"Error with HTTP request: {e}")
        # Render an error template with a message for the user
        return render_template('error.html', error_message="Error retrieving cocktails data")



@app.route('/<int:cocktail_id>', methods=['GET'])
def cocktail_details(cocktail_id):
    cocktail = requests.get('http://localhost:5000/cocktails/' + str(cocktail_id)).json()
    return render_template('cocktail.html', cocktail=cocktail)



# Endpoint to get all cocktails
@app.route('/cocktails', methods=['GET'])
def get_cocktails():
    return jsonify(cocktails)

# Endpoint to get a cocktail by ID
@app.route('/cocktails/<int:cocktail_id>', methods=['GET'])
def get_cocktail_by_id(cocktail_id):
    cocktail = next((c for c in cocktails if c['id'] == cocktail_id), None)
    if cocktail:
        return jsonify(cocktail)
    return jsonify({"error": "Cocktail not Found"}), 404


# Endpoint to get a cocktail by name
@app.route('/cocktails/search_by_name', methods=['GET'])
def get_cocktail_by_name():
    name_query = request.args.get('name')
    if not name_query:
        return jsonify({"error": "Insert name in the query"}), 400

    results = []
    for cocktail in cocktails:
        if name_query.lower() in cocktail['name'].lower():
            results.append(cocktail)

    if not results:
        return jsonify({"error": "Cocktail not Found"}), 404

    return jsonify(results)


# Endpoint to search cocktails by ingredients
@app.route('/cocktails/search', methods=['GET'])
def search_cocktails_by_ingredients():
    ingredient_query = request.args.get('ingredients')
    if not ingredient_query:
        return jsonify({"error": "Specify at least one ingredient in the query"}), 400

    # Split the ingredients query by comma
    ingredient_list = [ingredient.strip().lower() for ingredient in ingredient_query.split(',')]

    results = []
    for cocktail in cocktails:
        ingredients_list = [ingredient['name'].lower() for ingredient in cocktail['ingredients']]
        if all(ingredient in ingredients_list for ingredient in ingredient_list):
            results.append(cocktail)

    if not results:
        return jsonify({"error": "Cocktail not Found"}), 404

    return jsonify(results)


# Endpoint to search cocktails by difficulty
@app.route('/cocktails/difficulty/<string:difficulty>', methods=['GET'])
def get_cocktails_by_difficulty(difficulty):
    filtered_cocktails = [cocktail for cocktail in cocktails if cocktail['difficulty'].lower() == difficulty.lower()]
    if not filtered_cocktails:
        return jsonify({"message": "No cocktails found for the specified difficulty"}), 404
    return jsonify(filtered_cocktails)



if __name__ == '__main__':
    app.run(debug=True)