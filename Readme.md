ABOUT
Application to serve as the back-end of covid-times android App 
developed for  MSWE 264P University of California Irvine

NOTE:
This application is a minor modification of code at : https://github.com/Abdulaziz89/flask_api_demo
Please refer to the original author for specifics

URL Samples :
On Localhost
Get all users
http://127.0.0.1:5000/covidapi/resources/users

Get history of given user
http://127.0.0.1:5000/covidapi/resources/history/ben

Curl command to add user
curl -X POST http://127.0.0.1:5000/covidapi/resources/useradd -H "Content-type:application/json" -d "{\"name\":\"carol\"}"

Curl command add history for user
curl -X POST http://127.0.0.1:5000/covidapi/resources/historyadd -H "Content-type:application/json" -d "{\"name\":\"ben\",\"searchterm\":\"australia\"}"

On Elastic BeanStalk :
TBD

