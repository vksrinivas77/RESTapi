from app import app
import mysql.connector
import json

class model:
    def __init__(self):
        try:
            self.con =mysql.connector.connect( host='localhost',user='root',password='',database='todo_db')
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("succfull connection ")
        except:
            print("error in db connection")
    def read(self):
        self.cur.execute("Select * from todos")
        result=self.cur.fetchall()
        return {"payload": result}
        
    def add(self,data):
        try:
            self.cur.execute(f"insert into tb (task,role,department) VALUES('{data ['task']}', '{data['role']}', '{data['department']}') ")
            return "successfull inserted data into db"
        except:
            return "error"
    def update(self, data):
         try:
            query = "UPDATE tb SET task = %s, role = %s, department = %s WHERE id = %s"
            values = (data['task'], data['role'], data['department'], data['id'])
            self.cur.execute(query, values)
            return "Successfully updated"
         except Exception as e:
           print(f"An error occurred: {e}")
           return "Error occurred while updating"
    def delete(self, data):
         try:
            query = "DELETE FROM tb WHERE id=%s"
            values = ( data['id'],)
            self.cur.execute(query, values)
            return "Successfully deleted"
         except Exception as e:
           print(f"An error occurred: {e}")
           return "Error occurred while deleting"
            