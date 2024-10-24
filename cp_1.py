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

# Sidebar quiz or destination selection
st.sidebar.header("Choose Your Adventure")

quiz_option = st.sidebar.radio("Would you like to take a quiz or select a destination?", ('Take a Quiz', 'Select Destination'))

if quiz_option == 'Take a Quiz':
    st.header("Find Your Ideal Destination")

    # Quiz questions
    q1 = st.radio("What kind of weather do you prefer?", ("Mild", "Hot", "Cold"))
    q2 = st.radio("What activities do you enjoy?", ("City landmarks", "Nature and outdoor activities", "Cultural experiences"))
    q3 = st.radio("What's your travel budget?", ("Budget", "Mid-range", "Luxury"))

    if st.button("Get Recommendation"):
        if q1 == "Mild" and q2 == "City landmarks" and q3 == "Mid-range":
            st.success("We recommend visiting **Paris, France**!")
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg", use_column_width=True)
        elif q1 == "Hot" and q2 == "Cultural experiences" and q3 == "Budget":
            st.success("We recommend visiting **Tokyo, Japan**!")
            st.image("https://upload.wikimedia.org/wikipedia/commons/7/74/Tokyo_Tower_and_Zojo-ji_Temple.jpg", use_column_width=True)
        elif q1 == "Cold" and q2 == "City landmarks" and q3 == "Luxury":
            st.success("We recommend visiting **New York, USA**!")
            st.image("https://upload.wikimedia.org/wikipedia/commons/a/a1/Statue_of_Liberty_7.jpg", use_column_width=True)
        else:
            st.warning("We're still figuring out your perfect match! Try adjusting your answers or explore a new destination.")

else:
    # Destination selection
    st.sidebar.header("Select a Destination")
    destination = st.sidebar.selectbox("Choose a destination:", list(destinations.keys()))

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
