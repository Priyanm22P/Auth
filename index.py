import requests
import json

url = "https://dev.ndhm.gov.in/gateway/v0.5/sessions"

payload = json.dumps({
  "clientId": "SBX_000618",
  "clientSecret": "9550dda7-ffae-49c2-ba8b-b4aa07868a8a"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'TS01960242=01445fed042e8a23d4204b2ccc98a83618c32412203ca03ba7d852a6f41c8a879c76cff39999e1a0baff63e3fbe6e3cb3c99db6274'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
