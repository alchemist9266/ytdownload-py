#made by Leak#5749
#lmao

from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil

#ui yes
print("||======================================||")
print("[+] ytdownload-py - Made by Leak#5749")
print("[+] Github : https://github.com/leak37")
print("||======================================||")

vidlink = input("[>] Video Link : ")

print('\n')
print("[+] Download Logs : ")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([vidlink])