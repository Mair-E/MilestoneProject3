import os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


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
        'name': 'Sangria',
        'serves': '4',
        'ingredients': ['3 glasses red wine', '2 glasses lemonade', '1 glass orange juice', 'ice', ' fresh mint', 'sliced citrus fruit'],
        'instructions': ['Mix all ingrediants into a jug. Pour into glasses and serve with mint and fruit garnish'],
        'tools': 'No cooking required',
        'tags': 'Beverage',
    },
    {
        'id': 3,
        'name': 'Guacamole',
        'serves': '8-10',
        'ingredients': ['3 ripe avocados', '1/2 red onion', 'handful coriander', '1 lime', '1 finely chopped red chilli'],
        'instructions': ['Mash avo until smooth. Add onion, coriander and lime juice, season with salt and pepper and combine. Stir in red chilli and serve.'],
        'tools': '> 30 mins',
        'tags': 'Mexican',
    },
    {
        'id': 4,
        'name': 'Penne with Tomato and Roast Veg',
        'serves': '4',
        'ingredients': ['300 penne pasta', '400g tin chopped tomatoes', 'pinch mixed herbs', '250g frozen med vegetables', '4 tbsp freshly grated parmasan'],
        'instructions': ['Boil penna for 10-12 mins. Tip tomatoes and herbs into a saucepan and simmer for 2 mins. Stir in med veg and cook for further 2-3 mins. Drain penne and serve with sauce. Season and sprinkle with parmasan.'],
        'tools': '<10 mins prep',
        'tags': 'Italian',
    },
    {
        'id': 5,
        'name':'Airfryer Chicken Strips',
        'serves': '2',
        'ingredients': ['2 cloves garlic', '5 tbsp plain yoghurt', '1/4 tsp salt', '2 chicken breasts sliced', '6 tbsp tplain flour', '6 tbsp breadcrumbs', '1 tsp paprika', '1/2 tsp cayenne pepper', '1 egg'],
        'instructions': ['Marinate chicken in garlic, yoghurt and salt. In a bowl combine flour, breadcrumbs, paprika, cayenne papper and season. In a nother bowl beat the egg. Dip chicken strup into the egg and then the mixture. Arrange in airfryer for 15mins at 200C.'],
        'tools': 'Air fryer',
        'tags': 'American',
    },
    {
        'id': 6,
        'name': 'Chocolate Cookie',
        'serves': '6',
        'ingredients': ['100g chocolate spread', '75g plain flour', '3tbsp milk', '40g chocolate'],
        'instructions': ['Mix chocolate spread, flour milk and make into a dough. Roll into 6 balls and place in airfryer for 8-10 mins. Drizzle over melted chocolate.'],
        'tools': 'Preheat airfryer to 180C',
        'tags': 'American',
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