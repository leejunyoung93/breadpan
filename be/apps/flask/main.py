from flask import Flask
from flask_restful import Api
import resources as r

app = Flask(__name__)
api = Api(app)


##
# Actually setup the Api resource routing here
##

api.add_resource(r.FlaskTodoListController, '/todos')
api.add_resource(r.FlaskTodoController, '/todos/<todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
