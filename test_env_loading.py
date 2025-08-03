#!/usr/bin/env python3
"""
Test script to verify environment variable loading from .env file
"""

import os
from tradingagents.default_config import DEFAULT_CONFIG

def test_env_loading():
    """Test if environment variables are loaded from .env file"""
    print("🧪 Testing environment variable loading...")
    
    # Check if API keys are available
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    google_key = os.getenv('GOOGLE_API_KEY')
    finnhub_key = os.getenv('FINNHUB_API_KEY')
    
    print(f"🔑 ANTHROPIC_API_KEY: {'✅ Set' if anthropic_key else '❌ Not set'}")
    print(f"🔑 OPENAI_API_KEY: {'✅ Set' if openai_key else '❌ Not set'}")
    print(f"🔑 GOOGLE_API_KEY: {'✅ Set' if google_key else '❌ Not set'}")
    print(f"🔑 FINNHUB_API_KEY: {'✅ Set' if finnhub_key else '❌ Not set'}")
    
    # Test the config
    print(f"\n📋 Config loaded:")
    print(f"   - LLM Provider: {DEFAULT_CONFIG['llm_provider']}")
    print(f"   - Deep Think LLM: {DEFAULT_CONFIG['deep_think_llm']}")
    print(f"   - Quick Think LLM: {DEFAULT_CONFIG['quick_think_llm']}")
    print(f"   - Backend URL: {DEFAULT_CONFIG['backend_url']}")
    
    return True

if __name__ == "__main__":
    test_env_loading() 