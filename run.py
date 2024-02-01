import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_migrate import Migrate

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recipes.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#login_manager = LoginManager(app)
#login_manager.login_view = 'login'

#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))

# User model
#class User(db.Model, UserMixin):
 #   id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(50), unique=True, nullable=False)
#    password = db.Column(db.String(100), nullable=False)

# Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    tools = db.Column(db.String(255), nullable=False)
    cuisine = db.Column(db.String(255), nullable=False)
 #   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#    user = db.relationship('User', backref='recipes')
        
# Create the database tables
#with app.app_context():
#    try:
#        db.create_all()
#    except Exception as e:
#        print(f"Error creating database tables: {e}")

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html')

# Logout route
#@app.route('/logout')
#@login_required
#def logout():
#    logout_user()
#    return redirect(url_for('index'))

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

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) #Update to False before submitting