from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

food_data = {
    "apple": "Healthy food, Rich in Vitamin C!",
    "banana": "Healthy food, Rich in Fiber & Vitamin C, B6!",
    "orange": "Healthy food, Rich in Vitamin C!",
    "strawberry": "Healthy food, Rich in Vitamin C!",
    "pizza": "Unhealthy food, Contains lot of unhealthy Fats!",
    "burger": "Unhealthy food, Contains lot of unhealthy Fats!",
    "fries": "Unhealthy food, Contains lot of unhealthy Fats!",
    "idli": "Healthy food, Rich in carbohydrate!",
    "dosa": "Healthy food, Rich in carbohydrate!",
    "paratha": "Unhealthy food, Contains lot of unhealthy Fats!",
    "samosa": "Unhealthy food, Contains lot of unhealthy Fats!",
    "sandwich": "Healthy food, Contains veggies and low calories!",
    "jalebi": "Unhealthy food, contains lot of calories!",
    "upma": "Healthy food, upma has a balanced calorie distribution!",
    "pani puri": "Unhealthy food, Not good for health!",
    "mango": "Healthy food, Rich in Vitamin C, A, B6!",
    "grapes": "Healthy food, Rich in Vitamin K!",
    "chocolate": "Unhealthy food, High calorie and not good while over consuming !",
    "ice cream": "Unhealthy food!",
    "rice": "Healthy food, Rich in carbohydrate!",
    "dragon fruit": "Healthy food, Rich in vitamin C!"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        food = request.form["food"].lower()
        result = food_data.get(food, "Hmm, I'm not sure about that one. Check the spelling or Let's find out together!")
        return redirect(url_for("play", result=result))
    return render_template("index.html")

@app.route("/play/<result>")
def play(result):
    return render_template("play.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
