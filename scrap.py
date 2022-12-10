# Web Scrapping Code


import requests

shots_url = 'https://www.acko.com/motororchestrator/api/v2/proposals/Mjk1Q7L6d1TqbnxWbfEU9w/plans?include_addons_price=false&utm_campaign=1st_Party_Generic_Search_Hyderabad_Neev&utm_term=online+car+insurance&utm_content=614095725333&utm_medium=cpc&utm_source=google&gclid=CjwKCAiA-dCcBhBQEiwAeWidtWCAkcyvqTH_ZXR_xV_IxcwKpb_z9YggxvLtdGQQpYbsBUV5a4u6qRoCfd0QAvD_BwE&utm_adgroup=Insurance&utm_network=g&utm_matchtype=p&utm_device=c&utm_location=9062140'

# request the URL and parse the JSON
response = requests.get(shots_url)
response.raise_for_status() # raise exception if invalid response
shots = response.json()['plans']

# print data
print(shots)
