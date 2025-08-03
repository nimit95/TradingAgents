#!/usr/bin/env python3
"""
Simple test script to verify Anthropic API key authentication
"""

import os
from langchain_anthropic import ChatAnthropic

def test_anthropic_api():
    """Test if the Anthropic API key is valid"""
    try:
        # Check if API key is set
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            print("❌ ANTHROPIC_API_KEY environment variable is not set")
            return False
        
        print(f"🔑 API Key found (length: {len(api_key)})")
        print(f"🔑 API Key starts with: {api_key[:10]}...")
        
        # Try to create a ChatAnthropic instance
        llm = ChatAnthropic(
            model="claude-3-5-haiku-latest",
            api_key=api_key
        )
        
        # Try a simple test call
        response = llm.invoke("Say 'Hello, API key is working!'")
        print("✅ API key is valid!")
        print(f"📝 Response: {response.content}")
        return True
        
    except Exception as e:
        print(f"❌ API key test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Anthropic API key...")
    success = test_anthropic_api()
    if success:
        print("🎉 API key is working correctly!")
    else:
        print("💥 API key test failed. Please check your key.") 