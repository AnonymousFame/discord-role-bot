# Discord Code Submission Bot

This repository contains a Discord bot written in Python that allows users to submit code strings and assigns a specific role to them based on the code's validity.

## Prerequisites
- Python 3.6 or higher
- `discord.py` library installed (version 1.7.3 or higher)

## Setup

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   
1. Replace the placeholders in the code with the appropriate values:

**ENTER CHANNEL NUMBER** - Replace with the ID of the desired channel where the bot will send the code submission message.
**ROLE NAME** - Replace with the name of the role you want to assign to users with valid code strings.
**ENTER TOKEN** - Replace with your Discord bot token. You can obtain this token by creating a new bot on the Discord Developer Portal.

## Usage

1. Run the bot by executing the following command:

   ```bash
   python bot.py

2. The bot will print "Bot is ready!" once it has successfully connected to Discord.

3. In the specified channel, the bot will send a message with a button labeled "Submit Code". Users can click this button to initiate the code submission process.

4. After clicking the button, the bot will prompt the user to enter their code.

5. If the code string is valid and exists in the existing list (loaded from the **code_list.txt** file), the user will be assigned the specified role. Otherwise, an appropriate message will be sent.

## Customization
1. If you want to modify the command prefix, change the value assigned to the **command_prefix** variable in the following line:

bot = commands.Bot(command_prefix='!', intents=intents)

2. To customize the appearance and behavior of the button, you can modify the SubmitcodeView class. This class represents the view with the button displayed in the code submission message. You can change the button label, style, and other properties according to your requirements.

3. To modify the existing code list, update the **code_list.txt** file with the desired code strings. Each code should be on a separate line.

## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of this license.
