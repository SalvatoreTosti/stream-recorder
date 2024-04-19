FROM python:slim-buster

WORKDIR /home/app
RUN mkdir -p /home/app/out

RUN useradd app_user

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY main.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R app_user:app_user ./
USER app_user
ENV PYTHONUNBUFFERED 1
CMD ["./boot.sh"]

