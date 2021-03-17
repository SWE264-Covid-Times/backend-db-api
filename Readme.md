#ABOUT
Application to serve as the back-end of covid-times android App 
developed for  MSWE 264P University of California Irvine

Vaccination Information obtained from : 
https://github.com/datadesk/california-coronavirus-data/blob/master/cdph-vaccination-county-totals.csv

DB currently holds data from 28 Jan 2021 to March 7 2021

Nearest vaccine provider in Irvine by zipcode gleaned from :
https://vaccinefinder.org/


NOTE:
This application is a minor modification of code at : https://github.com/Abdulaziz89/flask_api_demo </br>
Please refer to the original repo for specifics

#URL Samples :
On Localhost</br>
Get all users

http://127.0.0.1:5000/covidapi/resources/users

Get history of given user

http://127.0.0.1:5000/covidapi/resources/history/ben

Vaccination counts for all California counties

http://127.0.0.1:5000/covidapi/resources/vaccinations/all

Vaccination counts per county in California

http://127.0.0.1:5000/covidapi/resources/vaccinations/Orange

Nearest vaccine provider in irvine by zip

http://127.0.0.1:5000/covidapi/resources/vaccinations/irvine/92616

Curl command to add user<br />

curl -X POST http://127.0.0.1:5000/covidapi/resources/useradd -H "Content-type:application/json" -d "{\\"name\\":\\"carol\\"}"

Curl command add history for given user

curl -X POST http://127.0.0.1:5000/covidapi/resources/historyadd -H "Content-type:application/json" -d "{\\"name\\":\\"ben\\",\\"searchterm\\":\\"south-africa\\",\\"fromdate\\":\\"2021-02-10\\",\\"todate\\":\\"2021-02-13\\",\\"casecount\\":100}"

(Beanstalk links are no longer active)
On Elastic BeanStalk :<br />
List all users <br />
http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/users

History of user <br />
http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/history/adam


All vaccination info <br />
Fields : date, county, fips, doses_administered, new_doses_administered <br />
http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/vaccinations/all

Vaccination info by county<br />
Fields : date, county, fips, doses_administered, new_doses_administered <br />
http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/vaccinations/Orange

Nearest Vaccine Provider based on Irvine Zip code <br />
Fields: zip, provider, address, phone <br />
http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/vaccinations/irvine/92618

Curl command to add user
<br />
curl -X POST http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/useradd -H "Content-type:application/json" -d "{\\"name\\":\\"carol\\"}"

Curl command to add user hisory
<br />
curl -X POST http://covidtimes-env.eba-yjpbhcys.us-east-2.elasticbeanstalk.com/covidapi/resources/historyadd -H "Content-type:application/json" -d "{\\"name\\":\\"evan\\",\\"searchterm\\":\\"south-africa\\",\\"fromdate\\":\\"2021-02-10\\",\\"todate\\":\\"2021-02-13\\",\\"casecount\\":100}"
