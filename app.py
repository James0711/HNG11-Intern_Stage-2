import os
import requests
import weatherloc
from markupsafe import Markup
from flask import Flask, jsonify, request, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']


def get_json_result(req, visitor_ip):
    """
    Function that generates and returns the required json response
    """
     
    visitor_name = req.args.get('visitor_name').replace('"', '').replace("'", '')

    # get gealocation info for IP address
    loc_info = requests.get(f'https://ipapi.co/{visitor_ip}/json/', timeout=1200).json()

    # init weather api client
    wea_client = weatherloc.Client(os.environ['WEATHER_API_KEY'])

    # get city
    visitor_city = loc_info.get('city')

    # get city weather details using weather api client
    city_weather = wea_client.current(visitor_city)
    city_temp = city_weather.feelslike_c

    # reatun json
    return jsonify(
        {
        "client_ip": f"{visitor_ip}", # The IP address of the request
        "location": f"{visitor_city}", # The city bearing the request
        "greeting": f"Hello, {visitor_name}!, the temperature "
                    f"is {city_temp} degrees Celcius in {visitor_city}",
        }
    )

# Creating a home page 
@app.route("/")
def home():
    """Just to have something on the home page"""
    return Markup(
        "<h1>Hello, Welcome!</h1> <br>"
        "<h3>This is HNG11 Stage One Task done by Eche James.</h3> <br>"
        f"<h3>Visit <u><em>{request.base_url}api/hello?visitor_name='YOUR NAME'</em></u> for take-away greeting</h3>"
    )


@app.route("/api/hello", methods=['GET'])
def hello_visitor():
    """
    This is the end point that bears the response to the task
    """
    # Get Visitor's IP Address
    if os.environ.get('APP_IN_PRODUCTION'):
        visitor_ip = str(request.environ.get(
            'HTTP_X_FORWARDED_FOR')) or str(request.environ.get('REMOTE_ADDR'))
    else:
        visitor_ip = request.remote_addr

    return get_json_result(request, visitor_ip)


@app.route("/api/hello2", methods=['GET'])
def hello_visitor2():
    """
    This is to specifically test usage of `ProxyFix` configuration
    to achieve dynamic IP detection when using `request.remote_addr` 
    in production; which means `Flask` is behind a proxy server
    """
    # Get Visitor's IP Address
    if os.environ.get('APP_IN_PRODUCTION'):
        from werkzeug.middleware.proxy_fix import ProxyFix  # noqa

        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )

    return get_json_result(request, request.remote_addr)


@app.route("/api/test-production/", methods=['GET'])
def test_production():
    """
    Testing the production locally
    """
   
    vercel_prod_url = "https://hng-11-intern-stage-2-eche-ngbede-james-projects.vercel.app//api/hello?visitor_name='Eche James'"

    try:
        rep = requests.get(vercel_prod_url, timeout=1200)
        return jsonify(rep.json())
    except ValueError:
        print("App seems not to be active on Vercel")
    
    print("App seems not to be active on both CleverCloud and Vercel")
    return redirect(url_for('home'))


if __name__ == "__main__":
    if os.environ.get('APP_IN_PRODUCTION'):
        app.run(debug=False)
    else:
        app.run(debug=True)