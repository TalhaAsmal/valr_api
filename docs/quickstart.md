# Quick Start

This guide will help you get started with the VALR API client quickly.

## Initialize the Client

```python
from valr_api import ValrClient

# For public endpoints only (no authentication)
client = ValrClient()

# For authenticated endpoints
client = ValrClient(
    api_key="your_api_key",
    api_secret="your_api_secret"
)
```

## Public API Examples

```python
# Get all supported currencies
currencies = client.public.get_currencies()
print(currencies)

# Get all currency pairs
pairs = client.public.get_currency_pairs()
print(pairs)

# Get market summary
market_summary = client.market_data.get_market_summary()
print(market_summary)

# Get orderbook for a specific pair
orderbook = client.market_data.get_orderbook("BTCZAR")
print(orderbook)
```

## Authenticated API Examples

```python
# Get account balances
balances = client.account.get_balances()
print(balances)

# Get transaction history
transactions = client.account.get_transaction_history(limit=10)
print(transactions)

# Get deposit address
btc_address = client.wallet.get_deposit_address("BTC")
print(btc_address)
```

## Error Handling

```python
from valr_api import ValrClient
from valr_api.exceptions import ValrApiError, ValrAuthenticationError

client = ValrClient(api_key="your_api_key", api_secret="your_api_secret")

try:
    balances = client.account.get_balances()
except ValrAuthenticationError as e:
    print(f"Authentication error: {e}")
except ValrApiError as e:
    print(f"API error: {e}")
```
