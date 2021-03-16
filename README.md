# AnnotationTools
## Features
This GUI annotation tool takes `pdf/docx/txt` files and helps annotate them
for `NER` tasks in NLP. The NER tags can be changed in annotation.py simply
by changing values of a dictionary.
Here are the example labels for a resume file.
```python3
line_labels = {0: 'experience', 1: 'skills', 2: 'education', 3: 'project', 4: 'others'}
```
## Usage
The GUI tool package can be installed with
```commandline
pip install tkinter
```
To use the `docx` and `pdf` features, simply install these two packages.
```commandline
pip install python-docx
```
```commandline
pip install pdfminer
```
The original training data should be inside the folder `training_data`,
and the generated data will be inside `annotated_data`.