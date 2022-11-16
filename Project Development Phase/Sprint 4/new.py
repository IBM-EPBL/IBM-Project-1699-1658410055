import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "9G6L7fYYvmvpB0mI2kqJFm5LyfDvSdIakixARdY-LpZ7"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring = {"input_data": [{"field": [['white blood cell count', 'blood urea', 'blood glucose random','serum creatinine', 'packed cell volume', 'albumin', 'haemoglobin','age', 'sugar', 'ypertension']],
  "values": [[7800.0,36.0,121.0,1.2,44.0,1.0,15.4,48.0,0.0,1]]}]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/b2d8555c-0595-43d8-abda-40bf8a6796d5/predictions?version=2022-11-09', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
print(predictions)