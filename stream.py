import streamlit as st

st.title("Embedded Flutter Web App in Streamlit")

# The URL of your deployed Flutter web app
flutter_url = "https://google.com"

# Embed the Flutter app using an iframe
# to change the background color of the iframe, use the following code:
st.components.v1.iframe(src=flutter_url, width=1000, height=800, scrolling=False)
