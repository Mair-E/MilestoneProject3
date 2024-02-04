from cookbook import db

# Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    tools = db.Column(db.String(255), nullable=False)
    cuisine = db.Column(db.String(255), nullable=False)
