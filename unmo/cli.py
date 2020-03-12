from .unmo import Unmo
import discord
import os
import traceback



def _build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)


def main():
    TOKEN = os.environ['DISCORD_BOT_TOKEN']
    print(TOKEN)
    client = discord.Client()
    @client.event
    async def on_ready():
        '''
        起動時に呼ばれるメソッド
        '''
        print('-----Logged in info-----')
        print(client.user.name)
        print(client.user.id)
        print('------------------------')

    @client.event
    async def on_message(message):
        # メッセージ送信者がBotだった場合は無視する
        #if message.author.bot:
            #return
        #if client.user in message.mentions:
        proto = Unmo('proto')
        text = message.content
        if not text:
            message.channel.send(f'{message.author.mention} なぁに？')
            return
        response = proto.dialogue(text)
        await message.channel.send(f'{message.author.mention} '+response)
        proto.save()
    client.run(TOKEN)
