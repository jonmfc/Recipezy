from flask import Flask, request, render_template

app = Flask(__name__)

# Dummy data for the purpose of this example
# In a real application, you might query a database or an API
available_recipes = {
    "Pasta with Garlic, Oil, and Chili Pepper": ["pasta", "garlic", "olive oil", "chili pepper", "salt"],
    "Classic Tomato Soup": ["tomato", "onion", "garlic", "vegetable broth", "salt", "pepper"],
    "Simple Salad": ["lettuce", "tomato", "cucumber", "olive oil", "vinegar", "salt"]
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_ingredients = request.form.get('ingredients').lower().split(',')
        user_ingredients = [ingredient.strip() for ingredient in user_ingredients]
        matching_recipes = {}
        for recipe, ingredients in available_recipes.items():
            if all(item in user_ingredients for item in ingredients):
                matching_recipes[recipe] = ingredients
        return render_template('recipes.html', recipes=matching_recipes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
