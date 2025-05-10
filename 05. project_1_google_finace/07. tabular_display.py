# ==== tabular display ====

import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tabulate import tabulate


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


def display_portfolio_summary(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError('Please provide an instance of the Portfolio type')

    portfolio_value = portfolio.get_total_value()

    position_data = []
    for position in sorted(portfolio.positions,
                           key=lambda x: x.quantity * x.stock.usd_price,
                           reverse=True):
        position_data.append([
            position.stock.ticker,
            position.stock.exchange,
            position.quantity,
            position.stock.usd_price,
            position.quantity * position.stock.usd_price,
            position.quantity * position.stock.usd_price / portfolio_value * 100
        ])

    print(tabulate(position_data,
                   headers=['Ticker', 'Exchange', 'Quantity',
                            'Price', 'Market Value', '% Allocation'],
                   tablefmt='psql',
                   floatfmt='.2f'
                   ))

    print(f'Total portfolio value: ${portfolio_value:,.2f}')


if __name__ == '__main__':
    # print(Stock('SHOP', 'TSE'))

    shop = Stock('SHOP', 'TSE')
    msft = Stock('MSFT', 'NASDAQ')
    googl = Stock('GOOGL', 'NASDAQ')
    bns = Stock('BNS', 'TSE')

    portfolio = Portfolio([
        Position(shop, 10),
        Position(msft, 2),
        Position(bns, 1000),
        Position(googl, 30)
    ])

    # print(portfolio.get_total_value())
    display_portfolio_summary(portfolio)


#
#
"""
== Purpose ==
- Add a user-friendly tabular display to the project using the `tabulate` library
- Format and summarize the portfolio holdings in a clean table
- Sort positions by market value
"""

"""
== Library Used ==
- `tabulate` is a third-party library (not part of the Python standard library)
- Must be installed manually: `pip install tabulate`
- Version consistency is recommended when following along
"""

"""
== Project Recap ==
- We have 3 key data types:
    - Stock: ticker, exchange, currency, price, USD price
    - Position: a Stock + quantity
    - Portfolio: list of Position instances

- We want to now *display* the portfolio with:
    - Ticker
    - Exchange
    - Quantity
    - Price (USD)
    - Market value
    - Percent allocation
"""

"""
== display_portfolio_summary() ==
- Defined as an external function, not part of the Portfolio class
- Reason: keeps tabulate dependency out of the core data structure
- Accepts a Portfolio instance
- First validates the input type using `isinstance(portfolio, Portfolio)`
    - If not valid, raises a TypeError with a helpful message
"""

"""
== Summary Table Construction ==
- Prepares a list of rows, one per Position
- Each row contains:
    - Ticker
    - Exchange
    - Quantity
    - USD Price
    - Market Value
    - Percent of total portfolio value

- Example logic:
    [
        position.stock.ticker,
        position.stock.exchange,
        position.quantity,
        f"${position.stock.usd_price:,.2f}",
        f"${market_value:,.2f}",
        f"{percent:.2f}%"
    ]
- Appended to a list called position_data
"""

"""
== Market Value and Allocation ==
- Market value = quantity x stock.usd_price
- Allocation % = (market value / total portfolio value) x 100
- Both are formatted to 2 decimal places using f-strings
"""

"""
== Sorting Positions by Value ==
- Uses Python's built-in sorted() function
- Sorts by market value in descending order
- Lambda function for sorting key:
    key=lambda x: x.quantity * x.stock.usd_price
- Sets reverse=True for descending order
"""

"""
== Tabulate Parameters ==
- Calls:
    tabulate(position_data, headers=headers, tablefmt="grid")
    - Header columns:
        • “Ticker”
        • “Exchange”
        • “Quantity”
        • “Price”
        • “Market Value”
        • “Percent Allocation”
    - Format:
        • tablefmt="grid" gives a SQL-style look
        • Numbers are formatted with commas and two decimals
"""

"""
== Additional Formatting ==
- Adds a dollar sign to price and market value
- Adds percent sign to percent allocation
- Formats the final portfolio total with commas and decimals:
    print(f"Total Portfolio Value: ${portfolio_value:,.2f}")
"""

"""
== Example Output ==
+----------+-----------+-----------+---------+---------------+---------------------+
| Ticker   | Exchange  | Quantity  | Price   | Market Value  | Percent Allocation  |
+----------+-----------+-----------+---------+---------------+---------------------+
| BNS      | TSE       | 10000     | $73.20  | $732,000.00   | 81.74%              |
| GOOG     | NASDAQ    | 30        | $120.00 | $3,600.00     | 0.40%               |
| MSFT     | NASDAQ    | 2         | $315.00 | $630.00       | 0.07%               |
| SHOP     | TSE       | 10        | $52.90  | $529.00       | 0.06%               |
+----------+-----------+-----------+---------+---------------+---------------------+
Total Portfolio Value: $896,759.00
"""

"""
== Performance Note ==
- Table generation takes time because:
    - Each Stock instance fetches live price data from Google Finance on creation
    - More positions = more web requests
- This can be optimized later by caching or batch API calls
"""

"""
== Summary ==
- Tabulate provides a clean and readable way to display portfolio data
- Sorting and formatting make it easier to analyze holdings
- This completes the scraping and structuring phases
- The rest is presentation, formatting, and future feature expansion
"""
