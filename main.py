import os
from pytubefix import *
from io import BytesIO
import customtkinter
from customtkinter import filedialog
from PIL import Image #biblioteca para colocar as imagens na interface
import requests
import moviepy.editor as mpe

yt = None
yt_title = None
yt_thumbail_url = None
folder = "videos/"
res = "480p" #resolução padrão

def search():
    global yt
    yt = YouTube(url_entry.get())

    if yt == "":
        print("Informe a URL primeiro!")
        
    else:
        try:           
            yt_title = yt.title
            yt_thumbail_url = yt.thumbnail_url

            response = requests.get(yt.thumbnail_url)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)

            thumb_image = customtkinter.CTkImage(
                light_image=img,
                size=(320, 180)
            )

            thumb_label.configure(image=thumb_image)
            thumb_label.image = thumb_image #aqui a gente mostra a imagem
        
        except Exception as erro:
            print(f"Imagem não pode ser carregada: {erro}")

        #title
        try:
            video_title.configure(text=yt.title)

        except Exception as erro:
            print(f"Não foi possível coletar o nome do vídeo: {erro}")

def getResolution(choice):
    global res
    res = resOptions.get()
    print(res)
    return res

def getFolder():
    global folder
    folder = "videos/"
    folder = filedialog.askdirectory()

    if folder == "":
        folder = "videos/"
        file_entry.configure(placeholder_text="videos/")
    
    print(folder)

    file_entry.configure(placeholder_text=folder)

def downloadVideo():
    global res, yt, folder

    if yt: #verifying if yt has a value (url)
        # print(f'Resolution: {res}\nVideo: {yt.embed_url}\nFolder: {folder}')
        video = yt.streams.filter(res=res, file_extension="mp4").first()
        audio = yt.streams.get_audio_only()

        video.download(output_path=folder)
        audio.download(output_path=folder)

        video_folder = f'{folder}/{yt.title}.mp4'
        audio_folder = f'{folder}/{yt.title}.m4a'
        print(f'{video_folder}\n{audio_folder}')

        video = mpe.VideoFileClip(video_folder)
        audio = mpe.AudioFileClip(audio_folder)
        final = video.set_audio(audio)

        final.write_videofile(f"videos/{yt.title}_{res}.mp4")

        os.remove(video_folder)
        os.remove(audio_folder)

    else:
        print("Informe a URL primeiro")

# =====================
#      INTERFACE
# =====================

app = customtkinter.CTk()
app.geometry("320x490") #thumbnail 1280x720 (320x180)
app.title("Youtube Downloader")
app.resizable(False, False)

#Responsividade usando grids
app.grid_columnconfigure(0, weight=3, minsize=300) #sets width to 75% on the first column
app.grid_columnconfigure(1, weight=1, minsize=20) #sets width to 25% on the second


url_entry = customtkinter.CTkEntry(app, placeholder_text="Cole aqui a URL do vídeo...")
url_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

search_button = customtkinter.CTkButton(app, text="🔎", command=search)
search_button.grid(row=0, column=1, padx=5, pady=10, sticky="ew")


#placeholder pro thumbnail
thumb_image = customtkinter.CTkImage(
                light_image=Image.open("img/placeholder_thumbnail.png"),
                size=(320, 180)
            )

thumb_label = customtkinter.CTkLabel(app, text="") #aqui a gente mostra a imagem
thumb_label.grid(row=1, column=0, columnspan=2, sticky="ew")

thumb_label.configure(image=thumb_image)
thumb_label.image = thumb_image

# Title
video_title = customtkinter.CTkLabel(app, 
    text="Cole a URL acima pra mostrar o título do vídeo", 
    font=("Roboto", 12))
video_title.grid(row=2, pady=10, columnspan=2, sticky="ew")

# Resolution
resLabel = customtkinter.CTkLabel(app, 
    text="Escolha a Resolução:")
resLabel.grid(row=4, padx=5, pady=10, sticky="ew")

resOptions = customtkinter.CTkComboBox(app, 
    values=['144p', '240p', '480p', '720p'], 
    command=getResolution)

resOptions.grid(row=5, padx=5, pady=1, columnspan=2, sticky="ew")

# Folder selection
file_label = customtkinter.CTkLabel(app, 
    text="Escolha o diretório:")
file_label.grid(row=6, padx=5, pady=10, sticky="ew")

file_entry = customtkinter.CTkEntry(app, 
    placeholder_text="videos/")
file_entry.grid(row=7, column=0, padx=5, sticky="ew")

file_button = customtkinter.CTkButton(app, 
    text="📁", 
    command=getFolder)
file_button.grid(row=7, column=1, padx=5, sticky="ew")


# Download button
download_button = customtkinter.CTkButton(app, text="BAIXAR", command=downloadVideo)
download_button.grid(row=8, padx=5, pady=20, columnspan=2, sticky="ew")

app.mainloop()
