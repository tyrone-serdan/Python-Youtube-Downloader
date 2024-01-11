from customtkinter import *
from customtkinter import filedialog
from structures.youtube import *

# yt = Video(
#               'https://www.youtube.com/watch?v=9bZkp7q19f0', 
#               'C:\\Users\\Tyrone\\Desktop\\testskies'
#           )
# yt.download_video()

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Downloader")
        self.geometry("640x360")

        self.input_frame = CTkFrame(self)
        self.input_frame.pack(side="left", expand=True, padx=0, pady=0)

        self.url_label = CTkLabel(self.input_frame, text="URL")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)

        self.url_entry = CTkTextbox(self.input_frame, height=10)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        self.path_label = CTkLabel(self.input_frame, text="Download Path")
        self.path_label.grid(row=1, column=0, padx=10, pady=10)

        self.path_entry = CTkTextbox(self.input_frame, height=10)
        self.path_entry.bind("<Button-1>", command=self.get_download_path_from_fp)
        self.path_entry.grid(row=1, column=1, padx=10, pady=10)

        self.download_btn = CTkButton(self.input_frame, text="Download Video", command=self.get_video)
        self.download_btn.grid(row=3, column=0, columnspan=2, sticky="news" ,padx=10, pady=10)

        # _________________
        
        # self.results_frame = CTkFrame(self)
        # self.results_frame.pack(side="left", expand=True, padx=20, pady=20)

        # self.title_label = CTkLabel(self.results_frame, text="title")
        # self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # self.by_label = CTkLabel(self.results_frame, text="by")
        # self.by_label.grid(row=1, column=0, padx=5, pady=0)

        # self.author_label = CTkLabel(self.results_frame, text="author")
        # self.author_label.grid(row=2, column=0, padx=10, pady=10)

    def get_download_path_from_fp(self, arg):
        # idk why i need to pass a random parameter
        # named arg ?? it gives me error without it so
        
        download_path = filedialog.askdirectory(initialdir=DEFAULT_PATH)
        self.path_entry.delete("1.0", END)
        self.path_entry.insert("1.0", download_path.strip())

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

        
        video = Video(url=url, download_path=path.strip() if path != DEFAULT_PATH else None)
        video.download_video()
        

if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()