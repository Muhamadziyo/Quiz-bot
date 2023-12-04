import sqlite3

from datetime import datetime

connection = sqlite3.connect('date.db')
sql = connection.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users1 (id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT,telegram_id INTEGER, phone_number TEXT,coin INTEGER, reg_date DATETIME);""")


sql.execute("""CREATE TABLE IF NOT EXISTS users2 (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, correct_answer INTEGER, optins TEXT);""")


sql.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMAY KEY AUTOINGCREMENT,telegram_id INTEGER,correct_answer,get_coind INTEGER, played_date DATATIME);")




def register_user(first_name,telegram_id,phone_number,coin=0):

    connection = sqlite3.connect('date.db')
    sql = connection.cursor()

    sql.execute(""" INSERT INTO users1 (first_name,telegram_id,phone_number,coin,reg_date) VALUES (?,?,?,?,?); """,(first_name,telegram_id,phone_number,coin,datetime.now()))
    connection.commit()
    connection.close()

def check_user(telegram_id):
    connection = sqlite3.connect('date.db')
    sql = connection.cursor()

    a = sql.execute("""SELECT * FROM users1 WHERE telegram_id=?;""",(telegram_id,)).fetchone()
    connection.commit()
    connection.close()
    
    if a:
        return True

    else:
        return False

connection.close()

def add_history(telegram_id,correct_answer,get_coins):
  connection = sqlite3.connect('data.db')
  sql = connection.cursor()
  
  sql.execute("INSERT INTO users(telegram_id,correct_answer,get_coins,played_date) VALUES(?,?,?,?);",(telegram_id,correct_answer,get_coins,datetime.now()))

  connection.commit()
  connection.close()

def get_history(telegram_id):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor() 

    user_history = sql.execute("SELECT correct_answer,get_coins,played_date FROM history WHERE telegram_id=?",(telegram_id,)).fetchall()
    connection.commit()
    connection.close()
    
    if user_history:
        return user_history.fetchall()
    
    else:
        return 
    

def add_question(question,correct_answer,options):
  connection = sqlite3.connect('data.db')
  sql = connection.cursor()
  
  sql.execute("INSERT INTO quustions(question,correct_answer,options) VALUES(?,?,?);",(question,correct_answer,options))  
  connection.commit()
  connection.close()
  

def delete_question(question):
    sql.execute("DELETE FROM question=?;",(question,))

    connection.commit()
    connection.close()

def update_question(new_question,question):
   connection =sqlite3.connect('data.db')
   sql = connection.cursor()  
    
   sql.execute("UPDATE question SET question=?WHERE question=?;",(new_question,question)) 
   connection.commit()
   connection.close()


