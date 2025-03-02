"""
VALR Market Data API endpoints
"""
from typing import Dict, List, Optional


class MarketDataAPI:
    """
    VALR Market Data API endpoints
    """
    
    def __init__(self, client):
        self.client = client
    
    def get_orderbook(self, pair: str) -> Dict:
        """
        Get the current orderbook for a given currency pair
        
        Args:
            pair: Currency pair (e.g., BTCZAR)
            
        Returns:
            Orderbook information
            
        Example:
            {
                "Asks": [
                    {"price": "10001.0", "quantity": "0.1"},
                    ...
                ],
                "Bids": [
                    {"price": "9999.0", "quantity": "0.1"},
                    ...
                ],
                "LastChange": 123456789
            }
        """
        return self.client.get(f"/v1/marketdata/{pair}/orderbook")
    
    def get_orderbook_summary(self, pair: str) -> List[Dict]:
        """
        Get a summary of the current orderbook for a given currency pair
        
        Args:
            pair: Currency pair (e.g., BTCZAR)
            
        Returns:
            Summary of orderbook
        """
        return self.client.get(f"/v1/marketdata/{pair}/orderbook/summary")
    
    def get_trade_history(self, pair: str, limit: Optional[int] = None, skip: Optional[int] = None) -> List[Dict]:
        """
        Get trade history for a given currency pair
        
        Args:
            pair: Currency pair (e.g., BTCZAR)
            limit: Maximum number of trades to return (default is 100, max is 100)
            skip: Number of trades to skip (for pagination)
            
        Returns:
            List of trade history objects
            
        Example:
            [
                {
                    "price": "9999.0",
                    "quantity": "0.001",
                    "currencyPair": "BTCZAR",
                    "tradedAt": "2019-06-28T10:01:09.465Z",
                    "takerSide": "buy",
                    "sequenceId": 123456
                },
                ...
            ]
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if skip is not None:
            params['skip'] = skip
        
        return self.client.get(f"/v1/marketdata/{pair}/tradehistory", params=params)
    
    def get_market_summary(self, pair: Optional[str] = None) -> List[Dict]:
        """
        Get market summary information
        
        Args:
            pair: Optional currency pair to filter results
            
        Returns:
            List of market summary objects
            
        Example:
            [
                {
                    "currencyPair": "BTCZAR",
                    "askPrice": "10000.0",
                    "bidPrice": "9999.0",
                    "lastTradedPrice": "9999.5",
                    "previousClosePrice": "10100.0",
                    "baseVolume": "10.0",
                    "quoteVolume": "100000.0",
                    "high": "10200.0",
                    "low": "9900.0",
                    "created": "2019-08-16T07:22:53.440Z",
                    "changeFromPrevious": "-0.01"
                },
                ...
            ]
        """
        if pair:
            return self.client.get(f"/v1/marketdata/{pair}/marketsummary")
        return self.client.get("/v1/marketdata/marketsummary")
    
    def get_server_time(self) -> Dict:
        """
        Get the current server time
        
        Returns:
            Server time in epoch time (milliseconds)
            
        Example:
            {
                "epochTime": 1562577006335
            }
        """
        return self.client.get("/v1/public/time") 