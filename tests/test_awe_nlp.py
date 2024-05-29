"""
--- [ Test: test_awe_nlp.py ] -----------------------------------------------------------

Set of corresponding tests for document features found in awe_nlp.py of writingobserver.

Author: Caleb Scott (cwscott3@ncsu.edu)

-----------------------------------------------------------------------------------------
"""

# --- [ IMPORTS ] -----------------------------------------------------------------------

import holmes_extractor.manager as holmes
import unittest
from awe_components.components.utility_functions import print_parse_tree
from awe_workbench.pipeline import pipeline_def

# --- [ CONSTS/VARS ] -------------------------------------------------------------------

holmes_manager = holmes.Manager(
    'en_core_web_lg', 
    perform_coreference_resolution=False, 
    number_of_workers=2, 
    extra_components=pipeline_def
)

# --- [ SETUP ] -------------------------------------------------------------------------

# GRE Sample from https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/sample_responses
holmes_manager.parse_and_register_document(
    document_text="The statement linking technology negatively with free thinking plays on recent human experience over the past century. Surely there has been no time in history where the lived lives of people have changed more dramatically. A quick reflection on a typical day reveals how technology has revolutionized the world. Most people commute to work in an automobile that runs on an internal combustion engine. During the workday, chances are high that the employee will interact with a computer that processes information on silicon bridges that are .09 microns wide. Upon leaving home, family members will be reached through wireless networks that utilize satellites orbiting the earth. Each of these common occurrences could have been inconceivable at the turn of the 19th century.\n\nThe statement attempts to bridge these dramatic changes to a reduction in the ability for humans to think for themselves. The assumption is that an increased reliance on technology negates the need for people to think creatively to solve previous quandaries. Looking back at the introduction, one could argue that without a car, computer, or mobile phone, the hypothetical worker would need to find alternate methods of transport, information processing and communication. Technology short circuits this thinking by making the problems obsolete.\n\nHowever, this reliance on technology does not necessarily preclude the creativity that marks the human species. The prior examples reveal that technology allows for convenience. The car, computer and phone all release additional time for people to live more efficiently. This efficiency does not preclude the need for humans to think for themselves. In fact, technology frees humanity to not only tackle new problems, but may itself create new issues that did not exist without technology. For example, the proliferation of automobiles has introduced a need for fuel conservation on a global scale. With increasing energy demands from emerging markets, global warming becomes a concern inconceivable to the horse-and-buggy generation. Likewise dependence on oil has created nation-states that are not dependent on taxation, allowing ruling parties to oppress minority groups such as women. Solutions to these complex problems require the unfettered imaginations of maverick scientists and politicians.\n\nIn contrast to the statement, we can even see how technology frees the human imagination. Consider how the digital revolution and the advent of the internet has allowed for an unprecedented exchange of ideas. WebMD, a popular internet portal for medical information, permits patients to self research symptoms for a more informed doctor visit. This exercise opens pathways of thinking that were previously closed off to the medical layman. With increased interdisciplinary interactions, inspiration can arrive from the most surprising corners. Jeffrey Sachs, one of the architects of the UN Millenium Development Goals, based his ideas on emergency care triage techniques. The unlikely marriage of economics and medicine has healed tense, hyperinflation environments from South America to Eastern Europe.\n\nThis last example provides the most hope in how technology actually provides hope to the future of humanity. By increasing our reliance on technology, impossible goals can now be achieved. Consider how the late 20th century witnessed the complete elimination of smallpox. This disease had ravaged the human race since prehistorical days, and yet with the technology of vaccines, free thinking humans dared to imagine a world free of smallpox. Using technology, battle plans were drawn out, and smallpox was systematically targeted and eradicated.\n\nTechnology will always mark the human experience, from the discovery of fire to the implementation of nanotechnology. Given the history of the human race, there will be no limit to the number of problems, both new and old, for us to tackle. There is no need to retreat to a Luddite attitude to new things, but rather embrace a hopeful posture to the possibilities that technology provides for new avenues of human imagination.", 
    label='GRE_Sample_Essay'
)

# --- [ CLASSES ] -----------------------------------------------------------------------

class AWENLPTest(unittest.TestCase):
    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='is_academic',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_interactive',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='is_latinate',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_evaluation',summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_emotionword',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_argumentword',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_explicit_argument',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='vwp_statements_of_opinion',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='vwp_statements_of_fact',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',summaryType='counts'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['positive'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['conditional'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['consequential'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['contrastive'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['counterpoint'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['comparative'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['crossreferential'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['illustrative'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['negative'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['emphatic'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['evidentiary'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['general'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['ordinal'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['purposive'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['periphrastic'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['hypothetical'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['summative'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='transitions',filters=[('==', ['introductory'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['ADJ'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['ADV'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['NOUN'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['PROPN'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['VERB'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['NUM'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['ADP'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['CCONJ'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['SCONJ'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['AUX'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='pos_',filters=[('==', ['PRON'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',summaryType='counts'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['Simple'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['SimpleComplexPred'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['SimpleCompoundPred'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['SimpleCompoundComplexPred'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['Compound'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['Complex'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sentence_types',filters=[('==', ['CompoundComplex'])],summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_source',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_attribution',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_cite',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_quoted',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='vwp_direct_speech',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_in_direct_speech',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_tone',filters=[('>', [0.4])],summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_tone',filters=[('<', [-0.4])],summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='concrete_details',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='main_ideas',summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='supporting_ideas',summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='supporting_details',summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='nSyll',filters=[('>', [3])],summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='max_freq',filters=[('<', [4])],summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='sents',summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='delimiter_n',summaryType='total'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='vwp_character',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(indicator='in_past_tense_scope',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='vwp_propositional_attitudes',summaryType='percent'))

    def test_is_academic(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        print(doc._.AWE_Info(infoType='Doc',indicator='vwp_social_awareness',summaryType='percent'))

# --- [ END ] ---------------------------------------------------------------------------