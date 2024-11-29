from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the /start command function
def start(update: Update, context: CallbackContext) -> None:
    # Send "Hello" message when /start command is called
    update.message.reply_text('Hello')

# Create the main function to run the bot
def main() -> None:
    # Replace 'YOUR_TOKEN' with the token you got from BotFather
    updater = Updater("7587163583:AAHLU4msNvgo19mmwloHie-3C5W98ZVY9gs")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start polling for new updates (messages, commands, etc.)
    updater.start_polling()

    # Run the bot until you send a signal to stop it (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
