import os
import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TO_PHONE_NUMBER = os.environ["MY_PHONE_NUMBER"]
FROM_PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]

STOCK_API_KEY = os.environ["ALPHAVANTAGE_STOCK_API_KEY"]
NEWS_API_KEY = os.environ["NEWSAPI_API_KEY"]

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_SYMBOL = "TSLA"

INCREASE_SYMBOL = "🔺"
DECREASE_SYMBOL = "🔻"

NOTABLE_STOCK_DIFFERENCE = 0.05 # Threshold to receive text alerts

def get_stock_data():
    stock_api_params = {
        "apikey": STOCK_API_KEY,
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_SYMBOL
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_api_params, verify=False)
    return response.json()

def get_closing_stock_price(stock_data, days_ago=1):
    date_to_acquire_stock_for = (date.today() - timedelta(days = days_ago)).strftime("%Y-%m-%d")
    requested_closing_price = float(stock_data['Time Series (Daily)'][date_to_acquire_stock_for]['4. close'])
    
    return requested_closing_price

def is_notable_stock_difference(oldest_day, most_recent_day):
    return abs(most_recent_day - oldest_day) / oldest_day > NOTABLE_STOCK_DIFFERENCE

def get_stock_direction_symbol(oldest_day, most_recent_day):
    if oldest_day > most_recent_day:
        return DECREASE_SYMBOL
    return INCREASE_SYMBOL

def get_stock_percent_change(oldest_day, most_recent_day):
    percent_change = abs(most_recent_day - oldest_day) / oldest_day
    return f"{percent_change:.0%}"

def get_company_name():
    stock_api_params = {
        "apikey": STOCK_API_KEY,
        "function": "OVERVIEW",
        "symbol": STOCK_SYMBOL
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_api_params, verify=False)

    return response.json()['Name']

def get_top_3_news_highlights(company):
    news_api_params = {
        "apikey": NEWS_API_KEY,
        "q": company
    }

    response = requests.get(NEWS_ENDPOINT, params=news_api_params, verify=False)

    top_3_news_articles = response.json()['articles'][:3]
    
    list_of_news_highlights = [{'headline': article['title'],'brief': article['description']} for article in top_3_news_articles]
    return list_of_news_highlights

def format_message_contents(direction, percent, headline, brief):
    message_contents = f"""{STOCK_SYMBOL}: {direction}{percent}
Headline: {headline}
Brief: {brief}"""
    return message_contents

def text_stock_update(message_contents):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(         
                              to=TO_PHONE_NUMBER,
                              from_=FROM_PHONE_NUMBER,
                              body=message_contents
                          )
    print(message.sid)

stock_data = get_stock_data()
closing_price_yesterday = get_closing_stock_price(stock_data, 1)
closing_price_two_days_ago = get_closing_stock_price(stock_data, 2)

if is_notable_stock_difference(closing_price_two_days_ago, closing_price_yesterday):
    direction = get_stock_direction_symbol(closing_price_two_days_ago, closing_price_yesterday)
    percent = get_stock_percent_change(closing_price_two_days_ago, closing_price_yesterday)
    company_name = get_company_name()
    news_highlights = get_top_3_news_highlights(company_name)

    for highlight in news_highlights:
        message_contents = format_message_contents(direction, percent, highlight['headline'], highlight['brief'])
        text_stock_update(message_contents)
