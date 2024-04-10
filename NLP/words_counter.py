from typing import Any
import pandas as pd
from pyodbc import Connection, connect, Cursor
from collections import Counter
from datetime import datetime
import json
import operator
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
        
    def build_dataset(query: str, cursor: Cursor) -> pd.DataFrame:
        df = pd.read_sql()

    


mssql = MSSQL("capnet.ddns.net", "sa", ".5capnet", "redmine")
cnxn = mssql.get_connect()
cursor = cnxn.cursor()

query = "SELECT [id], [description] FROM dbo.issues order by id desc;"
df = pd.read_sql(query, cnxn)
sentences = []
[sentences.append(df_element) for df_element in df["description"]]

words = []
for sentence in sentences:
    splited = sentence.split(" ")
    words.extend(splited)

words_data = dict(sorted(Counter(words).items(), key=operator.itemgetter(1), reverse=True))
with open('different_words.json', 'w', encoding='utf-8') as f:
    json.dump(words_data, f, ensure_ascii=False, indent=4)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))