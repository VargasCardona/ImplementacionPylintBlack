"""
This module sets up the database connection and defines the ORM models for the application.
Classes:
    PersonModel(Model): ORM model for the 'persons' table.
        Attributes:
            id (AutoField): Primary key.
            name (CharField): Name of the person.
            age (IntegerField): Age of the person.
            email (CharField): Email of the person.
            address (CharField): Address of the person.
            is_employed (BooleanField): Employment status of the person.
            salary (DoubleField): Salary of the person.
    CatModel(Model): ORM model for the 'cats' table.
        Attributes:
            id (AutoField): Primary key.
            name (CharField): Name of the cat.
            color (CharField): Color of the cat.
            age (IntegerField): Age of the cat.
            breed (CharField): Breed of the cat.
            weight (DoubleField): Weight of the cat.
            owner_id (IntegerField): ID of the owner (foreign key).
"""

import os
from dotenv import load_dotenv

from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DoubleField,
    IntegerField,
    Model,
    MySQLDatabase,
)


load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class PersonModel(Model):
    """
    PersonModel is a database model representing a person with various attributes.
    Attributes:
        id (AutoField): The primary key for the person.
        name (CharField): The name of the person, with a maximum length of 50 characters.
        age (IntegerField): The age of the person.
        email (CharField): The email address of the person, with a maximum length of 50 characters.
        address (CharField): The address of the person, with a maximum length of 50 characters.
        is_employed (BooleanField): Employment status of the person.
        salary (DoubleField): The salary of the person.
    Meta:
        database: The database connection to use for this model.
        table_name: The name of the table in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    age = IntegerField()
    email = CharField(max_length=50)
    address = CharField(max_length=50)
    is_employed = BooleanField()
    salary = DoubleField()

    class Meta:
        """
        Meta class for configuring database settings.
        Attributes:
            database: The database connection instance.
            table_name (str): The name of the table in the database.
        """

        database = database
        table_name = "persons"


class CatModel(Model):
    """
    CatModel is a database model representing a cat entity.
    Attributes:
        id (AutoField): The primary key for the cat.
        name (CharField): The name of the cat, with a maximum length of 50 characters.
        color (CharField): The color of the cat, with a maximum length of 50 characters.
        age (IntegerField): The age of the cat.
        breed (CharField): The breed of the cat, with a maximum length of 50 characters.
        weight (DoubleField): The weight of the cat.
        owner_id (IntegerField): The ID of the owner of the cat.
    Meta:
        database: The database connection to use for this model.
        table_name: The name of the table in the database.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    color = CharField(max_length=50)
    age = IntegerField()
    breed = CharField(max_length=50)
    weight = DoubleField()
    owner_id = IntegerField()

    class Meta:
        """
        Meta class for configuring the database settings.
        Attributes:
            database: The database connection instance.
            table_name (str): The name of the table in the database.
        """

        database = database
        table_name = "cats"
