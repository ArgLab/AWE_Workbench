#!/usr/bin/env python3.10
# Copyright 2022, Educational Testing Service

from multiprocessing import Process, Queue

import os
import time

import awe_languagetool.languagetoolServer
import awe_spellcorrect.spellcorrectServer
import awe_workbench.web.parserServer
import argparse


class startServers:

    # Initialize
    p1 = None
    p2 = None
    p3 = None
    queue = None

    def __init__(self):
        queue = Queue()

        pipeline_def = [{'package': 'spacytextblob',
                         'module': 'spacytextblob',
                         'component': 'spacytextblob',
                         'language': 'en'},
                        {'package': 'awe_components.components',
                         'module': 'lexicalFeatures',
                         'component': 'lexicalfeatures',
                         'language': 'en'},
                        {'package': 'awe_components.components',
                         'module': 'syntaxDiscourseFeats',
                         'component': 'syntaxdiscoursefeatures',
                         'language': 'en'},
                        {'package': 'awe_components.components',
                         'module': 'viewpointFeatures',
                         'component': 'viewpointfeatures',
                         'language': 'en'},
                        {'package': 'awe_components.components',
                         'module': 'lexicalClusters',
                         'component': 'lexicalclusters',
                         'language': 'en'},
                        {'package': 'awe_components.components',
                         'module': 'contentSegmentation',
                         'component': 'contentsegmentation',
                        'language': 'en'}]

        # Notes on the modules called here to be added to our parser pipeline

        # from spacytextblob.spacytextblob import SpacyTextBlob
        # https://github.com/SamEdwardes/spaCyTextBlob
        # wrapper for TextBlob, https://github.com/sloria/TextBlob, which offers other NLP services.
        # but the sentiment features contribute something that Spacy does not come with out of the box.
        # SpacyTextBlob sentiment analysis gives subjectivity dimension, not just positive/negative polarity
        # To get this to work with holmes, we need to use forked version of holmes extractor that
        # supports insertion of spacy components into it spacy pipeline.
        #
        # lexicalFeatures
        # Module that adds features reflecting lexical properties to tokens, including
        # the number of syllables, the number of morphemes, the size of morphological
        # word families, the number of word senses, the presence of academic or
        # latinate vocabulary, and other odds and ends such as identifying the
        # root word of a word's word family
        #
        # syntaxDiscourseFeats
        # Module that adds features reflecting syntax and discourse features,
        # such as paragraph length, sentence length and complexity, length of
        # coreference chains between pronouns, number and distriution of transition
        # words, and measures of text cohesion such as cosine similarity of content
        # words between adjacent sentences, before and after transition words, or
        # between adjacent ten-word blocks.
        #
        # viewpointFeatures
        # Module that identifies perspective, tone, stance, subjectivity related
        # elements, including important aspects of argumentation and narrative
        #
        # lexicalClusters
        # Module that clusters the words inside a document by cosine similarity
        # using Spacy's native tok2vec vectors
        #
        # contentSegmentation
        # module that rougly identifies main ideas/supporting ideas/details in
        # argument-style texts.
   
        p1 = Process(target=awe_languagetool.languagetoolServer.runServer, args=())
        p1.start()

        p2 = Process(target=awe_spellcorrect.spellcorrectServer.spellcorrectServer, args=())
        p2.start()

        p3 = Process(target=awe_workbench.web.parserServer.parserServer,
                     args=(),
                     kwargs={'pipeline_def':pipeline_def})
        p3.start()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run AWE Workbench server scripts')

    args = parser.parse_args()

    startServers()
    


