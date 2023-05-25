import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Function to generate a pick-up line
def generate_pickup_line(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=50,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Streamlit UI
def main():
    st.title("Pick-Up Line Generator")

    # Get user input
    user_input = st.text_input("You:", "")

    if user_input.lower() == "quit":
        st.text("Chatbot: Goodbye!")
    else:
        # Generate pick-up line
        prompt = "Generate a pick-up line using the word '{}'.".format(user_input)
        response = generate_pickup_line(prompt)

        if response:
            st.text("Chatbot: " + response)
        else:
            st.text("Chatbot: I'm sorry, I couldn't come up with a pick-up line. Can you try another word?")

if __name__ == "__main__":
    main()
