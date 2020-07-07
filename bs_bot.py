import os
import pytz
import discord
import pg_helper
import datetime
import data_transformer
from discord.ext import commands

def get_the_time():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    cst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
    return cst_now.strftime("%Y-%m-%d %H:%M:%S")


TOKEN = os.environ.get('discord_token')

client = commands.Bot(command_prefix = '.')

@client.command()
async def test(ctx):
    await ctx.send('testies testies one two three?')



@client.command()
async def bs(ctx, arg):
    
    datestamp = get_the_time()
    bs = arg.strip()
    pg_helper.enter_bs_row(bs,datestamp)
    await ctx.send('new row written!\n' + str(pg_helper.return_last_five()))
    

#######################  was working here ############################
    



# https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
# @client.command()
# async def bs(ctx, arg):
#     db_name, table_name = dis_helper.db_and_table_name_setter('test.db','blood_sugar')
#     bs = arg.strip()
#     print(args)
#     print(type(bs))
#     # TODO: try/asser that bs is an integer
#     dis_helper.create_table_for_bs(db_name, table_name)
#     # dtstmp = dis_helper.return_date()
#     new_row = dis_helper.reads_in_time_and_data(bs)
#     dis_helper.data_entry(new_row,db_name,table_name)
    
#     await ctx.send('new row written in ' + str(table_name) + ' table.')


# @client.command()
# async def food(ctx, *, arg):
#     db_name, table_name = dis_helper.db_and_table_name_setter('test_0.db','foods')
    

#     dis_helper.create_table_for_food(db_name, table_name)

#     new_row = dis_helper.reads_in_time_and_data_for_food(arg)

#     dis_helper.data_entry(new_row, db_name, table_name)

#     await ctx.send('new row written in the ' + str(table_name) + ' table.')


# @client.command()
# async def pic(ctx):
#     await ctx.send(file=discord.File('bar_test_png.png'))



    
    
    

@client.event
async def on_ready():
    print('Logged in as', flush=True)
    print(client.user.name, flush=True)
    print(client.user.id, flush=True)
    print('------', flush=True)

#pg_helper.drop_old_table()
#pg_helper.create_table()
#pg_helper.load_csv_data()
#pg_helper.return_table_data()
#data_transformer.transform_data()


client.run(TOKEN)

