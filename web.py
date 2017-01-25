# How to import the weather app we made previous: 
# in the html we change name to adress
# in this file we want to return the forecast - not adress. 
#so in the index function we run the functiion from weather.py called "get_location()"
#We pass through the "adress" which the user will fill in on the line above, which is linked
#to the html document. 

# This works but it returns the adress as "none", so we added a if statement so it would only
# print out the forecast if someone had put in their adress
# we also had to make forecast = none, because the return needed the forecast to run

from flask import Flask, render_template, request
import weater
import os
app = Flask(__name__)

@app.route("/")
def index():
    adress = request.values.get("adress")
    forecast = None
    if adress:   
        forecast = weater.get_location(adress)
    return render_template("index.html", forecast=forecast)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)















