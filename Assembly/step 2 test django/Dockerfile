from python:3.8.6 # по сути тоже самое что image: postgres:13.1 (по сути)

RUN apt-get update \ # выполнить команду
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./REST/ ./ # скопировать (первый путь это файл на основном компьютере, а второй это файл в контейнере)
RUN pip3 install -r requirements.txt

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh
