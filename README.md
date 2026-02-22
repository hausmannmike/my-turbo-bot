# Turbocharger Pairs Strategy
A research prototype evaluating a rule-based market-neutral strategy
applied to negatively correlated equity pairs.


## Objective
The objective of this project is to test whether temporary divergences 
between negatively correlated equities can be systematically exploited 
using a simple, rule-based, dollar-neutral trading framework.

## Strategy Overview

## Key Assumptions

## Architecture

## How to run
### 1. Clone the repository
```
git clone https://github.com/hausmannmike/my-turbo-bot.git
cd my-turbo-bot
```
### 2. Install dependencies
```
pip install alpaca-py pandas numpy python-dotenv
```

### 3. Configure API keys
Create a `.env` file:
```env
ALPACA_ENDPOINT_URL = "endpoint_url_here"
ALPACA_API_KEY = "your_key_here"
ALPACA_SECRET_KEY = "your_secret_here"
```
### 4. Run 
```
python main.py
```

