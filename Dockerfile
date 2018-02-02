FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
ADD /config/requirements.pip /config/
RUN pip install -r /config/requirements.pip

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/8ed92e8cab83cfed76ff012ed4a36cef74b28096/wait-for-it.sh ./wait-for-it.sh
RUN chmod a+x ./wait-for-it.sh

ADD /src /src

RUN mkdir /static
RUN python /src/manage.py collectstatic --noinput
VOLUME /static
