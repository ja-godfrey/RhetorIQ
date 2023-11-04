import openai
import streamlit as st
import random

model_to_use = "gpt-4" # "gpt-3.5-turbo"

st.set_page_config(
  page_title= "RhetorIQ", 
  page_icon= "📝"
)

openai.api_key = st.secrets["OPENAI_API_KEY"]

menu_selection = st.sidebar.radio("Select Chatbot:", ("Research Topic Helper", "Workshop Partner", "Rhetorical Suggestions"))

if menu_selection == "Rhetorical Suggestions":
    st.title("📝 RhetorIQ 📝")
    st.caption("Upload a few paragraphs of your writing, and RhetorIQ will suggest rhetorical devices for you to incorporate.")
    if "rhetoriq_messages" not in st.session_state:
        st.session_state["rhetoriq_messages"] = [{"role": "assistant", "content": "Hi! 👋 Paste in a paragraph or two, and let's get started!"}]

    for msg in st.session_state.rhetoriq_messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Enter your writing sample for RhetorIQ"):
        # Construct the user's input message for RhetorIQ
        user_message = f"You are the RhetorIQ teacher. \n\nThe user is going to show you a sample of their writing. You are going to point out up to two existing rhetorical devices with examples from the text they showed you. You are then going to offer a few options for incorporating new rhetorical devices. You draw on your comprehensive knowledge obscure and powerful rhetorical devices (e.g. YES to devices such as: acyrologia, hypotyposis, prosopopoeia NO to: irony, repetition, exclamation, metaphor) to suggest which rhetorical devices vould be included in their writing. Unless the user is asking follow-up questions to an on-going conversation, if the user inputs something that doesn't seem like a writing sample, gently and kindly prompt them to upload a paragraph or two of writing for you to look at. You are cheerful and enthusiastic. Occasionally, you'll use an appropriate emoji.\n\nThe user wants feedback on this piece of writing:\n\n{user_input}"

        st.session_state.rhetoriq_messages.append({"role": "user", "content": user_message})
        st.chat_message("user").write(user_input)
        st.info(random.choice(st.session_state["fun_facts"]))

        with st.spinner('Please wait... Reading your writing with care 📝'):
                try:
                    response = openai.ChatCompletion.create(
                        model=model_to_use,
                        messages=st.session_state.rhetoriq_messages
                    )

                    msg = response.choices[0].message
                    st.session_state.rhetoriq_messages.append(msg)
                    st.chat_message("assistant").write(msg.content)
                except openai.error.OpenAIError as e:
                    st.error(f"OpenAI API Error: {e}")

elif menu_selection == "Workshop Partner":
    st.title("🤝 Workshop Partner 🤝")
    st.caption("Upload a few paragraphs of your writing, and Workshop Partner will suggest rhetorical devices for you to incorporate.")
    if "workshop_messages" not in st.session_state:
        st.session_state["workshop_messages"] = [{"role": "assistant", "content": "Hello! 👋😄 Paste in a few lines of text, and I'll offer some positive and constructive feedback. I'm excited to workshop with you!"}]

    for msg in st.session_state.workshop_messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Enter your writing sample for Workshop Partner"):
        # Construct the user's input message for Workshop Partner
        user_message = f"You are the best writing workshop partner of all time. You give one piece of constructive advice that always references a specific section of the user writing. On both sides of the constructive advice you give one compliment about their writing that was done well. Your compliments also always reference the input text. The pattern is compliment, constructive advice, compliment. Each part of the pattern should be clearly demarcated through a list or a new paragraph. If the user inputs something that doesn't seem like a writing sample, gently and kindly prompt them to upload a paragraph or two of writing for you to look at. You are cheerful and enthusiastic. Occasionally, you'll use an appropriate emoji.\n\nUser Input:\n\n{user_input}"

        st.session_state.workshop_messages.append({"role": "user", "content": user_message})
        st.chat_message("user").write(user_input)
        st.info(random.choice(st.session_state["fun_facts"]))

        with st.spinner('Please wait... Reading your writing with care 📝'):
            try:
                response = openai.ChatCompletion.create(
                    model=model_to_use, # gpt-4
                    messages=st.session_state.workshop_messages
                )

                msg = response.choices[0].message
                st.session_state.workshop_messages.append(msg)
                st.chat_message("assistant").write(msg.content)
            except openai.error.OpenAIError as e:
                st.error(f"OpenAI API Error: {e}")

elif menu_selection == "Research Topic Helper":
    st.title("🎓 Research Topic Helper 🎓")
    st.caption("Share your initial thoughts or a vague topic idea, and I will help you formulate a precise thesis statement, research questions, and an abstract.")

    if "research_helper_messages" not in st.session_state:
        st.session_state["research_helper_messages"] = [{"role": "assistant", "content": "Hello! 🧠 Share with me your initial paper topic idea, and I'll assist you in shaping it into a well-defined thesis, research questions, and an abstract."}]

    for msg in st.session_state.research_helper_messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input("Enter your initial topic idea or thoughts here"):
        # Construct the user's input message for Research Topic Helper
        user_message = f"You are the Research Topic Helper. \n\nThe user will provide you with a vague idea or topic they are considering for an academic paper. Your task is to craft a detailed, scholarly thesis statement, formulate two related research questions, and write a concise 100-word abstract to encapsulate their proposed research. Your guidance will help them kick-start their research process with clarity and focus. At the end, acknowledge that there are many other ways to explore this topic-list 3-5 ways in one sentence each. If the user's input is too vague or not suitable for a rigorous, academic paper, kindly ask for more details or clarification. You reject inputs that frame issues in any subjective way (e.g. x is the best, y is the right thing to do, z would have huge impact on humanity) in favor of balanced, evidence-based, thorough analysis. \n\nUser's initial topic idea:\n\n{user_input}"

        st.session_state.research_helper_messages.append({"role": "user", "content": user_message})
        st.chat_message("user").write(user_input)
        st.info(random.choice(st.session_state["fun_facts"]))

        with st.spinner('Please wait... Reading your writing with care 📝'):
            try:
                response = openai.ChatCompletion.create(
                    model=model_to_use,
                    messages=st.session_state.research_helper_messages
                )

                msg = response.choices[0].message
                st.session_state.research_helper_messages.append({"role": "assistant", "content": msg["content"]})
                st.chat_message("assistant").write(msg["content"])
            except openai.error.OpenAIError as e:
                st.error(f"OpenAI API Error: {e}")

if "fun_facts" not in st.session_state:
    st.session_state["fun_facts"] = [
        "Did you know the longest sentence ever published in literature contains 823 words?",
        "The 'IMRaD' structure stands for Introduction, Methods, Results, and Discussion and is the standard for many academic papers.",
        "The oldest known alphabet was developed in central Egypt around 2000 B.C.",
        "The first ever paper was made in China, in the 2nd century B.C.",
        "The average PhD thesis is around 80,000 words long and takes years to complete.",
        "The 'Great Vowel Shift' was a major change in the pronunciation of the English language that took place between 1400 and 1700.",
        "The longest word in Shakespeare's works is 'honorificabilitudinitatibus' from 'Love's Labour's Lost'.",
        "George Bernard Shaw's play 'Pygmalion' is the inspiration for the musical 'My Fair Lady'.",
        "The word 'robot' was first used in Karel Čapek's play 'R.U.R.' ('Rossum's Universal Robots') in 1920.",
        "J.R.R. Tolkien created over 14 languages for the universe of Middle Earth.",
        "The Epic of Gilgamesh, written in ancient Mesopotamia, is one of the oldest known works of literature, dating back to around 2100 BC.",
        "A pangram is a sentence that contains every letter of the alphabet at least once, like 'The quick brown fox jumps over the lazy dog.'",
        "The term 'utopia', denoting an ideal place, comes from the book 'Utopia' by Sir Thomas More, published in 1516.",
        "The first novel ever written on a typewriter was 'The Adventures of Tom Sawyer' by Mark Twain.",
        "The Greek national anthem has 158 verses, and no one in Greece has memorized all of them.",
        "Edgar Allan Poe's 'The Raven' is one of the most parodied poems in English literature.",
        "A biblioklept is a person who steals books.",
        "The 'Oxford comma' is so named because it was traditionally used by printers, readers, and editors at Oxford University Press.",
        "The first recorded use of the word 'hello' dates back to 1826.",
        "Shakespeare added about 1,700 words to the English language by invention or combination.",
        "In the Harry Potter series, 'Dumbledore' is an Old English word for 'bumblebee'.",
        "A 'lexicon' is the vocabulary of a person, language, or branch of knowledge.",
        "The word 'nerd' was first coined by Dr. Seuss in 'If I Ran the Zoo' in 1950.",
        "Stephen King writes 2,000 words a day, even on holidays.",
        "The pen name 'Voltaire' is an anagram of 'Arouet l.j.', a shortened form of the author's real name, François-Marie Arouet."
        "Did you know the longest sentence ever published in literature contains 823 words?",
        "The 'IMRaD' structure stands for Introduction, Methods, Results, and Discussion and is the standard for many academic papers.",
        "The oldest known alphabet was developed in central Egypt around 2000 B.C.",
        "The first ever paper was made in China, in the 2nd century B.C.",
        "The average PhD thesis is around 80,000 words long and takes years to complete.",
        "Shakespeare added about 1,700 words to the English language by invention or combination.",
        "The epic poem 'Mahabharata' is about ten times the length of the 'Iliad' and the 'Odyssey' combined.",
        "'Pride and Prejudice' was originally titled 'First Impressions'.",
        "The dot on top of the letter 'i' is called a tittle.",
        "A pangram is a sentence that contains every letter of the alphabet at least once, like 'The quick brown fox jumps over the lazy dog.'",
        "The first novel ever written on a typewriter is believed to be 'The Adventures of Tom Sawyer'.",
        "A 'bibliopole' is a person who buys and sells books, especially rare ones.",
        "The 'Gothic' in 'Gothic novel' originally referred to the barbarous Germanic tribe, the Goths, and was meant to be derogatory.",
        "Dyslexia, a common learning difficulty can affect reading, writing, and spelling skills, and is not related to intelligence.",
        "J.R.R. Tolkien created over 14 languages for his books.",
        "'Eunoia' is the shortest word in English to contain all five main vowel graphemes.",
        "The word 'alphabet' comes from the first two letters of the Greek alphabet: alpha and beta.",
        "The most expensive book ever purchased was Leonardo da Vinci's 'Codex Leicester', bought by Bill Gates for $30.8 million in 1994.",
        "'Tsundoku' is the Japanese word for the habit of buying books and not reading them, leaving them to pile up.",
        "The Brontë sisters originally published their poems and novels under male pseudonyms.",
        "George Orwell's '1984' and 'Animal Farm' were once banned in the Soviet Union for being critical of communism.",
        "The term 'Utopia', in the literary context, was coined by Sir Thomas More for his 1516 book 'Utopia', describing a fictional island society.",
        "The first known use of 'OMG' was in a 1917 letter to Winston Churchill.",
        "Edgar Allan Poe married his 13-year-old cousin.",
        "The three most read books in the world are 'The Holy Bible', 'Quotations from Chairman Mao Tse-Tung', and 'Harry Potter'.",
        "The name for the love of books is 'bibliophilia', and a lover of books is called a 'bibliophile'.",
        "A 'lexicon' is the vocabulary of a person, language, or branch of knowledge.",
        "'Zyzzyva', a type of South American weevil, is usually the last word listed in many English dictionaries.",
        "The 'Oxford Comma' is a controversial serial comma used before the conjunction in a list of three or more items.",
        "Ernest Vincent Wright's novel 'Gadsby' is over 50,000 words long and doesn't contain the letter 'e'.",
        "Mark Twain's 'Adventures of Huckleberry Finn' was the first major American novel written in vernacular English.",
        "The writing system with the most characters is Chinese, with over 50,000 characters, although you only need to know about 2,000 to read a newspaper.",
        "The earliest surviving work of literature is the 'Epic of Gilgamesh' from ancient Mesopotamia, dating back to around 2100 BC.",
        "An 'epistolary novel' is a novel written as a series of documents, usually letters or diary entries.",
        "The longest word in the Oxford English Dictionary is 'pneumonoultramicroscopicsilicovolcanoconiosis', a lung disease caused by inhaling very fine ash and sand dust.",
        "Stephen King has published over 60 books and has written around 200 short stories.",
        "The first book ever printed is the 'Gutenberg Bible' by Johannes Gutenberg in the 1450s.",
        "Agatha Christie is the best-selling novelist of all time, according to the Guinness World Records.",
        "A 'mondegreen' is a misunderstood or misinterpreted word or phrase resulting from a mishearing of the lyrics of a song.",
        "The 'Chandos portrait' is the most famous image of William Shakespeare, but it is not certain that it actually depicts him."
    ]