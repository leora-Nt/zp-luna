# Copyright (C) 2022 szsupunma
# Copyright (C) 2021 @szlunabot

# This file is part of @szlunabot (Telegram Bot)

from luna.mongo import urllockdb as lockurl


def add_chat(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if stark:
        return False
    else:
        lockurl.insert_one({"chat_id": chat_id})
        return True


def remove_chat(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        lockurl.delete_one({"chat_id": chat_id})
        return True


def get_all_chats():
    r = list(lockurl.find())
    if r:
        return r
    else:
        return False


def get_session(chat_id):
    stark = lockurl.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        return stark
