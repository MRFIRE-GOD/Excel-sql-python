import subprocess

def view_data_in_info_db():
    subprocess.call(["sqlite3", "info.db", ".headers on", ".mode column", "SELECT * FROM name;"])

view_data_in_info_db()
