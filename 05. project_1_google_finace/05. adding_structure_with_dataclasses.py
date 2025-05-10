# ==== adding structure with dataclasses ====

import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = 'USD'
    usd_price = float = 0

    def __post_init__(self):
        price_info = get_price_information(self.ticker, self.exchange)

        if price_info['ticker'] == self.ticker:
            self.price = price_info['price']
            self.currency = price_info['currency']
            self.usd_price = price_info['usd_price']


def get_fx_to_usd(currency):
    fx_url = f'https://www.google.com/finance/quote/{currency}-USD'
    resp = r.get(fx_url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    fx_rate = soup.find('div', attrs={'data-last-price': True})
    fx = float(fx_rate['data-last-price'])
    return fx


def get_price_information(ticker, exchange):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    price_div = soup.find('div', attrs={'data-last-price': True})
    price = float(price_div['data-last-price'])
    currency = price_div['data-currency-code']

    usd_price = price
    if currency != 'USD':
        fx = get_fx_to_usd(currency)
        usd_price = round(price * fx, 2)

    return {
        'ticker': ticker,
        'exchange': exchange,
        'price': price,
        'currency': currency,
        'usd_price': usd_price
    }


if __name__ == '__main__':
    print(Stock('SHOP', 'TSE'))


#
#
"""
== Purpose ==
- Begin adding structure to how stock data is managed.
- Define types for:
    1. Stock - ticker + exchange + price data
    2. Position - a stock and quantity owned
    3. Portfolio - a combination of positions representing the user's investments
- The goal: enable clean portfolio valuation logic, not just raw scraping.
"""

"""
== Stock Concept ==
- Represents a specific stock:
    - Ticker (e.g., "SHOP")
    - Exchange (e.g., "TSE")
    - Currency it trades in (e.g., "CAD")
    - Live price and USD-converted price
- Does not contain quantity — that's for Position.
"""

"""
== Position and Portfolio Concepts ==
- A Position = stock + number of shares
    - e.g., 2 shares of SHOP on TSE
- A Portfolio = multiple positions
    - e.g., 2 SHOP + 3 AMZN = portfolio
- This structure allows us to build summaries and market value calculations.
"""

"""
== Why Data Classes ==
- Less boilerplate than regular Python classes.
- Ideal for storing and structuring data.
- Provide auto-generated methods like:
    - __init__ (constructor)
    - __repr__ (string display)
    - __eq__ (comparison)
- Easy to extend with logic like default values and post-processing.
"""

"""
== Defining the Stock Data Class ==
- Import `dataclass` from the `dataclasses` module.
- Define required and defaulted fields:
    ticker: str             # required
    exchange: str           # required
    price: float = 0.0      # default
    currency: str = "USD"   # default
    usd_price: float = 0.0  # default

- Only ticker and exchange are required to create an instance.
- Other fields will be filled automatically.
"""

"""
== Example Creation ==
    stock = Stock("SHOP", "TSE")
    print(stock)

- Output:
    Stock(ticker='SHOP', exchange='TSE', price=0.0, currency='USD', usd_price=0.0)

- Automatically provides a readable string output — no __str__ override needed.
"""

"""
== Fetching Live Data with __post_init__ ==
- Want to enrich each Stock with live data immediately after it's created.
- Use `__post_init__()` method:
    - Runs after the stock is initialized with default values.
    - Perfect place to pull live pricing.
"""

"""
== Implementation Steps ==
- Inside `__post_init__`:
    1. Call `get_price_info(self.ticker, self.exchange)`
    2. Validate the returned ticker matches `self.ticker`
    3. If valid, update:
        - self.price
        - self.currency
        - self.usd_price

    Example:
    def __post_init__(self):
        price_info = get_price_info(self.ticker, self.exchange)
        if price_info["ticker"] == self.ticker:
            self.price = price_info["price"]
            self.currency = price_info["currency"]
            self.usd_price = price_info["usd_price"]
"""

"""
== Why Validate Returned Ticker ==
- Google Finance might return:
    - No result (e.g., bad combo)
    - Incorrect info (e.g., for the wrong ticker)
- Checking returned ticker ensures the update is safe.
"""

"""
== Fallback Behavior ==
- If the fetch fails:
    - Stock instance retains default price, currency, usd_price
    - Does not break the app
- Later improvement: add proper error handling in `get_price_info`
"""

"""
== Final Behavior ==
- After creating:
    Stock("SHOP", "TSE")

- You get:
    - ticker = "SHOP"
    - exchange = "TSE"
    - price = <live CAD price>
    - currency = "CAD"
    - usd_price = <converted USD value>

- Example output:
    Stock(ticker='SHOP', exchange='TSE', price=70.93, currency='CAD', usd_price=52.93)
"""

"""
== Summary ==
- Data classes let us organize scraped data meaningfully.
- Stock now carries both static and dynamic values.
- Prepares us to define:
    - Position: adds quantity
    - Portfolio: adds value tracking and summaries
"""
