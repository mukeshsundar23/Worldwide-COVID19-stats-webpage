import requests

resp = requests.get("https://api.covid19api.com/summary")

print("---------------------------------------------Viewing the details of API---------------------------------------------\n")

print("Displaying the response of the API in text format :",resp.text)

print("Displaying the content of the response of the API :",resp.content,"\n")

print("Displaying the response of the API in json format :",resp.json(),"\n")

print("Displaying the type of the response type of the API:",type(resp.headers),"\n")

print("Displaying the headers of the response of the API :",resp.headers,"\n")

print("Displaying the cookies of the response of the API :",resp.cookies,"\n")

print("Displaying the encoding of the response of the API :",resp.encoding,"\n")

print("Displaying the URL of the API :",resp.url,"\n")
