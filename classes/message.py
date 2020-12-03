import discord


class Message:
    def help(self):
        return discord.Embed(
            title='Quote Bot - Help',
            description='**Usage**\n`!quo <command> "arguments" [optional arguments]`\n\n**Available Commands**\n`!quo help` - Print help\n`!quo add "title" "quote" "[author]"` - Add a quote\n`!quo random "[author]"` - Print a random quote from all/specific author.\n',
            color=discord.Color.blue()
        )

    def addSuccess(self):
        return discord.Embed(
            title='Success: Add Quote',
            description='Your quote was successfully added!',
            color=discord.Color.blue()
        )

    def quote(self, title, quote, author):
        embed = discord.Embed(
            title=title,
            description=quote,
            color=discord.Color.blue()
        )
        embed.set_footer(text=author)
        return embed

    def addError(self):
        return discord.Embed(
            title='Error: Add Quote',
            description='Sorry, that\'s not how to use the **add** command :(\nUsage: `!quo add "[title]" "[quote]" "[author (optional)]"`',
            color=discord.Color.red()
        )
    def duplicateKeyError(self):
        return discord.Embed(
            title='Error: Duplicated Poem',
            description='Sorry, that poem already exists. :(',
            color=discord.Color.red()
         )
    def randomError(self):
        return discord.Embed(
            title='Error: Random Quote',
            description='Sorry, that\'s not how to use the **random** command :(\nUsage: `!quo random "[author (optional)]"`',
            color=discord.Color.red()
        )

    def genericError(self):
        return discord.Embed(
            title='Ups',
            description='Sorry, I don\'t recognize that command :(\n Write **!quo help** to see the instructions.',
            color=discord.Color.red()
        )

    def quoteError(self):
        return discord.Embed(
            title='Error: Display Quote',
            description='Sorry, I have no quotes to display. Do you know one :)?\nUsage: `!quo add "[title]" "[quote]" "[author (optional)]"`',
            color=discord.Color.red()
        )

    def authorQuoteError(self, author):
        return discord.Embed(
            title='Error: Display Quote',
            description=f'Sorry, I have no quotes from **{author}**. Do you know one :)?\nUsage: `!quo add "[title]" "[quote]" "[author (optional)]"`',
            color=discord.Color.red()
        )
