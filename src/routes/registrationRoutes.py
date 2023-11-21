from flask import Blueprint, render_template, request
from src.controllers.setters import addTeam, addPlantonista
from src.controllers.getters import getTeamIDFromQualitorByName
import re

addRoute = Blueprint('add', __name__, url_prefix='/add')


@addRoute.route("/equipe", methods=["GET", "POST"])
def addequipe():
    if(request.method == "POST"):
        try:
            teamName = request.form['teamName']
            teamID, qualitorName = getTeamIDFromQualitorByName(teamName)
            added = addTeam(qualitorName, teamID)
            if(added==False):
                return render_template('addEquipe.html', blockToShow="Erro")
            return render_template('addEquipe.html', blockToShow="Sucesso", teamRegistered=qualitorName)
        except Exception as e:
            print(e)
            return render_template('addEquipe.html', blockToShow="Erro")
    else:    
        return render_template('addEquipe.html', blockToShow="Cadastro")


@addRoute.route("/plantonista", methods=["GET", "POST"])
def addplantonista():
    if request.method=="POST":
        try:
            plantonist = request.form
            addedplantonista = addPlantonista(plantonist["name"], plantonist["email"], plantonist["team"], re.sub("[^0-9]", "", plantonist["cellphone"]))
            if addedplantonista==True:
                return render_template('addplantonista.html', blockToShow="Sucesso")
                
            else:
                return render_template('addplantonista.html', blockToShow="Erro")
        except Exception as e:
            print(e)
            return render_template('addplantonista.html', blockToShow="Erro")

    return render_template ('addplantonista.html')


