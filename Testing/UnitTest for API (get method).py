import requests

resp = requests.get("https://api.covid19api.com/summary")

print("\n---------------------------------------------Testing the API---------------------------------------------\n")
json_response = resp.json()
print("API request ID :", json_response['ID'],"\n")
assert json_response['ID'] == '02f7e4ff-73b4-450c-bfed-e66719777fbd', "API ID Incorrect"

print("API requested date :", json_response['Date'],"\n")
assert (json_response['Date']).endswith(".148Z"), "Date format is incorrect"

print("Global data :", json_response['Global'],"\n")
assert json_response['Global'] == {'NewConfirmed': 88257, 'TotalConfirmed': 669442869, 'NewDeaths': 520, 'TotalDeaths': 6756231, 'NewRecovered': 0, 'TotalRecovered': 0, 'Date': '2023-02-07T05:02:08.148Z'}, "Global covid data is incorrect"

print("Data of the First country :", json_response['Countries'][0],"\n")
assert json_response['Countries'][0] == {'ID': '98d4f0e3-6331-4fff-86a5-7d27e3f13b13', 'Country': 'Afghanistan', 'CountryCode': 'AF', 'Slug': 'afghanistan', 'NewConfirmed': 6, 'TotalConfirmed': 208627, 'NewDeaths': 2, 'TotalDeaths': 7896, 'NewRecovered': 0, 'TotalRecovered': 0, 'Date': '2023-02-07T05:02:08.148Z', 'Premium': {}}, "The data of this country is incorrect"

print("Displaying only the name of the second country :", json_response['Countries'][1]['Country'])
assert json_response['Countries'][1]['Country'] == 'Albania', "Incorrect Country name"

print("Displaying some of the data of INDIA :","\n"" ->Total Confirmed :", json_response['Countries'][77]['TotalConfirmed'],"\n"" ->Total Deaths :", json_response['Countries'][77]['TotalDeaths'])
assert json_response['Countries'][77]['TotalConfirmed']  == 44684679, "Total confirmed cases is updated, this is old value"
assert json_response['Countries'][77]['TotalDeaths'] == 530745, "Total deaths is updated, this is old value"