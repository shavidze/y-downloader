import tkinter
import customtkinter as ctk
from pytube import YouTube


def on_progress(stream, chunk, byte_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - byte_remaining
    percentage_of_completion = (bytes_downloaded / total_size)*100
    onGoingPercentage = str(int(percentage_of_completion))
    progressPercentage.configure(text=onGoingPercentage+"%")
    progressPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion / 100))


def downloadFn():
    try:
        ytLink = link.get()
        youtubeObj = YouTube(ytLink, on_progress_callback=on_progress)
        video = youtubeObj.streams.get_highest_resolution()
        title.configure(text=youtubeObj.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.config(text="Download Error", text_color="red")


    # System Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# app frame

app = ctk.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI elemetns
title = ctk.CTkLabel(app, text="Paste your youtube link here")
title.pack(padx=10, pady=10)

# link input
url_input = tkinter.StringVar()
link = ctk.CTkEntry(app, width=350, height=40)
link.pack()

# Download button
downloadBtn = ctk.CTkButton(app, text="Download", command=downloadFn)
downloadBtn.pack(padx=10, pady=10)

# progress bar
progressPercentage = ctk.CTkLabel(app, text="0%")
progressPercentage.pack()

progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)
# Finished label
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()
# Run app
app.mainloop()
