from flask import Flask, render_template
from flask_login import LoginManager
from flask_blogging import BloggingEngine
from flask_blogging.dynamodbstorage import DynamoDBStorage
from routes import setup_auth

app = Flask(__name__)
app.config.from_object("config")

# extensions
# dyn_storage = DynamoDBStorage(endpoint_url='http://localhost:8000')  # local testing
dyn_storage = DynamoDBStorage(region_name='us-east-2')
blog_engine = BloggingEngine(app, dyn_storage)
login_manager = LoginManager(app)


@app.route("/")
def index():
    return render_template("index.html")

setup_auth(app, login_manager, blog_engine)

if __name__ == "__main__":
    app.run(debug=True, port=8001, use_reloader=True, )

