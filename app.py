import customtkinter
import tkinter
import os
from dotenv import load_dotenv
from PIL import Image
from query import Query


class ReActifyApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # attributes
        self.temperature = 0

        # basic window
        self.title("ReActify")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "resources")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "logo.png")), size=(60, 60))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat.png")), size=(20, 20))
        self.react_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logo.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "logo.png")), size=(20, 20))
        self.da_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "data.png")),
                                               dark_image=Image.open(os.path.join(image_path, "data.png")), size=(20, 20))
        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "setting.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "setting.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  ReActify", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.chat_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Chat",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.chat_image, anchor="w", command=self.chat_button_event)
        self.chat_button.grid(row=2, column=0, sticky="ew")

        self.react_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ReAct chat",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.react_image, anchor="w", command=self.react_button_event)
        self.react_button.grid(row=3, column=0, sticky="ew")

        self.da_chat_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Data-augmented chat",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.da_image, anchor="w", command=self.da_chat_button_event)
        self.da_chat_button.grid(row=4, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.settings_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(
            row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(
            self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(
            self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(
            row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(
            self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create chat frame
        self.chat_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.chat_frame.grid_rowconfigure(0, weight=1)
        self.chat_frame.grid_rowconfigure(1, weight=2)
        self.chat_frame.grid_columnconfigure(0, weight=1)
        self.chat_input_box = customtkinter.CTkTextbox(
            master=self.chat_frame, height=100)
        self.chat_input_box.grid(row=0, column=0,
                                 padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.chat_submit_button = customtkinter.CTkButton(
            master=self.chat_frame, command=self.chat_submit, text="", width=100)
        self.chat_submit_button.grid(row=0, column=1, padx=(
            20, 30), pady=(20, 20), sticky="ew")

        self.chat_output_box = customtkinter.CTkTextbox(
            master=self.chat_frame, state="disabled")
        self.chat_output_box.grid(row=1, column=0, columnspan=2,
                                  padx=20, pady=20, sticky="nsew")

        # create react frame
        self.react_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.react_frame.grid_rowconfigure(0, weight=1)
        self.react_frame.grid_rowconfigure(1, weight=2)
        self.react_frame.grid_columnconfigure(0, weight=1)
        self.react_input_box = customtkinter.CTkTextbox(
            master=self.react_frame, height=100)
        self.react_input_box.grid(row=0, column=0,
                                  padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.react_submit_frame = customtkinter.CTkFrame(
            self.react_frame, corner_radius=0, fg_color="transparent")
        self.react_submit_frame.grid(row=0, column=1, sticky="nsew")
        self.show_reasoning = tkinter.BooleanVar()
        self.show_reasoning.set(True)
        self.show_reasoning_checkbox = customtkinter.CTkCheckBox(self.react_submit_frame, text="Show reasoning",
                                                                 variable=self.show_reasoning)
        self.show_reasoning_checkbox.grid(
            row=0, column=0, padx=30, pady=(40, 20), stick="ew")
        self.react_submit_button = customtkinter.CTkButton(
            master=self.react_submit_frame, command=self.react_submit, text="", width=100)
        self.react_submit_button.grid(
            row=1, column=0, padx=30, pady=(10, 20))

        self.react_output_box = customtkinter.CTkTextbox(
            master=self.react_frame, state="disabled")
        self.react_output_box.grid(row=1, column=0, columnspan=2,
                                   padx=20, pady=20, sticky="nsew")

        # create data-augmented frame
        self.da_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.da_frame.grid_rowconfigure(0, weight=1)
        self.da_frame.grid_rowconfigure(1, weight=2)
        self.da_frame.grid_columnconfigure(0, weight=1)
        self.da_input_box = customtkinter.CTkTextbox(
            master=self.da_frame, height=100)
        self.da_input_box.grid(row=0, column=0,
                               padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.da_submit_frame = customtkinter.CTkFrame(
            self.da_frame, corner_radius=0, fg_color="transparent")
        self.da_submit_frame.grid(row=0, column=1, sticky="nsew")
        self.show_source = tkinter.BooleanVar()
        self.show_source.set(True)
        self.show_source_checkbox = customtkinter.CTkCheckBox(self.da_submit_frame, text="Show reasoning",
                                                              variable=self.show_source)
        self.show_source_checkbox.grid(
            row=0, column=0, padx=30, pady=(40, 10), stick="ew")
        self.da_select_file_button = customtkinter.CTkButton(
            master=self.da_submit_frame, command=self.select_file, text="sf", width=100)
        self.da_select_file_button.grid(
            row=1, column=0, padx=30, pady=(10, 10))
        self.da_submit_button = customtkinter.CTkButton(
            master=self.da_submit_frame, command=self.da_submit, text="", width=100)
        self.da_submit_button.grid(
            row=2, column=0, padx=30, pady=(10, 20))

        self.da_output_box = customtkinter.CTkTextbox(
            master=self.da_frame, state="disabled")
        self.da_output_box.grid(row=1, column=0, columnspan=2,
                                padx=20, pady=20, sticky="nsew")

        # create settings frame
        self.settings_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.openAI_token_label = customtkinter.CTkLabel(self.settings_frame,
                                                         textvariable=tkinter.StringVar(
                                                             value="OpenAI API token:"),
                                                         corner_radius=8)
        self.openAI_token_label.grid(
            row=0, column=0, padx=(80, 0), pady=(80, 20), sticky="e")
        self.openAI_token_input = customtkinter.CTkTextbox(
            self.settings_frame, height=20)
        self.openAI_token_input.grid(
            row=0, column=1, padx=(0, 30), pady=(80, 20), sticky="s")

        self.serpAPI_token_label = customtkinter.CTkLabel(self.settings_frame,
                                                          textvariable=tkinter.StringVar(
                                                              value="SERP API token:"),
                                                          corner_radius=8)
        self.serpAPI_token_label.grid(
            row=1, column=0, padx=(30, 0), pady=20, sticky="e")
        self.serpAPI_token_input = customtkinter.CTkTextbox(
            self.settings_frame, height=20)
        self.serpAPI_token_input.grid(
            row=1, column=1, padx=(0, 30), pady=20, sticky="s")

        self.temp_label = customtkinter.CTkLabel(self.settings_frame,
                                                 textvariable=tkinter.StringVar(
                                                     value="LLM temperature (0-1):"),
                                                 corner_radius=8)
        self.temp_label.grid(
            row=2, column=0, padx=(30, 0), pady=20, sticky="e")
        self.temp_input = customtkinter.CTkTextbox(
            self.settings_frame, height=20)
        self.temp_input.grid(
            row=2, column=1, padx=(0, 30), pady=20, sticky="s")

        self.save_settings_button = customtkinter.CTkButton(
            master=self.settings_frame, command=self.settings_submit, text="Save", width=100)
        self.save_settings_button.grid(
            row=3, column=0, columnspan=2, padx=30, pady=20)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.chat_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.react_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "chat":
            self.chat_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.chat_frame.grid_forget()
        if name == "react":
            self.react_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.react_frame.grid_forget()
        if name == "da":
            self.da_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.da_frame.grid_forget()
        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def chat_button_event(self):
        self.select_frame_by_name("chat")

    def react_button_event(self):
        self.select_frame_by_name("react")

    def da_chat_button_event(self):
        self.select_frame_by_name("da")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def chat_submit(self):
        prompt = self.chat_input_box.get("0.0", "end")
        myquery = Query()

        myquery.setModel(self.show_reasoning, self.temperature, 1)
        to_display = myquery.getResponse(prompt)
        print(to_display)
        self.chat_output_box.configure(state="normal")
        self.chat_output_box.insert("0.0", to_display)
        self.chat_output_box.configure(state="disabled")

    def react_submit(self):
        pass

    def da_submit(self):
        pass

    def settings_submit(self):
        openAI_token = self.openAI_token_input.get("0.0", "end")
        serpAPI_token = self.serpAPI_token_input.get("0.0", "end")
        with open('.env', 'w') as file:
            if openAI_token != "\n":
                file.write('OPENAI_API_KEY=' +
                           openAI_token + '\n')
                print("saved openai token")
            if serpAPI_token != "\n":
                file.write('SERPAPI_API_KEY=' +
                           serpAPI_token + '\n')
                print("saved serpAPI token")
        load_dotenv()
        temp_str = self.temp_input.get("0.0", "end")
        # print(temp_str)
        try:
            value = float(temp_str)
            if 0 <= value <= 1:
                self.temperature = value
                tkinter.messagebox.showinfo(
                    "Settings", "Settings saved")
            else:
                tkinter.messagebox.showwarning(
                    "Settings", "Please enter a valid temperature")
        except ValueError:
            tkinter.messagebox.showwarning(
                "Settings", "Please enter a valid temperature")

    def select_file(self):
        pass

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = ReActifyApp()
    app.mainloop()
