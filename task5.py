import argparse
import json
import requests


def listrequests(mydict):
    print(("{: <5}" + "{:35}" * 4).format("ID", "User Name", "Title",
                                          "Request Opened", "State\n"))
    for item in mydict:
        print(("{: <5}" + "{:35}" * 4).format(item["number"],
                                              item["head"]["user"][
                                                  "login"], item["title"],
                                              item["created_at"],
                                              item["state"]))


def getinfo(name, repo, user, passwd):
    url = "https://api.github.com/repos/{0}/{1}/pulls".format(name, repo)
    q = requests.get(url, params={"sort": "number", "page": "1",
                                  "per_page": "100"}, auth=(user, passwd))
    return (q.json())


def getsingle(name, repo, num, user, passwd):
    url = "https://api.github.com/repos/{0}/{1}/pulls/{2}".format(name,
                                                                  repo,
                                                                  num)
    mydict = requests.get(url, auth=(user, passwd))
    print(("{: <5}" + "{:35}" * 4).format("ID", "User Name", "Title",
                                          "Request Opened", "State\n"))
    print(
        ("{: <5}" + "{:35}" * 4).format(mydict.json()["number"],
                                        mydict.json()["user"]["login"],
                                        mydict.json()["title"],
                                        mydict.json()["created_at"],
                                        mydict.json()["state"]))


def userrepo(name, user, passwd):
    url = "https://api.github.com/users/{0}/repos".format(name)
    mydict = requests.get(url, auth=(user, passwd))
    print(("repositories of user {0} are:").format(name))
    for item in mydict.json():
        print(item["name"])


def writeinfo(mydict):
    with open("requests.txt", "w") as file:
        file.write(json.dumps(mydict))


def userrequests(mydict, user):
    print(("{: <5}" + "{:35}" * 4).format("ID", "User Name", "Title",
                                          "Request Opened", "State\n"))
    for item in mydict:
        if item["head"]["user"]["login"] == user:
            print(("{: <5}" + "{:35}" * 4).format(item["number"],
                                                  item["head"]["user"][
                                                      "login"],
                                                  item["title"],
                                                  item["created_at"],
                                                  item["state"]))


parser = argparse.ArgumentParser()
parser.add_argument("-u", metavar="<github_login>",
                    help="Auth: your github login", required=True)
parser.add_argument("-p", metavar="<github_passwd>",
                    help="Auth: your github password", required=True)
parser.add_argument("-id", metavar="<user_name>", help="Github user",
                    required=True)
parser.add_argument("-r", metavar="<repo_name>",
                    help="Lists requests, user(-id) required",
                    default=None)
parser.add_argument("-n", metavar="<number>",
                    help="Request info, user(-id) and repo(-r) required",
                    default=None)
parser.add_argument("-s", metavar="<user_name>",
                    help="Senders requests, user(-id) & repo(-r) required",
                    default=None)

args = parser.parse_args()

if not args.r:
    userrepo(args.id, args.u, args.p)
elif not (args.n or args.s):
    listrequests(getinfo(args.id, args.r, args.u, args.p))
elif args.n:
    getsingle(args.id, args.r, args.n, args.u, args.p)
elif args.s:
    userrequests(getinfo(args.id, args.r, args.u, args.p), args.s)
else:
    print("error")
