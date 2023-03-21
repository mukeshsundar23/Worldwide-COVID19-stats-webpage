import requests

resp = requests.get("https://api.covid19api.com/summary")

print("\n---------------------------------------------Testing the API---------------------------------------------\n")
json_response = resp.json()
print("API request ID :", json_response['ID'],"\n")
assert json_response['ID'] == '8e22bf71-4633-42fe-96b7-03a2abf6b85c', "API ID Incorrect"

print("API requested date :", json_response['Date'],"\n")
assert (json_response['Date']).endswith(".248Z"), "Date format is incorrect"

print("Global data :", json_response['Global'],"\n")
assert json_response['Global'] == {'NewConfirmed': 177325, 'TotalConfirmed': 674300771, 'NewDeaths': 1319, 'TotalDeaths': 6793224, 'NewRecovered': 0, 'TotalRecovered': 0, 'Date': '2023-03-21T07:26:20.248Z'}, "Global covid data is incorrect"

print("Data of the First country :", json_response['Countries'][0],"\n")
assert json_response['Countries'][0] == {'ID': 'f245408d-9e2b-4bf6-9ab6-46fa8c18d509', 'Country': 'Afghanistan', 'CountryCode': 'AF', 'Slug': 'afghanistan', 'NewConfirmed': 0, 'TotalConfirmed': 209451, 'NewDeaths': 0, 'TotalDeaths': 7896, 'NewRecovered': 0, 'TotalRecovered': 0, 'Date': '2023-03-21T07:26:20.248Z', 'Premium': {}}, "The data of this country is incorrect"

print("Displaying only the name of the second country :", json_response['Countries'][1]['Country'])
assert json_response['Countries'][1]['Country'] == 'Albania', "Incorrect Country name"

print("Displaying some of the data of INDIA :","\n"" ->Total Confirmed :", json_response['Countries'][77]['TotalConfirmed'],"\n"" ->Total Deaths :", json_response['Countries'][77]['TotalDeaths'])
assert json_response['Countries'][77]['TotalConfirmed']  == 44690738, "Total confirmed cases is updated, this is old value"
assert json_response['Countries'][77]['TotalDeaths'] == 530779, "Total deaths is updated, this is old value"
