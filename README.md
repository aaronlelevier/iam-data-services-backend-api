# backend_api

This is the backend API for the iam-data-services POC

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

## Roadmap

Read data in Policy and map fields to columns, create Policy DB Table