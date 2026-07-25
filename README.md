Vanguard AI Pro

Overview

Vanguard AI Pro is an AI-powered institutional trading bot designed for Smart Money Concepts (SMC), ICT, Price Action, and market structure analysis.

Features

- Smart Money Concepts (SMC)
- ICT Concepts
- Price Action Analysis
- BOS & CHoCH Detection
- Fair Value Gap (FVG)
- Order Blocks
- Liquidity Sweep Detection
- Multi-Timeframe Analysis
- Risk Management
- Telegram Signal Notifications
- 24/7 Cloud Deployment (Railway)

Project Structure

Vanguard-AI/
│
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── market.py
├── signals.py
├── smc.py
└── telegram_bot.py

Installation

pip install -r requirements.txt

Run

python main.py

Environment Variables

Create a ".env" file and add:

BOT_TOKEN=
OWNER_ID=
TWELVE_API_KEY=

License

MIT License
