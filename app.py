import tkinter as tk
import customtkinter as ctk


class ReActifyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ReActify")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self, bg="gray", height=50)
        header.pack(fill=tk.X)

        logo = tk.Label(header, text="Logo", bg="gray")
        logo.pack(side=tk.LEFT, padx=10)

        app_name = tk.Label(header, text="ChatGPT Enhancer", bg="gray")
        app_name.pack(side=tk.LEFT, padx=5)

        settings_icon = tk.Button(
            header, text="Settings", command=self.open_settings)
        settings_icon.pack(side=tk.RIGHT, padx=10)

        # Main content area
        main_content = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        main_content.pack(fill=tk.BOTH, expand=1)

        # User Query section
        user_query_frame = tk.Frame(main_content)
        main_content.add(user_query_frame)

        query_entry = tk.Entry(user_query_frame, width=40)
        query_entry.grid(row=0, column=0, pady=10, padx=10)

        send_button = tk.Button(
            user_query_frame, text="Send", command=self.send_query)
        send_button.grid(row=0, column=1, pady=10, padx=10)

        query_history = tk.Text(user_query_frame, wrap=tk.WORD)
        query_history.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        react_toggle = ctk.CTkCheckBox(
            user_query_frame, text="ReAct", onvalue=True, offvalue=False)
        react_toggle.grid(row=2, column=0, pady=10, padx=10)

        # ChatGPT Response section
        response_frame = tk.Frame(main_content)
        main_content.add(response_frame)

        response_history = tk.Text(response_frame, wrap=tk.WORD)
        response_history.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

    def send_query(self):
        # Define the function to send the user's query to ChatGPT
        pass

    def open_settings(self):
        # Define the function to open the settings window
        pass


if __name__ == "__main__":
    app = ReActifyApp()
    app.mainloop()
