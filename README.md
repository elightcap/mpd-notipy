# MPD-NotiPY

## A python rewrite of [XXioA's](https://github.com/XXiaoA) [mpd-notify](https://github.com/XXiaoA/dotfiles/blob/main/scripts/mpd-notify)

The main motivation for this was to add a method to get cover art for songs that don't have it embedded in the metadata.

###Installation

1. Clone this repository `git clone https://github.com/elightcap/mpd-notipy && cd mpd-notipy`
2. Copy the sample.env to .env `cp sample.env .env`
3. Fill in the missing values in .env. they are as follows:
    - HOST - ip address of the mpd server (or localhost)
    - PORT - port that mpd is running on
    - APIKEY - lastfm api key (can be obtained [here](https://www.last.fm/login?next=%2Fapi%2Faccount%2Fcreate%3F_pjax%3D%2523content))
    - TEMPCOVER - location where cover art is stored & read (can be anywhere that can be read, i use /tmp/cover.png)
    - MUSICDIR - root directory of music stuff (for example /home/elightcap/Music)
    - PLACEHOLDER - path to any picture. this is used if the metadata doesnt have a picture, and it cannot be found on LastFM.
4. Install requirements `pip install -r requirements.txt`
5. I have this launch with i3, so make the file executable `chmod +x mpd-notify.py`
6. I only know my i3 stuff, so i just have `exec --no-startup-id /path/to/script/mpd-notify.py`
