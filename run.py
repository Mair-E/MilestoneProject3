import os
from flask import Flask, render_template, request, redirect, url_for
from taskmanager import app

if__name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )


recipes = [ #Add prep/cook time, submitted by#
    {
        'id': 1,
        'name': 'Banana Bread',
        'serves': '10',
        'ingredients': ['3 very ripe medium bananas (approx. 225g peeled)', '3 large eggs', '100g light brown sugar', 
        '150ml vegetable oil', '275g white self-raising flour', '1 tsp ground mixed spice', '1 tsp baking powder'],
        'instructions': ['Mash bananas in a bowl, add eggs, sugar and oil and mix with fork. Add flour, spice, baking powder and whisk. Pour in a tin and bake for 40mins. Cool for 10mins and enjoy! '],
        'tools': 'Preheat oven at 180 degrees, prep < 30, cooking time 40',
        'tags': 'Cakes',
    },
    {
        'id': 2,
        'name': 'Veggie Spag Bal',
        'serves': '',
        'ingredients': '',
        'instructions': [''],
        'tools': '',
        'tags': 'Vegetarian',
    },
    {
        'id': 3,
        'name': 'Guacamole',
        'serves': '8-10',
        'ingredients': [''],
        'instructions': ['Mash avo until smooth. Add onion, coriander and lime juice, season with salt and pepper and combine. Stir in red chilli and serve.'],
        'tools': '> 30 mins',
        'tags': 'Mexican',
    },
    {
        'id': 4,
        'name': 'Penne with Tomato and Toast Veg',
        'serves': '',
        'ingredients': '',
        'tools': '',
        'tags': 'Italian',
    },
    {
        'id': 5,
        'name':'Airfryer Chicken Strips',
        'serves': '',
        'ingredients': '',
        'tools': '',
        'tags': 'American',
    },
    {
        'id': 6,
        'name': 'Cauliflower Sabji',
        'serves': '',
        'ingredients': '',
        'tools': '',
        'tags': 'Indian',
    }, 

]

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
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

    return render_template('addrecipe.html')

@app.route("/all")
def all():
    return render_template("all.html")

@app.route("/contact")
def contact():
    return render_template("contact.html") 

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) ##Update to False before submitting##