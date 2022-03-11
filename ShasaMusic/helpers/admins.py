from typing import List

from pyrogram.types import Chat

from ShasaMusic.function.admins import get as gett
from ShasaMusic.function.admins import set


async def get_administrators(chat: Chat) -> List[int]:
    if get := gett(chat.id):
        return get
    administrators = await chat.get_members(filter="administrators")
    to_set = [
        administrator.user.id
        for administrator in administrators
        if administrator.can_manage_voice_chats
    ]


    set(chat.id, to_set)
    return await get_administrators(chat)
