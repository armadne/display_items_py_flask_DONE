from flask import Flask, render_template, redirect, url_for, request 

app = Flask(__name__)

items = []


@app.route("/")
def home():
    return render_template("home.html", items=items)


@app.route("/add_item", methods=["POST", "GET"])
def add_item():    
    if request.method == "POST":
        name_item = request.form["name"]
        publication_date = request.form["publication_date"]
        short_description = request.form["short_description"]
        full_description = request.form["full_description"]
        
        if not name_item or not publication_date or not short_description or not full_description:
            return render_template("add_item.html", items=items)
        
        
        items.append({"name" : name_item, "publication_date" : publication_date, "short_description" : short_description, "full_description" : full_description})
    
    return render_template("add_item.html", items=items) 


@app.route("/items")
def view_item():
    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)