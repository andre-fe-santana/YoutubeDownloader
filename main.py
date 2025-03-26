from pytubefix import *
from io import BytesIO
import customtkinter
from PIL import Image, ImageTk #biblioteca para colocar as imagens na interface
import requests


def getURL():
    yt = YouTube(url_entry.get()) #objeto da API Youtube
    print(yt.title)
    print(yt.thumbnail_url)

    response = requests.get(yt.thumbnail_url)
    response.raise_for_status()
    img_data = BytesIO(response.content) 
    img = Image.open(img_data)

    if yt:
        #thumbnail
        try:            
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
        

app = customtkinter.CTk()
app.geometry("320x540") #thumbnail 1280x720 (320x180)
app.title("Youtube Downloader")

#Responsividade usando grids
app.grid_columnconfigure(0, weight=2)
app.grid_columnconfigure(1, weight=2)
app.grid_columnconfigure(2, weight=1)


url_entry = customtkinter.CTkEntry(app, placeholder_text="Cole aqui a URL do vídeo...")
url_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

search_button = customtkinter.CTkButton(app, text="Buscar", command=getURL)
search_button.grid(row=0, column=1, padx=5, pady=10)

thumb_label = customtkinter.CTkLabel(app, text="") #aqui a gente mostra a imagem
thumb_label.grid(row=1, column=0, columnspan=2, sticky="ew")

video_title = customtkinter.CTkLabel(app, text="")
video_title.grid(row=2, padx=10, pady=10, sticky="w")

# PyTube
#yt = YouTube(input("Cole aqui sua url:"))
#print(yt.title)
#print(yt.thumbnail_url)
#stream = yt.streams.get_highest_resolution()
#stream.download(output_path="videos/")

app.mainloop()
