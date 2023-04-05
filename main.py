import requests

MY_LATITUDE = 19.456360
MY_LONGITUDE = 72.792458
weather_api_key = "d1da006847b3a2770b6be6bf1a65288a"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": weather_api_key,
    "exclude": "current,minutely,daily,alert"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(12):
    print(i, data["hourly"][i]["weather"][0]["id"])
    if data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True

# Rain - 500
# Clear - 800
# clouds - >800

#
# if will_rain is True:
#     import smtplib
#
#     password = "bcbgslxltbgltbid"
#     my_email = "thakurved127@gmail.com"
#     subject = "bring an umbrella"
#     body = "it will rain today"
#
#     connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="thakurved156@gmail.com", msg=f"Subject:{subject}\n\n"
#                                                                                    f"{body}")
#     connection.close()


