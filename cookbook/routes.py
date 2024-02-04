from flask import render_template, request, redirect, url_for
from cookbook import app, db
from cookbook.models import Recipe

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# Index route
@app.route("/")
def index():
    recipes = Recipe.query.all()
    return render_template("index.html", recipes=recipes)


# Addrecipe route
@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    if request.method == 'POST':
        new_recipe = Recipe(
            name=request.form['name'],
            ingredients=request.form['ingredients'],
            instructions=request.form['instructions'],
            tools=request.form['tools'],
            cuisine=request.form['cuisine'],
        )

        # Save the new recipe to the database
        db.session.add(new_recipe)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('addrecipe.html')


# Edit_recipe route
@app.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe is None:
        return "Recipe not found", 404

    if request.method == 'POST':
        recipe.name = request.form['name']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        recipe.tools = request.form['tools']
        recipe.cuisine = request.form['cuisine']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_recipe.html', recipe=recipe)


# Delete_recipe route
@app.route('/delete_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe is None:
        return "Recipe not found", 404

    if request.method == 'POST':
        db.session.delete(recipe)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('delete_recipe.html', recipe=recipe)


# View full recipe route
@app.route('/full_recipe/<int:recipe_id>')
def full_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe is None:
        return "Recipe not found", 404

    return render_template('full_recipe.html', recipe=recipe)


# Contact route
@app.route("/contact")
def contact():
    return render_template("contact.html")
