import pandas as pd
from pyodbc import Connection, connect, Cursor

from datetime import datetime

start_time = datetime.now()

class MSSQL():
    def __init__(self, server: str,user: str, password: str, database: str) -> None:
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.port: str = "1433"
        self.driver: str = "{SQL Server}"
    
    
    def generate_string_connection(self) -> str:
        print(f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.user};PWD={self.password};PORT={self.port}")
        return f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.user};PWD={self.password};PORT={self.port}"
    
    def get_connect(self) -> Connection:
        try:
            connection = connect(self.generate_string_connection())
            return connection
        except Exception as error:
            return (error)
        
    def build_dataset(self, query: str, cursor: Cursor) -> pd.DataFrame:
        df = pd.read_sql()

    

## Colocal los datos de conexion en las siguientes variables 

SERVER = "capnet.ddns.net"
USER = "sa"
PASSWORD = ".5capnet"
DATABASE = "capnet-apps-bi-soni"
TABLE = "FV_DC_ANL_FV_DC_OPERACIONES_SERVICIO_KM"
mssql = MSSQL(f"{SERVER}", f"{USER}", f"{PASSWORD}", f"{DATABASE}")
cnxn = mssql.get_connect()
print(cnxn)


QUERY = "SELECT * FROM v_creta_nextgen_model"
df = pd.read_sql(QUERY, cnxn)

save_file_to_csv = df.to_csv("data_hyundai_creta.csv")