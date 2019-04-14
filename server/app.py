import os
from flask import Flask, request
from flask_cors import CORS

from views.home_view import HomeView


app = Flask(__name__, template_folder='templates')

# Enable CORS app-wide
CORS(app)


# TODO: add API endpoints using Flask Views
app.add_url_rule('/home', view_func=HomeView.as_view('home_view'))




if __name__ == '__main__':
    port = 8080
    print("Now running Flask Server out of port %s" % port) 
    app.run(port=port, host='0.0.0.0')
