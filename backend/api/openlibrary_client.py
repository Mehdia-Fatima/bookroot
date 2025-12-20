import requests
import pandas as pd

class OpenLibraryClient:
    """
    A client to interact with the Open Library Search API and 
    return data as structured DataFrames or Lists.
    """
    
    BASE_URL = "https://openlibrary.org/search.json"

    def __init__(self):
        self.session = requests.Session()

    def search(self, query=None, title=None, author=None, limit=10, advanced=True):
        """
        Executes search and returns a Pandas DataFrame with advanced fields.
        """
        # Define fields to fetch - (Added missing quotes from your draft)
        fields = [
            "key", "title", "author_name", "author_key", "first_publish_year",
            "edition_count", "subject", "ratings_average", "ratings_count",
            "readinglog_count", "want_to_read_count", "currently_reading_count",
            "already_read_count", "language", "number_of_pages_median",
            "first_sentence", "cover_i", "publisher", "publish_date", 
            "person", "place", "time"
        ]
        
        params = {
            "limit": limit,
            "fields": ",".join(fields)
        }
        
        if query: params["q"] = query
        if title: params["title"] = title
        if author: params["author"] = author

        try:
            response = self.session.get(self.BASE_URL, params=params)
            response.raise_for_status()
            docs = response.json().get('docs', [])
            
            return self._process_to_dataframe(docs)
            
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return pd.DataFrame()

    def _process_to_dataframe(self, docs):
        """Internal helper to clean data into a table format."""
        rows = []
        for doc in docs:
            # Helper to join list fields into strings for easier NLP cleaning later
            def safe_join(field_name):
                val = doc.get(field_name, [])
                return ", ".join(val) if isinstance(val, list) else str(val)

            rows.append({
                "title": doc.get("title"),
                "author": safe_join("author_name"),
                "author_key": safe_join("author_key"),
                "year": doc.get("first_publish_year"),
                "editions": doc.get("edition_count", 0),
                "rating_avg": round(doc.get("ratings_average", 0), 2) if doc.get("ratings_average") else None,
                "rating_count": doc.get("ratings_count", 0),
                "want_to_read": doc.get("want_to_read_count", 0),
                "currently_reading": doc.get("currently_reading_count", 0),
                "already_read": doc.get("already_read_count", 0),
                "readinglog_count": doc.get("readinglog_count", 0),
                "pages": doc.get("number_of_pages_median"),
                "language": safe_join("language"),
                "publisher": safe_join("publisher"),
                "subjects": safe_join("subject"),
                "people": safe_join("person"),
                "places": safe_join("place"),
                "times": safe_join("time"),
                "first_sentence": doc.get("first_sentence"),
                "cover_url": f"https://covers.openlibrary.org/b/id/{doc.get('cover_i')}-L.jpg" if doc.get("cover_i") else None,
                "work_key": doc.get("key")
            })
            
        df = pd.DataFrame(rows)
        
        # --- FEATURE ENGINEERING FOR YOUR APP ---
        # Create a 'popularity_score' for your prediction model
        if not df.empty:
            df['popularity_score'] = df['rating_count'] + df['want_to_read'] + df['already_read']
            
        return df