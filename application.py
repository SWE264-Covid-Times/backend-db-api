from flask import Flask, jsonify, request
import json
import sqlite3

application = Flask(__name__)

#home url to test
@application.route('/', methods=['GET'])
def home():
    return '<h1> COVID TIMES API </h1>'

# add a user to the DB
@application.route('/covidapi/resources/useradd', methods=['POST'])
def add_user():
    try:
        uname = request.json['name']
        with sqlite3.connect("covidtimesdata.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Users (name) VALUES(?)",(uname,))
            conn.commit()
            print("User {} added".format(uname))
    except Exception as e:
        print(e)
        print("There was an exception on adding user rolling back")
        conn.rollback()

    finally:
        return jsonify({'user name': uname}), 201
        conn.close()


# return all of the users, from a DB
@application.route('/covidapi/resources/users', methods=['GET'])
def get_all_users():
    with sqlite3.connect('covidtimesdata.db') as conn:
        #conn.row_factory = dict_factory
        cur = conn.cursor()
        all_users = cur.execute("SELECT * FROM Users;").fetchall()
        
        return jsonify(all_users)
        conn.close()

# return history of user, from a DB
@application.route('/covidapi/resources/history/<name>', methods=['GET'])
def get_all_user_history(name):
    with sqlite3.connect('covidtimesdata.db') as conn:
        #conn.row_factory = dict_factory
        cur = conn.cursor()
        userid = cur.execute("SELECT id FROM Users WHERE name=?;",[name]).fetchone()
        all_user_history = cur.execute("SELECT * FROM History WHERE userid=?;", userid).fetchall()

        return jsonify(all_user_history)      
        conn.close()  

# add user history to DB
@application.route('/covidapi/resources/historyadd', methods=['POST'])
def add_user_history():
    try:
        uname = request.json['name']
        searchterm = request.json['searchterm']
        fromdate = request.json['fromdate']
        todate = request.json['todate']
        casecount = request.json['casecount']
        
        with sqlite3.connect("covidtimesdata.db") as conn:
            cur = conn.cursor()
            userid = cur.execute("SELECT id FROM Users WHERE name=?;",[uname]).fetchone()

            cur.execute("INSERT INTO History (userid,searchterm, fromdate, todate, casecount) VALUES(?,?,?,?,?)",(userid[0],searchterm,fromdate, todate, casecount))
            conn.commit()
            print("Added to history {}, {}".format(uname,searchterm))
    except Exception as e:
        print (e)
        print("There was an error on adding history rolling back")
        conn.rollback()

    finally:
        return jsonify({'user name': uname,'search term': searchterm}), 201
        conn.close()

# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()