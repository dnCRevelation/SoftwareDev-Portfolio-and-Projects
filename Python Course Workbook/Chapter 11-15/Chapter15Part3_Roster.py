import json
import sqlite3

conn = sqlite3.connect('RosterDB2.sqlite')
cur = conn.cursor()

# Prevent SQL from having errors by dropping the current table so it doesnt read duplicate information #

cur.executescript('''
            
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS Member;
            DROP TABLE IF EXISTS Course;
                  
            CREATE TABLE User (
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  name TEXT UNIQUE
            );
                  
            CREATE TABLE Course (
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                  title TEXT UNIQUE
            );
                  
            CREATE TABLE Member (
                  user_id INTEGER,
                  course_id INTEGER,
                    role INTEGER,
                  PRIMARY KEY (user_id, course_id)

            );
''')

fname = input('Enter file name')
if len(fname) < 1:
    fname = 'roster_data.json'

handle = open(fname).read()
jsdata = json.loads(handle)

for entry in jsdata:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
                VALUES ( ?, ?, ? )''', (user_id, course_id, role ))
    

    conn.commit()

sqldata = '''
        SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''
for row in cur.execute(sqldata):
    print(row[0], row[1], str(row[2]))

cur.close() 