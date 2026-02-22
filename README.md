# Turbocharger Pairs Strategy
A simple statistical arbitrage ptototype designed to test mean-reversion in negatively correlated equity pairs. 


## Objective
The goal of this project is to evaluate whether temporary divergences between negatively correlated stocks can be exploited using a simple rule-based market-netural strategy.

## Strategy Overview

## Key Assumptions

## Architecture

## How to run
### 1. Clone the repository
git clone https://github.com/hausmannmike/my-turbo-bot.git

cd my-turbo-bot
### 2. Install dependencies
pip install alpaca-py pandas numpy python-dotenv
### 3. Configure API keys
Create a ".env" file:

ALPACA_ENDPOINT_URL = "endpoint_url_here"

ALPACA_API_KEY = "your_key_here"

ALPACA_SECRET_KEY = "your_secret_here"
### 4. Run 
python main.py
