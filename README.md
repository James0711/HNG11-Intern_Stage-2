# HNG11-Intern_Stage-2
Stage One Task for backend programming in HNG11 Internship, deployed [Here]()

It's a basic web app that exposes an API endpoint which retuns JSON object conforming to below criteria:

Endpoint:
```
[GET] <example.com>/api/hello?visitor_name="{REQUESTER_NAME}" (where <example.com> is server origin)
```

Response:
```
{
  "client_ip": "{THE.REQUESTER.IP.ADDRESS}",
  "location": "{REQUESTER_CITY}",
  "greeting": "Hello, {REQUESTER_NAME}!, the temperature is {CITY_TEMPERATURE} degrees Celcius in {REQUESTER_CITY}"
}
```