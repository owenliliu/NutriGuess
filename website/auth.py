from flask import Blueprint, render_template, request, flash
import pandas as pd

df = pd.read_csv('nutrition.csv')

auth = Blueprint("auth", __name__)
answer = ""
foodlist = [
    {
        "name": "Avocado",
        "carbohydrates": 8.5,
        "fats": 15.4,
        "protein": 2.0,
        "sodium": 10.0,
        "sugars": 0.7,
        "vitamin_c": 10.0,
        "calories": 160.0
    },

    {"name": "Banana",
     "carbohydrates": 27.0,
     "fats": 0.3,
     "protein": 1.3,
     "sodium": 1.0,
     "sugars": 14.4,
     "vitamin_c": 14.6,
     "calories": 105.0
     },
    {
        "name": "Beef",
        "carbohydrates": 0.0,
        "fats": 15.0,
        "protein": 26.0,
        "sodium": 54.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 248.0
    },
    {
        "name": "Carrots",
        "carbohydrates": 10.0,
        "fats": 0.2,
        "protein": 1.0,
        "sodium": 88.0,
        "sugars": 4.7,
        "vitamin_c": 7.6,
        "calories": 41.0
    },
    {
        "name": "Cheese",
        "carbohydrates": 1.3,
        "fats": 33.1,
        "protein": 24.9,
        "sodium": 618.0,
        "sugars": 0.5,
        "vitamin_c": 0.0,
        "calories": 402.0
    },
    {
        "name": "Egg",
        "carbohydrates": 0.6,
        "fats": 4.8,
        "protein": 6.5,
        "sodium": 62.0,
        "sugars": 0.6,
        "vitamin_c": 0.0,
        "calories": 78.0
    },
    {
        "name": "Mushroom",
        "carbohydrates": 3.3,
        "fats": 0.3,
        "protein": 3.1,
        "sodium": 5.0,
        "sugars": 1.9,
        "vitamin_c": 1.5,
        "calories": 22.0
    },
    {
        "name": "Pork",
        "carbohydrates": 0.0,
        "fats": 21.0,
        "protein": 26.0,
        "sodium": 65.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 288.0
    },
    {
        "name": "Salmon",
        "carbohydrates": 0.0,
        "fats": 12.7,
        "protein": 20.4,
        "sodium": 59.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 206},
    {"name": "Peanut Butter",
     "carbohydrates": 10.0,
     "fats": 80.0,
     "protein": 7.0,
     "sodium": 147.0,
     "sugars": 3.0,
        "vitamin_c": 0,
        "calories": 480},
    {
        "name": "Broccoli",
        "carbohydrates": 6.6,
        "fats": 0.6,
        "protein": 2.8,
        "sodium": 33.0,
        "sugars": 1.7,
        "vitamin_c": 89.2,
        "calories": 34.0
    },
    {
        "name": "Spinach",
        "carbohydrates": 1.4,
        "fats": 0.2,
        "protein": 2.9,
        "sodium": 79.0,
        "sugars": 0.1,
        "vitamin_c": 28.1,
        "calories": 23.0
    },
    {
        "name": "Lentils",
        "carbohydrates": 20.1,
        "fats": 0.8,
        "protein": 9.0,
        "sodium": 4.0,
        "sugars": 1.8,
        "vitamin_c": 4.5,
        "calories": 116.0
    },
    {
        "name": "Quinoa",
        "carbohydrates": 21.3,
        "fats": 4.1,
        "protein": 4.4,
        "sodium": 7.0,
        "sugars": 0.9,
        "vitamin_c": 0.0,
        "calories": 120.0
    },
    {
        "name": "Grapes",
        "carbohydrates": 27.3,
        "fats": 0.2,
        "protein": 0.7,
        "sodium": 3.0,
        "sugars": 23.4,
        "vitamin_c": 3.2,
        "calories": 104.0
    },
    {
        "name": "Oats",
        "carbohydrates": 66.3,
        "fats": 1.4,
        "protein": 16.9,
        "sodium": 2.0,
        "sugars": 0.9,
        "vitamin_c": 0.0,
        "calories": 389.0
    },
    {
        "name": "Turkey Breast",
        "carbohydrates": 0.0,
        "fats": 0.7,
        "protein": 29.5,
        "sodium": 41.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 130.0
    },
    {
        "name": "Brown Rice",
        "carbohydrates": 44.8,
        "fats": 1.8,
        "protein": 5.5,
        "sodium": 7.0,
        "sugars": 0.4,
        "vitamin_c": 0.0,
        "calories": 216.0
    },
    {
        "name": "Pineapple",
        "carbohydrates": 21.7,
        "fats": 0.1,
        "protein": 0.9,
        "sodium": 1.0,
        "sugars": 16.3,
        "vitamin_c": 78.9, },
    {
        "name": "Sweet potato",
        "carbohydrates": 20.1,
        "fats": 0.1,
        "protein": 1.6,
        "sodium": 55.0,
        "sugars": 4.2,
        "vitamin_c": 2.4,
        "calories": 86.0
    },
    {
        "name": "Chicken breast",
        "carbohydrates": 0.0,
        "fats": 3.6,
        "protein": 31.0,
        "sodium": 67.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 165.0
    },
    {
        "name": "Tuna",
        "carbohydrates": 0.0,
        "fats": 0.9,
        "protein": 29.0,
        "sodium": 268.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 130.0
    },
    {
        "name": "Brown rice",
        "carbohydrates": 45.0,
        "fats": 2.0,
        "protein": 5.0,
        "sodium": 1.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 216.0
    },
    {
        "name": "Almonds",
        "carbohydrates": 6.1,
        "fats": 49.9,
        "protein": 21.2,
        "sodium": 1.0,
        "sugars": 1.4,
        "vitamin_c": 0.0,
        "calories": 579.0
    },
    {
        "name": "Kale",
        "carbohydrates": 5.0,
        "fats": 0.5,
        "protein": 3.3,
        "sodium": 38.0,
        "sugars": 0.0,
        "vitamin_c": 120.0,
        "calories": 33.0
    },
    {
        "name": "Salad greens",
        "carbohydrates": 2.9,
        "fats": 0.2,
        "protein": 1.6,
        "sodium": 25.0,
        "sugars": 0.6,
        "vitamin_c": 10.0,
        "calories": 15.0
    },
    {
        "name": "Oatmeal",
        "carbohydrates": 27.0,
        "fats": 2.5,
        "protein": 5.0,
        "sodium": 2.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 147.0
    },
    {
        "name": "Black beans",
        "carbohydrates": 24.0,
        "fats": 0.9,
        "protein": 15.2,
        "sodium": 1.0,
        "sugars": 0.0,
        "vitamin_c": 0.0,
        "calories": 227.0
    }
]

foodguess = []
answer = "Salmon"
answerdict = {"name": "Salmon",
              "carbohydrates": 0.0,
              "fats": 12.7,
              "protein": 20.4,
              "sodium": 59.0,
              "sugars": 0.0,
              "vitamin_c": 0.0,
              "calories": 206}


@ auth.route("/about_us")
def about_us():
    return render_template("about_us.html")


@ auth.route("/game", methods=["GET", "POST"])
def game():
    isright = False
    if request.method == "POST":
        isright = False
        data = request.form["my-input"]
        for food in foodlist:
            if food["name"].lower() == data.lower().strip():
                foodguess.append(food)
                print(foodguess)
                flash("This food is in our database!", category="success")
                if data == answer:
                    isright = True

                return render_template("game.html", foodguess=foodguess, answerdict=answerdict, isright=isright, answer=answer)
        flash("This food does not seem to be in our database! "
              "Please check for typos or choose another food. ", category="error")
        return render_template("game.html", foodguess=foodguess, answerdict=answerdict, isright=isright, answer=answer)
    return render_template("game.html", foodguess=foodguess, answerdict=answerdict, answer=answer)


@ auth.route("/list_foods")
def list_foods():
    return render_template("list_foods.html")
