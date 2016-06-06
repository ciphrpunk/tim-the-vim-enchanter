import sqlite3

DBNAME = 'plugins'

try:
    conn = sqlite3.connect("." + DBNAME + ".db")
    print "Opened " + DBNAME + " database"
except:
    print "Failed to open " + DBNAME + " database"
    sys.exit(2)

try:
    conn.execute('''CREATE TABLE PLUGIN
    (id     Text   PRIMARY KEY   NOT NULL UNIQUE,
    Name    Text    NOT NULL,
    Owner   Text    NOT NULL,
    URL     Text    NOT NULL,
    Language    Text);''')

    print "PLUGIN table created"
    conn.close()
except:
    print "Failed to create PLUGIN table"
    sys.exit(2)



