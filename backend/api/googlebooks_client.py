import os
import requests
import pandas as pd
from dotenv import load_dotenv

class GoogleBooksClient:
    """A client to interact with the Google Books API."""

    def __init__(self):
        """Initialize the client and load the API key."""
        load_dotenv()
        self.api_key = os.getenv('GOOGLE_BOOKS_API_KEY')
        self.base_url = "https://www.googleapis.com/books/v1/volumes"
        
        if not self.api_key:
            raise ValueError("API Key not found! Make sure GOOGLE_BOOKS_API_KEY is in your .env file.")

    def search_books(self, query, max_results=10):
        """
        Performs a search and returns a Pandas DataFrame.
        """
        params = {
            'q': query,
            'key': self.api_key,
            'projection': 'full',
            'maxResults': max_results
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return self._parse_results(data)
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return pd.DataFrame()

    def _parse_results(self, data):
        """Internal helper to convert JSON response to a list of dicts."""
        books_extracted = []
        for item in data.get('items', []):
            info = item.get('volumeInfo', {})
            sale = item.get('saleInfo', {})
            access = item.get('accessInfo', {})
            
            record = {
                "id": item.get('id'),
                "title": info.get('title'),
                "authors": ", ".join(info.get('authors', [])),
                "publisher": info.get('publisher'),
                "published_date": info.get('publishedDate'),
                "page_count": info.get('pageCount'),
                "categories": ", ".join(info.get('categories', [])),
                "average_rating": info.get('averageRating'),
                "price": sale.get('retailPrice', {}).get('amount'),
                "currency": sale.get('retailPrice', {}).get('currencyCode'),
                "is_ebook": sale.get('isEbook'),
                "pdf_link": access.get('pdf', {}).get('downloadLink'),
                "viewability": access.get('viewability')
            }
            books_extracted.append(record)
        
        return pd.DataFrame(books_extracted)