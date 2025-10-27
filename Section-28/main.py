import speech_recognition as sr
from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer
import asyncio
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Speak in a cheerful and positive tone.",
        input=speech,
        response_format="pcm"
    ) as response:
        await LocalAudioPlayer().play(response)

def main():
    # take user input in form of speech
    # this converts speech to text
    r = sr.Recognizer() 

    # take the Mic access
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        # if the user pauses for 2 seconds, then audio starts to get processed
        r.pause_threshold = 2

        messages = []
        
        while True:
            print("Speak something !")
            audio = r.listen(source)

            print("Processing Audio (STT). . . ")
            stt = r.recognize_google(audio)

            print("You said : ", stt)


            SYSTEM_PROMPT = """

            You're an expert voice agent. You are given the transcript of what user has said using voice. You need to output as if you are a voice agent and whatever output you will provide will be converted back to audio using AI and played back to the user.

            """

            messages.append({"role" : "user", "content" : stt})
            messages.append({"role" : "system", "content" : SYSTEM_PROMPT})

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages
            )

            print("AI Response : ", response.choices[0].message.content)
            asyncio.run(tts(speech=response.choices[0].message.content))

main()