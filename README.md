# quick-share
QuickShare is a simple browser plugin that allows you to share a URL with a friend.

# How it works?
It has two components.
  1. The web API
  2. The browser extension

Every user first creates an account in the website. Then, he can share his username/email with his friends.The user should be able to share any URL via the plugin with any other user who has the browser extension, through his username/email.

The URL gets shared right in the browser of the other user.

# Technology used
1. Language - Python2.7
2. Framework - [Flask](http://flask.pocoo.org/)
3. Database - MySQL
4. ORM - [Peewee](https://github.com/coleifer/peewee)

###Installing Flask
```bash
    pip install Flask
```

###Before installing peewee
```bash
  sudo apt-get install build-essential python-dev libmysqlclient-dev
  sudo apt-get install python-mysqldb
```

###Install PeeWee
```
 pip install peewee
```

#####Configuring Your DB with Application
look for <b>configDB.py</b>
```py
    db_name = "replace with your mysql database name"
    db_host = "replace with your respective host"
    db_port = 3306 #chnage if required
    db_user = "root (you can change)"
    db_passwd = ""
```







# How to contribute?
Fork the repo --> Make changes <--> Test if working properly --> Commit changes --> Send pull request.
