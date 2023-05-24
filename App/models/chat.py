from datetime import datetime
from App.database import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(120), nullable=False)
    chat_name = db.Column(db.String(120), nullable=False)
    chat_type = db.Column(db.String(120), nullable=True)
    chat_description = db.Column(db.String(120), nullable=True)
    chat_image = db.Column(db.String, nullable=True)
    chat_created = db.Column(db.DateTime, nullable=True)
    chat_creator_id = db.Column(db.String(120), nullable=True)
    
    def __init__(self, chat_id, chat_name, chat_type, chat_description, chat_image, chat_creator_id):
        self.chat_id = chat_id
        self.chat_name = chat_name
        self.chat_type = chat_type
        self.chat_description = chat_description
        self.chat_image = chat_image
        self.chat_created = datetime.now()
        self.chat_creator_id = chat_creator_id
        
    def to_json(self):
        return {
            'id': self.id,
            'chat_id': self.chat_id,
            'chat_name': self.chat_name,
            'chat_type': self.chat_type,
            'chat_description': self.chat_description,
            'chat_image': self.chat_image,
            'chat_created': self.chat_created,
            'chat_creator_id': self.chat_creator_id
        }
    
    def get_chat_id(self):
        return self.chat_id
    
    def get_chat_name(self):
        return self.chat_name
    
    def get_chat_type(self):
        return self.chat_type
    
    def get_chat_description(self):
        return self.chat_description
    
    def get_chat_image(self):
        return self.chat_image
    
    def get_chat_created(self):
        return self.chat_created
    
    def get_chat_creator_id(self):
        return self.chat_creator_id
    
    def set_chat_id(self, chat_id):
        self.chat_id = chat_id
        
    def set_chat_name(self, chat_name):
        self.chat_name = chat_name
        
    def set_chat_type(self, chat_type):
        self.chat_type = chat_type
        
    def set_chat_description(self, chat_description):
        self.chat_description = chat_description
        
    def set_chat_image(self, chat_image):
        self.chat_image = chat_image
        
    def set_chat_created(self, chat_created):
        self.chat_created = datetime.now()
        
    def set_chat_creator_id(self, chat_creator_id):
        self.chat_creator_id = chat_creator_id
        
    