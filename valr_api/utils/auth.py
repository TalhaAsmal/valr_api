"""
Authentication utilities for VALR API
"""
import base64
import hashlib
import hmac
import json
import time
from typing import Dict, Optional, Union


def generate_signature(
    api_secret: str,
    timestamp: int,
    verb: str,
    path: str,
    body: Optional[Union[Dict, str]] = None,
) -> str:
    """
    Generate a signature for the VALR API request
    
    Args:
        api_secret: VALR API secret key
        timestamp: Unix timestamp in milliseconds
        verb: HTTP method (GET, POST, PUT, DELETE)
        path: API endpoint path
        body: Request body for POST/PUT requests
    
    Returns:
        Base64 encoded signature
    """
    # Create the payload string
    if body is None:
        body_str = ""
    elif isinstance(body, dict):
        body_str = json.dumps(body)
    else:
        body_str = body
    
    payload = str(timestamp) + verb.upper() + path + body_str
    
    # Create the signature using HMAC-SHA512
    signature = hmac.new(
        api_secret.encode(),
        payload.encode(),
        hashlib.sha512
    ).digest()
    
    # Base64 encode the signature
    return base64.b64encode(signature).decode()


def get_timestamp() -> int:
    """
    Get current timestamp in milliseconds
    
    Returns:
        Current timestamp in milliseconds
    """
    return int(time.time() * 1000) 