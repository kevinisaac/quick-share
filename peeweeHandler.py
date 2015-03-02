import peewee as pw
import configDB

#do not chnage DB connection parm from here i suggest you to use configDB.py
config = configDB.configdb()
db = pw.MySQLDatabase(config.db_name, host=config.db_host, port=config.db_port, user=config.db_user, passwd=config.db_passwd)

class MySQLModel(pw.Model):

	class Meta:
		database = db

class User(MySQLModel):

	username = pw.CharField(unique=True)
	password = pw.CharField()

def create_tables():
	db.connect()
	db.create_tables([User])
