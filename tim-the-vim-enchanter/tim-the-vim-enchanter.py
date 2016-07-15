import sys, os, re
import xml.etree.ElementTree as et
import urllib2 as req
import getopt
from xml.dom import minidom
from urlparse import urlparse, urljoin
from os.path import splitext, basename
import requests, json, getpass, subprocess, shlex

GITHUB_API = 'https://api.github.com'
THIS_DIR = os.path.dirname(__file__)
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
    payload['note'] = "Tim the Enchanter"
    res = requests.post(
            urljoin(GITHUB_API, 'authorizations'),
            auth = (username, password),
            data = json.dumps(payload)
            )
    auth = json.loads(res.text)
    return auth["token"]

def getPlugin(name):
    tree = et.parse('data/db/plugins.xml')
    root = tree.getroot
    for elem in tree.iterfind('Plugin[@name="' + name + '"]'): # dupe names will bug out here...
        return elem.attrib['name']

def getRepo(url):
    try:
        return requests.get(url).json()
    except:
        print("Not Valid")

def makeDirs():
    if(not os.path.exists(os.getenv('HOME') + '/.vim')):
        print "Making ~/.vim/"
        sendCmd('mkdir ' + os.getenv('HOME') + '/.vim/')
    if(not os.path.exists(os.getenv('HOME') + '/.vim/bundle/')):
        sendCmd('mkdir ' + os.getenv('HOME') + '/.vim/bundle/')

def appendPlugin(plugin):
    tree = et.parse('data/db/plugins.xml')
    root = tree.getroot()
    child = et.SubElement(root, "Plugin")
    child.set("name", plugin['name'])
    child.set("url", plugin['url'])
    tree = et.ElementTree(root)
    tree.write('data/db/plugins.xml')

def all():
    # makeDirs() 
    tree = et.parse('data/db/plugins.xml')
    root = tree.getroot()
    print "Getting plugins\n"
    for child in root:
        plugin = child.attrib
        process(plugin)
    print "Moving vimrc to ~/.vimrc\n"
    sendCmd('cp ' + THIS_DIR + 'vim.conf.d/vimrc ' + os.getenv('HOME') + '/.vimrc')
    print "Done!\n"

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
        print("Not Valid: checkURL")

def parseURL(url):
    parsed = {}
    try:
        print url
        path = urlparse(url).path[1:].split("/")
        parsed['owner'] = path[0]
        parsed['repo'] = path[1].split(".git")[0]
        return parsed
    except:
        print ("Not valid: parseURL")

def parseRepo(url):
    parsed = parseURL(url)
    return urljoin(GITHUB_API, '/repos/' + parsed['owner'] + '/' + parsed['repo'])

def sendCmd(cmd):
    kwargs = {}
    kwargs['stdout'] = subprocess.PIPE
    kwargs['stderr'] = subprocess.PIPE
    proc = subprocess.Popen(shlex.split(cmd), **kwargs)
    (stdout_str, stderr_str) = proc.communicate()
    if stdout_str != '':
        print stdout_str
    if stderr_str != '':
        print stderr_str

def process(plugin):
    print "Name       : " + plugin['name']
    print "Clone Url  : " + plugin['url']
    sendCmd('git clone ' + plugin['url'] + ' ' + THIS_DIR + 'build/stage/.unstaged/bundle/' + plugin['name'].replace(" ", "-"))
    if(plugin['name'] == 'Pathogen'):
        sendCmd('cp -R ' + THIS_DIR + 'build/stage/.unstaged/bundle/' + plugin['name'].replace(" ", "-") + "/autoload/ " + os.getenv('HOME') + '/.vim/')
    else:
        sendCmd('cp -R ' + THIS_DIR + 'build/stage/.unstaged/bundle/' + plugin['name'].replace(" ", "-") + " " + os.getenv('HOME') + '/.vim/bundle/')
    sendCmd('rm -rf ' + THIS_DIR + 'build/stage/.unstaged/bundle/' + plugin['name'].replace(" ", "-")) 

def remove(plugin):
    name = getPlugin(plugin)
    print "Removing " + name + " at " + os.getenv('HOME') + '/.vim/bundle/' + name.replace(" " , "-")
    sendCmd('rm -rf ' + os.getenv('HOME') + '/.vim/bundle/' + name.replace(" ", "-")) 

def main(argv):
    updateFlag = False
    getFlag = False
    name = ""
    url = ""
    username = ""
    try:
        opts, args = getopt.getopt(argv,"u:n:a:t:r:g", ["name=", "url=", "all", "update", "try", "remove="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--update":
            updateFlag = True
        elif opt in ("-a", "--all"):
            all()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("--url"):
            url = arg
        elif opt in ("-u"):
            username = arg
        elif opt in ("-t", "--try"):
            tryit()
        elif opt in ("-r", "--remove"):
            print arg
            remove(arg)
        elif opt in ("-g"):
            getFlag = True
        else:
            usage()
            sys.exit(2)

    if (updateFlag or getFlag) and checkURL(url):
        parsed = parseRepo(url)
        plugin = getRepo(parsed)
        plugin['name'] = makeTitle(plugin['name'])
        plugin['url'] = plugin['clone_url']
        appendPlugin(plugin)
        process(plugin)
if __name__ == "__main__":
    main(sys.argv[1:])
