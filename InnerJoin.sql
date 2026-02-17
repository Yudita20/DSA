CREATE TABLE Customer(
Cust_ID INT PRIMARY KEY,
Cust_name VARCHAR(50),
Contact_Name VARCHAR(50),
Country VARCHAR(40)
);

INSERT INTO Customer
VALUES
(1,"Anna Frank","ANNIE","GREMANY"),
(2,"ANNA TRU","TRU","MEXICO"),
(3,"ANTONIA MORENA","MORI","MEXICO");

CREATE TABLE Orders(
Order_ID INT PRIMARY KEY,
Cust_ID INT,
Order_date date);

INSERT INTO Orders
VALUES
(10308 , 2 , '1996-09-18'),
(10309,	37,	'1996-09-19'),
(10310,77,'1996-09-20');

SELECT * FROM Customer;
SELECT * FROM Orders;

-- INNER JOIN or JOIN
SELECT Customer.Cust_ID,Customer.Cust_name,Orders.Order_date
FROM Orders
INNER JOIN Customer ON Orders.Cust_ID = Customer.Cust_ID;

