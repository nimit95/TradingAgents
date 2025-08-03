"""
Rate limiting utilities for API calls
"""

import time
import random
from functools import wraps
from typing import Callable, Any
import logging

logger = logging.getLogger(__name__)

def exponential_backoff_retry(max_retries: int = 3, base_delay: float = 1.0):
    """
    Decorator to add exponential backoff retry logic for rate-limited API calls
    
    Args:
        max_retries: Maximum number of retry attempts
        base_delay: Base delay in seconds before exponential backoff
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    
                    # Check if it's a rate limit error
                    if "rate_limit" in str(e).lower() or "429" in str(e):
                        if attempt < max_retries:
                            # Calculate delay with exponential backoff and jitter
                            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                            logger.warning(f"Rate limit hit, retrying in {delay:.2f} seconds (attempt {attempt + 1}/{max_retries + 1})")
                            time.sleep(delay)
                            continue
                        else:
                            logger.error(f"Max retries ({max_retries}) exceeded for rate limit")
                    else:
                        # Not a rate limit error, re-raise immediately
                        raise e
            
            # If we get here, all retries failed
            raise last_exception
        
        return wrapper
    return decorator

def rate_limit_delay(calls_per_minute: int = 60):
    """
    Decorator to add rate limiting delay between API calls
    
    Args:
        calls_per_minute: Maximum calls per minute
    """
    def decorator(func: Callable) -> Callable:
        last_call_time = [0]  # Use list to make it mutable in closure
        
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_time = time.time()
            time_since_last_call = current_time - last_call_time[0]
            
            # Calculate minimum delay between calls
            min_delay = 60.0 / calls_per_minute
            
            if time_since_last_call < min_delay:
                sleep_time = min_delay - time_since_last_call
                logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)
            
            last_call_time[0] = time.time()
            return func(*args, **kwargs)
        
        return wrapper
    return decorator 