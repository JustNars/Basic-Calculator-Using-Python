from customtkinter import *
from PIL import Image
import json # im working with json files to store data cuz txt files 
            # are a pain to work with.

set_appearance_mode("dark")


class MainApp(CTk):

    def __init__(self):
        super().__init__()

        self.geometry("395x625")
        self.title("Nar's Calculator App!")
        self.resizable(False, False)
        self.calculate_var = ""

        # images
        self.calculator_image = CTkImage(Image.open(r"Folder-Images/calculator.png"), size=(25, 25))

        # A frame to make the background black.
        self.bg_frame = CTkFrame(self, fg_color="#010001")
        self.bg_frame.pack(fill="both", expand=True)

        self.show_keys_and_labels()

    def show_keys_and_labels(self):
        for children in self.bg_frame.winfo_children(): 
            children.destroy()

        # lebels and entrys
        self.show_cal = CTkEntry(self.bg_frame, fg_color="transparent", border_width=0, font=("Arial", 57), state="disabled",
                                width=265, justify="right")
        self.show_cal.place(x=100, y=100)
        
        self.idk_what_to_name_this_lebal = CTkLabel(self.bg_frame, text="", font=("Arial", 17))
        self.idk_what_to_name_this_lebal.place(x=35, y=45)

        # these are buttons for the calculator. if you didn't know.

        button_calculator = CTkButton(self.bg_frame, text="", image=self.calculator_image, command=self.history, fg_color="#2a2b2d" ,
                                      height=70, width=70, hover_color="#444747", corner_radius=20)
        
        dot_button = CTkButton(self.bg_frame, text="●", command=lambda: self.calculate("."), fg_color="#2a2b2d" ,
                                      height=70, width=70, hover_color="#444747", corner_radius=20)
        
        del_button = CTkButton(self.bg_frame, text="AC", command=self.clean, fg_color="#5c5c5e", font=("Arial", 20),
                                height=70, width=70, hover_color="#4A4A4C", corner_radius=20)
        
        

        # operations
        
        multiplication = CTkButton(self.bg_frame, text="x", font=("Arial", 25), command=lambda: self.calculate("*"), fg_color="#fe9f0b" ,
                                height=70, width=70, hover_color="#D7860A", corner_radius=20)
        
        addition = CTkButton(self.bg_frame, text="+", font=("Arial", 25), command=lambda: self.calculate("+"), fg_color="#fe9f0b" ,
                                height=70, width=70, hover_color="#D7860A", corner_radius=20)
        
        subtraction = CTkButton(self.bg_frame, text="-", font=("Arial", 25), command=lambda: self.calculate("-"), fg_color="#fe9f0b" ,
                                height=70, width=70, hover_color="#D7860A", corner_radius=20)
        
        division = CTkButton(self.bg_frame, text="÷", font=("Arial", 25), command=lambda: self.calculate("/"), fg_color="#fe9f0b" ,
                                height=70, width=70, hover_color="#D7860A", corner_radius=20)
        
        percentage = CTkButton(self.bg_frame, text="%", font=("Arial", 25), command=lambda: self.calculate("%"), fg_color="#5c5c5e" ,
                                height=70, width=70, hover_color="#4A4A4C", corner_radius=20)
                                                                                                        # im lazy as shit
        exponent = CTkButton(self.bg_frame, text="^", font=("Arial", 25), command=lambda: self.calculate("**"), fg_color="#5c5c5e" ,
                                height=70, width=70, hover_color="#4A4A4C", corner_radius=20)
        
        enter = CTkButton(self.bg_frame, text="=", font=("Arial", 25), command=self.enter, fg_color="#fe9f0b" ,
                                height=70, width=70, hover_color="#D7860A", corner_radius=20)
        
        # numbers
        
        zero_button = CTkButton(self.bg_frame, text="0", font=("Arial", 33), command=lambda: self.calculate("0"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20) 
        one_button = CTkButton(self.bg_frame, text="1", font=("Arial", 33), command=lambda: self.calculate("1"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20) 
        two_button = CTkButton(self.bg_frame, text="2", font=("Arial", 33), command=lambda: self.calculate("2"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)  
        three_button = CTkButton(self.bg_frame, text="3", font=("Arial", 33), command=lambda: self.calculate("3"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)    
        four_button = CTkButton(self.bg_frame, text="4", font=("Arial", 33), command=lambda: self.calculate("4"), fg_color="#2a2b2d", 
                                height=70, width=70, hover_color="#444747", corner_radius=20)      
        five_button = CTkButton(self.bg_frame, text="5", font=("Arial", 33), command=lambda: self.calculate("5"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)
        six_button = CTkButton(self.bg_frame, text="6", font=("Arial", 33), command=lambda: self.calculate("6"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)
        seven_button = CTkButton(self.bg_frame, text="7", font=("Arial", 33), command=lambda: self.calculate("7"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)
        eight_button = CTkButton(self.bg_frame, text="8", font=("Arial", 33), command=lambda: self.calculate("8"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)
        nine_button = CTkButton(self.bg_frame, text="9", font=("Arial", 33), command=lambda: self.calculate("9"), fg_color="#2a2b2d",
                                height=70, width=70, hover_color="#444747", corner_radius=20)


        # pls don't bully me I don't know to use the grid method.

        # first row
        button_calculator.place(x=27, y=525)
        zero_button.place(x=114, y=525)
        dot_button.place(x=202, y=525)
        enter.place(x=292, y=525)

        # Second row
        one_button.place(x=27,y=440)
        two_button.place(x=114,y=440)
        three_button.place(x=202,y=440)
        addition.place(x=292,y=440) 

        # third row
        four_button.place(x=27,y=355)
        five_button.place(x=114,y=355)
        six_button.place(x=202,y=355)
        subtraction.place(x=292,y=355)

        # fouth row
        seven_button.place(x=27, y=269)
        eight_button.place(x=114, y=269)
        nine_button.place(x=202, y=269)
        multiplication.place(x=292, y=269)

        # Fifth row
        del_button.place(x=27, y=185)
        exponent.place(x=114, y=185)
        percentage.place(x=202,y=185)
        division.place(x=292,y=185)

    def enter(self):
        try:

            with open("calculator_history.json", "r") as file:
                data = json.load(file)
            
            thing2 = self.calculate_var
            data["history"].append(f"{self.calculate_var} = {eval(thing2)}")
            result = eval(thing2)
            self.idk_what_to_name_this_lebal.configure(text=f"{self.calculate_var} = {result}")
            self.calculate_var = str(result)

            self.show_cal.configure(state="normal")
            self.show_cal.delete(0, "end")
            self.show_cal.insert("end", self.calculate_var)
            self.show_cal.configure(state="disabled")

            with open("calculator_history.json", "w") as file:
                json.dump(data, file, indent=2)

        except Exception:
            self.show_cal.configure(state="normal")
            self.show_cal.delete(0, "end")
            self.show_cal.insert("end", 0)
            self.show_cal.configure(state="disabled")
            


    
    def calculate(self, num_or_op):
        self.show_cal.configure(state="normal")

        self.show_cal.insert("end", num_or_op)
        self.calculate_var += str(num_or_op)

        self.show_cal.configure(state="disabled")


    def clean(self):
        self.idk_what_to_name_this_lebal.configure(text="")
        self.show_cal.configure(state="normal")
        self.show_cal.delete(0, "end")
        self.show_cal.configure(state="disabled")
        self.calculate_var = ""

    def history(self):
        # Load data from the JSON file
        with open("calculator_history.json", "r") as file:
            data = json.load(file)
        
        for children in self.bg_frame.winfo_children():
            children.destroy()

        frame_bals = CTkScrollableFrame(self.bg_frame, orientation="vertical", height=500, width=350)
        frame_bals.pack(pady=20, padx=20)

        for i in data["history"]:
            my_label = CTkLabel(frame_bals, text=i, font=("Arial", 25))
            my_label.pack(padx=10, pady=15)

        # buttons
        return_buton = CTkButton(self.bg_frame, text="Back", fg_color="#fe9f0b", hover_color="#D7860A", height=75, width=100, corner_radius=20,
                                 font=("Arial", 25), command=self.show_keys_and_labels)
        return_buton.place(x=140, y=540)




if __name__ == "__main__":
    MainApp().mainloop()
