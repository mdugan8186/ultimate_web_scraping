# ==== non-usd prices ====

import requests as r
from bs4 import BeautifulSoup


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
    print(get_price_information('MSFT', 'NASDAQ'))
    print(get_price_information('AMZN', 'NASDAQ'))
    print(get_price_information('SHOP', 'TSE'))
    print(get_price_information('SHOP', 'NASDAQ'))

    print(get_fx_to_usd('CAD'))
    print(get_fx_to_usd('EUR'))

#
#
"""
== Context ==
- We previously built scraping logic to extract price and currency for a given ticker and exchange
- However, prices may be listed in **non-USD currencies** (e.g., CAD for TSX stocks like Shopify)
- To calculate a consistent total portfolio value, we need all prices expressed in **USD**

Problem:
- Shopify listed on TSX returns price in CAD
- Currency = CAD
- We need to convert this CAD price to USD
"""

# == Strategy ==
"""
- If the currency is already USD → no conversion
- If the currency is NOT USD:
    1. Query Google Finance for the **FX rate** (e.g., CAD to USD)
    2. Multiply price by FX rate to get price in USD
"""

# == Implementation Plan ==
"""
1. Create a helper function: `get_fx_to_usd(currency)`
    - Build URL: `https://www.google.com/finance/quote/<CURRENCY>-USD`
      e.g., `https://www.google.com/finance/quote/CAD-USD`
    - Fetch page with `requests.get(url)`
    - Parse with `BeautifulSoup`
    - Use `soup.find("div", attrs={"data-last-price": True})` to extract FX rate
    - Convert it to `float` and return

2. In `get_price_info()`:
    - Add a default: `usd_price = price`
    - If `currency != "USD"`:
        - Call `get_fx_to_usd(currency)`
        - Set `usd_price = round(price * fx_rate, 2)`

3. Update the return dictionary:
    ```python
    {
        "ticker": ...,
        "exchange": ...,
        "price": ...,
        "currency": ...,
        "usd_price": ...
    }
    ```
"""

# == Testing ==
"""
- Tested with Shopify on TSX:
    - Price: 70.93 CAD
    - Currency: CAD
    - USD Price: 52.93 USD (after FX conversion)
- Verified accuracy by comparing to NYSE-listed Shopify (around $52.89 USD)
    - Minor difference confirms logic works
    - Helps detect arbitrage if discrepancies are large
"""

# == Notes ==
"""
- Google Finance uses consistent `data-last-price` markup for both stock prices and FX rates
- Relying on attributes like `data-last-price` avoids brittle class-based parsing
- Rounding the USD price avoids long floating-point values
"""
