#!/usr/bin/python3
# coding=utf-8

__Author__    = 'dafidxcode'
__Github__ = 'https://github.con/dafidxcode'

import os,time,requests,urllib.request
from bs4 import BeautifulSoup as bs

try:import bs4
except ImportError:os.system('pip install bs4')
try:import requests
except ImportError:os.system('pip install requests')

class Downloader:
	def __init__(self, Url):
		print(' ## DOWNLOADER TIKTOK VIDEOS WITH BS4 ##')
		self.Url = Url
		self.Path = '/sdcard/Download'
		self.Num = 0
		self.Tiktok()
	def Tiktok(self):
		url = 'https://ttsave.app/download'
		headers = { 'content-type': 'application/json', }
		json_data = { 'query': self.Url, }
		tete = requests.post(url, headers=headers, json=json_data)
		x = bs(tete.text, 'html.parser')
		##--------- Scrapping via Beautiful Soup
		Username = x.find(class_="font-extrabold text-blue-400 text-xl mb-2").text
		Description = x.find(class_="text-gray-600 px-2 text-center break-all w-3/4 oneliner").text
		Title = x.find("div", class_="flex flex-row items-center justify-center").text
		VideoLink = x.find(class_="flex flex-col text-center w-3/4 md:w-1/2").find_all("a", href=True)
		
		for z in VideoLink:
			self.Num += 1
			if self.Num == 1:no_watermark = z['href']
			elif self.Num == 2:watermark = z['href']
			elif self.Num == 3:audio = z['href']
			elif self.Num == 4:profile = z['href']
			elif self.Num == 5:thumbnail = z['href']
			
		##---------- Trying to download video file
		print(' [1] Download Video [ No Watermark ]\n [2] Download Video [ Watermark ]\n [3] Download Audio [ Mp3 ]\n [4] Download Photo [ Profile ]\n [5] Download Thumbnail [ Image ]')
		Select = input('   └─> ')
		if Select in ("1","a"):
			File = self.Path + '/' + Username + '.mp4'
			urllib.request.urlretrieve(no_watermark, File)
		elif Select in ("2","b"):
			File = self.Path + '/' + Username + '.mp4'
			urllib.request.urlretrieve(watermark, File)
		elif Select in ("3","c"):
			File = self.Path + '/' + Username + '.mp3'
			urllib.request.urlretrieve(audio, File)
		elif Select in ("4","d"):
			File = self.Path + '/' + Username + '.jpg'
			urllib.request.urlretrieve(profile, File)
		elif Select in ("5","e"):
			File = self.Path + '/' + Username + '.jpg'
			urllib.request.urlretrieve(thumbnail, File)
		else:
			print('Gajelas Lu Ajg!')
			exit()
			
		print('Download Succesfullly!')
		print(f'Username : {Username}\nDeskripsi : {Description}\nSaved to : {File}')
		time.sleep(2)
		exit()
		
if __name__ == "__ma%s"%('in__'):
	print('Submit Link Tiktok Videos Here')
	Url = input('└─> ')
	Downloader(Url)