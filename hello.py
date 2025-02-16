from flask import Flask, render_template
 #create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#localhost:5000/user/John

# def index():
#     return "<h1>Hello World!</h1>"


#these are the filters in jinja...
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags


def index():
    first_name="Super Man"
    stuff="This is <strong>bold</strong> text"

    favorite_pizza = ["Pepperoni","Cheese","Mushroom",41]
    return render_template("index.html",first_name=first_name, stuff=stuff,favorite_pizza = favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)



#create custom error pages

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500
    