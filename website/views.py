from flask import render_template, Blueprint, request, url_for


# blueprint
views = Blueprint(name='views', import_name=__name__)


@views.route("/")
def index():
    return render_template(template_name_or_list='index.html')
    # return "<h1 style='color: red';>Hello world</h1>"


# @views.route("/b")
# def home():
#     return render_template(template_name_or_list="send.html")

@views.route("/send")
def send():
    return render_template(template_name_or_list="send.html")


@views.route("/receive")
def receive():
    return render_template(template_name_or_list="receive.html")

@views.route("/pr1c3")
def prices():
    return render_template(template_name_or_list='price.html')
