import sys
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

matcher.add("greet", None, [{"LOWER": "hello"}],
                            [{"LOWER": "hi"}],
                            [{"LOWER": "hey"}],
                            [{"LOWER": "hai"}])

matcher.add("product", None, [{"LOWER": "ej2"}],
                            [{"LOWER": "essential"}, {"LOWER": "js"}])


responses = {
    "greet": "Hello there... How may I help you?",
    "product": "What do you wish to know about ",
    "default": "Sorry, I don't quite understand what you mean..."
}

# Pattern Matcher
def predict(query):
    resp = ''
    doc = nlp(query)
    matches = matcher(doc)
    if (len(matches) == 0):
        print(responses["default"])
        resp = responses["default"] 
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        resp = "Intent: " + string_id + "\n"
        cur_resp = responses[string_id] + (span.text if string_id == "product" else "")
        resp = resp + "\n" + cur_resp
    return resp
