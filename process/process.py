import sys, os, re
import xml.etree.ElementTree as et
import urllib2 as req
import getopt
from xml.dom import minidom
from urlparse import urlparse, urljoin
from os.path import splitext, basename
import requests, json, getpass

GITHUB_API = 'https://api.github.com'

def prettyPrint(elTree):
    return minidom.parseString(et.tostring(elTree, 'utf-8')).toprettyxml(indent="  ")

def makeTitle(name):
    parts = re.sub(r"\-(.)", r" \1", name).split()
    returnStr = ""
    for part in parts:
        returnStr += part.capitalize() + " "
    return returnStr.strip()

def getToken():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    username = raw_input("Github username: " )
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    password = getpass.getpass("Github password: ")
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    payload = {}
    payload['note'] = "admin script"
    res = requests.post(
            urljoin(GITHUB_API, 'authorizations'),
            auth = (username, password),
            data = json.dumps(payload)
            )
    auth = json.loads(res.text)
    return auth["token"]

def getPlugin(url, token):
    headers = {'content-type': 'application/json', "Authorization": 'token %s' % token}
    try:
        return requests.get(url, headers=headers).json()
    except:
        print("Not Valid")

def checkURL(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme in ('https', 'https'):
            if parsed.hostname in ('www.github.com', 'github.com', 'api.github.com'):
                return True
            else:
                return False
        else:
            return False
    except:
        print("Not Valid")

def main(argv):
    updateFlag = False
    name = ""
    url = ""
    try:
        opts, args = getopt.getopt(argv,"u:n:a", ["name=", "url=", "all", "update"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--update":
            updateFlag = True
        elif opt in ("-a", "--all"):
            process(getList())
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-u", "--url"):
            url = arg
        else:
            usage()
            sys.exit(2)

    if updateFlag and checkURL(url):
        plugin = getPlugin(url, getToken())

        print "Name       : " + plugin['name']
        print "Description: " + plugin['description']
        print "Clone Url  : " + plugin['clone_url']

if __name__ == "__main__":
    main(sys.argv[1:])
