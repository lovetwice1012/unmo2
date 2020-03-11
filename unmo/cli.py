from .unmo import Unmo
import discord

TOKEN = 'Njg3MjYyNTE2MzA4MzQ0ODM0.XmjQKQ.d2kd8QbSjRKwJzfCCxBU1jcDFAs'
client = discord.Client()

def _build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)


def main():
    @client.event
    async def on_message(message):
        # メッセージ送信者がBotだった場合は無視する
        if message.author.bot:
            return
        proto = Unmo('proto')
        text = message.content
        if not text:
            message.reply("なぁに？")
            return
        response = proto.dialogue(text)
        message.reply(response)
        proto.save()
    client.run("Njg3MjYyNTE2MzA4MzQ0ODM0.XmjQKQ.d2kd8QbSjRKwJzfCCxBU1jcDFAs")
