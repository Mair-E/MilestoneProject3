import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/all")
def all():
    return render_template("all.html")

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

recipes = [ #Add prep/cook time, submitted by#
    {
        'id': 1,
        'name'= 'Banana Bread',
        'serves'= '10',
        'ingredients': ['3 very ripe medium bananas (approx. 225g peeled)', '3 large eggs', '100g light brown sugar', 
        '150ml vegetable oil', '275g white self-raising flour', '1 tsp ground mixed spice', '1 tsp baking powder'],
        'instructions': [''],
        'tools': 'Preheat oven at 180 degrees',
        'tags': ['Vegetarian', 'Baking'],
    },
    {
        'id': 2,
        'name'= 'Veggie Spag Bal',
        'serves'= '',
        'ingredients': '',
        'tools': '',
        'tags': '',
    },
    {
        'id': 3,
        'name'= '',
        'serves'= '',
        'ingredients': '',
        'tools': '',
        'tags': '',
    },
    {
        'id': 4,
        'name'= '',
        'serves'= '',
        'ingredients': '',
        'tools': '',
        'tags': '',
    },
    {
        'id': 5,
        'name'='',
        'serves'= '',
        'ingredients': '',
        'tools': '',
        'tags': '',
    },
    {
        'id': 6,
        'name'= '',
        'serves'= '',
        'ingredients': '',
        'tools': '',
        'tags': 'Vegetarian',
    }, 

]

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        new_recipe = {
            'id': len(recipes) + 1,
            'name': request.form['name'],
            'serves': request.form['serves'],
            'ingredients': request.form.getlist('ingredients'),
            'instructions': request.form['instructions'],
            'tools': request.form.getlist('tools'),
            'tags': request.form.getlist['tags'],
        }
        recipes.append(new_recipe)
        return redirect(url_for('index'))

    return render_template('add_recipe.html')
    
    if __name__ == "__main__":
        app.run(
            host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True) ##Update to False before submitting##