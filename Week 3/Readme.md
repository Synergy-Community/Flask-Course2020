Steps to deploy app on Heroku:

1. $git init
2. $git add .
3. $git config user.email "your_email@address.com"
4. $git config user.name "your_name"
5. $git commit -m "First Commit"
6. $heroku login -i
7. $heroku create
8. $git push heroku master
9. $heroku logs --tail

for information about the app, type - 

$heroku ps


By default, your app is deployed on a free dyno. 
Free dynos will sleep after a half hour of inactivity (if they don’t receive any traffic). 
This causes a delay of a few seconds for the first request upon waking. 
Subsequent requests will perform normally. 
Free dynos also consume from a monthly, account-level quota of free dyno hours - as long as the quota is not exhausted, all free apps can continue to run.

This is the link of a sample app, hosted on heroku - 
https://shrouded-inlet-93069.herokuapp.com/