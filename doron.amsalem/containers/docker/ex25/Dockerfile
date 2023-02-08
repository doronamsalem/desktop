FROM python
WORKDIR /weather_web_proj
COPY requirements.txt /weather_web_proj
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD gunicorn --bind 0.0.0.0:5000 webpage:app

