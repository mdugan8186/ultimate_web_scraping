# ==== position and portfolio ====

import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = 'USD'
    usd_price: float = 0

    def __post_init__(self):
        price_info = get_price_information(self.ticker, self.exchange)

        if price_info['ticker'] == self.ticker:
            self.price = price_info['price']
            self.currency = price_info['currency']
            self.usd_price = price_info['usd_price']


@dataclass
class Position:
    stock: Stock
    quantity: int


@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        total_value = 0

        for position in self.positions:
            total_value += position.quantity * position.stock.usd_price

        return total_value


def get_fx_to_usd(currency):
    fx_url = f'https://www.google.com/finance/quote/{currency}-USD'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    resp = r.get(fx_url, headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')

    fx_rate = soup.find('div', attrs={'data-last-price': True})
    fx = float(fx_rate['data-last-price'])
    return fx


def get_price_information(ticker, exchange):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    resp = r.get(url, headers=headers)
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
    # print(Stock('SHOP', 'TSE'))

    shop = Stock('SHOP', 'TSE')
    msft = Stock('MSFT', 'NASDAQ')
    googl = Stock('GOOGL', 'NASDAQ')

    portfolio = Portfolio([
        Position(shop, 10),
        Position(msft, 2),
        Position(googl, 30)
    ])

    print(portfolio.get_total_value())

#
#
"""
== Purpose ==
- Extend the project by adding new data classes:
    1. Position: a Stock + quantity
    2. Portfolio: a list of Positions + total valuation logic
"""

"""
== Position Class ==
- Represents an investment in a specific stock (e.g., 10 shares of SHOP).
- Defined as a dataclass with:
    - stock: Stock
    - quantity: int

- stock is of type `Stock`, defined in the previous section.
- quantity is the number of shares owned.
- Example:
    ```python
    shop = Stock("SHOP", "TSE")
    position = Position(shop, 10)
    ```
- The price is automatically fetched due to Stock's `__post_init__`.
- String representation is handled by the dataclass.
"""

"""
== Portfolio Class ==
- Represents a collection of Position instances.
- Also defined as a dataclass:
    - positions: list[Position]

- Uses composition:
    - Portfolio contains a list of Positions
    - Position contains a Stock
"""

"""
== Portfolio.total_value() Method ==
- Defines an instance method to compute total portfolio market value in USD.
- self refers to the Portfolio instance.

Logic:
    1. Initialize total_value = 0
    2. Loop through self.positions
    3. For each position:
        - Multiply position.quantity * position.stock.usd_price
        - Add to total_value
    4. Return total_value

Example:
    ```python
    def total_value(self):
        total = 0
        for position in self.positions:
            total += position.quantity * position.stock.usd_price
        return total
    ```
"""

"""
== Notes on self ==
- `self` refers to the instance on which a method is called.
- All instance methods must accept `self` as the first parameter.
- You could technically rename it, but `self` is standard and expected.
"""

"""
== Instantiating and Using a Portfolio ==
1. Create stock instances:
    ```python
    shop = Stock("SHOP", "TSE")
    msft = Stock("MSFT", "NASDAQ")
    goog = Stock("GOOG", "NASDAQ")
    ```

2. Create position instances:
    ```python
    p1 = Position(shop, 10)
    p2 = Position(msft, 2)
    p3 = Position(goog, 30)
    ```

3. Create portfolio using a list of positions:
    ```python
    portfolio = Portfolio([p1, p2, p3])
    ```

4. Get the total value:
    ```python
    print(portfolio.total_value())
    ```

- Note: the portfolio must be passed a list of Position objects.
- If you pass them directly as separate arguments, it will raise a TypeError.
"""

"""
== Error Example ==
Incorrect:
    Portfolio(Position(shop, 10), Position(msft, 2), Position(goog, 30))  ❌

Correct:
    Portfolio([Position(shop, 10), Position(msft, 2), Position(goog, 30)]) ✅
"""

"""
== Adding Headers ==

documentation:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

When scraping Google Finance using the `requests` library, the response HTML
initially did not include key data attributes like `data-last-price`. This caused:

    soup.find(...) → None
    None['data-last-price'] → TypeError: 'NoneType' object is not subscriptable

This broke the code when trying to extract stock prices or FX rates.

------------------------------------
Why did this happen?
------------------------------------

Google Finance serves different versions of the page depending on the client.
If the request does not appear to come from a real browser, Google may serve:

- A stripped-down page without the data attributes
- A redirect or JavaScript-heavy page
- A blocking page (in some cases)

By default, `requests.get()` sends minimal headers — so Google treated it as a bot.

------------------------------------
✅ Solution: Add a User-Agent header
------------------------------------

A User-Agent string was added to the request headers to mimic a real browser.
This tricks Google into sending the full page, including `data-last-price`.

Example:
------------------------------------
import requests

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    )
}

url = "https://www.google.com/finance/quote/CAD-USD"
resp = requests.get(url, headers=headers)
------------------------------------

This fix applies to:
- get_price_information()  — for stocks like SHOP, GOOGL, etc.
- get_fx_to_usd()          — for currencies like CAD, EUR, etc.

------------------------------------
📌 Takeaway:
------------------------------------

✔ Always set a realistic `User-Agent` header when scraping pages that:
- Use dynamic rendering
- Block bots
- Serve different content to browsers vs scripts

✔ This is especially common with finance, e-commerce, and travel sites.

✔ You can inspect the original browser request headers in Chrome DevTools → Network tab → Request Headers.
"""

"""
== Summary ==
- Position = Stock + quantity
- Portfolio = list of Positions
- total_value() aggregates the USD value of the portfolio
- All prices and currency conversion handled via the Stock’s internal logic
- With scraping complete, the rest of the project is Python structure and logic
"""
