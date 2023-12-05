import json
import requests

def lambda_handler(event, context):
     # Get the POST data from the request body
        try:
            post_data = json.loads(event['body'])
            # The POST variable is named 'your_variable'
            your_variable = post_data.get('searchInput', 'Default Value')
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Bad Request: Invalid JSON in the request body.')
            }
        url = "https://the-cocktail-db.p.rapidapi.com/search.php"

        querystring = {"s":f"{your_variable}"}

        headers = {
	        "X-RapidAPI-Key": "29c38d7341msh7a15b3f6f2fbf49p192425jsn6de4d45dc56e",
	        "X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Define the keys to be filtered
        keys_to_filter = ['strDrink', 'strAlcoholic', 'strGlass', 'strInstructions', 'strDrinkThumb']
        ingredient_keys = [f'strIngredient{i}' for i in range(1, 16)]
        measure_keys = [f'strMeasure{i}' for i in range(1, 16)]

        # Create a new dictionary with filtered keys
        filtered_data = {
            'drinks': [{
                key: data['drinks'][0][key]
                for key in keys_to_filter + ingredient_keys + measure_keys
            }]
        }

        # Convert the filtered data back to JSON
        filtered_json = json.dumps(filtered_data, indent=4)

        # Extract the values of the specified keys and assign them to variables
        drink_data = data['drinks'][0]
        strDrink = drink_data['strDrink']
        strAlcoholic = drink_data['strAlcoholic']
        strGlass = drink_data['strGlass']
        strInstructions = drink_data['strInstructions']
        strDrinkThumb = drink_data['strDrinkThumb']

        strIngredients = [drink_data[f'strIngredient{i}'] for i in range(1, 16)]
        strMeasures = [drink_data[f'strMeasure{i}'] for i in range(1, 16)]

        # Create an HTML response with the received data
        html_response = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{strDrink}</title>
            <style>
                .medium-size-image {{
                    width: 200px; /* Set the width to 300 pixels */
                    height: auto; /* Maintain the aspect ratio */
                }}
                .max-width-text {{
                    max-width: 500px; /* Set the maximum width for the text to 500 pixels */
                    word-wrap: break-word; /* Allow the text to wrap to a new line if it exceeds the maximum width */
                }}
            </style>
        </head>
        <body>
            <h1>{strDrink}</h1>
            <img src="{strDrinkThumb}" alt="{strDrink}" class="medium-size-image" />
            <p class="max-width-text"><strong>Drink Type:</strong> {strAlcoholic}</p>
            <p class="max-width-text"><strong>Glass:</strong> {strGlass}</p>
            <p class="max-width-text"><strong>Instructions:</strong> {strInstructions}</p>
            <h2>Ingredients:</h2>
            <ul>
        """
        for ingredient, measure in zip(strIngredients, strMeasures):
            if ingredient:
                html_response += f"        <li>{ingredient} - {measure}</li>\n"

        html_response += """
            </ul>
        </body>
        </html>
        """
        
        if not response:
            html_response = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>No Cocktail Information</title>
            </head>
            <body>
                <p>Unfortunately, we don't have information on the cocktail...</p>
            </body>
        </html>
        """
        
        # Return the HTML response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': html_response
        }
