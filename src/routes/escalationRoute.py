from flask import Blueprint, render_template, request, redirect, url_for
from src.controllers.setters import deletePlantonistFromEscalaByTeamID, deletePlantonistsFromTeam, deletePlantonistFromEscala, createNewEscala, deleteEscala, deletePlantonista, updatePlantonista, deleteTeam
from src.controllers.getters import getAllEscalationTeams, getInfoByIDPlantonist, getTeamIdByPlantonistId, getEscalaByTeam_, getAllPlatonistsByTeam_, getTeamNameByID, getTeamIdByPlantonistId
import json, re

escalationRoute = Blueprint('escala', __name__, url_prefix='/escala')


@escalationRoute.route("/equipe/<teamID>", methods=["GET", "POST"])
def getEscalation(teamID):
    allPlantonistsInEscala = []
    if request.method == "GET":
        allPlantonistsInEscala = getEscalaByTeam_(teamID)
    
    teamName = getTeamNameByID(teamID)


    return render_template('escalationByTeam.html', teamID=teamID, inEscala=allPlantonistsInEscala, team=teamName)


@escalationRoute.route("/edit/<teamID>", methods=["GET", "POST"])
def editEscalation(teamID):
    allPlantonistsInEscala = []
    if request.method == "GET":
        allPlantonistsInEscala = getEscalaByTeam_(teamID)
        allPlantonists = getAllPlatonistsByTeam_(teamID)
        plantonitsNotInEscala = [plantonist for plantonist in allPlantonists 
                                    if plantonist['idplantonista'] not in[ 
                                    plantonistEscala['idplantonista'] for plantonistEscala in 
                                    allPlantonistsInEscala]]

    elif request.method == "POST":
        escalaJson = request.get_json()
        newEscala = escalaJson['newEscala']
        escala = []
        position = 0
        for plantonistId in newEscala:
            tuple = (plantonistId, position)
            escala.append(tuple)
            position += 1

        deletedEscalation = deleteEscala(teamID)
        addedEscalation = createNewEscala(escala)
        if(deletedEscalation and addedEscalation):
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

        else:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

    teamName = getTeamNameByID(teamID)
    return render_template('editEscalationByTeam.html', teamID=teamID, inEscala=allPlantonistsInEscala, notInEscala=plantonitsNotInEscala, team=teamName)


@escalationRoute.route("/edit/escalation/<teamID>", methods=["GET", "POST"])
def editPlantonista(teamID):
    if request.method == 'POST':
        idplantonista = request.form['plantid']
        deletePlantonista(idplantonista)
        deletePlantonistFromEscala(idplantonista)


    allPlantonists = getAllPlatonistsByTeam_(teamID)
    teamName = getTeamNameByID(teamID)


    return render_template('editPlantonista.html', teamID=teamID, allPlantonists=allPlantonists, team=teamName)


@escalationRoute.route("/edit/plantonist/<plantID>", methods=["GET", "POST"])
def editPlantonistaByID(plantID):
    if request.method == "POST":
        plantonist = request.form
        updatedPlantonista = updatePlantonista(plantonist['name'], plantonist['cellphone'], plantonist['email'], plantonist['team'], plantID)
        
        if updatedPlantonista:
            teamID = getTeamIdByPlantonistId(plantID)
            return redirect(url_for('escala.editPlantonista', teamID=teamID))

        else:
            return render_template('editPlantonistaById.html', plantID=plantID, plantonist=plantonistInfo, teamID=teamID)    
    
    
    plantonistInfo = getInfoByIDPlantonist(plantID)
    teamID = getTeamIdByPlantonistId(plantID)


    return render_template('editPlantonistaById.html', plantID=plantID, plantonist=plantonistInfo, teamID=teamID)


@escalationRoute.route("/remove", methods=["GET", "POST"])
def removeTeams():
    if request.method == "POST":
        teamID = request.form['teamID']
        deletePlantonistFromEscalaByTeamID(teamID)
        deletePlantonistsFromTeam(teamID)
        deleteTeam(teamID)


    teams = getAllEscalationTeams()

    return render_template('removeTeams.html', allTeams=teams)