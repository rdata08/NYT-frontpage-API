from backend.config import Config
from typing import Optional
import subprocess
import textwrap
import mysql.connector
import time

class DatabaseDriver():
  def __init__(self) -> None:
    while True:
      try:
        self.conn = mysql.connector.connect(host = Config.db_host, database=Config.db_database, user=Config.db_user, password=Config.db_password)
        print("Connection successful")
        break
      except Exception as e:
        print("Connection unsuccessful")
        print("Error", e)
        time.sleep(3)
  
  def nytUpdate(self) -> None:
    try:
      NYTdata = subprocess.run(['python3', 'backend/script.py'], capture_output= True, text= True)
      data = textwrap.dedent(str(NYTdata.stdout.strip()))
  
      cursor = self.conn.cursor()
      sql = "INSERT INTO mytable (address) VALUES (%s)"
      cursor.execute(sql, (data,))
      self.conn.commit()
      print("Data success")
    except Exception as e:
      print("New York Times Update unsuccessful")
      print("Error", e)
    finally:
      self.conn.close()

  def getRandom(self) -> Optional[tuple]:
    try:
      cursor = self.conn.cursor()
      cursor.execute("SELECT * FROM mytable LIMIT 1;")
      result = cursor.fetchone()
      return result 
    except Exception as e:
      print("Get random element unsuccessful")
      print("Error", e)
      return None
    finally:
      self.conn.close()
