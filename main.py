import openai
import streamlit as st

st.set_page_config(
  page_title= "RhetorIQ", 
  page_icon= "📝"
)

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Get writing feedback!")
st.caption("A series of chatbots designed to help your writing style flourish ✍️🤖🌸\n\n Select which chatbot you'd like to talk to on the left.")
menu_selection = st.sidebar.radio("Select Chatbot:", ("RhetorIQ", "Workshop Partner"))

if menu_selection == "RhetorIQ":
    st.title("📝 RhetorIQ 📝")
    if "rhetoriq_messages" not in st.session_state:
        st.session_state["rhetoriq_messages"] = [{"role": "assistant", "content": "Hi! 👋 I'm going to help you add more rhetorical devices to your writing. Paste in a paragraph or two, and let's get started!"}]

    for msg in st.session_state.rhetoriq_messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Enter your writing sample for RhetorIQ"):
        # Construct the user's input message for RhetorIQ
        user_message = f"You are the RhetorIQ teacher. \n\nThe user is going to upload a sample of their writing \ 
        You are going to point out existing rhetorical devices as well as point out options for incorporating new rhetorical devices. \ 
        You draw on your comprehensive knowledge of overlooked and obscure but powerful rhetorical devices (e.g. YES to: acyrologia, hypotyposis, \ 
        prosopopoeia NO to: irony, repetition, exclamation) to suggest which rhetorical devices vould be included in their writing.\n\nThe user \ 
        wants feedback on this piece of writing:\n\n{user_input}"

        st.session_state.rhetoriq_messages.append({"role": "user", "content": user_message})
        st.chat_message("user").write(user_input)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.rhetoriq_messages
            )

            msg = response.choices[0].message
            st.session_state.rhetoriq_messages.append(msg)
            st.chat_message("assistant").write(msg.content)
        except openai.error.OpenAIError as e:
            st.error(f"OpenAI API Error: {e}")

elif menu_selection == "Workshop Partner":
    st.title("🤝 Workshop Partner 🤝")
    if "workshop_messages" not in st.session_state:
        st.session_state["workshop_messages"] = [{"role": "assistant", "content": "Hello! 👋😄 I'm a writing workshop partner. Paste in a few lines of text, and I'll offer some positive and constructive feedback."}]

    for msg in st.session_state.workshop_messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Enter your writing sample for Workshop Partner"):
        # Construct the user's input message for Workshop Partner
        user_message = f"You are the best writing workshop partner of all time. \ 
        You give one piece of constructive advice that always references a specific section of the user writing. \ 
        On either side of the constructive advice are two compliments about writing that was done particularly well.\n\nUser Input:\n\n{user_input}"

        st.session_state.workshop_messages.append({"role": "user", "content": user_message})
        st.chat_message("user").write(user_input)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.workshop_messages
            )

            msg = response.choices[0].message
            st.session_state.workshop_messages.append(msg)
            st.chat_message("assistant").write(msg.content)
        except openai.error.OpenAIError as e:
            st.error(f"OpenAI API Error: {e}")