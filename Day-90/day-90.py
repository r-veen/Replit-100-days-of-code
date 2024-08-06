import requests, json

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()

  for person in user['results']:
    name = f"""{person["name"]["first"].lower()} {person["name"]["last"].lower()}.jpg"""
    picture = requests.get(person["picture"]["medium"])
    f = open(f"{name}.jpg", "wb")
    f.write(picture.content)
    f.close()
    print(f"Saved {name}")
