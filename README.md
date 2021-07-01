# Selects - discord_components
This repository is again, an example code for how to use discord's new feature, **selects**, in your bot's messages, using the discord_components library in python.
The syntax for selects is also pretty easy, and once you know how to use it, let your creativity go wild! As of 1/7/21 the code doesn't have a timeout and disable function, but this will be added real soon. 

## Pre Requisites
- Basic python knowledge
- Python 3.7+ installed on your computer
- Discord account (updated to latest version)

## Libraries
Install these by running `pip install <lib name here>` in your terminal
- discord.py
- discord_components
- asyncio 

## Usage
- Download or Copy the selects file
- Replace `<token>` with your bot's token
- Edit the contents of the message
- Edit the labels / descriptions of selects
- Add more selects if needed
- Run the code!

## More To Know
- You can add checks to the `wait_for` statement to check for a particular user
- The disabled attribute will come soon, and repo will be updated to accomodate soon
- There is also a way to add emotes, read the docs for the same
- Currently the select name is not fetchable by res.component.select or any such method, so we're analyzing the raw json response

