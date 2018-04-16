import argparse
from reader import page_downloader

parser = argparse.ArgumentParser()
parser.parse_args()

page = page_downloader("https://demo.gurisomali.com")
if page is None:
    print("nothing to display")
else:
    print(page)




