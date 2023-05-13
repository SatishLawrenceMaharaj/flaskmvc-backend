from App.models import Chat
from App.database import db


def get_all_chats():
    return Chat.query.all()

def get_all_chats_json():
    chats = Chat.query.all()
    if not chats:
        return []
    chats = [chats.to_json() for chat in chats]
    return chats