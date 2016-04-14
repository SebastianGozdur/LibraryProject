from sqlalchemy import create_engine
#import MySQLdb
import mysql.connector


engine = create_engine('mysql+mysqlconnector://librarysystem:mydatabse@librarysystem.mysql.pythonanywhere-services.com/librarysystemdatabase')
#connection = engine.connect()
