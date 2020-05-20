# Microsoft Build 2020 Speech Recognition with Python
# See github.com/JimBobBennett for source code

# Notes from Live Session May 19th, 2020, 8:15pm
# Why is Voice Recognition so hard? Countless difference dialects, pronounc.
# for every word, tonal languages, CONTEXT.
# Solution: Machine Learning --> millions of hours trained on models

# Microsoft Cog Services: https://azure.microsoft.com/en-us/services/cognitive-services/?&ef_id=CjwKCAjwh472BRAGEiwAvHVfGqTutKWY7gW9KuJ-0ftz0IL8r4kKQsxua-sB1iLq9WJrWNmiSEUnvRoCj34QAvD_BwE:G:s&OCID=AID2000128_SEM_CjwKCAjwh472BRAGEiwAvHVfGqTutKWY7gW9KuJ-0ftz0IL8r4kKQsxua-sB1iLq9WJrWNmiSEUnvRoCj34QAvD_BwE:G:s&gclid=CjwKCAjwh472BRAGEiwAvHVfGqTutKWY7gW9KuJ-0ftz0IL8r4kKQsxua-sB1iLq9WJrWNmiSEUnvRoCj34QAvD_BwE
# Take advantage of SDK built by Microsoft
# Python pip --> talk to AI models with python
# requirements.txt --> tells which packages to use in main part of code

# Azure is huge data center, runs in many places around the world
# Tell key (your service in Azure) --> "Keys and Endpoint", 5 hr speech-text FREE

# Other Capabilities: Speech to Text --> translate to multiple languages!!!
# Text to Speech to Text?????? Yes, that too.

# Definition: "Container" --> wrapped up app for you, can use offline
    # basically can use Speech To Text locally
    # Must apply to use (public gated preview)
    # This costs money $$$ :(, need to connect now and then for billing information
    # https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-container-support?tabs=luis

# Note: you will need to be a student --> limited but free Azure account 
# You will need pip + python, updated
# Set environment variables via terminal

import os
import time
import logging
from dotenv import load_dotenv
from variables import *
import azure.cognitiveservices.speech as speechsdk

# Load speech key + region
load_dotenv()
# key = os.getenv('KEY_AZURE_SPEECH')
# region = os.getenv('REGION_AZURE_SPEECH')
key = KEY_AZURE_SPEECH
region = REGION_AZURE_SPEECH

stop = False # stop the app when "stop" is spoken

# prints spoken text to the screen
def recognized(args):
    global stop # why global?
    text = args.result.text 
    print(text)
    if text == "Stop.": # will this catch things like "stop..."?
        stop = True
    
logging.info(key)
logging.info(region)

# Speech configuration using key and region
speech_config = speechsdk.SpeechConfig(
    subscription = key,
    region = region,
    speech_recognition_language='en-US') # English US

# Speech recognizer initialize
rec = speechsdk.SpeechRecognizer(speech_config = speech_config)

# Connect up the recognized event
rec.recognized.connect(recognized)

# Continuous recognition --> app runs in infinite loop until stopped
rec.start_continuous_recognition()

print("Speech Recognition App")

# Loop until we hear stop
while not stop:
    time.sleep(0.05) # originally set to 0.1