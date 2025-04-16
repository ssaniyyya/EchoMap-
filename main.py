import streamlit as st
from map_utils import get_location_details, create_map
from narration_utils import narrate_location
from ui_utils import get_accessibility_icons, get_tips, get_sign_language_resources
from favorites import save_favorite, get_favorites

# Set page config and theme
st.set_page_config(page_title="EchoMap+ - Assistive Map Companion", page_icon="🗺️", layout="wide")

# Background and styles
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #f0f8ff, #e6f7ff);
}
.title {
    color: #1e3d59;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    color: #1e3d59;
    font-size: 20px;
}
.section-header {
    font-size: 24px;
    color: #3a3a3a;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# UI Content
icons = get_accessibility_icons()
tips = get_tips()
resources = get_sign_language_resources()

st.markdown(f"<h1 class='title'>{icons['map']} EchoMap+ – Assistive Map Companion</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='subtitle'>Empowering {icons['visually']} visually, {icons['hearing']} hearing, and {icons['speech']} speech impaired users to explore locations independently.</p>", unsafe_allow_html=True)

# Session State for current place
if "current_place" not in st.session_state:
    st.session_state.current_place = ""

# Form for location
with st.form("location_form"):
    place = st.text_input("Type a location to explore:", "")
    language = st.selectbox("Choose narration language:", ["English", "Hindi", "Marathi"])
    submit = st.form_submit_button("Explore")

if submit and place:
    lat, lon, name = get_location_details(place)
    if lat and lon:
        st.session_state.current_place = name

        st.markdown(f"### {icons['location']} Location: {name}")
        m = create_map(lat, lon, name)
        st.components.v1.html(m._repr_html_(), height=400)

        # Narration
        narration_text = f"The location is {name}. Latitude is {lat} and longitude is {lon}."
        st.markdown(f"### {icons['info']} Narration")
        st.success(narration_text)
        narrate_location(narration_text, language)
    else:
        st.error("Could not find the location. Please try a different name.")

# Save button (after explore)
if st.session_state.current_place:
    if st.button("⭐ Save to Favorites"):
        save_favorite(st.session_state.current_place)
        st.success(f"'{st.session_state.current_place}' added to favorites!")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Accessibility Tips", "Sign Language Resources", "⭐ Saved Favorites", "About EchoMap+"])

with tab1:
    st.markdown("### Accessibility Tips")
    for tip in tips:
        st.info(tip)

with tab2:
    st.markdown("### Sign Language Resources")
    for title, link in resources.items():
        st.write(f"**{title}**: [Visit]({link})")

with tab3:
    st.markdown("### ⭐ Your Saved Favorite Locations")
    favorites = get_favorites()
    if favorites:
        for fav in favorites:
            st.write(f"🔖 {fav}")
    else:
        st.info("No favorites saved yet.")

with tab4:
    st.markdown("### About EchoMap+")
    st.write("""
EchoMap+ is a lightweight assistive mapping companion designed for accessibility.
It supports voice narration, readable on-screen guidance, and visual simplification for:
- Visually impaired users (voice output)
- Hearing impaired users (text narration)
- Speech impaired users (keyboard input)

This project focuses on inclusive, minimal, and offline-compatible design using data science tools.
    """)

