import customtkinter
import tkinter
import os
from PIL import Image


class ReActifyApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ReActify")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "resources")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

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
                                                    image=self.add_user_image, anchor="w", command=self.react_button_event)
        self.react_button.grid(row=3, column=0, sticky="ew")

        self.da_chat_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Data-augmented chat",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.da_chat_button_event)
        self.da_chat_button.grid(row=4, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       image=self.add_user_image, anchor="w", command=self.settings_button_event)
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
            row=0, column=0, padx=30, pady=(40, 20), stick="ew")
        self.da_submit_button = customtkinter.CTkButton(
            master=self.react_submit_frame, command=self.react_submit, text="", width=100)
        self.da_submit_button.grid(
            row=1, column=0, padx=30, pady=(10, 20))

        self.react_output_box = customtkinter.CTkTextbox(
            master=self.react_frame, state="disabled")
        self.react_output_box.grid(row=1, column=0, columnspan=2,
                                   padx=20, pady=20, sticky="nsew")
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
        if name == "frame_3":
            self.react_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.react_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def chat_button_event(self):
        self.select_frame_by_name("chat")

    def react_button_event(self):
        self.select_frame_by_name("frame_3")

    def da_chat_button_event(self):
        self.select_frame_by_name("frame_4")

    def settings_button_event(self):
        self.select_frame_by_name("frame_5")

    def chat_submit(self):
        pass

    def react_submit(self):
        pass

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = ReActifyApp()
    app.mainloop()
