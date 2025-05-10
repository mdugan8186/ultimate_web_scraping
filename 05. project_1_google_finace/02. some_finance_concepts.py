# ==== some finance concepts ====


#
#
"""
== Overview ==
- Before coding, it's important to understand the domain.
- This project revolves around tracking and valuing **stocks** as part of a **portfolio**.
"""

# == Stock Basics ==
"""
- A **stock** is defined by:
    - Ticker (e.g., BNS for Bank of Nova Scotia)
    - Exchange (e.g., TSX or NYSE)
- A **ticker** without an exchange may return multiple matches (e.g., BNS on TSX and NYSE).
- The same company can be listed in multiple exchanges with different prices due to **currency differences**.
    - Example: BNS at $54 USD on NYSE and $73 CAD on TSX.
- A **share** is a unit of ownership in a public company.
- **Market capitalization** = share price × total outstanding shares.
"""

# == Portfolio Components ==
"""
- A **portfolio** is a collection of stock positions.
- Each **position** includes:
    - A stock (ticker + exchange)
    - A quantity (number of shares owned)
- Example portfolio:
    - 100 shares of BNS
    - 30 shares of Google
    - 10 shares of Shopify
    - 2 shares of Microsoft
- The full set of positions = your portfolio.
"""

# == Suggested Data Structure ==
"""
The instructor uses three conceptual types:

1. **Stock**: Holds ticker, exchange, and price data
2. **Position**: Represents a stock plus a quantity (e.g., 10 shares of AAPL)
3. **Portfolio**: A collection (e.g., list) of positions

These help organize and operate on portfolio data cleanly.
"""

# == Currency Handling ==
"""
- If a portfolio contains stocks in multiple currencies, convert them to a common one.
    - Example: Convert CAD and USD stocks to USD
- Google Finance includes currency (FX) data on its pages, just like it includes stock data.
    - You can scrape currency pairs similarly to how you scrape stock prices.
"""

# == Output and Presentation ==
"""
- A display method (e.g., `display_portfolio_summary()`) is used to show the portfolio in table form.
    - This method is separate from the web scraping logic
    - It’s purely for readable, user-friendly output
"""

# == Summary ==
"""
- Understand how stocks, positions, and portfolios relate before jumping into scraping.
- Prepare to extract:
    - Stock prices
    - Associated currency data (FX)
- Convert values into a **single currency** for consistent output.
"""
