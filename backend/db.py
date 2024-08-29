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
  
  def insert(self, table, data, col) -> None:
    try:
      cursor = self.conn.cursor()
      sql = f"INSERT INTO {table} ({col}) VALUES (%s)"
      cursor.execute(sql, (data,))
      self.conn.commit()
      print("Data success")
    except Exception as e:
      print("New York Times Update unsuccessful")
      print("Error", e)
    finally:
      self.conn.close()

  def nytUpdate(self) -> None:
    NYTdata = subprocess.run(['python3', 'backend/script.py'], capture_output= True, text= True)
    data = textwrap.dedent(str(NYTdata.stdout.strip()))
    
    self.insert("mytable", data, "address")

  def getRandom(self) -> Optional[list]:
    try:
      cursor = self.conn.cursor()
      cursor.execute("SELECT * FROM mytable LIMIT 4;")
      results = cursor.fetchall()
      return results
    except Exception as e:
      print("Get random element unsuccessful")
      print("Error", e)
      return None
    finally:
      self.conn.close()
  
  # def retrieve(self, selector, )

  def getbyId(self, id) -> Optional[str]:
    try:
      cursor = self.conn.cursor()
      cursor.execute(f"SELECT id FROM mytable WHERE id={id};")
      result = cursor.fetchone()
      return result
    except Exception as e:
      print("Get by id unsuccessful")
      print("Error", e)
    finally:
      self.conn.close()

  # Returns article by headline
  def getArticlebyHeadline(self, headline) -> Optional[str]:
    try:
      cursor = self.conn.cursor()
      cursor.execute(f"SELECT article FROM mytable WHERE headline={headline};")
      result = cursor.fetchone()
      return result
    except Exception as e:
      print("Get by headline unsuccessful")
      print("Error", e)
    finally:
      self.conn.close()
  
  # gets link to article title
  def getLinkbyHeadline(self, headline) -> Optional[str]:
    try:
      cursor = self.conn.cursor()
      cursor.execute(f"SELECT link FROM mytable WHERE headline={headline};")
      result = cursor.fetchone()
      return result
    except Exception as e:
      print("Get by headline unsuccessful")
      print("Error", e)
    finally:
      self.conn.close()