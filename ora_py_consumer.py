#### https://datatofish.com/how-to-connect-python-to-an-oracle-database-using-cx_oracle/
#### https://www.oracletutorial.com/python-oracle/inserting-data/
#### https://medium.com/towards-artificial-intelligence/kafka-python-data-processing-25584415f7ab

import cx_Oracle
import random

def insert_to_ora(cust_id, amount, cust_name, note):

    conn = cx_Oracle.connect('system/oracle@127.0.0.1:1521/XEPDB1')

    ## sqlplus system/oracle@127.0.0.1:1521/XEPDB1
    ## 127.0.0.1:5500/em

    c = conn.cursor()

    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into bcp_from_ml (cust_id , amount, cust_name, note) values(:cust_id,:amount,:cust_name,:note)')

    # execute sql statement with bind variables
    c.execute(sql, [cust_id , amount, cust_name, note])

    # commit after insert statement
    conn.commit()

    # use triple quotes if you want to spread your query across multiple lines
    sql = ('select * from bcp_from_ml ')
    c.execute(sql) 
    for row in c:
        print (row[0], '-', row[1],'-', row[2],'-',row[3])

    conn.close()

## End of insert_to_ora

if __name__ == '__main__':
    insert_to_ora(random.randrange(1,100), random.randrange(100,1200), 'Dima' , 'None')


