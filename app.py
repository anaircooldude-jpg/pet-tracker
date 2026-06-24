import streamlit as st
import pandas as pd
import time
import random

# Set up the page configuration
st.set_page_config(page_title="Super Pet Tracker", page_icon="🐾", layout="centered")

# --- STEP 1: WELCOME SCREEN ---
st.title("🐾 Super Pet Tracker 3000")
st.subheader("Keep your furry and feathered friends safe!")
st.write("Welcome to the classroom demo! Use this app to enroll your pets and track them live anywhere in the world.")

st.divider()

# Initialize a "database" in the background to store enrolled pets
if "pet_list" not in st.session_state:
    st.session_state.pet_list = []

# --- STEP 2: ENROLL YOUR PET ---
st.header("📝 Enroll a New Pet")

col1, col2 = st.columns(2)

with col1:
    pet_name = st.text_input("Pet's Name", placeholder="e.g., Sparky or Flappy")
    pet_type = st.selectbox("What kind of pet?", ["Animal 🐶", "Bird 🦜", "Other 🦎"])

with col2:
    pet_breed = st.text_input("Breed / Species", placeholder="e.g., Golden Retriever, Parakeet")
    owner_name = st.text_input("Classroom Owner Name", placeholder="Your Name")

if st.button("✨ Enroll Pet"):
    if pet_name:
        # Generate random dummy GPS starting points (around a generic city layout)
        dummy_lat = 25.2048 + random.uniform(-0.05, 0.05)
        dummy_lon = 55.2708 + random.uniform(-0.05, 0.05)
       
        # Save pet details
        new_pet = {
            "Name": pet_name,
            "Type": pet_type,
            "Breed": pet_breed,
            "Owner": owner_name,
            "lat": dummy_lat,
            "lon": dummy_lon
        }
        st.session_state.pet_list.append(new_pet)
        st.success(f"Success! {pet_name} has been enrolled and fitted with a dummy GPS collar!")
    else:
        st.error("Please give your pet a name first!")

st.divider()

# --- STEP 3: TRACK PETS USING GPS ---
st.header("🛰️ Live GPS Pet Radar")

if len(st.session_state.pet_list) == 0:
    st.info("No pets enrolled yet. Add a pet above to see them on the GPS map!")
else:
    # Select which pet to track
    pet_names = [pet["Name"] for pet in st.session_state.pet_list]
    selected_pet_name = st.selectbox("Choose a pet to track live:", pet_names)
   
    # Find the selected pet's data
    selected_pet = next(p for p in st.session_state.pet_list if p["Name"] == selected_pet_name)
   
    # Show pet details card
    st.write(f"**Status:** Tracking {selected_pet['Name']} ({selected_pet['Breed']}) belonging to {selected_pet['Owner']}...")
   
    # Simulate a fake "GPS Ping" loading bar for school presentation effect
    with st.spinner("Pinging GPS Satellite..."):
        time.sleep(1) # Dramatic pause!
       
    st.metric(label="GPS Signal Strength", value="📶 Excellent", delta="Ping: 12ms")
   
    # Create a map dataframe for Streamlit
    map_data = pd.DataFrame([{
        'lat': selected_pet['lat'],
        'lon': selected_pet['lon']
    }])
 
    # Render the interactive map
    st.map(map_data)
    st.caption(" can see exactly where your pet is wandering!")
