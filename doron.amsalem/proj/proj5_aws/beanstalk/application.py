from flask import Flask, render_template, request
import requests
from modules import boto3_modules, url_creator
from week_days import Week

application = Flask(__name__)
home_page = "home_page.html"
forcast_page = "forecast.html"


@application.route('/')
def index():
    """open the home page"""
    return render_template(home_page, success="True")


@application.route('/weather', methods=["GET"])
def weather():
    """open page with data from api request"""
    global response, this_week
    response = this_week = None
    location = request.args.get('location')
    url_api = url_creator.get_url(location)
    try:
        response = requests.get(url_api).json()
        this_week = Week(response)
    except (Exception):
        return render_template(home_page, success="False")
    else:
        return render_template(forcast_page, place=response['resolvedAddress'], week=this_week)


@application.route("/store-data", methods=["GET"])
def store_dynamoDB():
    """tore currently viewed data to dynamo DB"""
    table_name = request.args.get('table name')
    try:
        boto3_modules.store_data(response, table_name)
    except (Exception):
        return render_template(forcast_page, place=response['resolvedAddress'], week=this_week, DB_store="failed")
    else:
        return render_template(forcast_page, place=response['resolvedAddress'], week=this_week, DB_store="succeed")


if __name__ == "__main__":
    application.run(port=5051)
