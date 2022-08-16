![SparkXcloud](https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/raw/master/assets/banner.png)

# SparkXcloud-Gdrive-MirrorBot/LeechBot v2.0
[![Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://ko-fi.com/harshhaareddy)
[![GitHub watchers](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://img.shields.io/github/watchers/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot)
[![Docker Pulls](https://img.shields.io/badge/Docker-ff1709?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/harshhaareddy/mega-sdk-python)
[![Channel](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/SparkXcloud)

**SparkXcloud-Gdrive-MirrorBot** *is a _multipurpose_ Telegram Bot writen in Python for mirroring files on the Internet to our beloved Google Drive.*

# Features:

## By [Sparkxcloud](https://github.com/Spark-X-Cloud)
-----
### ➡️ Spark-x-cloud mirrorbot main features :-

***In each single file there is a major change from base code, it's almost totaly different. Here some of features and fixes that I remember.***
### 🥀 qBittorrent
- *Qbittorrent support*
- *Select files from Torrent before and while downloading*
- *Seed torrents to specific ratio and time*
### 🥀 Aria2c
- *Select files from Torrent before and while downloading*
- *Seed torrents to specific ratio and time*
- *Netrc support*
- *Direct link authentication for specific link while using the bot (it will work even if only username or password)*
- *Improve aria.sh*
- *Fix all download listener functions and status*
### 🥀 Leech
- *Leech support*
- *Splitting*
- *Thumbnail for each user*
- *Set upload as document or as media for each user*
- *4GB file upload with premium account*
### 🥀 Google
- *Stop duplicates for all tasks except yt-dlp tasks*
- *Download G-Drive links*
- *Counting files/folders from Google Drive link*
- *Search in multiple Drive folder/TeamDrive*
- *Recursive Search (only with `root` or TeamDrive ID, folder ids will be listed with non-recursive method)*
- *Use Token.pickle if file not found with Service Account, for all Gdrive functions*
- *List result in html file instead of telegraph or telegram message to avoid limits by @junedkh*
- *Random Service Account at startup*
### 🥀 Status
- *Clone Status*
- *Extract Status*
- *Archive Status*
- *Seed Status*
- *Status Pages for unlimited tasks*
- *Ability to cancel upload/clone/archive/extract/split*
- *Cancel all buttons for choosing specific tasks status to cancel*
- *Fix flooding issues*
- *Fix overall upload and download speed*
### 🥀 Yt-dlp
- *Switch from youtube-dl to yt-dlp and fix all conflicts*
- *Yt-dlp quality buttons*
- *Support for download live streams*
- *Ability to use specific yt-dlp arg for each task*
- *Fix download progress*
### 🥀 Database
- *SQL Database support*
- *Save leech settings including thumbnails in database*
- *Save sudo and authorized users*
- *Incomplete task notifier to get incomplete task messages after restart*
### 🥀 Torrents Search
- *Torrent search support*
- *Search on torrents with Torrent Search API*
- *Search on torrents with variable plugins using qBittorrent search engine*
### 🥀 Archives
- *Zip instead of tar*
- *Using 7-zip tool to extract all supported files*
- *Extract rar, zip and 7z within folder or splits with or without password*
- *Zip file/folder with or without password*
### 🥀 RSS
- *Rss feed. Based on this repository* [rss-chan](https://github.com/hyPnOtICDo0g/rss-chan)
- *Filter added and all functions have been improved*
### 🥀 Overall
- *Docker image support for linux `amd64, arm64/v8, arm/v7, s390x`*
- *Update bot at startup and with restart command using `UPSTREAM_REPO`*
- *Mirror/Leech/Watch/Clone/Count/Del by reply*
- *Mirror/Leech/Clone multi links/files with one command*
- *Custom name for all links except torrents. For files you should add extension except yt-dlp links*
- *Extensions Filter for the files to be uploaded/cloned*
- *View Link button. Extra button to open index link in broswer instead of direct download for file*
- *Almost all repository functions have been improved and many other details can't mention all of them*
- *Many bugs have been fixed*
-----
## Bot commands
### ➡️ Required Fields
- `BOT_TOKEN`: *The Telegram Bot Token that you got from* [@BotFather](https://t.me/BotFather)
- `GDRIVE_FOLDER_ID`: *This is the Folder/TeamDrive ID of the Google Drive Folder to which you want to upload all the mirrors.*
- `OWNER_ID`: *The Telegram User ID (not username) of the Owner of the bot. `Int`*
- `DOWNLOAD_DIR`: *The path to the local folder where the downloads should be downloaded to.*
- `DOWNLOAD_STATUS_UPDATE_INTERVAL`: *Time in seconds after which the progress/status message will be updated. Recommended `10` seconds at least. `Int`*
- `AUTO_DELETE_MESSAGE_DURATION`: *Interval of time (in seconds), after which the bot deletes it's message and command message which is expected to be viewed instantly. **NOTE**: Set to `-1` to disable auto message deletion. `Int`*
- `IS_TEAM_DRIVE`: *Set `True` if uploading to TeamDrive. Default is `False`. `Bool`*
- `TELEGRAM_API`: *This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org. `Int`*
- `TELEGRAM_HASH`: *This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org.*
-----
### ➡️ Optional Fields
- `DATABASE_URL`: *Your SQL Database URL. Follow this [Generate Database](https://github.com/anasty17/mirror-leech-telegram-bot/tree/master#generate-database) to generate database. Data will be saved in Database: auth and sudo users, leech settings including thumbnails for each user, rss data and incomplete tasks. **NOTE**: If deploying on heroku and using heroku postgresql delete this variable from **config.env** file. **DATABASE_URL** will be grabbed from heroku variables.*
- `AUTHORIZED_CHATS`: *Fill user_id and chat_id of groups/users you want to authorize. Separate them by space.*
- `SUDO_USERS`: *Fill user_id of users whom you want to give sudo permission. Separate them by space.*
- `IGNORE_PENDING_REQUESTS`: *Ignore pending requests after restart. Default is `False`. `Bool`*
- `USE_SERVICE_ACCOUNTS`: *Whether to use Service Accounts or not. For this to work see Using Service Accounts section. Default is `False`. `Bool`*
- `INDEX_URL`: *Refer to https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index.*
- `STATUS_LIMIT`: *Limit the no. of tasks shown in status message with buttons. **NOTE**: Recommended limit is `4` tasks.*
- `STOP_DUPLICATE`: *Bot will check file in Drive, if it is present in Drive, downloading or cloning will be stopped.* (**NOTE**: *File will be checked using filename not file hash, so this feature is not perfect yet). Default is `False`. `Bool`*
- `CMD_INDEX`: *commands index number. This number will added at the end all commands.*
- `UPTOBOX_TOKEN`: *Uptobox token to mirror uptobox links. Get it from [Uptobox Premium Account](https://uptobox.com/my_account).*
- `TORRENT_TIMEOUT`: *Timeout of dead torrents downloading with qBittorrent and Aria2c in seconds.*
- `EXTENTION_FILTER`: *File extentions that won't upload/clone. Separate them by space.*
- `INCOMPLETE_TASK_NOTIFIER`: *Get incomplete task messages after restart. Require database and (supergroup or channel). Default is `False`. `Bool`*
-----
### ➡️ Update
- `UPSTREAM_REPO`: *Your github repository link, if your repo is private add `https://username:{githubtoken}@github.com/{username}/{reponame}` format. Get token from [Github settings](https://github.com/settings/tokens). So you can update your bot from filled repository on each restart. ***NOTE***: Any change in docker or requirements you need to deploy/build again with updated repo to take effect. DON'T delete .gitignore file.*
- `UPSTREAM_BRANCH`: *Upstream branch for update. Default is `master`.*
-----
### ➡️ Leech
- `USER_SESSION_STRING`: *To download/upload from your telegram account. To generate session string use this command `python3 generate_string_session.py` after mounting repo folder for sure.* ***NOTE***: *You can't use bot with private message, use it with supergroup or channel.*
- `LEECH_SPLIT_SIZE`: *Size of split in bytes. Default is `2GB`. Default is `4GB` if your account is premium.*
- `AS_DOCUMENT`: *Default type of Telegram file upload. Default is `False` mean as media. `Bool`*
- `EQUAL_SPLITS`: *Split files larger than **LEECH_SPLIT_SIZE** into equal parts size (Not working with zip cmd). Default is `False`. `Bool`*
- `CUSTOM_FILENAME`: *Add custom word to leeched file name.*
-----
### ➡️ qBittorrent/Aria2c
- `BASE_URL_OF_BOT`: *Valid BASE URL where the bot is deployed to use qbittorrent web selection. Format of URL should be `http://myip`, where `myip` is the IP/Domain(public) of your bot or if you have chosen port other than `80` so write it in this format `http://myip:port` (`http` and not `https`). This Var is optional on VPS and required for Heroku specially to avoid app sleeping/idling. For Heroku fill `https://yourappname.herokuapp.com`. Still got idling? You can use http://cron-job.org to ping your Heroku app.*
- `SERVER_PORT`: *Only For VPS even if `IS_VPS` is `False`, which is the **BASE_URL_OF_BOT** Port.*
- `WEB_PINCODE`: *If empty or `False` means no more pincode required while qbit web selection. `Bool`*
  - ***Qbittorrent NOTE***: *If your facing ram exceeded issue then set limit for `MaxConnecs` and decrease `AsyncIOThreadsCount` in qbittorrent config.*
-----
### ➡️ RSS
- `RSS_DELAY`: *Time in seconds for rss refresh interval. Recommended `900` second at least. Default is `900` in sec.*
- `RSS_COMMAND`: *Choose command for the desired action.*
- `RSS_CHAT_ID`: *Chat ID where rss links will be sent. If using channel then add channel id.*
- `RSS_USER_SESSION_STRING`: *To send rss links from your telegram account. Instead of adding bot to channel then linking the channel to group to get rss link since bot will not read command from itself or other bot. To generate session string use this command `python3 generate_string_session.py` after mounting repo folder for sure. **NOTE**: Don't use same session string as* `USER_SESSION_STRING`.
  - ***RSS NOTE***: `DATABASE_URL` *and* `RSS_CHAT_ID` *is required, otherwise all rss commands will not work. You must use bot in group. You can add the bot to a channel and link this channel to group so messages sent by bot to channel will be forwarded to group without using* `RSS_USER_STRING_SESSION`.
-----
### ➡️ Private Files
- `ACCOUNTS_ZIP_URL`: *Only if you want to load your Service Account externally from an Index Link or by any direct download link NOT webpage link. Archive the accounts folder to ZIP file. Fill this with the direct download link of zip file. If index need authentication so add direct download as shown below:*
  - `https://username:password@example.workers.dev/...`
- `TOKEN_PICKLE_URL`: *Only if you want to load your ***token.pickle*** externally from an Index Link. Fill this with the direct link of that file.*
- `MULTI_SEARCH_URL`: *Check `drive_folder` setup. Write **drive_folder** file [here](https://gist.github.com/). Open the raw file of that gist, it's URL will be your required variable. Should be in this form after removing commit id:* https://gist.githubusercontent.com/username/gist-id/raw/drive_folder
- `YT_COOKIES_URL`: *Youtube authentication cookies. Check setup* [Here](https://github.com/ytdl-org/youtube-dl#how-do-i-pass-cookies-to-youtube-dl). *Use gist raw link and remove commit id from the link, so you can edit it from gists only.*
- `NETRC_URL`: *To create .netrc file contains authentication for aria2c and yt-dlp. Use gist raw link and remove commit id from the link, so you can edit it from gists only. ***NOTE***: After editing .nterc you need to restart the docker or if deployed on heroku so restart dyno in case your edits related to aria2c authentication.*
  - ***NOTE***: *All above url variables used incase you want edit them in future easily without deploying again or if you want to deploy from public fork. If deploying using cli or private fork you can leave these variables empty add token.pickle, accounts folder, drive_folder, .netrc and cookies.txt directly to root but you can't update them without rebuild OR simply leave all above variables and use private UPSTREAM_REPO.*
-----
### ➡️ MEGA
- `MEGA_API_KEY`: *Mega.nz API key to mirror mega.nz links. Get it from* [Mega SDK Page](https://mega.nz/sdk)
- `MEGA_EMAIL_ID`: *E-Mail ID used to sign up on mega.nz for using premium account.*
- `MEGA_PASSWORD`: *Password for mega.nz account.*
-----
### ➡️ Shortener
- `SHORTENER_API`: *Fill your Shortener API key.*
- `SHORTENER`: *Shortener URL.*
  - *Supported URL Shorteners:*
  >exe.io, gplinks.in, shrinkme.io, urlshortx.com, shortzon.com, bit.ly, shorte.st, linkvertise.com , ouo.io, adfoc.us, cutt.ly

-----
### ➡️ GDTOT

- `CRYPT`: *Cookie for gdtot google drive link generator. Paste below code in browser or make below code as bookmark in browser to run code easily.*

1. *Login/Register to* [gdtot](https://new.gdtot.top).

2. *Copy this script and paste it in browser address bar.*
  - ***Note***: *After pasting it check at the beginning of the script in broswer address bar if `javascript:` exists or not, if not so write it as shown below.*
```
javascript:(function () {
 const input = document.createElement('input');
 COOKIE = JSON.parse(JSON.stringify({cookie : document.cookie}));
 input.value = COOKIE['cookie'].split('crypt=')[1];
 document.body.appendChild(input);
 input.focus();
 input.select();
 var result = document.execCommand('copy');
 document.body.removeChild(input);
  if(result)
    alert('Crypt copied to clipboard');
  else
    prompt('Failed to copy Crypt. Manually copy below Crypt\n\n', input.value);
})();
```
3. *Now you'll get Crypt value in your clipboard*
   ```
   NGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxWdSVT0%3D
   ```
4. *From this you have to paste value for **CRYPT** in config.env file.*    
-----
### ⬇️ Size Limits
-----
- `TORRENT_DIRECT_LIMIT`: *To limit the Torrent/Direct mirror size. Don't add unit. Default unit is `GB`.*
- `ZIP_UNZIP_LIMIT`: *To limit the size of zip and unzip commands. Don't add unit. Default unit is `GB`.*
- `CLONE_LIMIT`: *To limit the size of Google Drive folder/file which you can clone. Don't add unit. Default unit is `GB`.*
- `MEGA_LIMIT`: *To limit the size of Mega download. Don't add unit. Default unit is `GB`.*
- `STORAGE_THRESHOLD`: *To leave specific storage free and any download will lead to leave free storage less than this value will be cancelled. Don't add unit. Default unit is `GB`.*
-----
### ⬇️ Buttons
- *`VIEW_LINK`: View Link button to open file Index Link in browser instead of direct download link, you can figure out if it's compatible with your Index code or not, open any video from you Index and check if its URL ends with `?a=view`. Compatible with [BhadooIndex](https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index) Code. Default is `False`. `Bool`*

- *Three buttons are already added including Drive Link, Index Link, and View Link, you can add extra buttons, if you don't know what are the below entries, simply leave them empty.*
  - `BUTTON_FOUR_NAME`:
  - `BUTTON_FOUR_URL`:
  - `BUTTON_FIVE_NAME`:
  - `BUTTON_FIVE_URL`:
  - `BUTTON_SIX_NAME`:
  - `BUTTON_SIX_URL`:
-----
### ⬇️ Torrent Search
- `SEARCH_API_LINK`: *Search api app link. Get your api from deploying this [repository](https://github.com/Ryuk-me/Torrent-Api-py).*
  - Supported Sites:
  >1337x, Piratebay, Nyaasi, Torlock, Torrent Galaxy, Zooqle, Kickass, Bitsearch, MagnetDL, Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject and YourBittorrent
- `SEARCH_LIMIT`: *Search limit for search api, limit for each site and not overall result limit. Default is zero (Default api limit for each site).*
- `SEARCH_PLUGINS`: *List of qBittorrent search plugins (github raw links). I have added some plugins, you can remove/add plugins as you want. Main Source: [qBittorrent Search Plugins (Official/Unofficial)](https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins).*

------

#### ⬇️ Notes

* ***All commands can also be called using dot(.) instead of slash(/). For e.x:*** `.mirror <url>` or `.m <url>`

* ***All commands except** `list` **can have the bot's username appended to them. See*** `COMMANDS_USE_BOT_NAME` ***under [constants description](#Constants-description).*** *This is useful if you have multiple instances of this bot in the same group.*

* *While creating a Telegram bot in the [pre-installation](#Pre-installation]) section below, you might want to add the above commands to your new bot by using `/setcommand` in BotFather, make sure all the commands are in lower case. This will cause a list of available bot commands to pop up in chats when you type `/`, and you can long press one of them to select it instead of typing out the entire command.*

# Features supported:
<details>
    <summary><b>Click Here For More Details</b></summary>

## ⬇️ Additional Features
- qBittorrent supported
- Updater (**NOTE**: You must upload your **token.pickle** to Index and fill your **token.pickle** url to **TOKEN_PICKLE_URL**, because your **token.pickle** will deleted after update, for more info please check [Setting up config file](https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/tree/majorupdate#setting-up-config-file))
- Limiting size Torrent/Direct, Tar/Unzip, Mega, cloning Google Drive support
- Stop duplicate cloning Google Drive & mirroring Mega support
- Tar/Unzip Google Drive link support
- Select files from Torrent before downloading
- Sudo with Database support
- Multiple Trackers support
- Extracting **tar.xz** support
- Counting Google Drive link
- Heroku config support
- View Link button
- Shell and Executor
- Speedtest
- Torrent search Supported:
```
nyaa.si, sukebei, 1337x, piratebay,
tgx, yts, eztv, torlock, rarbg
```
- Direct links Supported:
```
 >mediafire, letsupload.io, hxfile.co, anonfiles.com, bayfiles.com, antfiles, fembed.com, fembed.net, femax20.com, layarkacaxxi.icu, fcdn.stream, sbplay.org, naniplay.com, naniplay.nanime.in, naniplay.nanime.biz, sbembed.com, streamtape.com, streamsb.net, feurl.com, upload.ee, pixeldrain.com, racaty.net, 1fichier.com, 1drv.ms (Only works for file not folder or business account), uptobox.com and solidfiles.com
```
-----
## ⬇️ From Base and other Repositories
- *Mirror direct download links, Torrent, Mega.nz and Telegram files to Google Drive*
- *Copy files from someone's Drive to your Drive*
- *Download/Upload progress, Speeds and ETAs*
- *Mirror all Youtube-dl supported links*
- *Docker support*
- *Uploading to Team Drive*
- *Index Link support*
- *Service Account support*
- *Delete files from Drive*
- *Shortener support*
- *Custom Filename (Only for URL, Telegram files and Youtube-dl. Not for Mega links and Magnet/Torrents)*
- *Extracting password protected files, using custom filename and download from password protected Index Links see these examples:*
<p><a href="https://telegra.ph/Magneto-Python-Aria---Custom-Filename-Examples-01-20"> <img src="https://img.shields.io/badge/see%20on%20telegraph-grey?style=for-the-badge" width="190""/></a></p>

- *Extract these filetypes*
```
ZIP, RAR, TAR, 7z, ISO, WIM, CAB, GZIP, BZIP2, 
APM, ARJ, CHM, CPIO, CramFS, DEB, DMG, FAT, 
HFS, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, 
NTFS, RPM, SquashFS, UDF, VHD, XAR, Z.
```

</details>

-----
# How to deploy?
*Deploying is pretty much straight forward and is divided into several steps as follows:*

- Tutorial Video from A to Z:
  - Thanks to [Wiszky](https://github.com/vishnoe115)
 <p><a href="https://youtu.be/IUmq1paCiHI"> <img src="https://img.shields.io/badge/See%20Video-black?style=for-the-badge&logo=YouTube" width="160""/></a></p>

## ⬇️ Installing requirements

- *Clone this repo:*
```
git clone https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/
cd mirrorbot
```

- *Install requirements
For Debian based distros*
```
sudo apt install python3 python3-pip
```
*Install Docker by following the* [official Docker docs](https://docs.docker.com/engine/install/debian/)

- *For Arch and it's derivatives:*
```
sudo pacman -S docker python
```
- *Install dependencies for running setup scripts:*
```
pip3 install -r requirements-cli.txt
```
-----
## Bittorrent Seed

- Add `d:ratio:time` perfix along with leech or mirror cmd.
- Using `d` perfix alone will lead to use global options for aria2c or qbittorrent.

### Qbittorrent
- Global options: `MaxRatio` and `GlobalMaxSeedingMinutes` in qbittorrent.conf, `-1` means no limit, but you can cancel manually.
  - **NOTE**: Don't change `MaxRatioAction`.

### Aria2c
- Global options: `--seed-ratio` (0 means no limit) and `--seed-time` (0 means no seed) in aria.sh.

------
### ⬇️ Using Service Accounts for uploading to avoid user rate limit

>For Service Account to work, you must set `USE_SERVICE_ACCOUNTS` = "True" in config file or environment variables.
>**NOTE**: Using Service Accounts is only recommended while uploading to a Team Drive.

### *1. Generate Service Accounts.* [What is Service Account?](https://cloud.google.com/iam/docs/service-accounts)
*Let us create only the Service Accounts that we need.*

**Warning**: *Abuse of this feature is not the aim of this project and we do **NOT** recommend that you make a lot of projects, just one project and 100 SAs allow you plenty of use, its also possible that over abuse might get your projects banned by Google.*

>**NOTE**: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```
>**NOTE:** 1 Service Account can upload/copy around 750 GB a day, 1 project can make 100 Service Accounts so you can upload 75 TB a day or clone 2 TB from each file creator (uploader email).

#### ⬇️ Two methods to create service accounts
**Choose one of these methods*

##### *1. Create Service Accounts in existed Project (Recommended Method)*
- *List your projects ids*
```
python3 gen_sa_accounts.py --list-projects
```
- *Enable services automatically by this command*
```
python3 gen_sa_accounts.py --enable-services $PROJECTID
```
- *Create Sevice Accounts to current project*
```
python3 gen_sa_accounts.py --create-sas $PROJECTID
```
- *Download Sevice Accounts as accounts folder*
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```

##### *2. Create Service Accounts in New Project*
```
python3 gen_sa_accounts.py --quick-setup 1 --new-only
```
*A folder named accounts will be created which will contain keys for the Service Accounts.*

### *2. Add Service Accounts*

#### *Two methods to add service accounts*
*Choose one of these methods*

##### *1. Add Them To Google Group then to Team Drive (Recommended)*
- *Mount accounts folder*
```
cd accounts
```
- *Grab emails form all accounts to emails.txt file that would be created in accounts folder*
- `For Windows using PowerShell`
```
$emails = Get-ChildItem .\**.json |Get-Content -Raw |ConvertFrom-Json |Select -ExpandProperty client_email >>emails.txt
```
- `For Linux`
```
grep -oPh '"client_email": "\K[^"]+' *.json > emails.txt
```
- *Unmount acounts folder*
```
cd ..
```
*Then add emails from emails.txt to Google Group, after that add this Google Group to your Shared Drive and promote it to manager and delete email.txt file from accounts folder*

##### *2. Add Them To Team Drive Directly*
- *Run:*
```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```

------

### ⬇️ Generate Database

***1. Using Railway***
- *Go to [railway](https://railway.app) and create account*
- *Start new project*
- *Press on `Provision PostgreSQL`*
- *After creating database press on `PostgresSQL`*
- *Go to `Connect` column*
- *Copy `Postgres Connection URL` and fill `DATABASE_URL` variable with it*

***2. Using Heroku PostgreSQL***
<p><a href="https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1"> <img src="https://img.shields.io/badge/See%20Dev.to-black?style=for-the-badge&logo=dev.to" width="160""/></a></p>

***3. Using ElephantSQL***
- *Go to [elephantsql](https://elephantsql.com) and create account*
- *Hit `Create New Instance`*
- *Follow the further instructions in the screen*
- *Hit `Select Region`*
- *Hit `Review`*
- *Hit `Create instance`*
- *Select your database name*
- *Copy your database url, and fill `DATABASE_URL` variable with it*

------

# Extras

## ⬇️ Bot commands to be set in [@BotFather](https://t.me/BotFather)

```
mirror - or /m Mirror
zipmirror - or /zm Mirror and upload as zip
unzipmirror - or /uzm Mirror and extract files
qbmirror - or /qm Mirror torrent using qBittorrent
qbzipmirror - or /qzm Mirror torrent and upload as zip using qb
qbunzipmirror - or /quzm Mirror torrent and extract files using qb
leech - or /l Leech
zipleech - or /zl Leech and upload as zip
unzipleech - or /uzl Leech and extract files
qbleech - or /ql Leech torrent using qBittorrent
qbzipleech - or /qzl Leech torrent and upload as zip using qb
qbunzipleech - or /quzl Leech torrent and extract using qb
clone - Copy file/folder to Drive
count - Count file/folder of Drive
ytdl - or /y Mirror yt-dlp supported link
ytdlzip - or /yz Mirror yt-dlp supported link as zip
ytdlleech - or /yl Leech through yt-dlp supported link
ytdlzipleech - or /yzl Leech yt-dlp support link as zip
leechset - Leech settings
setthumb - Set thumbnail
status - Get Mirror Status message
btsel - select files from torrent
rsslist - or /rl List all subscribed rss feed info
rssget - or /rg Get specific No. of links from specific rss feed
rsssub - or /rs Subscribe new rss feed
rssunsub - or /rus Unsubscribe rss feed by title
rssset - or /rst Rss Settings
list - Search files in Drive
search - Search for torrents with API
cancel - Cancel a task
cancelall - Cancel all tasks
del - Delete file/folder from Drive
log - Get the Bot Log
shell - Run commands in Shell
restart - Restart the Bot
stats - Bot Usage Stats
ping - Ping the Bot
help - All cmds with description
```
------
## ⬇️ UPSTREAM REPO (Recommended)

- *`UPSTREAM_REPO` variable can be used for edit/add any file in repository.*
- *You can add private/public repository link to grab/overwrite all files from it.*
- *You can skip adding the privates files like token.pickle or accounts folder before deploying, also no need to add variables direct links except **config.env**, simply fill `UPSTREAM_REPO` private one in case you want to grab all files including private files.*
- *If you added private files while deploying and you have added private `UPSTREAM_REPO` and your private files in this private repository, so your private files will be overwritten from this repository. Also if you are using URL variables like `TOKEN_PICKLE_URL` then all files from those variables will override the private files that added before deploying or from private `UPSTREAM_REPO`.*
- *If you filled `UPSTREAM_REPO` with the official repository link, then be carefull incase any change in requirements.txt your bot will not start after restart. In this case you need to deploy again with updated code to install the new requirements or simply by changing the `UPSTREAM_REPO` to you fork link with that old updates.*
- *In case you you filled `UPSTREAM_REPO` with your fork link be carefull also if you fetched the commits from the official repository.*
- *The changes in your `UPSTREAM_REPO` will take affect only after restart.*
- *`UPSTREAM_BRANCH` don't ever fill heroku here.*
------
## ⬇️ Bittorrent Seed
- *Add `d:ratio:time` perfix along with leech or mirror cmd.*
- *Using `d` perfix alone will lead to use global options for aria2c or qbittorrent.*

### ⬇️ Qbittorrent
- *Global options: `MaxRatio` and `GlobalMaxSeedingMinutes` in qbittorrent.conf, `-1` means no limit, but you can cancel manually.*
  - ***NOTE***: *Don't change `MaxRatioAction`*.

### ⬇️ Aria2c
- *Global options: `--seed-ratio` (0 means no limit) and `--seed-time` (0 means no seed) in aria.sh.*
------

## ⬇️ Getting Google OAuth API credential file
- *Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)*
- *Go to the OAuth Consent tab, fill it, and save.*
- *Go to the Credentials tab and click Create Credentials -> OAuth Client ID*
- *Choose Desktop and Create.*
- *Use the download button to download your credentials.*
- *Move that file to the root of mirrorbot, and rename it to **credentials.json***
- *Visit [Google API page](https://console.developers.google.com/apis/library)*
- *Search for Drive and enable it if it is disabled*
- *Finally, run the script to generate **token.pickle** file for Google Drive:*
```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```
-----

### ⬇️ Deploying

- Start Docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
docker build . --rm --force-rm --compress --no-cache=true --pull --file Dockerfile -t mirrorbot
```
- Run the image:
```
sudo docker run mirrorbot
```

----

### ⬇️ Deploying on VPS Using docker-compose

***NOTE***: *If you want to use port other than 80, change it in [docker-compose.yml](https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/blob/majorupdate/docker-compose.yml) also.*

```
sudo apt install docker-compose
```
- Build and run Docker image:
```
sudo docker-compose up
```
- After editing files with nano for example (nano start.sh):
```
sudo docker-compose up --build
```
- To stop the image:
```
sudo docker-compose stop
```
- To run the image:
```
sudo docker-compose start
```
-----
- ***Tutorial video from Tortoolkit repo for docker-compose and checking ports***
<p><a href="https://youtu.be/c8_TU1sPK08"> <img src="https://img.shields.io/badge/See%20Video-black?style=for-the-badge&logo=YouTube" width="160""/></a></p>

------

## ⬇️ Deploying on Heroku 

### ***Note : Use Only this method for Heroku deployments***
<p><a href="https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/tree/heroku"> <img src="https://img.shields.io/badge/Deploy%20Guide-blueviolet?style=for-the-badge&logo=heroku" width="170""/></a></p>

-----
## ***Deploying on Heroku with heroku-cli and Goorm IDE***
<p><a href="https://telegra.ph/How-to-Deploy-a-Mirror-Bot-to-Heroku-with-CLI-05-06"> <img src="https://img.shields.io/badge/see%20on%20telegraph-grey?style=for-the-badge" width="190""/></a></p>

-----
## ⬇️ **Using Service Accounts for uploading to avoid user rate limit**
*For Service Account to work, you must set **USE_SERVICE_ACCOUNTS=**"True" in config file or environment variables, 
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) for the scripts.
**NOTE**: Using Service Accounts is only recommended while uploading to a Team Drive.*

## ⬇️ **Generate Service Accounts.** [What is Service Account](https://cloud.google.com/iam/docs/service-accounts)
<details>
    <summary><b>Click Here For More Details</b></summary>

Let us create only the Service Accounts that we need. 
**Warning**: abuse of this feature is not the aim of this project and we do **NOT** recommend that you make a lot of projects, just one project and 100 SAs allow you plenty of use, its also possible that over abuse might get your projects banned by Google. 

**NOTE:** 1 Service Account can copy around 750gb a day, 1 project can make 100 Service Accounts so that's 75tb a day, for most users this should easily suffice.
```
python3 gen_sa_accounts.py --quick-setup 1 --new-only
```
A folder named accounts will be created which will contain keys for the Service Accounts.

Or you can create Service Accounts to current project, no need to create new one

- List your projects ids
```
python3 gen_sa_accounts.py --list-projects
```
- Enable services automatically by this command
```
python3 gen_sa_accounts.py --enable-services $PROJECTID
```
- Create Sevice Accounts to current project
```
python3 gen_sa_accounts.py --create-sas $PROJECTID
```
- Download Sevice Accounts as accounts folder
```
python3 gen_sa_accounts.py --download-keys $PROJECTID
```
If you want to add Service Accounts to Google Group, follow these steps

- Mount accounts folder
```
cd accounts
```
- Grab emails form all accounts to emails.txt file that would be created in accounts folder
```
grep -oPh '"client_email": "\K[^"]+' *.json > emails.txt
```
- Unmount acounts folder
```
cd -
```
Then add emails from emails.txt to Google Group, after that add Google Group to your Shared Drive and promote it to manager.

**NOTE**: If you have created SAs in past from this script, you can also just re download the keys by running:
```
python3 gen_sa_accounts.py --download-keys project_id
```

</details>

## ⬇️ Add all the Service Accounts to the Team Drive
- Run:
```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```
-----

-----
## ⬇️ Youtube-dl authentication using [.netrc](https://github.com/Spark-X-Cloud/SparkXcloud-Gdrive-MirrorBot/blob/master/.netrc) file
*For using your premium accounts in Youtube-dl or for protected Index Links, edit the netrc file according to following format:*
```
machine host login username password my_youtube_password
```
*For Index Link with only password without username, even http auth will not work, so this is the solution.*
```
machine example.workers.dev password index_password
```
-----
*Where host is the name of extractor (eg. Youtube, Twitch). Multiple accounts of different hosts can be added each separated by a new line.*

