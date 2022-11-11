import discum
token = input('input a token:')
server_id = input('input the server id:')
channel_id = input('input the channel id:')
msg = input('input the message you want to send')

bot = discum.Client(token=token)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members(server_id,channel_id)
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID, 'has been fetched')

for id in memberslist:
    newDM = bot.createDM([id]).json()["id"] 
    bot.sendMessage(newDM,msg)
