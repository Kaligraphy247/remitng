from flask import Flask

# app
app = Flask(__name__)


# Database config
# nothing for now


# import the views, after the model has been initialized
from website.views import views



# register blueprints. either register this blueprint or import "app" instance in the views and auth module
app.register_blueprint(blueprint=views, url_prefix='/')




# if __name__ == "__main__":
#     app.run(debug=True, port=3000)
