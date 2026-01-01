import streamlit as st
import pandas as pd
import sys
import os

# --- PATH BRIDGE ---
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# --- CLIENT IMPORTS (Optimized) ---
@st.cache_resource
def get_clients():
    from backend.api.googlebooks_client import GoogleBooksClient
    from backend.api.openlibrary_client import OpenLibraryClient
    return GoogleBooksClient(), OpenLibraryClient()

try:
    gb_client, ol_client = get_clients()
except Exception as e:
    st.error(f"Initialization Error: {e}")
    st.stop()

# --- STYLED UI ---
st.set_page_config(page_title="HabitRoot Prototype", page_icon="🌿", layout="wide")

# --- INITIALIZE BOOKROOT STORAGE ---
if 'rooted_books' not in st.session_state:
    st.session_state.rooted_books = []

# --- SIDEBAR: BOOKROOT HUB ---
with st.sidebar:
    st.title("📖 BookRoot Hub")
    
    st.subheader("📍 Explore Forests")
    # Cleaned up the radio to match the search logic
    page = st.radio("Choose API Source:", ["Google Books Forest", "Open Library Forest"])
    
    st.divider()

    st.subheader("🌱 Rooted in Library")
    if st.session_state.rooted_books:
        for book_title in st.session_state.rooted_books:
            st.info(f"📗 {book_title}")
        
        if st.button("Clear Garden"):
            st.session_state.rooted_books = []
            st.rerun()
    else:
        st.caption("Your library is empty. Sprout a book to begin!")

# --- SHARED SEARCH UI ---
st.title(f"📚 {page}")
st.write(f"Search this forest to find books to 'water' your habit tree.")

query = st.text_input("Enter keywords (Title, Author, or Genre):", placeholder="e.g. Atomic Habits")

if query:
    with st.spinner(f"Exploring the {page}..."):
        if page == "Google Books Forest":
            df = gb_client.search_books(query, max_results=30)
        else:
            df = ol_client.search(query=query, limit=30)

    # FIXED: Added proper logic to check if results exist
    if df is not None and not df.empty:
        for _, row in df.iterrows():
            with st.container(border=True):
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    img_url = row.get('image_links') if page == "Google Books Forest" else row.get('cover_url')
                    if img_url:
                        st.image(img_url, use_container_width=True)
                    else:
                        st.image("https://via.placeholder.com/150x200?text=No+Cover", use_container_width=True)

                with col2:
                    st.subheader(row.get('title', 'Unknown Title'))
                    
                    author_display = row.get('authors') or row.get('author') or "Unknown Species"
                    st.write(f"**Author(s):** {author_display}")
                    
                    if page == "Google Books Forest":
                        rating = row.get('average_rating')
                        if pd.notnull(rating):
                            stars = '⭐' * int(float(rating))
                            st.write(f"**Rating:** {stars} ({rating})")
                        else:
                            st.write("**Rating:** No nutrients yet 🌱")
                        
                        pages = row.get('page_count')
                        st.write(f"**Pages:** {int(pages) if pd.notnull(pages) else '???'} 📄")
                    else:
                        st.write(f"**Year:** {row.get('year', 'N/A')} | **Popularity:** {row.get('popularity_score', 'N/A')}")

                    with st.expander("🌿 Growth Insights"):
                        if page == "Google Books Forest":
                            desc = row.get('description', "No description available.")
                            st.write(f"**Description:** {str(desc)[:500]}...")
                        else:
                            st.write(f"**First Sentence:** {row.get('first_sentence', 'N/A')}")
                            st.write(f"**Subjects:** {row.get('subjects', 'N/A')}")
                                    
                    # Button Key Safety: Added page to the ID
                    raw_id = row.get('id') if page == "Google Books Forest" else row.get('work_key')
                    button_key = f"add_{raw_id}_{page.replace(' ', '')}"
                    
                    if st.button(f"Sprout this Book", key=button_key):
                        if row['title'] not in st.session_state.rooted_books:
                            st.session_state.rooted_books.append(row['title'])
                            st.balloons()
                            st.rerun() # Refresh to show in sidebar immediately
    else:
        # FIXED: Only shows warning if search was actually performed and failed
        st.warning("No seeds found for this search in this forest.")