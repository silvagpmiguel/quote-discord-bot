import discord

class Message:
    def help(self):
        return discord.Embed(
            title = 'Quote Bot - Help',
            description = '**Usage**\n`!quo <command> [arguments]`\n\n**Available Commands**\n- `!quo help` - Print help\n- `!quo add "[title]" "[quote]"` - Add a quote\n- `!quo random` - Print random quote\n',
            color = discord.Color.blue()
        )

    def addSuccess(self):
        return discord.Embed(
            title = 'Success: Add Quote',
            description = 'Your quote was successfully added!',
            color = discord.Color.blue()
        )

    def quote(self, title, quote, author):
        embed = discord.Embed(
            title = title,
            description = quote,
            color = discord.Color.blue()
        )
        embed.set_footer(text=author)
        return embed

    def addError(self):
        return discord.Embed(
            title = 'Error: Add Quote',
            description = 'Sorry, that\'s not how to use the add command.\nUsage: `!quo add "[title]" "[quote]"`',
            color = discord.Color.red()
        )

    def genericError(self):
        return discord.Embed(
            title = 'Ups',
            description = 'Sorry, something went wrong.\n Write **!quo help** to see how to use me!',
            color = discord.Color.red()
        )

    def quoteError(self):
        return discord.Embed(
            title = 'Error: Display Quote',
            description = 'Sorry, I have no quotes to display. Try to add one :)\nUsage: `!quo add "[title]" "[quote]"`',
            color = discord.Color.red()
        )