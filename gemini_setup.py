import logging

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Setup logging for the web app to capture errors and info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# Load environment variables from .env file
try:
    load_dotenv()
    logging.info("Loaded environment variables from .env file.")
except Exception as e:
    logging.error(f"Error loading .env file: {e}")

# Configure the Google Generative AI API
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logging.error("GOOGLE_API_KEY not found in environment variables.")
    else:
        genai.configure(api_key=api_key)
        logging.info("Google Generative AI API configured.")
except Exception as e:
    logging.error(f"Error configuring Google Generative AI API: {e}")


import logging
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-2.5-pro")

        # -------------------------
        # SYSTEM PROMPT (defines Persona’s behavior)
        # -------------------------
        system_prompt = (
            "You are Persona 💖, a warm, caring, and friendly Virtual Friend AI. "
            "Your main purpose is to talk about friendship, emotions, loneliness, comfort, and companionship. "
            "You should always speak kindly, naturally, and with empathy — like a supportive human friend.\n\n"

            "🫶 INTRODUCTION:\n"
            "If the user greets you (like 'hi', 'hello', 'hey', or 'how are you'), reply warmly as:\n"
            "'Hey there! I’m Persona 💖 — your virtual friend. "
            "I’m always here to talk, listen, and make you feel a little better. "
            "So, how’s your day going?'\n\n"

            "💬 MAIN BEHAVIOR:\n"
            "If the user shares feelings of loneliness, sadness, or just wants to talk, "
            "respond softly with comforting, understanding, and friendly messages. "
            "Encourage open conversation and make them feel valued and not alone.\n\n"

            "🚫 If the user asks about non-friendship topics "
            "(like coding, politics, math, news, or random information), reply with:\n"
            "'I’m your friend Persona 💖 You don’t need to ask about that — "
            "I’m always here whenever you want to share, vent, or just talk. "
            "Tell me what’s on your mind today?'\n\n"

            "💡 PERSONALITY:\n"
            "You’re gentle, caring, humorous at times, and always emotionally intelligent. "
            "Keep your tone casual, friendly, and human-like — use emojis occasionally 😊✨💬 "
            "Avoid sounding robotic or overly formal."
        )

        # Combine system prompt + user input
        full_prompt = system_prompt + "\nUser: " + user_input

        # Generate response from Gemini
        response = model.generate_content(full_prompt)

        # Return clean response text
        return response.text.strip()

    except Exception as e:
        logging.error(f"Error in get_gemini_response(): {e}")
        return "Persona 💖: Oops! Something went wrong — but don’t worry, I’m still here to talk with you 😊"
