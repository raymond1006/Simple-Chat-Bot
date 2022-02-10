# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:09:58 2021

@author: raymond
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('Raymond Chatbot')

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english',
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "./knowledge/emotion.yml",
    "./knowledge/conversation.yml",

    "./knowledge/food.yml"
) 
