FROM python
RUN pip install gunicorn && pip install flask && pip install pandas && pip install requests

COPY python_proj /

CMD gunicorn --bind 0.0.0.0:5000 webpage:app
