import json
import requests
import os

my_data = {
 "survey_id": "002",
 "user_id": "12098789",
 "report_date": "2020-03-27 12:00:00",
 "report_source": "report_diagnosis",
 "gender": "Female",
 "age": "54",
 "calendar": {"onset" : "03/16/2020", "tested" : "04/24/2020"},
 "postcode": "07093",
 "country": "United States of America",
 "country_code" : "USA",
 "diagnosis": {"tested" : "no" },
 "symptoms": {"fever": "False", "cough": "True", "runny_nose": "false"}
}

local = False

if local:
    base_url = "http://0.0.0.0:5000/"
else:
    base_url = "http://54.165.239.34:5000"


endpoint = "fit_data/"
my_url = os.path.join(base_url, endpoint)


r = requests.get(my_url, data={"data":json.dumps(my_data)})
print(r.text)
