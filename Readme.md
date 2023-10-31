# How to run?
### Pre-requisites that are needed to set up
> 1. Install latest version of python
> 2. Install postgresql and pgAdmin
> 3. Create database using pgAdmin and remember the database credentials( like database user, database password, database name)
> 4. Clone the repository and open the project in any suitable IDE (preferred in pycharm)
> 5. install requirements.txt using command:<br> <I>pip install requirements.txt</I>
> 6. create ".env" file in the directory where main.py file is located having following attributes: > <br>a. DATABASE_HOST = localhost <br>b. DATABASE_USER = postgres (or the user that you setup while creating database)<br> c. DATABASE_PASSWORD = (Password that you set for your database while setting up pgAdmin) <br> d. DATABASE_NAME = (Database name which you created using pgAdmin)<br>

### To start and use the application
> 1. Run the following command to start up the application:<br><b><i>python main.py</i></b>
> 2. You can see the APIs at the following postman link<br>https://www.postman.com/red-space-314271/workspace/assessment/collection/23667429-e82b94c7-55ff-4100-a9d0-d1db2ecf8d2f?action=share&creator=23667429