import os
from taskmanager import app

#Recipe model

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    tools = db.Column(db.String(255), nullable=False)
    cuisine = db.Column(db.String(255), nullable=False)
    
# Create the database tables
db.create_all()

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

    if __name__ == "__main__":
        app.run(
            host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True) #Update to False before submitting