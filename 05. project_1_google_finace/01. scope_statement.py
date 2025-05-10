# ==== scope statement ====


#
#
"""
== Objective ==
- Build a program that:
    - Scrapes live price information from Google Finance
    - Calculates a portfolio's market value using stock quantities and prices
    - Supports multiple stocks and exchanges, converting to a common currency (e.g., USD)
"""

# == Key Concepts ==
"""
- Google Finance provides free near real-time stock data.
  Example: Apple stock (AAPL) recently closed at $154.50 USD on NASDAQ.
- The app will:
    1. Generate a URL for a given stock ticker and exchange
    2. Scrape the resulting HTML page
    3. Extract stock price and currency
    4. Multiply by number of shares to get market value
    5. Convert all values to a common currency (if necessary)
"""

# == Multi-Currency Support ==
"""
- Example:
    - Apple (AAPL) on NASDAQ (USD)
    - Enbridge (ENB) on Toronto Stock Exchange (CAD)
- Convert both to a common currency for accurate portfolio valuation.
- Never mix CAD and USD directly without conversion.
"""

# == Example Output Structure ==
"""
| Ticker | Exchange | Quantity | Price | Market Value | % Allocation |
|--------|----------|----------|-------|---------------|---------------|
| AAPL   | NASDAQ   | 10       | 154.5 | $1,545.00     | 50%           |
| ENB    | TSX      | 20       | 100   | $2,000.00     | 50%           |

- Aggregate value at the bottom: $3,545.00 USD
"""

# == Implementation Tips ==
"""
- Scrape:
    - Construct ticker-specific URLs dynamically
- Extract:
    - Pull price and currency from the HTML
- Calculate:
    - Market Value = Price x Quantity
    - % Allocation = (Market Value / Total Portfolio Value) x 100
"""

# == Next Steps ==
"""
- Next lecture will cover key finance terms (tickers, exchanges, allocations)
- Multiple valid ways to implement this — follow the structure above for guidance
"""
