from dotenv import load_dotenv
from peewee import *
                                                                                                                                                                      
import os                                                                                                                                                             
                                                                                                                                                                      
load_dotenv()
                                                                                                                                                                      
database = MySQLDatabase(                                                                                                                                             
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        passwd=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),                                                                                                                                 
        port=int(os.getenv("MYSQL_PORT"))    
        )                                                                                                                                                             

class PersonModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    age = IntegerField()
    email = CharField(max_length=50)
    address = CharField(max_length=50)
    is_employed = BooleanField()
    salary = DoubleField()

    class Meta:
       database = database
       table_name = "persons"

class CatModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    color = CharField(max_length=50)
    age = IntegerField()
    breed = CharField(max_length=50)
    weight = DoubleField()
    owner_id = IntegerField()

    class Meta:
       database = database
       table_name = "cats"


