from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import ( 
    get_all_chats,
    get_all_chats_json,
)

chat_views = Blueprint('chat_views', __name__, template_folder='../templates')

@chat_views.route('/api/chats/all', methods=['GET'])
def get_chats_action():
    chats = get_all_chats_json()
    if not chats:
        return jsonify(["empty chat list"]), 200
    return jsonify(chats)