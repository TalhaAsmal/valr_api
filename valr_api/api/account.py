"""
VALR Account API endpoints
"""
from typing import Dict, List, Optional


class AccountAPI:
    """
    VALR Account API endpoints
    """
    
    def __init__(self, client):
        self.client = client
    
    def get_balances(self, subaccount_id: Optional[str] = None) -> List[Dict]:
        """
        Get the account balances
        
        Args:
            subaccount_id: Optional subaccount ID
            
        Returns:
            List of account balances
            
        Example:
            [
                {
                    "currency": "BTC",
                    "available": "0.1",
                    "reserved": "0.0",
                    "total": "0.1"
                },
                ...
            ]
        """
        return self.client.get("/v1/account/balances", auth_required=True, subaccount_id=subaccount_id)
    
    def get_transaction_history(
        self,
        skip: int = 0,
        limit: int = 100,
        currency: Optional[str] = None,
        transaction_types: Optional[List[str]] = None,
        subaccount_id: Optional[str] = None,
    ) -> Dict:
        """
        Get transaction history
        
        Args:
            skip: Number of transactions to skip (for pagination)
            limit: Maximum number of transactions to return (default is 100, max is 100)
            currency: Filter by currency
            transaction_types: Filter by transaction types
            subaccount_id: Optional subaccount ID
            
        Returns:
            Dictionary containing transaction history and pagination info
            
        Example:
            {
                "transactions": [
                    {
                        "transactionType": "WITHDRAWAL",
                        "currency": "BTC",
                        "amount": "0.01",
                        "fee": "0.0001",
                        "timestamp": "2019-06-28T10:01:09.465Z",
                        "status": "COMPLETED",
                        ...
                    },
                    ...
                ],
                "isLastPage": true
            }
        """
        params = {
            "skip": skip,
            "limit": limit,
        }
        
        if currency:
            params["currency"] = currency
            
        if transaction_types:
            params["transactionTypes"] = ",".join(transaction_types)
            
        return self.client.get(
            "/v1/account/transactionhistory",
            params=params,
            auth_required=True,
            subaccount_id=subaccount_id,
        )
    
    def get_trade_history(
        self,
        pair: str,
        skip: int = 0,
        limit: int = 100,
        subaccount_id: Optional[str] = None,
    ) -> Dict:
        """
        Get trade history for a specific currency pair
        
        Args:
            pair: Currency pair (e.g., BTCZAR)
            skip: Number of trades to skip (for pagination)
            limit: Maximum number of trades to return (default is 100, max is 100)
            subaccount_id: Optional subaccount ID
            
        Returns:
            Dictionary containing trade history and pagination info
            
        Example:
            {
                "trades": [
                    {
                        "price": "9999.0",
                        "quantity": "0.001",
                        "currencyPair": "BTCZAR",
                        "tradedAt": "2019-06-28T10:01:09.465Z",
                        "side": "buy",
                        "orderId": "123456",
                        ...
                    },
                    ...
                ],
                "isLastPage": true
            }
        """
        params = {
            "skip": skip,
            "limit": limit,
        }
        
        return self.client.get(
            f"/v1/account/{pair}/tradehistory",
            params=params,
            auth_required=True,
            subaccount_id=subaccount_id,
        )
    
    def get_subaccounts(self) -> List[Dict]:
        """
        Get all subaccounts
        
        Returns:
            List of subaccounts
            
        Example:
            [
                {
                    "id": "123456",
                    "label": "Trading Account",
                    "isDefault": true,
                    ...
                },
                ...
            ]
        """
        return self.client.get("/v1/account/subaccounts", auth_required=True) 