from flask import Flask, render_template
from src.routes.registrationRoutes import addRoute
from src.routes.escalationRoute import escalationRoute
from src.controllers.getters import getAllEscalationTeams

app = Flask(__name__, template_folder='src/templates',  static_folder='src/static')

app.config['SECRET_KEY'] = '59371830d4ba99ddf9ff52a4d02dd56a6daf130c4417b9f7'

app.register_blueprint(addRoute)
app.register_blueprint(escalationRoute)

@app.context_processor
def setMenuGlobalVariables():
  allTeams = getAllEscalationTeams()
  return {"allTeams":allTeams}

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/_/edit")
def editIndex():
  return render_template('indexEdit.html')
  

if __name__=='__main__':  
  app.run(debug=True, host="0.0.0.0")

  