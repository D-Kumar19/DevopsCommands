FROM python:3.13-rc-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PAGE_COLOR=lightblue

EXPOSE 5000

CMD ["python", "webpage.py"]
