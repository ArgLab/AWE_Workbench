import awe_workbench.parser.manager as holmes
import unittest
    
holmes_manager = holmes.Manager(
    'en_core_web_lg', perform_coreference_resolution=False, number_of_workers=2)

# GRE Sample from https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/sample_responses
holmes_manager.parse_and_register_document(
            document_text="The statement linking technology negatively with free thinking plays on recent human experience over the past century. Surely there has been no time in history where the lived lives of people have changed more dramatically. A quick reflection on a typical day reveals how technology has revolutionized the world. Most people commute to work in an automobile that runs on an internal combustion engine. During the workday, chances are high that the employee will interact with a computer that processes information on silicon bridges that are .09 microns wide. Upon leaving home, family members will be reached through wireless networks that utilize satellites orbiting the earth. Each of these common occurrences could have been inconceivable at the turn of the 19th century.\n\nThe statement attempts to bridge these dramatic changes to a reduction in the ability for humans to think for themselves. The assumption is that an increased reliance on technology negates the need for people to think creatively to solve previous quandaries. Looking back at the introduction, one could argue that without a car, computer, or mobile phone, the hypothetical worker would need to find alternate methods of transport, information processing and communication. Technology short circuits this thinking by making the problems obsolete.\n\nHowever, this reliance on technology does not necessarily preclude the creativity that marks the human species. The prior examples reveal that technology allows for convenience. The car, computer and phone all release additional time for people to live more efficiently. This efficiency does not preclude the need for humans to think for themselves. In fact, technology frees humanity to not only tackle new problems, but may itself create new issues that did not exist without technology. For example, the proliferation of automobiles has introduced a need for fuel conservation on a global scale. With increasing energy demands from emerging markets, global warming becomes a concern inconceivable to the horse-and-buggy generation. Likewise dependence on oil has created nation-states that are not dependent on taxation, allowing ruling parties to oppress minority groups such as women. Solutions to these complex problems require the unfettered imaginations of maverick scientists and politicians.\n\nIn contrast to the statement, we can even see how technology frees the human imagination. Consider how the digital revolution and the advent of the internet has allowed for an unprecedented exchange of ideas. WebMD, a popular internet portal for medical information, permits patients to self research symptoms for a more informed doctor visit. This exercise opens pathways of thinking that were previously closed off to the medical layman. With increased interdisciplinary interactions, inspiration can arrive from the most surprising corners. Jeffrey Sachs, one of the architects of the UN Millenium Development Goals, based his ideas on emergency care triage techniques. The unlikely marriage of economics and medicine has healed tense, hyperinflation environments from South America to Eastern Europe.\n\nThis last example provides the most hope in how technology actually provides hope to the future of humanity. By increasing our reliance on technology, impossible goals can now be achieved. Consider how the late 20th century witnessed the complete elimination of smallpox. This disease had ravaged the human race since prehistorical days, and yet with the technology of vaccines, free thinking humans dared to imagine a world free of smallpox. Using technology, battle plans were drawn out, and smallpox was systematically targeted and eradicated.\n\nTechnology will always mark the human experience, from the discovery of fire to the implementation of nanotechnology. Given the history of the human race, there will be no limit to the number of problems, both new and old, for us to tackle. There is no need to retreat to a Luddite attitude to new things, but rather embrace a hopeful posture to the possibilities that technology provides for new avenues of human imagination.", label='GRE_Sample_Essay')


class LexicalFeatureTest(unittest.TestCase):

    def test_clusterInfo(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        clusterInfo = [[14, 3.6747192922762837, ['technology', 'emerge', 'market', 'nanotechnology'], [3, 46, 161, 212, 229, 247, 286, 307, 333, 334, 405, 537, 552, 589, 606, 623, 640, 695]], [51, 2.7333009865760953, ['thinking', 'assumption', 'argue', 'hypothetical', 'think', 'fact', 'consider', 'layman', 'actually', 'imagine'], [7, 154, 183, 196, 216, 284, 411, 459, 468, 538, 561, 594, 598]], [33, 2.6008002462296087, ['human', 'earth', 'humanity'], [11, 112, 147, 239, 277, 288, 408, 545, 579, 595, 628, 647, 701]], [31, 2.4556616643929057, ['computer', 'wireless', 'network', 'mobile', 'phone', 'communication', 'digital', 'internet'], [82, 105, 106, 189, 192, 193, 210, 255, 257, 414, 421, 435]], [8, 2.0428751576292563, ['creativity', 'create', 'imagination', 'idea', 'inspiration'], [235, 299, 356, 386, 409, 429, 475, 500, 702]], [43, 1.9424460431654675, ['century', 'history', '19th', 'obsolete', '20th', 'prehistorical'], [16, 25, 128, 129, 221, 565, 566, 582, 644]], [39, 1.82370820668693, ['smallpox', 'ravage', 'vaccine', 'eradicate'], [572, 577, 591, 603, 615, 620]], [35, 1.7955112219451372, ['reliance', 'negate', 'preclude'], [159, 162, 227, 233, 273, 550]], [32, 1.7208413001912044, ['free', 'information', 'exchange', 'portal', 'visit'], [6, 85, 207, 427, 436, 439, 452, 593, 601]], [50, 1.5462672143029716, ['recent', 'past', 'change', 'previous', 'prior', 'late', 'day'], [10, 15, 33, 139, 172, 243, 564, 583]], [5, 1.5203226807322372, ['utilize', 'ability', 'convenience', 'provide', 'complete'], [108, 145, 250, 531, 539, 569, 696]], [20, 1.5090853095164767, ['dramatically', 'reach', 'increase', 'achieve'], [35, 103, 158, 329, 471, 548, 559]], [22, 1.5081563558017852, ['quandary', 'problem', 'issue', 'concern'], [173, 220, 294, 301, 340, 382, 659]], [37, 1.4794685990338161, ['medical', 'doctor', 'emergency', 'care', 'triage', 'medicine'], [438, 451, 467, 502, 503, 504, 513]], [15, 1.4314115308151094, ['revolutionize', 'introduction', 'introduce', 'generation', 'revolution', 'advent'], [48, 179, 317, 349, 415, 418]], [49, 1.3787281935846938, ['typical', 'common', 'example', 'popular', 'base'], [42, 117, 244, 310, 434, 498, 530]], [12, 1.2813941568426448, ['inconceivable', 'surprising', 'unlikely', 'impossible'], [122, 341, 481, 508, 554]], [29, 1.2761613067891782, ['allow', 'free', 'permit'], [248, 287, 367, 406, 441]], [19, 1.2591815320041972, ['play', 'run', 'chance', 'attempt', 'Goals', 'goal'], [8, 61, 72, 134, 496, 555]], [34, 1.1895910780669146, ['oppress', 'unfettered', 'dare', 'embrace'], [371, 385, 596, 687]], [64, 1.1611030478955007, ['silicon', 'micron', 'satellite', 'orbit'], [87, 92, 109, 110]], [4, 1.1552680221811462, ['link', 'bridge', 'complex', 'tense'], [2, 88, 136, 381, 516]], [3, 1.142595978062157, ['process', 'method', 'processing', 'circuit', 'technique'], [84, 203, 208, 214, 505]], [11, 1.086484137331595, ['automobile', 'car', 'transport'], [59, 187, 205, 253, 315]], [62, 1.053324555628703, ['proliferation', 'dependence', 'dependent', 'pathway'], [313, 352, 363, 457]], [46, 1.0183299389002036, ['South', 'Eastern', 'battle', 'fire', 'retreat'], [521, 524, 608, 635, 676]], [52, 1.008827238335435, ['commute', 'workday', 'leave', 'arrive'], [54, 70, 96, 477]], [41, 0.9193054136874362, ['WebMD', 'Jeffrey', 'Sachs'], [431, 484, 485]], [6, 0.9153318077803205, ['wide', 'tackle', 'target'], [93, 292, 618, 669]], [42, 0.9153318077803203, ['UN', 'Millenium', 'America', 'Europe'], [493, 494, 522, 525]], [60, 0.9024252679075014, ['scientist', 'research', 'interdisciplinary', 'discovery'], [389, 445, 472, 633]], [58, 0.898876404494382, ['surely', 'necessarily', 'exist', 'likewise'], [18, 232, 305, 351]], [16, 0.8923591745677636, ['reduction', 'efficiency', 'energy', 'elimination'], [142, 270, 330, 570]], [38, 0.8913649025069637, ['patient', 'symptom', 'heal', 'disease'], [442, 446, 515, 575]], [36, 0.8810572687224669, ['self', 'exercise', 'attitude', 'posture'], [444, 455, 680, 690]], [10, 0.8771929824561403, ['horse', 'buggy', 'race'], [344, 348, 580, 648]], [57, 0.8645533141210374, ['creatively', 'efficiently', 'systematically'], [169, 267, 617]], [2, 0.8560727661851258, ['reveal', 'release', 'previously'], [44, 245, 259, 462]], [18, 0.8398950131233597, ['global', 'warming', 'oil'], [325, 336, 337, 354]], [45, 0.8376963350785341, ['nation', 'state', 'rule', 'minority'], [357, 359, 368, 372]], [17, 0.8341056533827617, ['taxation', 'economic', 'hyperinflation'], [365, 511, 518]], [26, 0.8264462809917356, ['statement', 'informed'], [1, 133, 398, 450]], [30, 0.8209338122113904, ['additional', 'require', 'allow', 'limit'], [260, 383, 423, 654]], [44, 0.8040201005025126, ['member', 'party', 'group', 'politician'], [100, 369, 373, 391]], [24, 0.8016032064128256, ['Development', 'future', 'plan', 'implementation'], [495, 543, 609, 638]], [56, 0.7778317938745746, ['mark', 'give', 'number'], [237, 626, 642, 657]], [13, 0.7679180887372014, ['alternate', 'possibility', 'avenue'], [202, 693, 699]], [61, 0.7563025210084033, ['negatively', 'interact', 'interaction'], [4, 79, 473]], [48, 0.7540056550424129, ['lived', 'life', 'family', 'live'], [28, 29, 99, 265]], [7, 0.7469654528478057, ['quick', 'look', 'short', 'make'], [38, 175, 213, 218]], [9, 0.72, ['corner', 'architect', 'draw'], [482, 490, 611]], [21, 0.6891271056661562, ['dramatic', 'scale', 'unprecedented'], [138, 326, 426]], [27, 0.6854531607006855, ['combustion', 'engine', 'fuel'], [65, 66, 321]], [63, 0.6772009029345373, ['reflection', 'internal', 'contrast'], [39, 64, 395]], [23, 0.6751687921980495, ['solve', 'demand', 'solution'], [171, 331, 378]], [54, 0.6181318681318683, ['experience', 'environment'], [12, 519, 629]], [28, 0.614334470989761, ['turn', 'open', 'close'], [125, 456, 463]], [25, 0.6134969325153373, ['hope', 'hopeful'], [534, 540, 689]]]
        self.assertEqual(doc._.clusterInfo,clusterInfo)

    def test_mean_main_cluster_span(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.mean_main_cluster_span,199.44444444444446)

    def test_median_main_cluster_span(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.median_main_cluster_span,187.0)

    def test_max_main_cluster_span(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.max_main_cluster_span,375)

    def test_min_main_cluster_span(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.min_main_cluster_span,3)

    def test_stdev_main_cluster_span(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.stdev_main_cluster_span,108.55696375214704)

    def test_devwords(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        devwords = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]

        self.assertEqual(doc._.devwords,devwords)

    def test_mean_devword_nsyll(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.mean_devword_nsyll,2.488095238095238)

    def test_median_devword_nsyll(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.median_devword_nsyll,2)

    def test_max_devword_nsyll(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.max_devword_nsyll,7)

    def test_min_devword_nsyll(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.min_devword_nsyll,1)

    def test_stdev_devword_nsyll(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.stdev_devword_nsyll,1.1517599311925815)

    def test_mean_devword_nmorph(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.mean_devword_nmorph,1.5720164609053497)

    def test_median_devword_nmorph(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.median_devword_nmorph,1)

    def test_max_devword_nmorph(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.max_devword_nmorph,4)

    def test_min_devword_nmorph(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.min_devword_nmorph,1)

    def test_stdev_devword_nmorph(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.stdev_devword_nmorph,0.7537501612026646)

    def test_mean_devword_nsenses(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.mean_devword_nsenses,7.4574898785425106)

    def test_median_devword_nsenses(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.median_devword_nsenses,5)

    def test_max_devword_nsenses(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.max_devword_nsenses,57)

    def test_min_devword_nsenses(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.min_devword_nsenses,1)

    def test_stdev_devword_nsenses(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.stdev_devword_nsenses,8.979041460178047)

    def test_mean_devword_token_freq(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.mean_devword_token_freq,4.463452380952381)

    def test_median_devword_token_freq(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.median_devword_token_freq,4.645)

    def test_max_devword_token_freq(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.max_devword_token_freq,5.66)

    def test_min_devword_token_freq(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.min_devword_token_freq,1.39)

    def test_stdev_devword_token_freq(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.stdev_devword_token_freq,0.7984509315879537)

    def test_mean_devword_concreteness(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.mean_devword_concreteness,3.895841018849968)

    def test_median_devword_concreteness(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.median_devword_concreteness,3.758)

    def test_max_devword_concreteness(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.max_devword_concreteness,6.485)

    def test_min_devword_concreteness(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.min_devword_concreteness,3.758)

    def test_stdev_devword_concreteness(self):
        doc = holmes_manager.get_document('GRE_Sample_Essay')
        self.assertEqual(doc._.stdev_devword_concreteness,1.1279373211867478)

