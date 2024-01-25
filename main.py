from customtkinter import *
from customtkinter import filedialog
from structures.youtube import *

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Downloader")
        self.geometry("854x480")

        self.input_frame = CTkFrame(self)
        self.input_frame.pack(side="top", expand=True, padx=5, pady=5)

        self.url_label = CTkLabel(self.input_frame, text="URL")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = CTkTextbox(self.input_frame, height=10)
        self.url_entry.bind("<KeyRelease>", command=self.get_video_data)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        self.path_label = CTkLabel(self.input_frame, text="Download Path")
        self.path_label.grid(row=1, column=0, padx=10, pady=10)

        self.path_entry = CTkTextbox(self.input_frame, height=10)
        self.path_entry.bind("<Button-1>", command=self.get_download_path)
        self.path_entry.grid(row=1, column=1, padx=10, pady=10)

        self.download_btn = CTkButton(self.input_frame, text="Download Video", command=self.get_video)
        self.download_btn.grid(row=3, column=0, columnspan=2, sticky="news" ,padx=10, pady=10)

        self.details_frame = CTkFrame(self)
        self.details_frame.pack(side="bottom", expand=True, padx=5, pady=5)

        self.detail_title = CTkLabel(self.details_frame, text="Title", font=("Arial", 18))
        self.detail_title.pack(padx=20, pady=5)

        self.detail_by = CTkLabel(self.details_frame, text="by", font=("Arial", 14))
        self.detail_by.pack(pady=10)

        self.detail_author = CTkLabel(self.details_frame, text="Author", font=("Arial", 18))
        self.detail_author.pack(padx=20, pady=5)


    def get_download_path(self, arg):
        # idk why i need to pass a random parameter
        # named arg ?? it gives me error without it so
        
        download_path = filedialog.askdirectory(initialdir=DEFAULT_PATH)
        self.path_entry.delete("1.0", END)
        self.path_entry.insert("1.0", download_path.strip())


    def get_video_data(self, arg):
        url = self.url_entry.get("1.0", END)

        if (url.__len__() <= 1):
            return

        try:
            video = Video(url=url, download_path=None)
            video_data = video.data

            self.detail_title.configure(text=video_data[1])
            self.detail_author.configure(text=video_data[2])
        except:
            self.detail_title.configure(text="undefined (check your URL)")
            self.detail_author.configure(text="undefined (check your URL)")


    def get_video(self):
        URL_ERROR_TEXT = "Input a valid URL"

        path = self.path_entry.get("1.0", END)
        url = self.url_entry.get("1.0", END)

        if len(path) == 1:
            self.path_entry.delete("1.0", END)
            self.path_entry.insert("1.0", DEFAULT_PATH)

            self.get_video()
            
        if len(url) == 1:
            self.url_entry.delete("1.0", END)
            self.url_entry.insert("1.0", URL_ERROR_TEXT)

            return

        path = path.strip()
        
        video = Video(url=url, download_path=path)
        video.download_video()
        

if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()