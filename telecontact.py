from selenium import webdriver as wd
import requests
from bs4 import BeautifulSoup as BS

base_url = "http://www.telecontact.ma/trouver/index.php?nxo=moteur&nxs=process&string="
keyword_one = "pharmacie"
middle_url = "&ou="
keyword_two = "el+jadida"
end_url = "&aproximite=&produit="

url = base_url + keyword_one + middle_url + keyword_two + end_url

