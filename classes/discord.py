import discord
import logging
import re

from classes.quote import Quote
from classes.message import Message


class Client(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = kwargs['db']
        self.u = kwargs['u']
        self.passw = kwargs['passw']
        self.host = kwargs['host']
        self.port = kwargs['port']
        self.quote = Quote(
            self.db, self.u, self.passw, self.host, self.port
        )
        self.message = Message()

    def __del__(self):
        self.quote.closeConnection()

    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!quo help'))
        logger = logging.getLogger('discord')
        logger.setLevel(logging.WARNING)
        logging.basicConfig(
            format='%(asctime)s, %(levelname)s -> %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='running.log',
            filemode='a', level=logging.INFO
        )

    async def on_message(self, message):
        content = message.content
        author = message.author.name
        quote = None
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
                info = re.findall('"[^"]*"', content[9:])
                info_len = len(info)
                if info_len not in [2, 3]:
                    logging.error('Error, wrong arguments')
                    await message.channel.send(embed=self.message.addError())
                    return
                title = info[0]
                quote = info[1]
                if info_len == 3:
                    author = info[2]
                    author = author[1:len(author)-1]
                logging.info('Add Quote')
                duplicated = self.quote.addQuote(title[1:len(title)-1], quote[1:len(quote)-1], author)
                if duplicated:
                    logging.error('Error, duplicated key')
                    await message.channel.send(embed=self.message.duplicateKeyError())
                    return
                await message.channel.send(embed=self.message.addSuccess())
            elif content[5:11] == 'random':
                if len(content) == 11:
                    quote = self.quote.getRandomQuote()
                    if quote == None:
                        logging.error('Error, there are no quotes on db')
                        await message.channel.send(embed=self.message.quoteError())
                        return
                    logging.info('Display Random Quote')
                else:
                    splitted = content[5:].split(' ', 1)
                    if len(splitted) != 2:
                        logging.error('Error, wrong arguments')
                        await message.channel.send(embed=self.message.randomError())
                        return
                    author = splitted[1]
                    author = author[1:len(author)-1]
                    quote = self.quote.getRandomQuoteFromUser(author)
                    if quote == None:
                        logging.error('Error, {author} has no quotes')
                        await message.channel.send(embed=self.message.authorQuoteError(author))
                        return
                    logging.info(f'Display Random Quote for User {author}')
                await self.sendQuote(message, quote[2], quote[3], quote[4])
            else:
                await message.channel.send(embed=self.message.genericError())

    async def sendQuote(self, message, title, text, author):
        quote = "```\n"
        quote += text
        quote += "```"
        await message.channel.send(embed=self.message.quote(title, quote, author))
