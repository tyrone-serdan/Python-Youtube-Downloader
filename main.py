from customtkinter import *
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

    def get_video(self):
        url_error_text = "Input a valid URL"
        path = self.path_entry.get("1.0", END)
        url = self.url_entry.get("1.0", END)

        if path.__len__() >= 1:
            path.strip()

        if url.__len__() >= 1:
            url.strip()

        if len(path) == 1:
            self.path_entry.delete("1.0", END)
            self.path_entry.insert("1.0", DEFAULT_PATH)

            self.get_video()
            
        if len(url) == 1:
            self.url_entry.delete("1.0", END)
            self.url_entry.insert("1.0", url_error_text)

            return
    
        
        video = Video(url=url, download_path=path if path != DEFAULT_PATH else None)
        video.download_video()

if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop()

# def test():
#     print("wah")

# set_appearance_mode("System")
# set_default_color_theme("green")

# app = CTk()


# app.title("Youtube Downloader")
# app.geometry("854x480")

# button = CTkButton(master=app, text="test", command=test)
# button.place(relx=0.5, rely=0.5, anchor=CENTER)

# app.resizable(False, False)
# app.mainloop()