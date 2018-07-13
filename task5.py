from github import Github
import json
import requests
def listrequests(mydict):
    print(("{: <5}"+"{:35}" * 4).format("ID", "User Name", "Title", "Request Opened", "State\n"))
    for item in mydict:
        print(("{: <5}"+"{:35}" * 4).format(item["number"], item["head"]["user"]["login"], item["title"], item["created_at"], item["state"]))
def getinfo():
    q = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls?page=1&per_page=100",
                     auth=("DaryaZhukova", password))
    return (q.json())
def writeinfo(mydict):
    with open("requests.txt", "w") as file:
        file.write(json.dumps(mydict))
def userrequests(mydict, user):
    print(("{: <5}" + "{:35}" * 4).format("ID", "User Name", "Title", "Request Opened", "State\n"))
    for item in mydict:
        if item["head"]["user"]["login"] == user:
            print(("{: <5}"+"{:35}" * 4).format(item["number"], item["head"]["user"]["login"], item["title"], item["created_at"], item["state"]))


#auth = requests.get("https://api.github.com", auth=("DaryaZhukova", "Admin123"))
#token = auth.headers["ETAg"].split("\"")[1]
#print(token)
#q = requests.get("https://api.github.com/user/repos", headers={"Authorization": "5b491d78c5e20454548a852ac46fbd38"})
#password = input("Enter password\n")
password = "Admin123"
#q = requests.get("https://api.github.com/users/alenaPy/repos", auth=("DaryaZhukova", password))
#print(q.json()['title'])
q = getinfo()
#listrequests(q)
userrequests(q, "DaryaZhukova")