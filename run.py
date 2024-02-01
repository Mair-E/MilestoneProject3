import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recipes.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    tools = db.Column(db.String(255), nullable=False)
    cuisine = db.Column(db.String(255), nullable=False)
    
# Create the database tables
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error creating database tables: {e}")

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
            cuisine=request.form['cuisine']
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

# Contact route
@app.route("/contact")
def contact():
    return render_template("contact.html") 

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) #Update to False before submitting