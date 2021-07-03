# Importing libraries
from discord.ext import commands
import discord, asyncio
from discord_components import *

# Initialising components and client
bot = commands.Bot(command_prefix="sc.")  # Your prefix here
DiscordComponents(bot)  # Necessary

# Ready event
@bot.event
async def on_ready():
    print("Online.")


# Single Select Command
@bot.command(name="test_1")
async def test_1(ctx):
    msg = await ctx.reply(  # Replying to message
        "Singular Selects Below.",
        components=[  # List of components
            [
                Select(  # Denotes a select box
                    placeholder="Please Choose A Car",  # Text displayed in the select (default box)
                    options=[
                        SelectOption(  # Creating an option
                            label="Ferrari",  # Name displayed on top
                            value="fer",  # Distinguishes in the interaction response
                            description="Italian Automaker",  # Extra info
                        ),
                        SelectOption(  # Same as above
                            label="Bugatti", value="bug", description="French Automaker"
                        ),
                        SelectOption(  # Same as above
                            label="Audi", value="aud", description="German Automaker"
                        ),
                    ],
                )
            ]
        ],
    )

    # Waiting for response...
    # Using try and except loop for the timeout
    try:
        # Wait_for statement
        ##Event is on_select_option
        interaction = await bot.wait_for(
            "select_option",  # Once someone selects and clicks out of the dropdown
            check=None,
            timeout=10.0,  # 10 Second timeout
        )
        name = interaction.component[0].label  # Getting label of select

        # Responding with the option they chose
        await interaction.respond(
            type=4,  # New Message in channel
            ephemeral=False,  # Not hidden
            content=f"Thank you for using selects! \n> Your favourite car brand is **{name}**",  # Telling them what they chose
        )
    except asyncio.TimeoutError:
        # The disabling of select should come soon, rn its buggy so avoid it
        await msg.edit(
            components=[  # List of components
                [
                    Select(  # Denotes a select box
                        placeholder="Please Choose A Car",  # Text displayed in the select (default box)
                        disabled=True,  # Disabling it
                        options=[
                            SelectOption(  # Creating an option
                                label="Ferrari",  # Name displayed on top
                                value="fer",  # Distinguishes in the interaction response
                                description="Italian Automaker",  # Extra info
                            ),
                            SelectOption(  # Same as above
                                label="Bugatti",
                                value="bug",
                                description="French Automaker",
                            ),
                            SelectOption(  # Same as above
                                label="Audi",
                                value="aud",
                                description="German Automaker",
                            ),
                        ],
                    )
                ]
            ]
        )


bot.run(
    "<token>"
)  # Put your token here
