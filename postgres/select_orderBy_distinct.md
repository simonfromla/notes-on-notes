# psql-select


One of the most common tasks is to query the DB by using the SELECT statement. 
It can also become complex due to its ability to combine a number of clauses to perform a query.  
The clauses that appear with the SELECT statement are:  

* Select distinct rows by using the __DISTINCT__ operator  
* Filter rows by using the __WHERE__ clause  
* Select rows by using the __ORDER BY__ clause  
* Select rows based on various operators such as __BETWEEN__, __IN__ and __LIKE__  
* Group rows into groups using the __GROUP BY__ clause  
* __HAVING__ to apply conditions to the groups  
* Join tables together using __INNER JOIN__, __LEFT JOIN__, __FULL OUTER JOIN__, and __CROSS JOIN__  

### Using the SELECT statement  

First, specify the columns comma-separated, then select the table from which to query.  
```sql
SELECT  
 username,
 email,
 profile_picture
FROM
 User_Profile;
```
*note:* 
- (\*) will query all columns (usage not advised).  
- Semi-colon specifies the end of the SELECT statement.  
- SQL is case-insensitive.  
Retrieving unnecessary data from a table increases traffic from a DB server to the application.  
It is therefore good practice to specify the names of only the columns you need, when querying the DB. 


### Using the ORDER BY clause  
*Sort the result set returned from the SELECT statement using ORDER BY*  

```sql
SELECT  
 username,
 first_name,
 last_name
FROM
 User_Profile;
ORDER_BY
 last_name DESC,
 first_name;
```  

* Ommision of either DESC or ASC will result in a ordering by ASC by default.  
* Although PSQL allows you to sort rows based on columns not specfied in the SELECT statement, SQL standard does not. It is good practice to follow SQL standard to make the code more portable.  
  
 
 
### Using the DISTINCT clause  
*Remove duplicate rows from a result set returned by a query*  
Keep one row for each group of duplicates. Can be used on one or more columns of a table.  

```sql
SELECT
 DISTINCT username,
 profile_picture
FROM
 User_Profile
```
If you specify multiple columns, duplicates will be evaluated based on the combination of these column values.
  
  
__DISTINCT ON (expression)__ to keep the "first" row of the group of duplicates.  
Good practice to use DISTINCT ON together with ORDER BY, since the order of rows returned from SELECT is unpredictable.  
```sql
SELECT
 DISTINCT ON
 (last_name),
 first_name
FROM
 User_Profile
ORDER BY
 last_name,
 first_name;
```

