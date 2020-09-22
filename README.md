### 1) pull Oracle XE image

docker pull oracleinanutshell/oracle-xe-11g

### 2) run image as docker container

docker run -d -p 1521:1521 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g 

### 3) Check container id was running

docker ps

### 4) run bash in container to operate with Oracle XE instance 

docker exec -it 1a9f39ca5c93  bash

### 5) create table in sqlplus

sqlplus system/oracle@localhost:1521/XE   


SQL> drop table emp;

Table dropped.

SQL> create table emp as select 1 col1, 'Bogdan' col2, 'Dmytrovych' col3, 'Koval' col4 from dual;

Table created.

SQL> select * from emp;

      COL1 COL2   COL3       COL4
---------- ------ ---------- -----
         1 Bogdan Dmytrovych Koval

SQL> desc emp
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 COL1                                               NUMBER
 COL2                                               CHAR(6)
 COL3                                               CHAR(10)
 COL4                                               CHAR(5)
 
### 6) Download oracle thin client driver ojdbc8.jar into work dir

https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html


### 7) Compile java code to class

 !!! Urgent !!! on Linux   -cp list separated by :
                on Windows -cp list separated by ;


javac -cp "c:\Dima\work\ojdbc8.jar;c:\Dima\work"  OracleCon.java

### 8) Run java code

java -cp "c:\Dima\work\ojdbc8.jar;c:\Dima\work" OracleCon


