import nextcord
from nextcord.ext import commands
from nextcord.ui import View, Button
import asyncio

intents = nextcord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

existing_list_file = 'code_list.txt'  # Path to the file containing the existing list


def load_existing_list():

  with open(existing_list_file, 'r') as file:

    return [line.strip() for line in file]


existing_list = load_existing_list()

message = ""


class SubmitcodeView(View):
  def __init__(self):
    super().__init__()
    self.add_item(
      Button(style=nextcord.ButtonStyle.primary,
             label="Submit Code",
             custom_id="submit_code"))

  async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
    if interaction.data["custom_id"] == "submit_code":
      #message = await interaction.send("Enter your code:", ephemeral=True)
      await self.submit_code(interaction)
      pass
      return False
    return True

  async def on_timeout(self) -> None:
    await self.disable_buttons()

  async def disable_buttons(self):
    for item in self.children:
      if isinstance(item, Button):
        item.disabled = True

  async def submit_code(self, interaction: nextcord.Interaction):
    member = interaction.user
    form = nextcord.ui.Modal(f'Form for {interaction.user}')
    frm = nextcord.ui.TextInput(label="Enter your code",
                                placeholder="Your code:",
                                style=nextcord.TextInputStyle.paragraph)
    form.add_item(frm)
    await interaction.response.send_modal(form)
      
    async def modal_callback(interaction):
      code_string = frm.value  # get text input data
      print(code_string)
      if code_string and code_string.strip():
        if code_string in existing_list:
          role = nextcord.utils.get(member.guild.roles, name='ROLE HERE')  # Replace with the name of the role you want to assign
          if role:
            await member.add_roles(role)
            await interaction.send("You have been assigned the role.",
                                   ephemeral=True)
          else:
            await interaction.send("The role was not found.", ephemeral=True)
        else:
          await interaction.send("Invalid code string.", ephemeral=True)
      else:
        await interaction.send("No code string entered.", ephemeral=True)
    form.callback = modal_callback


@bot.event
async def on_ready():
  print('Bot is ready!')
  channel = bot.get_channel(
    1096149268022169700)  # Replace with the ID of the desired channel
  if channel:
    view = SubmitcodeView()
    await channel.send("Click the button below to submit your code:",
                       view=view)


@bot.event
async def on_message(message):
  if message.author.bot:
    return  # Ignore messages from other bots
  await bot.process_commands(message)


@bot.event
async def on_interaction(interaction: nextcord.Interaction):
  if interaction.data["custom_id"] == "submit_code":
    view = SubmitcodeView()

bot.run("TOKEN HERE")
