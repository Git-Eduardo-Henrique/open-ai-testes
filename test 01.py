import openai
from tkinter import *

resolution = ["1080","720"]


def submit():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=str(question.get()),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_label["text"] = str(response["choices"][0]["text"])


openai.api_key = "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"

window = Tk()
window.geometry(f'{resolution[0]}x{resolution[1]}')

question = Entry(window)
response_label = Label(window, text="", font="Arial 10")
submit = Button(window, text="SUBMIT", font="Arial 10", background="green",
                command=submit)

question.place(x=0, y=0, height=50, width=int(resolution[0]) - 100)
submit.place(x=int(resolution[0])-100, y=0, height=50, width=100)
response_label.place(x=0, y=60)

window.mainloop()