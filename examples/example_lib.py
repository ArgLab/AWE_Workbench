import collections
import math
import re
import colorama  # https://pypi.org/project/blessings/ <-- This looks better?
import sys

from awe_workbench.web.websocketClient import websocketClient
from pylt_classifier.languagetoolClient import languagetoolClient

colorama.init()


def initialize():
    """
    Initialize our CorpusSpellcheck and parser objects (for spell-
    correction and parsing with spacy + coreferee and other extensions
    using a modified version of the holmes extractor library. While
    doing so, we initialize a series of lexical databases that support
    some of the metrics we want to capture.
    """
    # Initialize the spellchecker
    spellchecker = websocketClient()
    languagetool = languagetoolClient()

    # Initialize the parser
    parser = websocketClient()
    parser.set_uri("ws://localhost:8766")

    # return spellchecker and parser objects
    return spellchecker, parser, languagetool


# These should not have a space before them, even if they are
# split across tokens, or we've added a space in processing. For
# example, don't is two tokens, corresponding to "do" and "not"
NO_SPACE_BEFORE = [
    ".", ",", ";", ":", "!", "?", " ", "-",
    "'s", "'d", "'ve", "'ll", "'t", "'s", "n't",
    "’s", "’d", "’ve", "’ll", "’t", "’s", "n’t",
    None, "\n"
]

NO_SPACE_AFTER = [' ', '', '\n', '-', None]

SUBSTITUTIONS = [
    ['&nbsp;', ' '],
    [' - ', '-'],
    ['- ', '-'],
    ['"', '" '],
    ['”', '"'],
    ['“', '"'],
    ['  ', ' '],
    ['\n ', '\n']
]


def normalize(text, suffix=""):
    '''
    Correct simple formatting issues, such as extra spaces or different
    characters
    '''
    for token in NO_SPACE_BEFORE:
        if token is None:
            continue
        if suffix.startswith(token):
            text = text.rstrip(" \t")
        while " " + token in text:
            text = text.replace(" " + token, token)

    for source, replacement in SUBSTITUTIONS:
        text = text.replace(source, replacement)

    return text


def ends_with_any(string, items):
    """
    Helper to check if the string ends with any of the items in the list
    """
    return any(string.endswith(item) for item in items
               if item is not None and len(item) > 0)


def starts_with_any(string, items):
    """
    Helper to check if the string starts with any of the items in the list
    """
    if string is None:
        return False
    return any(string.startswith(item) for item in items
               if item is not None and len(item) > 0)


def doctokens_to_text(doctokens):
    '''
    Convert doctokens to text. Returns text and a mapping of tokens
    to posiitons. We actually need two mapping, for the starts and
    stops of tokens, due to spaces (which fall between tokens)
    This is deeply imperfect with spaces around quotes. We don't have
    a quick way to understand opening versus closing
    quotes. Sometimes, we have “ and ”, but with ", we'd want some
    ad-hoc algorithm.
    '''
    text = []
    start_positions = []
    stop_positions = []
    for token, next_token in zip(doctokens, doctokens[1:]+[None]):
        token = token.strip(' ')
        for search, replace in SUBSTITUTIONS:
            token = token.replace(search, replace)
        start_positions.append(len("".join(text)))
        text.append(token)
        stop_positions.append(len("".join(text)))
        if next_token is not None and \
           not starts_with_any(next_token.rstrip(), NO_SPACE_BEFORE) and \
           not ends_with_any(token, NO_SPACE_AFTER) and not \
           token == '':
            text.append(" ")
    start_positions.append(len("".join(text)))
    stop_positions.append(len("".join(text)))
    return "".join(text), start_positions, stop_positions


FEATURE_LIST = {
    "ACADEMICS": {"description": "Academic Words"},
    "ARGUMENTWORDS": {
        "description": "Explicit Argumentation Words",
        "notes": "We will get some explicit argumentation words showing up,"
        + "since the code is based on a wordlist, but there won't"
        + " be a lot"
    },
    "ATTRIBUTIONS": {"description": "Attribution", "type": "binary_map"},
    "CHARACTERWORDS": {"description": "Character Words", "type": "binary_map"},
    "CITES": {"description": "Citations"},
    "CONCRETEDETAILS": {"description": "Concrete Details"},
    "CONTENTSEGMENTS": {"description": "Content Segments"},
    "CORESENTENCES": {"description": "Core Sentences"},
    "DIRECTSPEECHSPANS": {"description": "Direct Speech Spans"},
    "DOCTOKENS": {"description": "Tokens (mostly individual words)"},
    "EMOTIONWORDS": {"description": "Emotion Words", "type": "binary_map"},
    "EXTENDEDCORESENTENCES": {"description": "Extended Core Sentences"},
    "FREQUENCIES": {"description": "Frequencies"},
    "HALROOTFREQS": {"description": "Dunno"},
    "LATINATES": {"description": "Latinates"},
    "LOCATIONS": {"description": "Locations", "type": "binary_map"},
    "NOMINALREFERENCES": {"description": "Nominal References"},
    "PARAGRAPHS": {"description": "Paragraphs"},
    "PERSPECTIVES": {"description": "Perspectives"},
    "POS": {"description": "Part-of-speech tags"},
    "PROMPTLANGUAGE": {"description": "Language from the Prompt"},
    "PROMPTRELATED": {"description": "Language Related to the Prompt"},
    "QUOTEDTEXT": {"description": "Quotes"},
    "SENTENCES": {"description": "Sentences"},
    "SOCIAL_AWARENESS": {"description": "Social"},
    "SOURCES": {"description": "Sources", "type": "binary_map"},
    "TENSECHANGES": {"description": "Tense Changes"},
    "TRANSITIONPROFILE": {"description": "Transition Profile"},
}


def extract_features(parser, text, label):
    processed = {}
    ok = parser.send(['PARSEONE', label, text])
    for feature in FEATURE_LIST:
        processed[feature.lower()] = \
            parser.send([feature, label])
        if FEATURE_LIST[feature].get("type",
                                     None) == "binary_map":
            processed[feature.lower()] = \
                binary_map_to_indexes(processed[feature.lower()])
    ok = parser.send(['REMOVE', label])
    return processed

# Render functions. This allows us to generate our out semantically,
# so that we can later more easily replace these if we wish to generate
# an RTF file, web page, or otherwise.


def em(text):
    return colorama.Fore.BLUE + text + colorama.Fore.RESET


def strong(text):
    return colorama.Fore.GREEN + text + colorama.Fore.RESET


def weak(text):
    return colorama.Fore.YELLOW + text + colorama.Fore.RESET


def hr():
    '''
    Print a rule
    '''
    print(em('-'))


def ul(items):
    '''
    Unordered list, short rendering
    '''
    return weak(" : ").join(items)


def h1(label):
    '''
    Print a header
    '''
    remaining = 54 - len(label)
    left = math.floor(remaining/2)-1
    right = math.floor(remaining/2)-1
    text = "\n"+"-"*left+" "+label+" "+"-"*right
    print(strong(text))


def h2(label):
    '''
    Print a lesser header
    '''
    print(em("\n{label}:".format(label=label)))


def dt(label, text):
    '''
    Print text with a label
    '''
    print("    {label}: {text}".format(label=label, text=text))


HTML_MODE = False  # Eventually, should be an enum of some kind


def render_header():
    '''
    Top of an HTML document if in HTML mode.
    '''
    if HTML_MODE:
        return '<!DOCTYPE html><html><head></head><body>'
    return ""


def render_footer():
    '''
    Bottom of a document if in HTML mode.
    '''
    if HTML_MODE:
        return '</body></html>'
    return ""


def highlight_text(text, highlights, formatter):
    '''
    This is a functon used to highlight things like corrections in
    text. `text` is the source text. `highlights` is a list of
    dictionaries. Each item *must* contain an offset and a length (for
    which text to mark up), and *may* contain additional parameters
    which are passed to the formatter.
    '''
    lastoffset = 0
    lastlength = 0
    output_text = [render_header()]
    for item in highlights:
        source_text_before_highlight = text[lastoffset:item['offset']]
        output_text.append(source_text_before_highlight)

        text_to_highlight = text[item['offset']:item['offset']+item['length']]

        text_with_highlight = formatter(
            text=text_to_highlight,
            item=item
        )
        output_text.append(text_with_highlight)

        lastoffset = item['offset'] + item['length']
        lastlength = item['length']
    output_text.append(text[lastoffset+lastlength:])
    output_text.append(render_footer())

    return "".join(output_text)


def highlight_tokens(tokens, highlights, formatter):
    '''
    This does the same thing as highlight_text, but with stream of
    document tokens, because data formats are insane, and sometimes
    deal with text and sometimes with tokens.
    '''
    pass


def render_correction_item(text, item):
    if HTML_MODE:
        format_string = '"<error class="highlight",+ " type="{label}"' \
                        + ' subtype="{detail}"' \
                        + ' title="{message}">{text}</error>"'
    else:
        format_string = colorama.Fore.RED + \
                        "{text}" \
                        + colorama.Fore.YELLOW \
                        + " ({label}/{detail}: {message})" \
                        + colorama.Fore.RESET
    return format_string.format(
        text=text,
        **item
    )


def render_corrections(text, result, header=None):
    errorcounts = collections.defaultdict(lambda: 0)
    detailcounts = collections.defaultdict(lambda: 0)
    for item in result:
        errorcounts[item['label']] += 1
        detailcounts[item['label'] + '/' + item['detail']] += 1

    dt('Total grammar, usage, mechanics, style errors', len(result))
    h1("Major error categories")

    for key in sorted(errorcounts.keys()):
        dt(key, errorcounts[key])

    h1("Minor error categories")
    for key in sorted(detailcounts.keys()):
        dt(key, detailcounts[key])

    hr()

    h2("Corrections indicated")
    print(highlight_text(text, result, render_correction_item))


def render_transition_item(text, item):
    if HTML_MODE:
        format_string = '<transition type="{tt}">{text}</transition>'
    else:
        format_string = colorama.Fore.GREEN + "{text}" \
                        + colorama.Fore.YELLOW \
                        + "({tt})" \
                        + colorama.Fore.RESET
    return format_string.format(
        text=text,
        **item
    )


def render_token_text_obsolete(tokens):
    '''
    Paul's code to render token text.
    This was pulled out into a function, and later obsoleted.
    # We should remove this once we're happy with the new renderer
    '''
    normalize(' '.join(tokensfixed)).replace('= "',
                                             '="').replace('\n', '<br>\n')


def render_transitions(features, header=None):
    h1("Transitions")
    (text, start_location_map, stop_location_map) = \
        doctokens_to_text(features['doctokens'])
    transition_profile = [
        {
            'offset': start_location_map[item[2]],
            'length': stop_location_map[item[3]]-start_location_map[item[2]],
            'tt': item[4]
        }
        for item in features['transitionprofile'][3]
    ]
    h2("Version with transition words/phrases marked")
    print(highlight_text(text, transition_profile, render_transition_item))

    dt('No of transition words', features['transitionprofile'][0])
    render_histogram_from_dictionary(
        features['transitionprofile'][1],
        label='Types of transitions'
    )
    render_histogram_from_dictionary(
        features['transitionprofile'][2],
        label='Specific transitions used'
    )
    hr()


def render_text(version, label):
    hr()
    print('\n{label} version:\n\n'.format(label=label), version)


def render_summary_statistics(features):
    hr()
    h1("Summary Statistics")
    dt('No. paragraphs', len(features['paragraphs']))
    dt('No. sentences', len(features['sentences']))
    dt('No. words', len(features['doctokens']))


def render_histogram_from_dictionary(dictionary, label=None):
    '''
    Takes a dictionary, with values as numbers (typically, frequencies), and
    renders that.
    '''
    if label is not None:
        h2(label)
    for key, value in dictionary.items():
        dt(key, value)


def render_index_list(features, topic):
    '''
    Show all of the words in an index list, as well as their count
    '''
    h1(FEATURE_LIST[topic.upper()]['description'])
    dt("Occurances", len(features[topic]))
    dt("Words", ul(index_to_words(features['doctokens'], features[topic])))


def binary_map_to_indexes(binary_map):
    '''
    Convert a vector of flags (e.g. [True, False, False, True, False])
    to a vector of locations (e.g. [0,3])
    Returns the location of all `true` items in list `l`
    '''
    return [i for i, x in enumerate(binary_map) if x]


def index_to_words(word_list, index_list):
    '''
    Return all of the words at the indexes contained in the index_list
    '''
    return [word_list[i] for i in index_list]
