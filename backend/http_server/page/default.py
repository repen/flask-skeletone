from flask import render_template


def welcome_page():
    return render_template("welcome_page.html")