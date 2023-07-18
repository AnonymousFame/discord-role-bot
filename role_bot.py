import discord
from discord.ext import commands
from discord.ui import View, Button

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
existing_list_file = 'code_list.txt'  # Path to the file containing the existing list

def load_existing_list():
    with open(existing_list_file, 'r') as file:
        return [line.strip() for line in file]

existing_list = load_existing_list()

class SubmitcodeView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(style=discord.ButtonStyle.primary, label="Submit Code", custom_id="submit_code"))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.data["custom_id"] == "submit_code":
            await interaction.response.send_message("Enter your code:", ephemeral=True)
            return False
        return True

    async def on_timeout(self) -> None:
        await self.disable_buttons()

    async def disable_buttons(self):
        for item in self.children:
            if isinstance(item, Button):
                item.disabled = True

    async def submit_code(self, button: discord.ui.Button, interaction: discord.Interaction):
        member = interaction.user
        code_string = interaction.message.content  # Retrieve the entered code string from the message content
        if code_string and code_string.strip():
            if code_string in existing_list:
                role = discord.utils.get(member.guild.roles, name='ROLE HERE')  # Replace with the name of the role you want to assign
                if role:
                    await member.add_roles(role)
                    await interaction.response.send_message("You have been assigned the role.", ephemeral=True)
                else:
                    await interaction.response.send_message("The role was not found.", ephemeral=True)
            else:
                await interaction.response.send_message("Invalid code string.", ephemeral=True)
        else:
            await interaction.response.send_message("No code string entered.", ephemeral=True)

@bot.event
async def on_ready():
    print('Bot is ready!')
    channel = bot.get_channel(CHANNEL HERE)  # Replace with the ID of the desired channel
    if channel:
        view = SubmitcodeView()
        await channel.send("Click the button below to submit your code:", view=view)

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    await bot.process_commands(message)

@bot.event
@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data["custom_id"] == "submit_code":
        view = SubmitcodeView()
        await interaction.component.callback(interaction)

                
bot.run('TOKEN HERE')
