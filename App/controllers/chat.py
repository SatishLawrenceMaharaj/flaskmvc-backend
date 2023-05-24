from App.models import Chat
from App.database import db


def get_all_chats():
    chats= Chat.query.all()
    if chats:
        return chats
    return None

def get_all_chats_json():
    chats = get_all_chats()
    if chats:
        return [chat.to_json() for chat in chats]
    return []

def get_chat_by_id(id):
    return Chat.query.get(id)

def get_chat_by_id_json(id):
    return get_chat_by_id(id).to_json()

def get_chat_by_name(name):
    return Chat.query.filter_by(chat_name=name).first()

def get_chat_by_name_json(name):
    return get_chat_by_name(name).to_json()

def create_chat(chat_id, chat_name, chat_type, chat_description, chat_image, chat_creator_id):
    chat = Chat(chat_id, chat_name, chat_type, chat_description, chat_image, chat_creator_id)
    db.session.add(chat)
    db.session.commit()
    return chat

def delete_chat(id):
    chat = get_chat_by_id(id)
    if chat:
        db.session.delete(chat)
        db.session.commit()
        return True
    return None