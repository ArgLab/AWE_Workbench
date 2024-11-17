#!/usr/bin/env python3.10
# Copyright 2022, Educational Testing Service

import awe_workbench
import asyncio
import base64
import websockets
import json
import spacy
import coreferee
import spacytextblob.spacytextblob
import json

from awe_components.components.utility_functions import content_pos
import awe_components.components.lexicalFeatures
import awe_components.components.syntaxDiscourseFeats
import awe_components.components.viewpointFeatures
import awe_components.components.lexicalClusters
import awe_components.components.contentSegmentation
from awe_components.components.utility_functions import content_pos
from awe_workbench.pipeline import pipeline_def



# --- [ CONSTS/VARS ] -------------------------------------------------------------------

HOST = 'localhost'
PORT = 8766
MAX_DATA_LIMIT = 2 ** 24
SPACY_MODEL = 'en_core_web_lg'
COMPONENTS = [el['component'] for el in pipeline_def]
AWE_INFO_KEYS = ['indicator', 'infoType', 'summaryType', 'filters', 'transformations']

# --- [ CLASSES ] -----------------------------------------------------------------------


class parserServer:

    # Initialize
    parser = None
    documents = {} #dict to store parsed documents

    def __init__(self, pipeline_def=[]):

        # Set up the NLP pipeline
        print("initializing NLP pipeline...")
        try:
            self.nlp = spacy.load(SPACY_MODEL)
            for comp in COMPONENTS:
                self.nlp.add_pipe(comp)
        except OSError as e:
            print("There was an error loading 'en_core_web_lg' from spacy.")
            raise OSError() from e
        
        # Start the event loop, and run until the kill command
        print("starting event loop -- use [KILL] command to terminate.")
        asyncio.get_event_loop().run_until_complete(
            websockets.serve(self.run_parser, HOST, PORT, max_size=MAX_DATA_LIMIT))
        print('parser server running...')
        asyncio.get_event_loop().run_forever()
        print('parser server terminated...')

    async def kill(self, websocket):
        """
        Command called to kill the parser server.
        """
        self.parser.close()
        await websocket.send(json.dumps(True))
        await websocket.close()
        exit()
        
    '''
    This is a function that iterates over a JSON with the contents of AWE_INFO objects
    This function also serves the purpose of making all the objects which can be used
    later on (as opposed to creating them later)
    '''
    def getSummaryFeats(self, file_name):
        # Load JSON file
        with open(file_name, 'r') as file:
            data = json.load(file)
        
        summaryFeats = []
        
        # Iterate through each JSON object
        for entry in data:
            indicator = entry.get("indicator")
            filters = entry.get("filters", [])
            transformations = entry.get("transformations", [])
            summary_types = entry.get("summaryTypes")
            
            # Ensure summary_types is a list for the few times it isnt
            if not isinstance(summary_types, list):
                summary_types = [summary_types]
            
            # make the AWE_info objects
            for summary_type in summary_types:
                awe_info_obj = f"doc._.AWE_Info(indicator='{indicator}'"
                
                # Add filters if they exist
                if filters:
                    filter_str = ", ".join([f"('{f[0]}', {f[1]})" for f in filters])
                    awe_info_obj += f", filters=[{filter_str}]"
                    
                # Add transformations if they exist
                if transformations:
                    transform_str = ", ".join([f"{t}" for t in transformations])
                    awe_info_obj += f", transformations=[{transform_str}]"
                
                # Add the summary type
                awe_info_obj += f", summaryType='{summary_type}')"
                
                # Append to the list of created objects
                summaryFeats.append(awe_info_obj)
        return summaryFeats




    # instead of making the summaryLabels array here (since it is rather large) the contents are now 
    # stored in the summaryLabels.txt file
    with open('summaryLabels.txt', 'r') as file:
        summaryLabels = [line.strip().strip(',') for line in file]

    async def run_parser(self, websocket, path):
        # we're making this up here, so that if any of these AWE_info objects are used later
        # we can just grab it from in here instead of creating it in more than one place
        summaryFeats = self.getSummaryFeats('summaryFeatsConfig.json')

        current_doc = ''
        async for message in websocket:

            messagelist = json.loads(message)
            print(messagelist)
            command = messagelist[0] # helps reduce lines a bit
            if command == 'KILL':
                await websocket.send(json.dumps(True))
                await self.kill(websocket)
            elif command == 'CLEARPARSED':
                self.documents.clear()
                await websocket.send(json.dumps(True))
            elif command == 'REMOVE':
                label = messagelist[1]
                if label in self.documents:
                    del self.documents[label]
                await websocket.send(json.dumps(True))
            elif command == 'PARSEONE':
                label = messagelist[1]
                text = current_doc + messagelist[2]
                current_doc = ''
                if label in self.documents:
                    del self.documents[label]
                self.documents[label] = text
                self.documents[label] = text
                doc = self.documents[label]
                await websocket.send(json.dumps(True))
            elif command == 'PARSESET':
                [labels, texts] = messagelist[1]
                for i, text in enumerate(texts):
                    text = texts[i]
                    print('parsed document', str(i+1), 'of', len(texts))
                    if (text is not None and len(text) > 0) and (labels[i]in self.documents):
                        del self.documents[labels[i]]
                    self.documents[labels[i]] = self.nlp(text)
                await websocket.send(json.dumps(True))
            elif command == 'NORMEDSYNTACTICPROFILE':
                # Returns a dictionary containing normalized
                # frequency information (proportionas) for the
                # syntactic relations and categories in the text.
                doc = self.documents[messagelist[1]] # the param here is the label
                await websocket.send(json.dumps(doc._.syntacticProfileNormed))
            elif command == 'DOCSUMMARYLABELS':
                await websocket.send(json.dumps(self.summaryLabels))
            elif command == 'DOCSUMMARYFEATS':
                doc = self.documents[messagelist[1]] # the param here is the label
                summaryFeats = self.getSummaryFeats('summaryFeatsConfig.json')
                await websocket.send(json.dumps(summaryFeats))
            else:
                await websocket.send(False)

if __name__ == '__main__':
    print('parser server loading')
    wsc = parserServer()
