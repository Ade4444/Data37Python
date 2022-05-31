import requests
from pprint import pprint
import json

headers = {'Content-Type': 'application/json'}
body = {'postcodes': ["PR3 0SG", "M45 6GN", "EX16 5BL"]}


pc_req = requests.post(
    url="https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
)
print(pc_req)
pcs = pc_req.json()["result"]
pprint(pcs, sort_dicts=False)

for pc_data in pcs:
   result = pc_data["result"]
   print(result["postcode"])
   print(result["admin_ward"])
   print(result["eastings"], result["northings"])
   print(result["codes"]["nuts"])



   #print(type(pc_data))




# print()

# print(pc_req.status_code)


#if pc_req.status_code == 200:
    # print(pc_req.headers)
    # print(pc_req.headers, type(pc_req.headers))

    # pprint(dict(pc_req.headers))
    # print(type(pc_req.content))
    # pprint(pc_req.content)
    # postcode = json.loads(pc_req.content)
    # print(postcode)
    # print(postcode["result"]["postcode"])
    # print(postcode["result"]["nuts"])
    # print(postcode["result"]["admin_district"])
    # print(postcode["result"]["eastings"])
    # print(postcode["result"]["northings"])

    # print(postcode["results"]["nuts"])

    # postcode = pc_req.json()
    # print(type(postcode))



