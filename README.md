# Blackjack

<p> 
    <img src="Discord-Server-Banner.jpg">
</p>


## Features 
- Slot machine
- Blackjack
- Sauce
- Money System

## Create the Bot
- go to https://discord.com/developers/applications and create a new application the application and bot share the same name and can be changed later 
- click OAuth2 on the left side
    - under scopes click bot and copy the generated url then paste into the browser and select which server to add the bot in
- click bot on the left side then create bot
    - click presence & server member intents under `Privileged Gateway Intents` this allows the bot to send links
    - under `bot permissions` click administrator
    - copy/write down the bot generated token you can always generate another one if it gets exposed

## Installations
- Clone the repository
- in the `.env` file replace the token with your own this links the bot to the python script


# Commands
> all commands must begin with `.`
- balance
- gift
- sauce

### to begin slot machine game
- slot high
- slot low

### to begin blackjack game
- sit
- bj
- hit
- stand



## Tools Used
* [<b>Discord Dev Portal</b>](https://discord.com/developers/docs/intro) - To create the bot.
* [<b>MySQL</b>](https://www.mysql.com/) - To create a database that holds user specific money values.


## Content for future updates
- pokemon games (catch wild pokemon)
- music station

