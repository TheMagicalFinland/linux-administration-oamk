from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/')

def home():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host="localhost",
 user="exampleuser",
 password="_",
 database="exampledb"
 )

 cursor = conn.cursor()
 cursor.execute("SELECT 'Hello from MySQL!'")
 original_message = cursor.fetchone()
 cursor.execute("SELECT NOW();")
 server_time = cursor.fetchone()[0] 

 # Clean up
 cursor.close()
 conn.close()
 return f"<h1>{original_message[0]}</h1><br/><br/>Tietokannan kellonaika on tällä hetkellä:<br/>{server_time}<br\><br/>Tähän tälläinen hauska lopputeksti personoinniksi :)"

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)