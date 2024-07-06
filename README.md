# Weather API using Flask

This is a basic Python API that retrieves weather information based on the requester's location.

### Framework:
- Flask

### Python Version:
- 3.10.11

### Public APIs Used:
- [OpenWeatherMap](https://openweathermap.org): Provides weather status based on location.
- [IPinfo.io](https://ipinfo.io): Provides geolocation information based on IP address.

### Public URL:
- [API Endpoint]()

### Example Response:
```json
{
  "client_ip": "127.0.0.1", // The IP address of the requester
  "location": "New York", // The city of the requester
  "greeting": "Hello, Michael!, the temperature is 11 degrees Celcius in New York"
}


Description:

This API will serve fetch requests with the help of Flask and we will receive weather data at OpenWeatherMap, based on the city which is derived from given IP address by usign IPinfo. io. It then sends back a JSON object with their IP, city location and an introduced statement followd by the temp in that part of ith world

You can use this API for getting weather detail according to your location.