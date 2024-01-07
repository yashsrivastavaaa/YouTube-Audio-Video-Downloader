import customtkinter
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("800x400")
app.title("YouTube Audio-Video Downloader")
app.config(padx=20,pady=20)
app.resizable(False, False)

def Convert_Click(entry_of_url,combobox_var):
    url = entry_of_url.get()
    video_list = combobox_var.get()
    if(url == ""):
        messagebox.showerror("Error","Please Enter a URL")
    
    elif (video_list == "Video") :
        getVideo = YouTube(url)
        videoStream = getVideo.streams.get_highest_resolution()
        videoStream.download('./Video')
        messagebox.showinfo("Successful", "Downloaded Successfully! You Can Access the Video")
    
    elif (video_list == "Audio") :
        getAudio = YouTube(url)
        audioStream = getAudio.streams.filter(only_audio=True).get_audio_only()
        audioStream.download('./Audio')
        messagebox.showinfo("Successful", "Downloaded Successfully! You Can Access the Audio")
    
    else:
        messagebox.showerror("Error","Please Select Download Type")

text = customtkinter.CTkLabel(app, text="YouTube Audio-Video Downloader",font=('Century Gothic',35))
text.place(relx=0.12, rely=0.10)

entry_of_url = customtkinter.CTkEntry(master=app,corner_radius=10,placeholder_text='Enter URL',font=('Century Gothic',15))
entry_of_url.place(relx=0.05, rely=0.37, relheight=0.10, relwidth=0.91)

video_list = ["Video","Audio"]
combobox_var = StringVar(value="Download Type")
status_combobox = customtkinter.CTkComboBox(app,variable=combobox_var,values=video_list,state="readonly",font=("Century Gothic",18),dropdown_hover_color="blue",dropdown_font=("Century Gothic",18))
status_combobox.place(relx=0.38, rely=0.60, relheight=0.09, relwidth=0.30)

Convert_Button = customtkinter.CTkButton(app,text="Download",command=lambda : Convert_Click(entry_of_url,combobox_var))
Convert_Button.place(relx=0.38, rely=0.82, relheight=0.09, relwidth=0.30)

app.mainloop()
