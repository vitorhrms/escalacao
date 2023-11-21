from src.connections.escalationdb import connectToEscalationDB

def getAllPlatonistsByTeam(teamID: int) -> list:
    query = '''
            SELECT
                idplantonista, 
                idequipe, 
                nome, 
                telefone, 
                email, 
                escalado 
            FROM 
                escalation_plantonista 
            WHERE
                idequipe = {} 
            '''.format(teamID)
    conn = connectToEscalationDB()

    conn.execute(query)
    plantonists = conn.fetchall()
    conn.commit()
    conn.close()

    return plantonists

def getAllPlatonistsByTeam_(teamID: int) -> dict:
    query = '''
            SELECT 
                idplantonista,
                idequipe,
                nome, 
                telefone, 
                email, 
                escalado 
            FROM
                escalation_plantonista 
            WHERE 
                idequipe = {}
            '''.format(teamID)
    conn = connectToEscalationDB()

    conn.execute(query)
    columns = [column[0] for column in conn.description]

    plantonists = []
    for row in conn.fetchall():
        plantonists.append(dict(zip(columns, row)))
     
    conn.commit()
    conn.close()

    return plantonists

def getEscalaByTeam(teamID: int) -> list:
    query = '''
            SELECT 
                plant.idplantonista, 
                escala.ordem, 
                plant.idequipe, 
                plant.nome, 
                plant.telefone, 
                plant.email, 
                equipe.idequipe, 
                equipe.nome 
            FROM 
                escalation_plantonista AS plant
            JOIN escalation_escala AS escala ON escala.idplantonista = plant.idplantonista
            JOIN escalation_equipe AS equipe ON equipe.idequipe = plant.idequipe
            WHERE 
                plant.idequipe = {}
            ORDER BY 
                escala.ordem
            '''.format(teamID)
    conn = connectToEscalationDB()
    
    conn.execute(query)
    escalation = conn.fetchall()
    conn.commit()
    conn.close()

    return escalation

def getEscalaByTeam_(teamID: int) -> dict:
    query = '''
            SELECT 
                plant.idplantonista, 
                escala.ordem, 
                plant.idequipe, 
                plant.nome AS nome_plantonista, 
                plant.telefone, 
                plant.email, 
                equipe.idequipe, 
                equipe.nome AS nome_equipe 
            FROM 
                escalation_plantonista AS plant
            JOIN escalation_escala AS escala ON escala.idplantonista = plant.idplantonista
            JOIN escalation_equipe AS equipe ON equipe.idequipe = plant.idequipe
            WHERE 
                plant.idequipe = {}
            ORDER BY 
                escala.ordem
            '''.format(teamID)
    conn = connectToEscalationDB()
     
    conn.execute(query)
    columns = [column[0] for column in conn.description]

    escalation = []
    for row in conn.fetchall():
        escalation.append(dict(zip(columns, row)))
    
    
    conn.commit()
    conn.close()


    return escalation

def getTeamNameByID (teamID: int) -> str:
    query = ''' 
            SELECT 
                nome
            FROM 
                escalation_equipe 
            WHERE 
                idequipe = {} 
            '''.format(teamID)
    conn = connectToEscalationDB()

    conn.execute(query)
    teamName = conn.fetchone()
    conn.commit()
    conn.close()

    try:
        return teamName[0]
    except:
        return ""

def getAllEscalationTeams() -> list:
    query = '''
            SELECT
                * 
            FROM 
                escalation_equipe 
            ORDER BY
                nome asc
            '''
    conn = connectToEscalationDB()

    conn.execute(query)
    teams = conn.fetchall()
    conn.commit()
    conn.close()

    return teams

    

def getTeamIDFromQualitorByName(name:str) -> tuple:
    query = ''' - '''.format(name)
    conn = connectToEscalationDB()
    
    conn.execute(query)
    teamInfo = conn.fetchone()
    conn.commit()
    conn.close()
    try:
        return int(teamInfo[0]), str(teamInfo[1])
    except:
        return None



def getTeamIdByPlantonistId(plantID: int) -> list:
    query = '''
            SELECT
                idequipe 
            FROM 
                escalation_plantonista
            WHERE 
                idplantonista = {}
            '''.format(plantID)

    conn = connectToEscalationDB()

    conn.execute(query)
    teamID = conn.fetchone()
    conn.commit()
    conn.close()
    try:
        return int(teamID[0])
    except:
        return None




def getInfoByIDPlantonist(plantID: int) -> dict:
    query = '''
            SELECT 
                * 
            FROM 
                escalation_plantonista 
            WHERE 
                idplantonista = {} 
            '''.format(plantID)
    conn = connectToEscalationDB()

    conn.execute(query)
    columns = [column[0] for column in conn.description]

    plantonistInfo = []
    for row in conn.fetchall():
        plantonistInfo.append(dict(zip(columns, row)))
    
    
    conn.commit()
    conn.close()


    return plantonistInfo[0]




