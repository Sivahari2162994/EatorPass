from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

food_data = {
    "apple": "Healthy food!",
    "banana": "Healthy food!",
    "orange": "Healthy food!",
    "strawberry": "Healthy food!",
    "pizza": "Unhealthy food!",
    "burger": "Unhealthy food!",
    "fries": "Unhealthy food!",
    "idli": "Healthy food!",
    "dosa": "Healthy food!",
    "paratha": "Unhealthy food!",
    "samosa": "Unhealthy food!",
    "sandwich": "Healthy food!",
    "jalebi": "Unhealthy food!",
    "upma": "Healthy food!",
    "pani puri": "Unhealthy food!",
    "mango": "Healthy food!",
    "grapes": "Healthy food!",
    "chocolate": "Unhealthy food!",
    "ice cream": "Unhealthy food!",
    "rice": "Healthy food!",
    "noodles": "Unhealthy food!"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        food = request.form["food"].lower()
        result = food_data.get(food, "Hmm, I'm not sure about that one. Let's find out together!")
        return redirect(url_for("play", result=result))
    return render_template("index.html")

@app.route("/play/<result>")
def play(result):
    return render_template("play.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
