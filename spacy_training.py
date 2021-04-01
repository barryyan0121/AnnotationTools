import spacy
import os
import random

from spacy.scorer import Scorer
from spacy.training import Example
from pathlib import Path

epochs = 30
# nlp = spacy.blank("en")
nlp = spacy.load('en_core_web_sm')
LABEL = "SKILL"
optimizer = nlp.resume_training()
ner = nlp.get_pipe("ner")
ner.add_label(LABEL)
current_dir = os.path.dirname(__file__)
data_path = current_dir + '/training_data'
annotated_path = current_dir + '/annotated_data'
train_data = []
for f in os.listdir(data_path):
    csv = f.replace('.txt', '.csv')
    data_str = os.path.join(data_path, f)
    csv_str = os.path.join(annotated_path, csv)
    data_file = open(data_str, 'r', errors='ignore')
    csv_file = open(csv_str, 'r', errors='ignore')
    data_lines = data_file.readlines()
    csv_lines = csv_file.readlines()
    # print('doing csv file ' + csv)
    for csv_line in csv_lines:
        if csv_line == '\n':
            continue
        arr = csv_line.split(',')
        line_number = arr[0].strip()
        line_data = arr[1].strip()

        sentence = data_lines[int(line_number) - 1]
        start_index = sentence.find(line_data)
        end_index = start_index + len(line_data) - 1
        if start_index != -1:
            dictionary = (sentence, {"entities": [(start_index, end_index, "SKILL")]})
            train_data.append(dictionary)
    data_file.close()
    csv_file.close()
    # print('done with file ' + f)
    # print(train_data)

label_path = os.path.join(os.path.dirname(__file__), 'data.txt')
trained_file = open(label_path, 'w+')
trained_file.write(str(train_data))
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*unaffected_pipes):

    # Training for 30 iterations
    for epoch in range(epochs):
        # shuffling examples  before every iteration
        random.shuffle(train_data)
        losses = {}
        examples = []
        for text, annots in train_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annots)
            examples.append(example)

        nlp.update(examples, sgd=optimizer, drop=0.35, losses=losses)
        print("Losses ({}/{})".format(epoch + 1, epochs), losses)

output_dir = Path('content/')
nlp.to_disk(output_dir)
print("Saved model to", output_dir)
