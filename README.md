[![SparkXcloud](https://telegra.ph/file/edf199710d567dc54ed97.png)](https://youtu.be/Pk_TthHfLeE)

# SparkXcloud-Gdrive-MirrorBot/LeechBot v2.0 - Deploy Branch

# Heroku Deploy

**Important Notes**
1. Generate all your private files from master branch (token.pickle, config.env, drive_folder, cookies.txt etc...) since the generators not available in heroku branch but you should add the private files in heroku branch not in master or use variables links in `config.env`.
2. Don't add variables in heroku Environment, you can only add `CONFIG_FILE_URL`.
3. Don't deploy using hmanager or github integration.
4. This branch use megasdkrest and latest version of qBittorrent.
5. More notes will be added soon for upstream branch...

------

## Deploy With CLI

- Clone this repo:
```
git clone https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot mirrorbot/ && cd mirrorbot
```
- Switch to heroku branch
  - **NOTE**: Don't commit changes in master branch. If you have committed your changes in master branch and after that you switched to heroku branch, the new added files(private files) will `NOT` appear in heroku branch.
```
git checkout heroku
```
- After adding your private files
```
git add . -f
```
- Commit your changes
```
git commit -m token
```
- Login to heroku
```
heroku login
```
- Create heroku app
```
heroku create --region us YOURAPPNAME
```
- Add remote
```
heroku git:remote -a YOURAPPNAME
```
- Create container
```
heroku stack:set container
```
- Push to heroku
```
git push heroku heroku:master -f
```

------

### Extras

- To create heroku-postgresql database
```
heroku addons:create heroku-postgresql
```
- To delete the app
```
heroku apps:destroy YOURAPPNAME
```
- To restart dyno
```
heroku restart
```
- To turn off dyno
```
heroku ps:scale web=0
```
- To turn on dyno
```
heroku ps:scale web=1
```
- To set heroku variable
```
heroku config:set VARNAME=VARTEXT
```
- To get live logs
```
heroku logs -t
```

------

## Deploy With Github Workflow

1. Go to Repository Settings -> Secrets

![Secrets](https://telegra.ph/file/e5943673de7508a8152f0.jpg)

2. Add the below Required Variables one by one by clicking New Repository Secret every time.

   - HEROKU_EMAIL: Heroku Account Email Id in which the above app will be deployed
   - HEROKU_API_KEY: Your Heroku API key, get it from https://dashboard.heroku.com/account
   - HEROKU_APP_NAME: Your Heroku app name, Name Must be unique
   - CONFIG_FILE_URL: Copy [This](https://raw.githubusercontent.com/https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/master/config_sample.env) in any text editor.Remove the _____REMOVE_THIS_LINE_____=True line and fill the variables. For details about config you can see Here. Go to https://gist.github.com and paste your config data. Rename the file to config.env then create secret gist. Click on Raw, copy the link. This will be your CONFIG_FILE_URL. Refer to below images for clarity.

![Steps from 1 to 3](https://telegra.ph/file/194b7a945e3973379dd47.jpg)

![Step 4](https://telegra.ph/file/c7b5160f102a2ecf8755d.jpg)

![Step 5](https://telegra.ph/file/5c8d2f2e24bfa1b8b76af.jpg)

3. Remove commit id from raw link to be able to change variables without updating the CONFIG_FILE_URL in secrets. Should be in this form: https://gist.githubusercontent.com/username/gist-id/raw/config.env

4. Add all your private files in this branch or use variables links in `config.env`.

5. After adding all the above Required Variables go to Github Actions tab in your repository.
   - Select Manually Deploy to Heroku workflow as shown below:

![Select Manual Deploy](https://telegra.ph/file/fa4475c09f0f802e57361.jpg)

6. Choose `heroku` branch and click on Run workflow

![Run Workflow](https://telegra.ph/file/2dd025473949136cf27d9.png)

