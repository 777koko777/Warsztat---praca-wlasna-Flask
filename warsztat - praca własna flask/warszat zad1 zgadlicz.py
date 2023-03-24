from flask import Flask, render_template, request
import random

app = Flask(__name__)

number = random.randint(1, 100)


@app.route('/', methods=['GET', 'POST'])
def play_game():
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
        except:
            return render_template("game.html", message="It's not a number!")
        if guess < number:
            message = "Too small!"
        elif guess > number:
            message = "Too big!"
        else:
            message = "You win!"
        return render_template("game.html", message=message)
    else:
        return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)
