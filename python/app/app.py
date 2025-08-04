from flask import Flask, render_template, request 
#render a template for you and send it to the server

app = Flask(__name__)

SPORTS = [ #List
    "Basketball",
    "Soccer",
    "Ultimate Frisbee",
]

REGISTRANTS = {} #Empty dictionary 


@app.route("/") #function called when this root is visited
def index():

    return render_template("index.html",sports=SPORTS)

@app.route("/greet")
def greet(): #name of the function
    name = request.args.get("name","world")
    return render_template("greet.html", name=name)

@app.route("/register", methods = ["POST"])
def register():
    name= request.form.get ("name")
    if not name:
        return render_template("error.html", message = "Missing name w")
    
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message = "Missing sport w")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport name")
    
    REGISTRANTS[name] = sport #key and value pair
    
    return render_template("success.html")

    # if not request.form.get("name") or request.form.get("sport") not in SPORTS:
    #     return render_template ("failures.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)

if __name__ == "__main__":
    app.run(debug=True)


    # name = request.args.get ("name", "world") #second argument is default value
    # name = request.args["name"] #request.args is a python dictionary
    # return render_template("index.html", name=name) #remplace placeholder by the variable name
