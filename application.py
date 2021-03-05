from flask import Flask, jsonify, request
import json
import sqlite3

application = Flask(__name__)

#home url to test
@application.route('/', methods=['GET'])
def home():
    return '<h1> COVID TIMES API </h1>'
# returns items as dictionaries {col: row}
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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
        return jsonify({'name': uname}), 201
        conn.close()


# return all of the users, from a DB
@application.route('/covidapi/resources/users', methods=['GET'])
def get_all_users():
    with sqlite3.connect('covidtimesdata.db') as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_users = cur.execute("SELECT * FROM Users;").fetchall()
        
        return jsonify(all_users)
        conn.close()

# return history of user, from a DB
@application.route('/covidapi/resources/history/<name>', methods=['GET'])
def get_all_user_history(name):
    with sqlite3.connect('covidtimesdata.db') as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        #userid = cur.execute("SELECT id FROM Users WHERE name=?;",[name]).fetchone()
        all_user_history = cur.execute("SELECT * FROM History WHERE userid=(SELECT id FROM Users WHERE name=?);", [name]).fetchall()

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

# return all of the vaccination info, from  DB
@application.route('/covidapi/resources/vaccinations/all', methods=['GET'])
def get_all_vaccine_info():
    with sqlite3.connect('covidtimesdata.db') as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_vaccine_info = cur.execute("SELECT * FROM Vaccinations;").fetchall()
        
        return jsonify(all_vaccine_info)
        conn.close()

# return vaccination info by county
@application.route('/covidapi/resources/vaccinations/<county>', methods=['GET'])
def get_vaccinations_county(county):
    with sqlite3.connect('covidtimesdata.db') as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        county_vaccines = cur.execute("SELECT * FROM Vaccinations WHERE county=?;", [county]).fetchall()

        return jsonify(county_vaccines)      
        conn.close() 

# return vaccination provider by irvine zip code
@application.route('/covidapi/resources/vaccinations/irvine/<zip>', methods=['GET'])
def get_vaccine_provider_irvine(zip):
    with sqlite3.connect('covidtimesdata.db') as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        vaccine_provider = cur.execute("SELECT * FROM Provider WHERE zipcode=?;", [zip]).fetchall()

        return jsonify(vaccine_provider)      
        conn.close() 


# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()