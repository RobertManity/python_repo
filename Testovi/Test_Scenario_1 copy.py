from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from google.colab import drive
drive.mount('/content/gdrive')
import csv
path_to_file = '/content/gdrive/MyDrive/stock_prices.csv'
open_file = open(path_to_file, 'r')
content = csv.reader(open_file, delimiter=",")
for line in content:
    print(line)
open_file.close()