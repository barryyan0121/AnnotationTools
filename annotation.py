import os
from tkinter import *
from utility.io_utils import read_pdf_and_docx

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

line_labels = {0: 'experience', 1: 'skills', 2: 'education', 3: 'project', 4: 'others', 5: 'language'}


class AnnotatorGui(Frame):
    def __init__(self, master, table_content):

        Frame.__init__(self, master=master)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W + E + N + S)

        for line_index in table_content:
            self.build_line(table_content, line_index)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

    def build_line(self, table_content, line_index):
        (line_content, _) = table_content[line_index][0]

        line_index_label = Label(self.master, width=10, height=1, text=str(line_index))
        self.master.create_window(50, line_index * 35, height=40, width=50, window=line_index_label)

        line_content_text = Text(self.master, width=100, height=1)
        line_content_text.insert(INSERT, line_content)
        self.master.create_window(600, line_index * 35, height=40, width=1050, window=line_content_text)

        def line_label_button_click(_line_index):
            value = table_content[_line_index]
            if len(value) == 1:
                line_label = 0
                table_content[_line_index].append(('', line_label))
                line_label_button["text"] = "Type: " + line_labels[line_label]
            else:
                content, line_label = table_content[_line_index][-1]
                line_label = (line_label + 1) % len(line_labels)
                if content == '':
                    table_content[_line_index][-1] = (content, line_label)
                    line_label_button["text"] = "Type: " + line_labels[line_label]
                else:
                    table_content[_line_index].append(('', line_label))
                    line_label_button["text"] = "Type: " + line_labels[line_label]

        def line_selection_button_click(_line_index, _line_content_text):
            content, label = table_content[_line_index][0]
            if label == 0:
                table_content[_line_index][0] = (content, 1)
            content = _line_content_text.get(SEL_FIRST, SEL_LAST)
            _, label = table_content[_line_index][-1]
            table_content[_line_index][-1] = (content, label)
            table_content[_line_index].append(('', label))

        line_label_button = Button(self.master, text="Type: Unlabeled", width=20,
                                   command=lambda: line_label_button_click(line_index))
        self.master.create_window(1200, line_index * 35, height=40, width=150, window=line_label_button)

        line_selection_button = Button(self.master, text='Generate Annotation', width=20,
                                       command=lambda: line_selection_button_click(line_index, line_content_text))
        self.master.create_window(1350, line_index * 35, height=40, width=150, window=line_selection_button)


def gui_annotate(training_data_dir_path, name, file_content):
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    canvas = Canvas(root, width=170, height=300)
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.grid(row=0, column=0, sticky=W + E + N + S)
    vsb.grid(row=0, column=1, sticky=N + S)

    table_content = {}
    for i in range(len(file_content)):
        line = file_content[i]
        table_content[i + 1] = [(line, 0)]
    AnnotatorGui(canvas, table_content)

    def callback():
        root.destroy()
        output_file_path = os.path.join(training_data_dir_path, name)
        with open(output_file_path, 'wt', encoding='utf8') as f:
            print("Annotated Data")
            for key in table_content:
                value = table_content[key]
                _, label = value[0]
                if label == 1:
                    for count in range(len(value) - 1):
                        line_content, line_label = value[count + 1]
                        if line_content != '':
                            print(str(key) + ',' + line_content + ',' + line_labels[line_label])
                            f.write(str(key) + ',' + line_content + ',' + line_labels[line_label])
                            f.write('\n')

    # Define scroll region AFTER widgets are placed on canvas
    canvas.config(yscrollcommand=vsb.set, scrollregion=canvas.bbox("all"))

    root.protocol("WM_DELETE_WINDOW", callback)
    root.mainloop()


def rename_files(data_dir_path):
    files = os.listdir(data_dir_path)
    pattern = '^(([0-9]|[1-9][0-9]|[1][0-9][0-9]|20[0-0]).txt)$'
    for count, filename in enumerate(files):
        if re.search(pattern, filename) is None:
            src = data_dir_path + '/' + filename
            dst = data_dir_path + '/' + str(count) + ".txt"
            os.rename(src, dst)


def main():
    current_dir = os.path.dirname(__file__)
    current_dir = current_dir if current_dir != '' else '.'
    data_dir_path = current_dir + '/training_data'  # directory to scan for any pdf files

    # rename_files(data_dir_path)

    annotated_data_dir_path = current_dir + '/annotated_data'
    collected = read_pdf_and_docx(data_dir_path, annotated_data_dir_path, command_logging=True, callback=lambda name, file_path, file_content: {
        gui_annotate(annotated_data_dir_path, name, file_content)
    })
    print('count: ', len(collected))


if __name__ == '__main__':
    main()
