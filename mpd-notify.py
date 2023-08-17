#!/usr/bin/python3

import requests 
import shutil
import urllib.parse

from os import system,getenv
from mpd import MPDClient
from dotenv import load_dotenv

load_dotenv()

SERVER = getenv("HOST")
PORT = getenv("PORT")
APIKEY = getenv("APIKEY")
TEMPCOVER = getenv("TEMPCOVER")
MUSICDIR = getenv("MUSICDIR")

client = MPDClient()
client.timeout = 10
client.idletimeout = None

def get_current_song():
    client.connect(SERVER, PORT)
    song_info = client.currentsong()
    file = song_info["file"]
    title = song_info["title"]
    artist = song_info["artist"]
    album = song_info["album"]
    get_album_art(title,artist,album,file)
    i = client.idle()
    client.disconnect()

def get_album_art(title,artist,album,file):
    ffm = system("ffmpeg -i '{dir}/{filename}' {coverfile} -y &> /dev/null".format(dir=MUSICDIR,filename=file,coverfile="/tmp.cover.png"))
    if ffm == 256: 
        print("not found")
        url = "http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={apikey}&artist={artist}&album={album}&format=json".format(apikey=APIKEY,artist=(urllib.parse.quote(artist)), album=(urllib.parse.quote(album)))
        album_info = requests.get(url)
        album_json = album_info.json()
        art_url = album_json["album"]["image"][3]["#text"]
        get_image = requests.get(art_url)
        image_data = get_image.content
        if get_image.status_code == 200:
            f = open("/tmp/cover.png", "wb")
            f.write(image_data)
            f.close()
        else:
            shutil.copyfile('/home/evan/Pictures/music.png','/tmp/cover.png')

    song_note = "{song} - {artist}".format(song=title,artist=artist)
    print(song_note)
    send_notification(song_note)

def send_notification(song_note):
    system("dunstify -a Music --replace=27072 -t 2000 -i {albumcover} '{songinfo}'".format(albumcover="/tmp/cover.png", songinfo=song_note))


while True:
    get_current_song()
