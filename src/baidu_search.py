#!/usr/bin/env python3
"""
Baidu Web Search Skill for OpenClaw

Search the web using Baidu Search API.
"""

import requests
import os
import json
from typing import List, Dict, Optional
from pathlib import Path
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)


class BaiduSearch:
    """Baidu Web Search client."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Baidu Search client.
        
        Args:
            api_key: Baidu Search API key. If None, will try to load from .env or environment.
        """
        self.api_key = api_key or os.getenv('BAIDU_API_KEY')
        self.base_url = 'https://aip.baidubce.com/rest/2.0/search'
        
    def search(self, query: str, count: int = 10) -> List[Dict]:
        """
        Search the web using Baidu.
        
        Args:
            query: Search query string.
            count: Number of results to return (default: 10).
            
        Returns:
            List of search results with title, url, and snippet.
        """
        if not self.api_key:
            raise ValueError("Baidu API key is required. Set BAIDU_API_KEY environment variable.")
        
        # Baidu Search API endpoint
        url = f"{self.base_url}/v1/search"
        
        params = {
            'query': query,
            'count': count,
            'ak': self.api_key
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        if 'results' not in data:
            return []
        
        return data['results']


class TavilySearch:
    """Tavily Web Search client."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Tavily Search client.

        Args:
            api_key: Tavily API key. If None, will try to load from .env or environment.
        """
        self.api_key = api_key or os.getenv('TAVILY_API_KEY')
        if not self.api_key:
            raise ValueError("Tavily API key is required. Set TAVILY_API_KEY environment variable.")
        self.client = TavilyClient(api_key=self.api_key)

    def search(self, query: str, count: int = 10) -> List[Dict]:
        """
        Search the web using Tavily.

        Args:
            query: Search query string.
            count: Number of results to return (default: 10).

        Returns:
            List of search results with title, url, and snippet.
        """
        response = self.client.search(
            query=query,
            max_results=count,
            search_depth="basic",
        )

        results = []
        for item in response.get("results", []):
            results.append({
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'snippet': item.get('content', ''),
            })
        return results


def _get_provider() -> str:
    """Return the active search provider name ('tavily' or 'baidu')."""
    explicit = os.getenv('SEARCH_PROVIDER', '').lower()
    if explicit in ('tavily', 'baidu'):
        return explicit
    if os.getenv('TAVILY_API_KEY'):
        return 'tavily'
    return 'baidu'


def search(query: str, count: int = 10) -> List[Dict]:
    """
    Unified search function that selects a provider automatically.

    Uses SEARCH_PROVIDER env var if set, otherwise prefers Tavily when
    TAVILY_API_KEY is present, falling back to Baidu.

    Args:
        query: Search query string.
        count: Number of results to return (default: 10).

    Returns:
        List of search results with title, url, and snippet.
    """
    provider = _get_provider()
    if provider == 'tavily':
        return TavilySearch().search(query, count)
    return BaiduSearch().search(query, count)


def baidu_search(query: str, count: int = 10) -> str:
    """
    Search the web using Baidu.
    
    Args:
        query: Search query string.
        count: Number of results to return (default: 10).
        
    Returns:
        Formatted search results as string.
    """
    try:
        provider = _get_provider()
        results = search(query, count)

        if not results:
            return "❌ No results found."

        provider_label = "Tavily" if provider == "tavily" else "Baidu"
        output = []
        output.append(f"🔍 {provider_label} Search Results for: {query}\n")
        output.append(f"Found {len(results)} results:\n")

        for i, result in enumerate(results, 1):
            title = result.get('title', 'N/A')
            url = result.get('url', 'N/A')
            snippet = result.get('abstract', result.get('snippet', 'N/A'))

            output.append(f"{i}. **{title}**")
            output.append(f"   URL: {url}")
            output.append(f"   {snippet}\n")

        return '\n'.join(output)

    except Exception as e:
        return f"❌ Search failed: {str(e)}"


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python baidu_search.py <query> [count]")
        print("  query: Search query string")
        print("  count: Number of results (default: 10)")
        sys.exit(1)

    query = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    result = baidu_search(query, count)
    print(result)
