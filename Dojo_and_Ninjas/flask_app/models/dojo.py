from unittest import result
from xml.etree.ElementTree import QName
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
      self.id = data('id')
      self.name = data('name')
      self.created_at = data('created_at')
      self.updated_at = data('updated_at')
      self.ninjas = []

    @classmethod
    def get_all(cls):
      query = "SELECT * FROM dojos"  

      results = connectToMySQL('Dojos_Ninjas_Schema').query_db(query)
      dojo = []

      for d in results:
        dojos.append( cls(d))
      return dojos  

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('Dojos_and_Ninjas_Schema').query_db(query,data)
        return result  