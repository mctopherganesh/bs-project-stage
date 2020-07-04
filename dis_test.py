import discord
from discord.ext import commands
import os
import dis_helper

TOKEN = os.environ.get('discord_token')

client = commands.Bot(command_prefix = '$')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! (round(client.latency*1000))ms')


# https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
@client.command()
async def bs(ctx, arg):
    db_name, table_name = dis_helper.db_and_table_name_setter('test.db','blood_sugar')
    bs = arg.strip()
    print(args)
    print(type(bs))
    # TODO: try/asser that bs is an integer
    dis_helper.create_table_for_bs(db_name, table_name)
    # dtstmp = dis_helper.return_date()
    new_row = dis_helper.reads_in_time_and_data(bs)
    dis_helper.data_entry(new_row,db_name,table_name)
    
    await ctx.send('new row written in ' + str(table_name) + ' table.')


@client.command()
async def food(ctx, *, arg):
    db_name, table_name = dis_helper.db_and_table_name_setter('test_0.db','foods')
    

    dis_helper.create_table_for_food(db_name, table_name)

    new_row = dis_helper.reads_in_time_and_data_for_food(arg)

    dis_helper.data_entry(new_row, db_name, table_name)

    await ctx.send('new row written in the ' + str(table_name) + ' table.')


@client.command()
async def pic(ctx):
    await ctx.send(file=discord.File('bar_test_png.png'))



    
    
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)

