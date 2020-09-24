/* 
 bcp_from_ml (cust_id , amount, cust_name, note)
*/
CREATE TABLE bcp_from_ml (
    cust_id         NUMBER NOT NULL,
    amount          NUMBER NOT NULL,
    cust_name VARCHAR2(50) NOT NULL,
    note      VARCHAR2(50) NOT NULL
);