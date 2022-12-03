#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if sentence:
        return len_sentence, sentence[0]
    return len_sentence, None
