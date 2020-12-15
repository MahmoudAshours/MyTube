import pytube
from selenium import webdriver
from bs4 import BeautifulSoup

print("0:If you want to download list of youtube videos. (from txt file) \n")
print("1:If you want to download Youtube playlist.\n")
dec = input()


def from_playlist():
    url = input("Insert youtube playlist link : ")
    options = webdriver.ChromeOptions()
    options.add_argument('-incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(f"{url}")
    content = driver.page_source
    links = []
    soup = BeautifulSoup(content, features="html.parser")

    for a in soup.findAll('a', attrs={
        'class': 'yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer'}):
        links.append(f'youtube.com{a["href"]}')
    print(links)
    for link in links:
        url = link
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        if video is None: continue
        print(f"Downloading {video.title} . . .")
        video.download()


def from_txt():
    with open('links.txt') as f:
        lines = f.readlines()
    for line in lines:
        url = line
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        print(f"Downloading {video.title} . . .")
        video.download()


if dec == 0:
    from_txt()
else:
    from_playlist()
