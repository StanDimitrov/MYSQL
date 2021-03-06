

CODE: Creating Databases
Creating Databases Code
Start the CLI:

mysql-ctl cli;

List available databases:

show databases;

The general command for creating a database:

CREATE DATABASE database_name;

A specific example:

CREATE DATABASE soap_store;

#####################################
CODE: Dropping Databases
To drop a database:

DROP DATABASE database_name;

For Example:

DROP DATABASE hello_world_db;

Remember to be careful with this command! Once you drop a database, it's gone!

#########################################################


CODE: Using Databases
USE <database name>;

-- example:
USE dog_walking_app;

SELECT database();

################################################################