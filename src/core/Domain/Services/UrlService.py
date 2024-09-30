
import random
import string

from flask import request
from src.core.Infra.Repositories.UrlRepository import *
from src.core.Infra.Repositories.UrlRepository import UrlRepository

class UrlService:
    def __init__(self):
        self.repository = UrlRepository()

@staticmethod
def find_all():
    return GetAll()

def find_ById(id):
    return GetById(id)

def Save_Url(UrlData: URL):
    try:
        UrlData.short_url = generate_short_url() 
        url_ = request.url
        print(url_)
        UrlData.short_url_link= url_+UrlData.short_url;
        Save(UrlData)
        return UrlData
    except Exception as e:
        return "duplicate url" +str(e)


def Update_(UrlData: URL):
    try:
        UrlData.short_url = generate_short_url() 
        return Update(UrlData)
    except Exception as e:
        return "update Error : "+str(e)

def Delete_(id):
    try:
        return Delete(id)
    except Exception as e:
        return "delete Error : "+str(e)
    
def find_by_short_url_ (short_url):
    return find_by_short_url(short_url)

def generate_short_url(num_chars=8):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(num_chars)) 
