import tkinter as tk


class App:
    def __init__(self, master):
        root=tk.Tk()
        self.text = tk.Text(root)
        self.text.pack()
        self.button = tk.Button(root, text="Get Selection", command=self.OnButton)
        self.button.pack()
        root.mainloop()

    def OnButton(self):
        print("selected text: '%s'" % self.text.get(tk.SEL_FIRST, tk.SEL_LAST))


app=App()