# backend_api

make readme

record what pip requirements were used


## MySQL setup

```
# start mysql server
sudo /usr/local/mysql/support-files/mysql.server start

# create database
create database backend;
show databases;

# create user
CREATE USER 'backend'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'backend'@'localhost' WITH GRANT OPTION;
```