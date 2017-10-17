# psql

### SELECT  

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

##### Using the SELECT statement  

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


