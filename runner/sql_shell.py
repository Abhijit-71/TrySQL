import sqlite3
from tabulate import tabulate  # for formatting tables like sql shell
        

def sql_runner(user:str,query:str) -> str:
    
    with sqlite3.connect(f"user_db\\{user}.db") as conn:
        
        cursor = conn.cursor()
        
        while True:
           
            try: 
                ch_query = query.strip().upper()
                result = ""
                
                if ch_query.startswith("SELECT"):    # handles read 
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    cols = [desc[0] for desc in cursor.description]
                    result += tabulate(rows, headers=cols, tablefmt="grid") + f"\n\n{len(rows)} row(s) in set"
                
                elif "DATABASE" in ch_query or "DATABASE" in ch_query or ch_query.startswith("USE"):
                    raise Exception("Database level command not supported")
                
                elif ch_query.startswith("SHOW TABLES"): # exceptional sqlite command handling
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                    rows = cursor.fetchall()
                    cols = ["list_of_tables"]
                    result += tabulate(rows, headers=cols, tablefmt="grid") + f"\n\n{len(rows)} row(s) in set"
                
                elif ch_query.startswith(("DESC","DESCRIBE")): # exceptional sqlite command handling
                    table = query.split()[1]
                    cursor.execute(f"PRAGMA table_info({table});")
                    rows = cursor.fetchall()
                    cols = [desc[0] for desc in cursor.description]
                    result += tabulate(rows, headers=cols, tablefmt="grid") + f"\n\n{len(rows)} row(s) in set"
                
                else:
                    cursor.execute(query)
                    affected = cursor.rowcount
                    if affected == -1:  # DDL usually returns -1
                        affected = 0
                    result += f"Query OK, {affected} row(s) affected"


            
                if ch_query.startswith(("INSERT", "UPDATE", "DELETE", "REPLACE")): #commits DML
                    conn.commit() 
                
                return result
            
            except Exception as e:
                conn.rollback()
                error = "Error occurred : "+ str(e) +"\nNo changes committed."
                return error
                
                