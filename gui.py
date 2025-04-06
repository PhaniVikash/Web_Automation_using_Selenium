import tkinter as tk
from main import WebAutomation

class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Web Automation GUI ")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text='Username').grid(row=0, column=0, sticky='w')
        self.username=tk.Entry(self.login_frame)
        self.username.grid(row=0, column=1, sticky='ew')

        tk.Label(self.login_frame, text='Password').grid(row=1, column=0, sticky='w')
        self.password = tk.Entry(self.login_frame,show='*')
        self.password.grid(row=1, column=1, sticky='ew')

        # Form Frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)


        tk.Label(self.form_frame, text='Full Name').grid(row=0, column=0, sticky='w')
        self.full_name = tk.Entry(self.form_frame)
        self.full_name.grid(row=0, column=1, sticky='ew')

        tk.Label(self.form_frame, text='Email').grid(row=1, column=0, sticky='w')
        self.email = tk.Entry(self.form_frame)
        self.email.grid(row=1, column=1, sticky='ew')

        tk.Label(self.form_frame, text='Current Address').grid(row=2, column=0, sticky='w')
        self.curr_address = tk.Entry(self.form_frame)
        self.curr_address.grid(row=2, column=1, sticky='ew')

        tk.Label(self.form_frame, text='Permanent Address ').grid(row=3, column=0, sticky='w')
        self.per_address = tk.Entry(self.form_frame)
        self.per_address.grid(row=3, column=1, sticky='ew')

        # Add Buttons
        self.button = tk.Frame(self.root)
        self.button.pack(padx=10, pady=10)

        tk.Button(self.button, text='Submit',command=self.submit_button).grid(row=0, column=0,padx=5)
        tk.Button(self.button, text='Close Browser',command=self.close_browser).grid(row=0, column=3,padx=5)


    def submit_button(self):
        username = self.username.get()
        password = self.password.get()
        full_name= self.full_name.get()
        email= self.email.get()
        curr_address= self.curr_address.get()
        per_address= self.per_address.get()

        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(name=full_name,email=email,cur_add=curr_address,per_add=per_address)

    def close_browser(self):

        self.web_automation.close()


root = tk.Tk()
app = App(root)
root.mainloop()