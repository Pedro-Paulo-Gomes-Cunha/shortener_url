
from src.core.Domain.models.URL import URL, db

class UrlRepository():

 """   def __init__(self):
        super().__init__(Url)
"""

def find_by_short_url (short_url):
    return URL.query.filter_by(short_url=short_url).first()

def GetAll():
    return URL.query.all()
    #return Urls_objetos


def GetById(id):
    Url_objeto = URL.query.filter_by(id=id).first()
    return Url_objeto


def Save(UrlData: URL):
    try:
        db.session.add(UrlData)
        db.session.commit()
        return "sucess"
    except Exception:
        db.session.rollback()
        return "url save error: duplicate url"


def Update(UrlData: URL):
    try:
        data= URL.query.filter_by(id=UrlData.id).first()
        if not data:
            return  'url not found 404'
        
        data.id=UrlData.id
        data.short_url=UrlData.short_url
        data.original_url=UrlData.original_url
       
        db.session.add(data)
        db.session.commit()
        return  "sucess"
    except Exception as e:
        db.session.rollback()
    return "update error: "+str(e)

def Delete(id):
    Url_objeto = URL.query.filter_by(id=id).first()
    try:
        db.session.delete(Url_objeto)
        db.session.commit()
        return  "sucess"
    except Exception as e:
        db.session.rollback()
        return "Delete error: "+str(e)
