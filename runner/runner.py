import sqlite3
user = "temp"
with sqlite3.connect(f"{user}.db") as conn:
    cursor = conn.cursor()
    while True:
        inp = input(f"\nsql@{user}>>> ")
        try:
            out = cursor.execute(inp)
            print(out.fetchall())
        except sqlite3.OperationalError:
            print(f"Recheck query ---- '{inp}'")
        
# conn.close() is automatic here
