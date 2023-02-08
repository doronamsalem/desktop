from flask import Flask, render_template, request
import requests

from week_days import Week


def get_url(location):
    """makes the url for api requests"""
    my_key = "V7CK4U8J5FYGWDCU7UBCAE4SU"
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    days = f"/next7days?unitGroup=metric&include=datetime%2Cname%2Caddress%2Ctempmax%2Ctempmin%2Ctemp%2Chumidity%2Cicon&include=days&key={my_key}&contentType=json"
    return f"{base_url}{location}{days}"


app = Flask(__name__)


@app.route('/')
def index():
    """open the home page"""
    html_page = "home_page.html"
    return render_template(html_page, success="True")


@app.route('/weather', methods=["GET"])
def weather():
    """open page with data from api request"""
    html_page = "forecast.html"
    location = request.args.get('location')     # post request from home_page.html
    url_api = get_url(location)
    try:
        response = requests.get(url_api).json()
        this_week = Week(response)

    except (Exception):
        return render_template("home_page.html", success="False")

    else:
        return render_template(html_page, place=response['resolvedAddress'], week=this_week)


if __name__ == "__main__":
    app.run(port=5050)
