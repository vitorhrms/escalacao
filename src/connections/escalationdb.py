import pyodbc
from dotenv import load_dotenv
import os
load_dotenv()

conn_str = (
  r'Driver={driver};'
  r'Server={ip};'
  r'Database={db};'
  r'UID={login};'
  r'PWD={password};'
  r'TrustServerCertificate=Yes;'
).format(driver=os.environ.get("DRIVER_PATH"),
         ip=os.environ.get("ESCALATION_IP"),
         db=os.environ.get("ESCALATION_DB"), 
         login=os.environ.get("ESCALATION_DB_LOGIN"), 
         password=os.environ.get("ESCALATION_DB_PASSWORD"))

def connectToEscalationDB():
  connection = pyodbc.connect(conn_str)
  return connection.cursor()