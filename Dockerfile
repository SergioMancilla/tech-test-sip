FROM python:3.12.2

RUN wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip && \
    unzip web2py_src.zip && \
    rm web2py_src.zip

RUN apt-get update && \
    apt-get install -y npm && \
    npm install -g n && \
    n stable

COPY . /web2py/applications/sip_students
RUN cd /web2py/applications/sip_students

WORKDIR /web2py/applications/sip_students

RUN python -m venv sip_students_env
ENV VIRTUAL_ENV=sip_students_env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . sip_students_env/Scripts/activate

# Install requirements
RUN pip install -r requirements.txt
RUN npm install

# RUN apt-get install -y postgresql-client
# RUN service postgresql start
# RUN psql -U postgres -c 'CREATE DATABASE school'

# RUN alembic upgrade head

# Expón el puerto 8000
EXPOSE 8000

WORKDIR /
# Ejecuta Web2py
CMD python /web2py/web2py.py -i 0.0.0.0 -p 8000 -a '123456'