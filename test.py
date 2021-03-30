from pathlib import Path
import spacy
from spacy.scorer import Scorer
from spacy.training import Example


def evaluate(ner_model, examples):
    scorer = Scorer()
    for sents, ents in examples:
        doc = ner_model.make_doc(sents)
        example = Example.from_dict(doc, {"entities": ents['entities']})
        print(scorer.score(example))


output_dir = Path('pretrained_model')
print("Loading from", output_dir)
nlp_blanked = spacy.load(output_dir)
doc = nlp_blanked("""FEI PENG




GRAPHIC DESIGNER /
Fei Peng Faye0315@gmail.com (415)425-7456
feipengdesign.com

OBJECTIVE /
I�m seeking a position as a junior designer that focuses on visual design, branding design and UI/UX design in a company where I can utilize my skills and contribute to a creative design team.





EDUCATION / 
MFA
Academy of Art University, San Francisco
Graphic Design and Digital Media

BFA
Hubei University of Technology, China Computer Art Design

EXPERIENCE /
BLUE WANDER
Helping BlueWander with the design of its product, website, and communication materials.
www.bluewander.life
Position: Graphic Designer Consultant / June 2018 - Currently

ROBOT GYMS
Created a brand system for this company including a logo system, advertising brochures and class lists. Character design, layout design and organize published books.
robotgyms.com
Position: Graphic Designer (Freelance) / Sep 2017 - Currently

PAPER CULTURE
Review overall design aesthetic including colors, typography and
layout - making suggestions and changes where appropriate. Review customer files for typographical errors, grammar, style suggestions, and missing information. Provide feedback directly to customers via email
paperculture.com
Position: Associate Designer / Apr 2018� July 2018

SKILLS /
Adobe Creative Cloud, Google Suite

LANGUAGES /
English, Mandarin Chinese

INTERESTS /
Traveling, Play Traditional Music Instrument, Skiing

REFERENCES /
Furnished upon request.
""")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
