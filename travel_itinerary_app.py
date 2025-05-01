import streamlit as st
import openai

# Set your OpenAI API Key
openai.api_key = "your_openai_api_key"

st.title("🧳 AI Travel Itinerary Generator")

# Collect user input
location = st.text_input("Enter your destination (e.g., Kerala, Japan)")
days = st.number_input("Number of days", min_value=1, max_value=30, value=5)
budget = st.text_input("Budget (e.g., ₹30K, $1000)")
interests = st.multiselect("Interests", ["Food", "Beaches", "History", "Nightlife", "Shopping", "Adventure"])
travel_style = st.selectbox("Travel Style", ["Solo", "Couple", "Family", "Backpacking"])

# Submit button
if st.button("Generate Itinerary"):
    with st.spinner("Creating your personalized trip..."):
        prompt = f"""
        Plan a {days}-day itinerary to {location} under {budget}.
        Interests include: {', '.join(interests)}.
        Travel style: {travel_style}.
        Make it fun, local, and detailed with daily plans and food suggestions.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        itinerary = response['choices'][0]['message']['content']
        st.markdown("### ✨ Your Itinerary")
        st.write(itinerary)
# Add this to display a map using Google Static Maps
if location:
    import urllib.parse

    map_location = urllib.parse.quote(location)
    google_maps_api_key = "your_google_maps_api_key"

    map_url = f"https://www.google.com/maps/embed/v1/place?key={google_maps_api_key}&q={map_location}"

    st.markdown("### 📍 Location on Map")
    st.components.v1.iframe(map_url, height=450)
