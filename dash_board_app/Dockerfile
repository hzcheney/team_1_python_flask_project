# syntax=docker/dockerfile:1
FROM tiangolo/uwsgi-nginx:python3.8


WORKDIR /app

# Copy to our working directory
COPY requirements.txt requirements.txt

ENV FLASK_APP=main.py
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
