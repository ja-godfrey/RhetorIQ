# RhetorIQ: Your Writing Enhancement Sidekick 🤖✍️

Welcome to the README for RhetorIQ, your friendly chatbot designed to help you polish and perfect your writing skills! Let's dive into how you can get started with this Streamlit app and make the most out of your writing workshop sessions.

## Getting Started 🚀

Before you can run this app, you'll need a few things:

1. **OpenAI API Key**: Make sure you have an API key from OpenAI. You'll need this to interact with the chatbot.
2. **Streamlit**: This app is built on Streamlit, which makes it super easy to run and deploy.

Once you have your API key, follow these steps:

1. Clone this repository to your local machine.
2. Create a `secrets.toml` file in your `.streamlit` folder with your OpenAI API key like so:

```toml
# .streamlit/secrets.toml
OPENAI_API_KEY="your-super-secret-key"
```

3. Install the required packages using pip:

```bash
pip install openai streamlit
```

4. Run the Streamlit app:

```bash
streamlit run your_script.py
```

## Features 🌟

- **Two Modes**: Choose between 'RhetorIQ' for an AI-driven analysis of rhetorical devices in your writing, or 'Workshop Partner' for constructive feedback sandwiched between compliments.
- **Interactive Chat**: Just type your writing sample and get instant feedback right within the chat interface.
- **Session State Memory**: Your conversation with the chatbot is remembered during the session, so you can pick up where you left off.

## Usage 🖊️

Navigate through the app using the sidebar where you can select the chatbot of your choice:
- 📝 **RhetorIQ**: Focused on enhancing your argumentation skills with rhetorical devices.
- 💬 **Workshop Partner**: Your buddy for well-rounded writing feedback.

After choosing your chatbot, simply input your text and let the magic happen!

## Troubleshooting 🛠️

- If you encounter any errors with the OpenAI API, make sure your API key is valid and correctly placed in `secrets.toml`.
- Ensure you have an internet connection, as the app needs to communicate with OpenAI's servers.

## Contributing 🤝

Love RhetorIQ? Here's how you can contribute:
- **Report Bugs**: If you find a bug, open an issue with the details.
- **Suggest Features**: Have an idea to make RhetorIQ even better? We'd love to hear it!

## Feedback 💌

If you have any feedback, please reach out to us. We're always looking to improve!

## Enjoy Writing ✨

Remember, whether you're drafting an essay, a blog post, or the next bestselling novel, RhetorIQ is here to guide you towards eloquence and flair in your writing!

Let's get writing, and make your words shine! 🌟

---

That's a wrap on our README! Don't forget to star this repo if you find RhetorIQ helpful. Happy writing! 🎉🖋️