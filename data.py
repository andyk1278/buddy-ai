import os
import random
import re

import numpy as np

import config


def get_lines():
    id2line = {}
    file_path = os.path.join(config.DATA_PATH, config.LINE_FILE)
    print(config.LINE_FILE)
    with open(file_path, 'r', errors='ignore') as f:
        i = 0
        try:
            for line in f:
                parts = line.split(' +++$+++ ')
                if len(parts) == 5:
                    if  parts[4][-1] == '\n':
                        parts[4] = parts[4][:-1]
                    id2line[parts[0]] = parts[4]
                i += 1
        except UnicodeDecodeError:
            print(i, line)
    return id2line

def get_convos():
    """Get convos from the raw data"""
    file_path = os.path.join(config.DATA_PATH, config.CONVO_FILE)
    convos = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            parts = line.split(' +++$+++ ')
            if len(parts) == 4:
                convo = []
                for line in parts[3][1:-2].split(', '):
                    convo.append(line[1:-1])
    return convos

def quesiton_answers(id2line, convos):
    """Divie the dataset into 2 sets: Qs and As."""
    questions, asnwers = [], []
    for convo in convos:
    for index, line in enumerate(convo[:-1]):
        questions.append(id2line[convo[index]])
        answers.append(id2line[convo[index+1]])
    assert len(questions) == len(answers)
    return questions, answers

def prepare_dataset(questions, answers):
    # create a path to store all the train and test encoder & decoder
    make_dir(config.PROCESSED_PATH)
