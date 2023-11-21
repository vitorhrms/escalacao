from src.connections.escalationdb import connectToEscalationDB

'''
    function createNewEscala
    params: list of tuples containing plantonist id and teamid
    return: true for success, false for any errors.
'''
def createNewEscala(escalationList: list) -> bool:
    try:
        valuesToInput = ""
        for escalation in escalationList:
            valuesToInput += str(escalation) + ","
        query = '''
                INSERT INTO 
                    escalation_escala (idplantonista, ordem) 
                VALUES
                    {}
                '''.format(valuesToInput[:-1])
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        return True
    except: 
        print("Erro no insert new escala")
        return False


def deleteEscala(teamID: int) -> bool:
    try:
        query = '''
                DELETE FROM escalation_escala
                WHERE 
                    idplantonista 
                    IN 
                    (select idplantonista from escalation_plantonista WHERE idequipe = '{}')
                '''.format(teamID)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao deletar escala")
        return False


def addPlantonista(name: str, email: str, teamID: int, cellphone: str) -> bool:
    try:
        query = '''
            INSERT INTO 
                escalation_plantonista (idequipe, nome, email, telefone) 
            VALUES ('{}', '{}', '{}', '{}')
            '''.format(teamID, name, email, str(cellphone))
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("Erro ao add novo plantonista")
        return False

def addTeam(name: str, id: int) -> bool:
    try:
        query = ''' 
                INSERT INTO 
                    escalation_equipe (idequipe, nome) 
                VALUES
                    ('{}', '{}')
        '''.format(id, name)

        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("failed to add team")
        return False


        
def deletePlantonista(IDplantonista: int) -> bool:
    try:
        query = '''
            DELETE FROM 
                escalation_plantonista
            WHERE 
                idplantonista = '{}'
            '''.format(IDplantonista)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar plantonista")
        return False


def updatePlantonista(nome: str, cellphone: str, email: str, IDequipe: int, IDplantonista: int) -> bool:
    try:
        query = '''
            UPDATE 
                escalation_plantonista 
            SET 
                nome='{}', 
                telefone='{}', 
                email='{}', 
                idequipe='{}' 
            WHERE 
                idplantonista = '{}'
            '''.format(nome, cellphone, email, IDequipe, IDplantonista)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro no update plantonista")
        return False

def deleteTeam(teamID: int) -> bool:
    try:
        query = '''
            DELETE FROM 
                escalation_equipe
            WERE 
                idequipe = '{}'
            '''.format(teamID)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar equipe")
        return False

def deletePlantonistsFromTeam(teamID: int) -> bool:
    try:
        query = '''
            DELETE FROM 
                escalation_plantonista 
            WHERE 
                idequipe = '{}'
            '''.format(teamID)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar plantonista do time")
        return False

def deletePlantonistFromEscala(plantID: int) -> bool:
    try:
        query = '''
            DELETE FROM 
                escalation_escala 
            WHERE 
                idplantonista = '{}'
            '''.format(plantID)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar plantonista da escala")
        return False


def deletePlantonistFromEscalaByTeamID(teamID: int) -> bool:
    try:
        query = """
        DELETE FROM 
            escalation_escala 
        WHERE 
            idplantonista 
        IN 
            (select idplantonista FROM escalation_plantonista WHERE idequipe = '{}')
        """.format(teamID)
        conn = connectToEscalationDB()
        conn.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        print("Erro ao deletar plantonista da escala")
        return False