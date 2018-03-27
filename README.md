# argumentum
## How to run a development server
git clone -b development https://github.com/pjwalen/argumentum.git
cd argumentum
python application.py
Open a browser to: http://127.0.0.1:5000/

A pre-populated in-memory database will be set up for the development environment every time the development environment is started. 

If need or want a real (persistent) database for you'll need to install PostgreSQL and set the following environment variables before running application.py

RDS_USERNAME=<database username>
RDS_PASSWORD=<database username>
RDS_HOSTNAME=127.0.0.1
RDS_PORT=5432
RDS_DB_NAME=<database name>

## Running this in a free-tier AWS account.

This application will fit nicely in a free-tier AWS account using elastic beanstalk backed by an postgresql RDS database.

All you need to do to package up an instance to upload is create a zip file containing the following:

requirement.txt
application.py
argumentum/*

Next, edit the environment configuration to re-point the /static to /argumentum/static 

Finally, set the appropriate RDS_* environment variables for your postrgresql instance.