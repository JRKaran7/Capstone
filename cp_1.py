import streamlit as st

# Sample data for destinations
destinations = {
    "Paris": {
        "country": "France",
        "top_attractions": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "travel_tips": "Best visited in the spring and fall. Avoid peak summer months.",
        "weather": "Mild in spring, hot in summer, and chilly in winter."
    },
    "Tokyo": {
        "country": "Japan",
        "top_attractions": ["Tokyo Tower", "Shibuya Crossing", "Meiji Shrine"],
        "travel_tips": "Best visited in March for cherry blossoms or in the fall.",
        "weather": "Hot and humid in summer, cool and dry in winter."
    },
    "New York": {
        "country": "USA",
        "top_attractions": ["Statue of Liberty", "Central Park", "Empire State Building"],
        "travel_tips": "New York is great to visit year-round, but avoid winter if you don’t like cold.",
        "weather": "Cold in winter, hot and humid in summer."
    }
}

# Streamlit page setup
st.title("Travel Advisor")

# Search form or dropdown for destination selection
st.sidebar.header("Choose Your Destination")
destination = st.sidebar.selectbox("Select a destination:", list(destinations.keys()))

# Display destination details
st.header(f"Travel to {destination}")

if destination:
    info = destinations[destination]
    st.subheader(f"{destination}, {info['country']}")
    
    st.markdown(f"**Top Attractions:**")
    st.write(", ".join(info['top_attractions']))

    st.markdown(f"**Travel Tips:**")
    st.write(info['travel_tips'])

    st.markdown(f"**Weather Information:**")
    st.write(info['weather'])

# Travel advice section
st.sidebar.header("General Travel Advice")
advice_options = st.sidebar.checkbox("Show Travel Advice")

if advice_options:
    st.subheader("General Travel Tips")
    st.markdown("""
    - **Pack Light:** Take only what you need to avoid baggage fees and stress.
    - **Stay Safe:** Research the safety of the destination and keep your belongings secure.
    - **Learn Basic Phrases:** If traveling abroad, knowing a few words in the local language can be helpful.
    - **Get Travel Insurance:** Always travel with proper insurance for emergencies.
    - **Check Weather Forecasts:** Stay updated on the weather to pack accordingly.
    """)

# Footer
st.sidebar.markdown("Enjoy your trip!")
