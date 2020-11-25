import discord
import logging
import re

from classes.quote import Quote
from classes.message import Message

class Client(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!quo help'))
        self.quote = Quote()
        self.message = Message()
        logger = logging.getLogger('discord')
        logger.setLevel(logging.WARNING)
        logging.basicConfig(
            format='%(asctime)s, %(levelname)s -> %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='running.log',
            filemode='a', level=logging.INFO
        )
    def __del__(self):
        self.quote.closeConnection() 

    async def on_message(self, message):
        content = message.content
        author = message.author.name

        if content == '!quo':
            await message.channel.send(embed=self.message.help())
            return
            
        if content.startswith('!quo '):
            logging.info(
                '%s, %s, %s: %s',
                message.guild.name, message.channel.name, message.author.name, content
            )
            if content[5:9] == 'help' and len(content) == 9:
                logging.info('Help Message')
                await message.channel.send(embed=self.message.help())
                return
            elif content[5:9] == 'add ':
                logging.info('Add Quote')
                info = re.findall('"[^"]*"', content[9:])
                if(len(info) != 2):
                    logging.error('Error, wrong usage')
                    await message.channel.send(embed=self.message.addError())
                    return
                title = info[0]
                quote = info[1]
                self.quote.addQuote(title[1:len(title)-1], quote[1:len(quote)-1], author)
                await message.channel.send(embed=self.message.addSuccess())
            elif content[5:11] == 'random' and len(content) == 11:
                logging.info('Display Random Quote')
                quote = self.quote.getRandomQuote()
                if(quote == None):
                    logging.error('Error, there are no quotes on db')
                    await message.channel.send(embed=self.message.quoteError())
                    return
                await self.sendQuote(message, quote[1], quote[2], quote[3])
            else:
                await message.channel.send(embed=self.message.genericError())

    async def sendQuote(self, message, title, text, author):
        quote = "```\n"
        quote += text
        quote += "```"
        await message.channel.send(embed=self.message.quote(title, quote, author))