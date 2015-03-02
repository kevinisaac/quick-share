#db_ops.py is database operations
from flask import Flask, render_template, request
import peeweeHandler as pwH

user = pwH.User()

def signup(uname, passwd):
	
	flag = 1
	if not uname:
		flag = 0
		error = "Bad usersame"
		state = error
		return state
	if not passwd:
		flag = 0
		error = "Bad Password"
		state = error
		return state
	if(flag == 1):
		user.create(username=uname, password=passwd)
		state = "Account Created"
		return state

