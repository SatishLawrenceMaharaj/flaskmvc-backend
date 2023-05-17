from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import ( 
    create_chat,
    get_all_chats,
    get_all_chats_json,
    get_chat_by_id,
    get_chat_by_id_json,
    get_chat_by_name,
    get_chat_by_name_json
)

chat_views = Blueprint('chat_views', __name__, template_folder='../templates')

@chat_views.route('/api/chats', methods=['GET'])
def get_chats():
    chats = get_all_chats_json()
    if chats:
        return render_template('chats.html', chats=chats)
    return render_template('chats.html', chats=[])
        
@chat_views.route('/api/chats/all', methods=['GET'])
def get_chats_action():
    chats = get_all_chats_json()
    if not chats:
        return jsonify([]), 200
    return jsonify(chats)

@chat_views.route("/api/chat/create", methods=["POST"])
def create_chat_action():
    data = request.json
    if not data["chat_id"] or not data["chat_name"] or not data["chat_type"] or not data["chat_description"] or not data["chat_image"] or not data["chat_creator_id"]:
        return jsonify({"message": "Please fill out all fields"}), 400
    chat = get_chat_by_id(data["chat_id"])
    if chat:
        return jsonify({"message": "Chat already exists"}), 400
    chat = get_chat_by_name(data["chat_name"])
    if chat:
        return jsonify({"message": "Chat already exists"}), 400
    new_chat = create_chat(data["chat_id"], data["chat_name"], data["chat_type"], data["chat_description"], data["chat_image"], data["chat_creator_id"])
    if new_chat:
        return jsonify(new_chat.to_json()), 201
    return jsonify({"message": "Chat could not be created"}), 400
