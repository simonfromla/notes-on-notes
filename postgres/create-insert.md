# psql-create  


### CREATE TABLE  
```sql
CREATE TABLE my_users (
 username VARCHAR (20) column_constraint,
 table_constraint table_constraint
) INHERITS existing_table_name;
```


### INSERT INTO  
```sql
INSERT INTO my_users VALUES ('snape', 'snaper@gmail.com');
INSERT INTO my_users (username, email) VALUES ('rmis', 'hello@gmail.com');
INSERT INTO my_users (email, username) VALUES ('yoyo@yahoo.com', 'bboy12');
```





##### Further Reading
[PSQL datatypes](https://www.postgresql.org/docs/current/static/datatype.html)