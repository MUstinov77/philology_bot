from aiogram.enums import ContentType


async def func_by_message_type(
        message,
        bot,
        chat_id
):
    content_type = message.content_type
    try:
        if content_type == ContentType.TEXT:
            await bot.send_message(chat_id, text=message.text)
        elif content_type == ContentType.PHOTO:
            await bot.send_photo(chat_id, photo=message.photo[-1].file_id)
        elif content_type == ContentType.DOCUMENT:
            await bot.send_document(
                chat_id=chat_id,
                document=message.document.file_id
            )
        elif content_type == ContentType.VIDEO:
            await bot.send_video(
                chat_id=chat_id,
                video=message.video.file_id
            )
        elif content_type == ContentType.VOICE:
            await bot.send_voice(
                chat_id=chat_id,
                voice=message.voice
            )
        elif content_type == ContentType.STICKER:
            await bot.send_sticker(
                chat_id=chat_id,
                sticker=message.sticker.file_id
            )
    except Exception as e:
        print(e)