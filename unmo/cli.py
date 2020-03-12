from .unmo import Unmo
import discord



def _build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}:{responder}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)


def main():
    TOKEN = 'Njg3MjYyNTE2MzA4MzQ0ODM0.XmmZ2w.wEJLBCnCigvDmFVJqtr10z7EV9E'
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
    client.run(TOKEN)
