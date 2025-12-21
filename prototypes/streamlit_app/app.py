import streamlit as st
import pandas as pd
import sys
import os

# --- UPDATED PATH BRIDGE ---
# Current file is in: bookroot/prototypes/streamlit_app/app.py
# We need to add 'bookroot' to the path to import 'backend.api.open_library_client'
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))

if root_dir not in sys.path:
    sys.path.append(root_dir)

try:
    # Adjusted import to match your nested directory: backend -> api -> client
    from backend.api.openlibrary_client import OpenLibraryClient
    client = OpenLibraryClient()
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.info(f"Looking in: {root_dir}")
    st.stop()

# --- STREAMLIT UI ---
st.set_page_config(page_title="BookRoot Prototype", page_icon="🌿", layout="wide")

# Sidebar for Book Progress
with st.sidebar:
    st.title("🌳 Your Growth")
    xp = st.slider("Tree XP", 0, 1000, 120)
    level = (xp // 100) + 1
    st.progress(xp / 1000)
    st.write(f"**Current Level:** {level}")
    
    stages = {1: "🌱 Seedling", 2: "🌿 Sprout", 3: "🌳 Sapling"}
    st.write(f"Stage: {stages.get(level, '🌳 Mature Tree')}")

st.title("📚 BookRoot Discovery")
st.write("Find books to 'water' your Book tree.")

query = st.text_input("Search for a book (Title, Author, or Subject):")

if query:
    with st.spinner("Searching..."):
        df = client.search(query=query, limit=60)
    
    if not df.empty:
        for _, row in df.iterrows():
            with st.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    if row['cover_url']:
                        st.image(row['cover_url'])
                with col2:
                    st.subheader(row['title'])
                    st.write(f"**Author:** {row['author']} | **Year:** {row['year']}")
                    st.write(f"**Popularity Score:** {row['popularity_score']}")
                    
                    with st.expander("AI Insights"):
                        st.write(f"**First Sentence:** {row['first_sentence']}")
                        st.write(f"**Subjects:** {row['subjects']}")
                    
                    if st.button(f"Add to Tree", key=row['work_key']):
                        st.balloons()
                        st.success(f"Added to growth queue!")
            st.divider()
    else:
        st.warning("No results found.")
