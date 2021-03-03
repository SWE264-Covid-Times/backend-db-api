#ABOUT
Application to serve as the back-end of covid-times android App 
developed for  MSWE 264P University of California Irvine

Vaccination Information obtained from : 
https://github.com/datadesk/california-coronavirus-data/blob/master/cdph-vaccination-county-totals.csv

DB currently holds data from 15 Feb 2021 to March 2 2021


NOTE:
This application is a minor modification of code at : https://github.com/Abdulaziz89/flask_api_demo </br>
Please refer to the original repo for specifics

#URL Samples :
On Localhost</br>
Get all users

http://127.0.0.1:5000/covidapi/resources/users

Get history of given user

http://127.0.0.1:5000/covidapi/resources/history/ben

Vaccination counts by California county

127.0.0.1:5000/covidapi/resources/vaccinations

Curl command to add user

curl -X POST http://127.0.0.1:5000/covidapi/resources/useradd -H "Content-type:application/json" -d "{\\"name\\":\\"carol\\"}"

Curl command add history for given user

curl -X POST http://127.0.0.1:5000/covidapi/resources/historyadd -H "Content-type:application/json" -d "{\\"name\\":\\"ben\\",\\"searchterm\\":\\"south-africa\\",\\"fromdate\\":\\"2021-02-10\\",\\"todate\\":\\"2021-02-13\\",\\"casecount\\":100}"

On Elastic BeanStalk :
http://covidtimes-env.eba-zjmz2ppq.us-east-1.elasticbeanstalk.com/covidapi/resources/users

http://covidtimes-env.eba-zjmz2ppq.us-east-1.elasticbeanstalk.com/covidapi/resources/history/adam

http://covidtimes-env.eba-zjmz2ppq.us-east-1.elasticbeanstalk.com/covidapi/resources/vaccinations

curl -X POST http://covidtimes-env.eba-zjmz2ppq.us-east-1.elasticbeanstalk.com/covidapi/resources/useradd -H "Content-type:application/json" -d "{\\"name\\":\\"carol\\"}"

curl -X POST http://covidtimes-env.eba-zjmz2ppq.us-east-1.elasticbeanstalk.com/covidapi/resources/historyadd -H "Content-type:application/json" -d "{\\"name\\":\\"evan\\",\\"searchterm\\":\\"south-africa\\",\\"fromdate\\":\\"2021-02-10\\",\\"todate\\":\\"2021-02-13\\",\\"casecount\\":100}"