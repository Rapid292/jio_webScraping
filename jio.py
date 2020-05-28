from bs4 import BeautifulSoup
import requests
import csv


# Get Csrf hidden token value
s = requests.get(
    "https://idm.jioconnect.com/jiosso/SSOLogin.jsp?bmctx=3EFEAF9AEA94839518B74FDD125F6C8596DF233B9A74ADF72F1976EDF644EA6D&contextType=external&username=string&password=secure_string&challenge_url=https%3A%2F%2Fidm.jioconnect.com%3A443%2Fjiosso%2FSSOLogin.jsp&request_id=-38536904530323905&authn_try_count=0&locale=en_IN&resource_url=%252Fuser%252Floginsso"
).text

soup = BeautifulSoup(s, "lxml")

for e in soup.find_all("input", {"name": "resource_url"}):
    csrf = e["value"]
# , "resource_url": csrf

# Start a session
session = requests.Session()

# Create the payload
payload = {"request_id": "your_id", "password": "your_password"}

# Post the payload to the site to log in
source = requests.post(
    "https://login.jioconnect.com/oam/server/auth_cred_submit", data=payload
)

new_s = session.get("https://partnercentral.jioconnect.com/group/guest/home").text
soup = BeautifulSoup(new_s, "lxml")
print(soup.prettify())


# Navigate to the next page and scrape the data
source = session.get(
    "https://fiori.jioconnect.com/sap/bc/ui5_ui5/sap/zehys_dashboard/index.html#"
)


soup = BeautifulSoup(source, "lxml")
text = soup.find("div", class_="_4bl9 _42n-").textarea

print(text)
