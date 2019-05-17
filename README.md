
# Ocean Luxury Hotel Software
 A python application running TKinter that is meant to serve a hotel and their services.

## Requirements

 - Python 3

 - [Bcrypt](https://pypi.org/project/bcrypt/)
`pip install bcrypt`
 - [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
 `pip install mysql-connector-python`

## Running the Program
Just run main.py and the program should start up (Asumming python installed is python3)
`python main.py`

## Test Accounts
Below are acccount used to test both versions of the UI.



 User Type | Username | Password  |
-----------|----------|-----------|
  Front Desk | admin | admin |
 Guest | abcd | 1234 |


## Technical Problems
- .encode /.decode is varying on machine. Change that line in verify_login() in DatabaseFunctions.py if you run into that problem
