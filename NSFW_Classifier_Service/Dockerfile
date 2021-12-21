FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip
WORKDIR /classifier/

COPY requirements.txt /classifier/
RUN pip install -r requirements.txt

COPY . /classifier/
EXPOSE 8000
CMD ["python", "api/__main__.py"]
