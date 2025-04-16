import streamlit as st

st.set_page_config(page_title="🌱 Growth Mindset Challenge", layout="centered")

st.title("🌱 Growth Mindset Challenge")
st.markdown("Welcome! Each day brings a new challenge to grow your mindset. Reflect, learn, and grow. 💪")

# Challenge dictionary
challenges = {
    1: {
        "title": "Reframe a Failure",
        "description": "Think of a recent failure or setback. What did you learn from it?"
    },
    2: {
        "title": "Learn Something New",
        "description": "Try something completely new today — a skill, a recipe, or even a new word. What was it like to be a beginner?"
    },
    3: {
        "title": "Embrace Struggle",
        "description": "Pick something difficult. Don’t avoid it — break it down and try one piece of it."
    },
    4: {
        "title": "Use 'Yet'",
        "description": "Find something you feel you 'can’t do'. Add **yet** to the sentence. How does that change your perspective?"
    },
    5: {
        "title": "Feedback is a Gift",
        "description": "Ask someone for feedback — or give thoughtful feedback to someone. What did you learn from the exchange?"
    },
    6: {
        "title": "Celebrate Effort",
        "description": "Reflect on something you worked hard on this week. Effort matters more than results."
    },
    7: {
        "title": "Reflect & Share",
        "description": "Reflect on your journey. What mindset shifts have you noticed? Share your thoughts."
    }
}

# Day selection
selected_day = st.selectbox("Choose a day:", list(challenges.keys()), format_func=lambda x: f"Day {x}: {challenges[x]['title']}")

# Show selected challenge
challenge = challenges[selected_day]
st.header(f"Day {selected_day}: {challenge['title']}")
st.markdown(challenge["description"])

# Reflection input
reflection = st.text_area("📝 Your Reflection", height=200, placeholder="Write your thoughts here...")

# Submit button
if st.button("Save Reflection"):
    if reflection.strip() == "":
        st.warning("Please write something before submitting.")
    else:
        st.success("✅ Reflection saved (not really — unless you connect a database 😉)")

# Footer
st.markdown("---")

