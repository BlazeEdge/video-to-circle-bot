# Video to circle - Telegram bot

A simple Telegram bot that can turn a square video into a circular one. The bot uses the `pyTelegramBotAPI` library.
**Important: the video needs to have an aspect ratio of 1:1.**

## How to install
- Clone the repository and enter to the directory<br>
`git clone https://github.com/BlazeEdge/video-to-circle-bot.git && cd video-to-circle-bot`

- Create a Python Virtual Environment and activate it<br>
`python3 -m venv venv && source venv/bin/activate`

- Install the necessary library<br>
`pip install pyTelegramBotAPI`

## How to configure
- Open file `config.py`

- In the `START_MSG` field, you can type a message that the bot will say when you run the `/start` command.

- In the `TOKEN` field, you can move your bot's token over to Telegram.

## How to run
- `python3 ./bot.py`


<sub>Well, that's all lol</sub>