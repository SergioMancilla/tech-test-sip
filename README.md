# Steps for the project setup

- Create a virtual env in the root of the project with a Python version upper to 3.7, using the command `python -m venv sip_students_env`. This is for simplify the development experience with Python dependencies
- Run `sip_students_env\scripts\activate` to activate the virtual env
- Execute `pip install -r requirements.txt`
- Run `npm run dev` to install node dependencies
- Create database and set the name in `appconfig.ini` file, or create database `schol`
- Run all the migrations with `alembic upgrade head`

Once development has finished, all this proccess should be automated in a Docker file
