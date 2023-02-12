import random
from flask import flash
from flask import render_template
from flask import request
from . import blueprint


@blueprint.route("/")
@blueprint.route("/home")
def home():
    return render_template("home.html")


@blueprint.route("/about")
def about():
    return render_template("about.html")


@blueprint.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy-policy.html")

POKER_RANKS = {0:"2", 1:"3", 2:"4", 3:"5", 4:"6", 5:"7", 6:"8", 7:"9", 8:"10", 9:"J", 10:"Q", 11:"K", 12:"A"}
POKER_SUITS = {0:"♣梅花", 1:"♦方塊", 2:"♥紅心", 3:"♠黑桃"}


@blueprint.route("/highcard", methods=["GET", "POST"])
def highcard():

    def get_card():
        value = random.sample(range(0, 51), k=1)[0]
        card = f"{POKER_SUITS.get(value % 4)}{POKER_RANKS.get(value // 4)}"
        return card, value

    first_card, first_card_value = get_card()

    if request.method == "POST":
        card = request.form.get("firstCard")
        card_value = int(request.form.get("firstCardValue"))
        guess = request.form.get("guess")
        second_card, second_card_value = get_card()

        match guess:
            case "大":
                win = True if second_card_value > card_value else False
            case "小":
                win = True if second_card_value < card_value else False

        if win:
            flash(f"你贏了，第二張牌是 {second_card}")
        else:
            flash(f"你輸了，第二張牌是 {second_card}")

    return render_template(
        "highcard.html",
        first_card=first_card,
        first_card_value=first_card_value,
    )