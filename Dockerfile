FROM python:3.12.2

RUN wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip && \
    unzip web2py_src.zip -d /opt && \
    rm web2py_src.zip

RUN apt-get update && \
    apt-get install -y npm && \
    npm install -g n && \
    n stable

RUN apt-get install tree

COPY . /opt/web2py/applications/sip_students
RUN cd opt/web2py/applications/sip_students

WORKDIR /opt/web2py/applications/sip_students

RUN python -m venv sip_students_env
ENV VIRTUAL_ENV=sip_students_env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . sip_students_env/Scripts/activate

# Install requirements
RUN pip install -r requirements.txt
RUN npm install

RUN apt-get install -y postgresql-client
# RUN service postgresql start
# RUN psql -U postgres -c 'CREATE DATABASE school'
RUN psql -h postgres -U postgres

# RUN alembic upgrade head

# Expón el puerto 8000
EXPOSE 8000

# Ejecuta Web2py
CMD python /opt/web2py/web2py.py -i 0.0.0.0 -p 8000 -a '123456'