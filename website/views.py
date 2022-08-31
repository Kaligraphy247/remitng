from flask import render_template, Blueprint, request, url_for, redirect
# import website.black
from website.black import main



views = Blueprint(name='views', import_name=__name__)


@views.route("/")
def index():
    # it is reverse in this case
    buy_eur = main.selling_rate_eur
    sell_eur = int(main.buying_rate_eur) - 15
    date = main.current_date_eur
    price_info = (buy_eur, sell_eur, date)
    return render_template(template_name_or_list='index.html', price_info=price_info)
    # return "<h1 style='color: red';>Hello world</h1>"


@views.route("/b")
def home():
    # return render_template(template_name_or_list="send.html")
    # EUR = main.buying_rate_eur
    # EUR2 = main.selling_rate_eur
    # return f"{EUR}, {EUR2}"
    return render_template(template_name_or_list='404_temp.html')

@views.route("/send")
def send():
    return render_template(template_name_or_list="send.html")


@views.route("/receive")
def receive():
    return render_template(template_name_or_list="receive.html")

@views.route("/price")
def prices():
    buy_eur = main.selling_rate_eur 
    sell_eur = int(main.buying_rate_eur) - 15
    date = main.current_date_eur
    price_info = (buy_eur, sell_eur, date)
    return render_template(template_name_or_list='price.html', price_info=price_info)


@views.errorhandler(404)
def notFound(error):
    """Not Found error, 404"""
    return render_template(template_name_or_list="404.html")