# sbi-tkinter
SBI site has been used as GUI for creating a basic tkinter GUI(Graphic User Interface). SQL server has been used to store the data

You may download the files in C Drive in SBI folder or make changes in the images open command sources accordingly.

The GUI also has SQL server connected for storing data.

You'll have to create a database with following tables:

Database name:
sbi_proj

Tables:

1. account_balance:
+------------+---------+------+-----+---------+----------------+
| Field      | Type    | Null | Key | Default | Extra          |
+------------+---------+------+-----+---------+----------------+
| trans_num  | int(11) | NO   | PRI | NULL    | auto_increment |
| cust_id    | int(11) | NO   |     | NULL    |                |
| deposit    | float   | YES  |     | NULL    |                |
| withdrawal | float   | YES  |     | NULL    |                |
| balance    | float   | YES  |     | NULL    |                |
+------------+---------+------+-----+---------+----------------+

2. account_deposits:

+------------------+-------------+------+-----+---------+----------------+
| Field            | Type        | Null | Key | Default | Extra          |
+------------------+-------------+------+-----+---------+----------------+
| deposit_id       | int(11)     | NO   | PRI | NULL    | auto_increment |
| cust_id          | int(11)     | NO   |     | NULL    |                |
| deposit_type     | varchar(45) | YES  |     | NULL    |                |
| deposit_amount   | float       | NO   |     | NULL    |                |
| deposit_interest | float       | NO   |     | NULL    |                |
| deposit_duration | float       | NO   |     | NULL    |                |
| final_amount     | float       | NO   |     | NULL    |                |
+------------------+-------------+------+-----+---------+----------------+

3. loans_hist:

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| cust_id       | int(11)      | NO   |     | NULL    |                |
| loan_number   | int(11)      | NO   | PRI | NULL    | auto_increment |
| loan_type     | varchar(100) | YES  |     | NULL    |                |
| loan_amount   | float        | NO   |     | NULL    |                |
| loan_period   | float        | YES  |     | NULL    |                |
| loan_interest | float        | NO   |     | NULL    |                |
| emi           | float        | YES  |     | NULL    |                |
| final_amount  | float        | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

4. login_credentials:

+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| cust_id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| u_name        | varchar(45)  | NO   |     | NULL    |                |
| password      | varchar(45)  | NO   |     | NULL    |                |
| email_address | varchar(100) | YES  |     | NULL    |                |
| sec_ques1     | varchar(200) | NO   |     | NULL    |                |
| sec_ans1      | varchar(100) | NO   |     | NULL    |                |
| sec_ques2     | varchar(200) | NO   |     | NULL    |                |
| sec_ans2      | varchar(100) | NO   |     | NULL    |                |
| sec_ques3     | varchar(200) | NO   |     | NULL    |                |
| sec_ans3      | varchar(100) | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

5. profile_details:

+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| cust_id        | int(11)     | NO   |     | NULL    |       |
| first_name     | varchar(45) | NO   |     | NULL    |       |
| middle_name    | varchar(45) | YES  |     | NULL    |       |
| last_name      | varchar(45) | NO   |     | NULL    |       |
| account_number | varchar(45) | YES  |     | NULL    |       |
| ifsc_code      | varchar(45) | YES  |     | NULL    |       |
| email          | varchar(45) | NO   |     | NULL    |       |
| contact        | int(11)     | NO   |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
