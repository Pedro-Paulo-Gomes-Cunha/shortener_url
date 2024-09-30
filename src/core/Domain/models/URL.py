from src.config.extensions import db
from sqlalchemy.orm import Mapped, relationship, backref

class URL(db.Model):
  __tablename__ = "urls"
  id = db.Column(db.Integer, primary_key=True) 
  original_url = db.Column(db.String(512),  unique=True, nullable=False)
  short_url = db.Column(db.String(8), unique=True, nullable=False)
  short_url_link = db.Column(db.String(200),  nullable=True)


  def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url 

  def to_json(self):
    return {"id": self.id, "original_url": self.original_url, "short_url": self.short_url}
  
  def to_json_shotUrl(self):
       return { "short_url": self.short_url,  "short_url_link": self.short_url_link}



  
