from Main import admin
from datetime import datetime
from calendar import month_name
from tkinter import ttk, messagebox, Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import ConnectionPatch
import os
try:
    import customtkinter
except ImportError:
    print("CustomTkinter is not installed. Please install it using 'pip install customtkinter' on console or terminal ")
    exit()
    
try:
    from tkcalendar import Calendar
except ImportError:
    print("tkcalendar is not installed. Please install it using 'pip install tkcalendar' on console or terminal ")
    exit()

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Please install it using 'pip install pillow' on console or terminal ")
    exit()
    
try:
    import numpy as np
except ImportError:
    print("numpy is not installed. Please install it using 'pip install numpy' on console or terminal ")
    exit()
    
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib is not installed. Please install it using 'pip install matplotlib' on console or terminal ")
    exit()




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hospital Management System")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
       
        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Login", font=("Roboto", 24))
        self.login_label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(self.login_frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)

        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.handle_login)
        self.login_button.pack(pady=12, padx=10)

        self.login_error_label = customtkinter.CTkLabel(self.login_frame, text="", text_color="red")
        self.login_error_label.pack(pady=12, padx=10)

        # Load navigation and home frames but keep them hidden initially
        self.navigation_frame = None
        self.dashboard_frame = None
        self.home_frame = None
        self.second_frame = None
        self.third_frame = None
        self.fourth_frame = None
        self.fifth_frame = None
        
        
        # Store selected date and time
        self.selected_date = None
        self.selected_time = None
        

    def handle_login(self):
        """Handles the login button click."""
        username = self.entry1.get()
        password = self.entry2.get()

        if admin.login(username, password):
            self.show_main_app()
        else:
            self.login_error_label.configure(text="Incorrect username or password.")
            
  
        

    def show_main_app(self):
        """Reveals the main application interface after login."""
        self.login_frame.pack_forget()
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hospital_logo.png")), size=(50, 50))

        #self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "doc_icon.png")), size=(500, 150))
        #self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hospital_logo.png")), size=(20, 20))

        self.dashboard = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "dashboard.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "dashboard.png")), size=(20, 20))

        self.doctor_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "stethoscope.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "stethoscope.png")), size=(20, 20))
        
        self.patient_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "patient.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "patient.png")), size=(20, 20))
        
        self.appointment_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "calender.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "calender.png")), size=(20, 20))
        
        self.system_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings.png")), size=(20, 20))
        
        self.admin_update_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "edit.png")), size=(20, 20))
        
        self.patients_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "patients1.png")), size=(40, 40))
        self.doc_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "stethoscope.png")), size=(40, 40))
        self.specialty_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "specialty.png")), size=(40, 40))
        self.illness_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "illness.png")), size=(50, 50))
        self.add_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "register_user.png")), size=(15, 15))
        self.update_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "edit.png")), size=(15, 15))
        self.delete_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "delete_img.png")), size=(17, 17)) 
        self.assign_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "assign_img.png")), size=(17, 17)) 
        self.relocate_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "relocate_img.png")), size=(17, 17)) 
        self.discharge_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "discharge_img.png")), size=(17, 17))
        self.view_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "view_img.png")), size=(17, 17))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Health-Ease", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=15)
        
        self.dashboard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dashboard",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.dashboard, anchor="w", command=self.dashboard_button_event)
        self.dashboard_button.grid(row=1, column=0, sticky="ew")

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Doctor Management",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.doctor_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=2, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Patient Management",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.patient_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Appointment",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.appointment_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=4, column=0, sticky="ew")
        
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Management Report",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.system_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=5, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Admin Update",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.admin_update_image, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=6, column=0, sticky="ew")
        


        #self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                #command=self.change_appearance_mode_event)
        #self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        

        # create dashboard frame
        self.create_dashboard_frame()

        self.create_doctor_management_frame()

        self.create_patient_management_frame()

        self.create_appointment_management_frame()

        self.create_system_frame()

        
        
        # Select default frame
        self.select_frame_by_name("dashboard")

        

        

    def create_dashboard_frame(self):
      
        """Creates and returns the dashboard frame."""
        
        self.dashboard_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.dashboard_frame.grid(row=0, column=1, sticky="nsew")

        # Configure grid for dashboard sub-frames
        self.dashboard_frame.grid_rowconfigure(0, weight=0)
        self.dashboard_frame.grid_rowconfigure(2, weight=3)  # Make row 2 (calendar & chart) larger
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        

        # Title Label
        label = customtkinter.CTkLabel(
            self.dashboard_frame, text="Welcome to Dashbaord!", font=customtkinter.CTkFont("Times New Roman", size=20, weight="bold")
        )
        label.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="w")


        # Create sub-frames for stats, calendar, and stats chart
        self.stats_frame = customtkinter.CTkFrame(self.dashboard_frame, height=100, corner_radius=10, fg_color="transparent")
        self.stats_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        total_patient = self.get_total_patients()
        total_doctor = self.get_total_doctors()
        specialty_count = self.get_doctors_by_specialty()
        illnesses_count = admin.get_patients_by_illness(admin.patients)  # Adjust based on your Admin instance


        # Statistics Boxes
        box_width = 50
        box_height = 100
        self.create_stat_box(self.stats_frame, "Patients" , str(total_patient), 0, width=box_width, height=box_height, image=self.patients_image)
        self.create_stat_box(self.stats_frame, "Doctors", str(total_doctor), 1, width=box_width, height=box_height, image=self.doc_img) 
        self.create_stat_box(self.stats_frame, "Specialities", str(len(specialty_count)), 2, width=box_width, height=box_height, image=self.specialty_img)
        self.create_stat_box(self.stats_frame, "Illnesses", str(len(illnesses_count)), 3, width=box_width, height=box_height, image=self.illness_img)

        # Sub-frame for Calendar and Chart (split second row)
        bottom_frame = customtkinter.CTkFrame(self.dashboard_frame, corner_radius=10, fg_color="transparent")
        bottom_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        bottom_frame.grid_rowconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(0, weight=2)  # Calendar takes less width
        bottom_frame.grid_columnconfigure(1, weight=3)  # Chart takes more width

        # Calendar Frame
        self.calendar_frame = customtkinter.CTkFrame(bottom_frame, height=200, corner_radius=10, fg_color="white")  # Increased height
        self.calendar_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.create_calendar_widget(self.calendar_frame)

        # Stats Chart Frame
        self.stats_chart_frame = customtkinter.CTkFrame(bottom_frame, height=200, corner_radius=10, fg_color="lightgray")  # Increased height
        self.stats_chart_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.create_pie_chart(self.stats_chart_frame)

        return self.dashboard_frame


    def create_stat_box(self, parent, label, value, column, width, height, image=None):
        """Creates a stat box with given value and label."""
        box = customtkinter.CTkFrame(parent, width=width, height=height, corner_radius=10, fg_color="white")
        box.grid(row=0, column=column, padx=5, pady=10, sticky="nsew")
        box.grid_columnconfigure(0, weight=1)  # Left content
        box.grid_columnconfigure(1, weight=0)  # Icon column

        
        label_label = customtkinter.CTkLabel(box, text=label, font=customtkinter.CTkFont("Times New Roman", size=18, weight="bold"))
        label_label.grid(row=0, column=0, padx=10, pady=(8, 1), sticky="w")
        # Box content
        value_label = customtkinter.CTkLabel(box, text=value, font=customtkinter.CTkFont("Times New Roman", size=16))
        #value_label.pack()
        value_label.grid(row=1, column=0, padx=10, pady=(0, 6),  sticky="w")


        # Dynamic creation of placeholders
         # Add the image if provided
        if image:
            icon_placeholder = customtkinter.CTkLabel(box, text="", image=image)
            icon_placeholder.grid(row=0, column=1, rowspan=2, padx=10, sticky="e")


        self.slider_1 = customtkinter.CTkProgressBar(box)
        self.slider_1.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 8), sticky="nsew")

  
    def create_pie_chart(self, parent_frame):
        """Creates a pie chart displaying patient illnesses."""
        # Get the illness data for the pie chart
        illness_data = admin.get_patients_by_illness(admin.patients)
        illnesses = list(illness_data.keys())
        counts = list(illness_data.values())

        # Create a Matplotlib figure and axis
        fig, ax = plt.subplots(figsize=(3, 3), dpi=100)

        # Function for displaying raw values in the pie chart
        def autopct_raw(pct, all_vals):
            absolute = int(round(pct / 100.0 * sum(all_vals)))
            return f"{absolute}"
        
       
        # Plot the pie chart
        wedges, texts, autotexts = ax.pie(
            counts,
            labels=illnesses,
            autopct=lambda pct: autopct_raw(pct, counts),
            startangle=90,
            colors=plt.cm.Paired.colors[:len(illnesses)],
            textprops=dict(color="black"),
        )
        ax.set_title("Number of Patients by Illness", fontweight="bold")

            # Add legend
        ax.legend(
            wedges,
            illnesses,
            title="Illness",
            loc="upper left",
            bbox_to_anchor=(1, 1),
            fontsize=10,
        )

        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill="both", expand=True)

        # Interactive click handler for pie chart
        def on_click_pie(event):
            if event.inaxes == ax:  # Check if the click is inside the pie chart axes
                for wedge in wedges:
                    if wedge.contains(event)[0]:  # Check if the click is on a wedge
                        index = wedges.index(wedge)
                        category = illnesses[index]
                        value = counts[index]
                        messagebox.showinfo(
                            "Data Point", f"Illness: {category}\nCount: {value}"
                        )
                        break

        canvas.mpl_connect("button_press_event", on_click_pie)


    #from tkcalendar import Calendar

    def create_calendar_widget(self, parent_frame):
        """
        Creates a calendar widget with a 'Book Appointment' button and a slider,
        ensuring all elements occupy the parent frame.
        """
        # Configure parent frame to fill the space
        parent_frame.grid_rowconfigure(0, weight=0)  # Top frame (button)
        parent_frame.grid_rowconfigure(1, weight=5)  # Calendar frame
        parent_frame.grid_rowconfigure(2, weight=0)  # Bottom frame (slider)
        parent_frame.grid_columnconfigure(0, weight=1)

        # Create a top frame for the button
        top_frame = customtkinter.CTkFrame(parent_frame, fg_color="transparent", height=30)
        top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        # Add 'Book Appointment' button
        book_button = customtkinter.CTkButton(
            top_frame,
             height=30,
             text_color="#FFFFFF",
             font=customtkinter.CTkFont("Times New Roman", size=16, weight="bold"),
            text="Schedule an Appointment",
            command=self.add_appointment_frame
        )
        book_button.pack(expand=True, fill="both", padx=5)

        # Create a frame for the calendar widget
        cal_frame = customtkinter.CTkFrame(parent_frame, fg_color="transparent")
        cal_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Create the Calendar widget
        cal = Calendar(
            cal_frame,
            selectmode='day',  # Options: 'day', 'month', 'year'
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            date_pattern='yyyy-mm-dd'
        )
        cal.pack(expand=True, fill="both", padx=5, pady=5)

        # Optional: Add an event to handle date selection
        def on_date_select(event):
            selected_date = cal.get_date()
            print(f"Selected date: {selected_date}")
            # Perform actions with the selected date

        cal.bind("<<CalendarSelected>>", on_date_select)

        # Add a slider (progress bar) at the bottom
        bottom_frame = customtkinter.CTkFrame(parent_frame, height=10, fg_color="transparent")
        bottom_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5, 10))

        slider = customtkinter.CTkProgressBar(bottom_frame, height=10)
        slider.pack(expand=True, fill="both", padx=5, pady=5)
        slider.set(0.5)  # Set slider value (0.0 to 1.0)

        # Store slider for later use (if needed)
        self.slider_1 = slider




    def get_total_patients(self):
        return len(admin.patients)
    
    def get_total_doctors(self):
        return len(admin.doctors)
    

    def refresh_dashboard_frame(self):
        """Perform updates and refresh the frame."""
        for widget in self.dashboard_frame.winfo_children():
            widget.destroy()
        # Rebuild the frame
        self.create_dashboard_frame() 



    def create_doctor_management_frame(self):
        """Creates and returns the doctor management frame."""
        #frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        #frame.grid(row=0, column=0, sticky="nsew")  # Ensure the frame occupies the entire parent frame

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=0, sticky="nsew")  # Ensure the frame is added to the grid

        self.home_frame.grid_forget()

        # Configure grid for layout
        self.home_frame.grid_rowconfigure(1, weight=1)  # Row for doctor list table
        self.home_frame.grid_columnconfigure(0, weight=1)  # Entire frame adjusts dynamically

        # Top Sub-frame for Label and Buttons
        top_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent", height=10)
        top_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=10,)
        top_frame.grid_columnconfigure(0, weight=1)  # Label on the left
        top_frame.grid_columnconfigure(1, weight=3)  # Buttons on the right

        # Doctor List Label
        doctor_list_label = customtkinter.CTkLabel(
            top_frame,
            text="Doctor List",
            font=customtkinter.CTkFont("Times New Roman", size=20, weight="bold"),
            text_color="black"
        )
        doctor_list_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)

        # Buttons Frame
        button_frame = customtkinter.CTkFrame(top_frame, fg_color="transparent", height=10)
        button_frame.grid(row=0, column=1, sticky="e", padx=5, pady=10)
        #button_frame.grid_rowconfigure((0), weight=1)

        button_width = 105
        button_height = 28
        button_fg_color = "lightgray"
        button_text_color = "black"
        button_corner_radius = 2
        button_hover_color = ("gray70", "gray30")
        button_border_spacing = 4
        button_anchor = "center"
        button_compound = "left"
        button_text_font = customtkinter.CTkFont("Times New Roman", weight="bold", size=11)

        # Buttons for various actions
       

        register_button = customtkinter.CTkButton(
            button_frame, text="Register", width=button_width, height=button_height, fg_color=button_fg_color, text_color=button_text_color, command=self.register_doctor_frame, corner_radius=button_corner_radius, hover_color=button_hover_color,  border_spacing=button_border_spacing, image=self.add_img, anchor=button_anchor, compound=button_compound, font=button_text_font
        )
        register_button.grid(row=0, column=0, padx=2, pady=5)

        

        update_button = customtkinter.CTkButton(
            button_frame, text="Update", width=button_width, height=button_height, command=self.update_doctor_frame, fg_color=button_fg_color, text_color=button_text_color, corner_radius=button_corner_radius, compound=button_compound, image=self.update_image, border_spacing=button_border_spacing, anchor=button_anchor, font=button_text_font, hover_color=button_hover_color
        )
        update_button.grid(row=0, column=1, padx=2, pady=5)

        delete_button = customtkinter.CTkButton(
            button_frame, text="Delete", width=button_width, height=button_height, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=self.delete_doctor_frame, corner_radius=button_corner_radius, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor,font=button_text_font, image= self.delete_img
        )
        delete_button.grid(row=0, column=2, padx=2, pady=5)

        assign_button = customtkinter.CTkButton(
            button_frame, text="Assign Doctor", width=button_width, height=button_height, fg_color=button_fg_color, text_color=button_text_color, command=self.assign_doctor_to_patient_frame, image=self.assign_img, corner_radius=button_corner_radius, hover_color=button_hover_color, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor, font=button_text_font
        )
        assign_button.grid(row=0, column=3, padx=2, pady=5)

        relocate_button = customtkinter.CTkButton(
            button_frame, text="Relocate Doctor", width=button_width, height=button_height, fg_color=button_fg_color, text_color=button_text_color, command=self.relocate_doctor_to_patient_frame, image=self.relocate_img, corner_radius=button_corner_radius, hover_color=button_hover_color, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor, font=button_text_font
        )
        relocate_button.grid(row=0, column=4, padx=2, pady=5)

        # Main Sub-frame for Doctor List Table Placeholder
        table_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=10, fg_color="lightgray")
        table_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Configure grid weights for the frame
        table_frame.grid_rowconfigure(0, weight=1)  # Table row
        table_frame.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14))
        style.map("Treeview", background=[("selected", "gray75")])

        

        # Add a table to the frame
        self.table = ttk.Treeview(
            table_frame,
            columns=('ID', 'Full_Name', 'Speciality'),
            show='headings',
        )
        # Configure columns alignment
        self.table.column('ID', anchor="center", width=100)  # Center-align ID column
        self.table.column('Full_Name', anchor="center", width=200)  # Left-align Full Name column
        self.table.column('Speciality', anchor="center", width=200)  # Left-align Speciality column
        
        # Configure headers alignment
        self.table.heading('ID', text='ID', anchor="center")  # Center-align header
        self.table.heading('Full_Name', text='Full Name', anchor="center")  # Left-align header
        self.table.heading('Speciality', text='Speciality', anchor="center")  # Left-align header
        
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space
        
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
    
        self.refresh_doctor_table()

      

        return self.home_frame

    def refresh_doctor_table(self):
        """Refresh the doctor table with updated data."""
        # Clear existing rows
        for row in self.table.get_children():
            self.table.delete(row)
            
        
        # Populate the table with updated doctor data
        for i, doctor in enumerate(admin.get_doctors(), start=1):
            full_name = f"{doctor.get_first_name()} {doctor.get_surname()}"
            speciality = doctor.get_speciality()
            self.table.insert('', 'end', values=(i, full_name, speciality))


    def refresh_frame(self):
        """Perform updates and refresh the frame."""
        for widget in self.home_frame.winfo_children():
            widget.destroy()
        # Rebuild the frame
        self.create_doctor_management_frame() 


    

    def create_patient_management_frame(self):
        """Creates and returns the doctor management frame."""
          # Create second frame
        

        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid(row=0, column=0, sticky="nsew")  # Ensure the frame is added to the grid

        self.second_frame.grid_forget()

        # Configure grid for layout
        self.second_frame.grid_rowconfigure(1, weight=1)  # Row for doctor list table
        self.second_frame.grid_columnconfigure(0, weight=1)  # Entire frame adjusts dynamically

        # Top Sub-frame for Label and Buttons
        top_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=0, fg_color="transparent", height=10)
        top_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
        top_frame.grid_columnconfigure(0, weight=1)  # Label on the left
        top_frame.grid_columnconfigure(1, weight=3)  # Buttons on the right

        # Patient List Label
        patient_list_label = customtkinter.CTkLabel(
            top_frame,
            text="Patient List",
            font=customtkinter.CTkFont("Times New Roman", size=20, weight="bold"),
            text_color="black"
        )
        patient_list_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)

        # Buttons Frame
        button_frame = customtkinter.CTkFrame(top_frame, fg_color="transparent", height=10)
        button_frame.grid(row=0, column=1, sticky="e", padx=5, pady=10)
        #button_frame.grid_rowconfigure((0), weight=1)

        button_width = 105
        button_height = 28
        button_fg_color = "lightgray"
        button_text_color = "black"
        button_corner_radius = 2
        button_hover_color = ("gray70", "gray30")
        button_border_spacing = 4
        button_anchor = "center"
        button_compound = "left"
        button_text_font = customtkinter.CTkFont("Times New Roman", weight="bold", size=11)

        # Buttons for various actions
       

        register_button = customtkinter.CTkButton(
            button_frame, text="Register", width=button_width, height=button_height, fg_color=button_fg_color, text_color=button_text_color, command=self.register_patient_frame, corner_radius=button_corner_radius, hover_color=button_hover_color,  border_spacing=button_border_spacing, image=self.add_img, anchor=button_anchor, compound=button_compound, font=button_text_font
        )
        register_button.grid(row=0, column=0, padx=2, pady=5)

        update_button = customtkinter.CTkButton(
           button_frame, text="Update", width=button_width, height=button_height, command=self.update_patient_frame, fg_color=button_fg_color, text_color=button_text_color, corner_radius=button_corner_radius, compound=button_compound, image=self.update_image, border_spacing=button_border_spacing, anchor=button_anchor, font=button_text_font, hover_color=button_hover_color
        )
        update_button.grid(row=0, column=1, padx=2, pady=5)

        delete_button = customtkinter.CTkButton(
           button_frame, text="Delete", width=button_width, height=button_height, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=self.delete_patient_frame, corner_radius=button_corner_radius, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor,font=button_text_font, image= self.delete_img
        )
        delete_button.grid(row=0, column=2, padx=2, pady=5)

        discharge_button = customtkinter.CTkButton(
           button_frame, text="Discharge", width=button_width, height=button_height, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=self.discharge_patient_frame, corner_radius=button_corner_radius, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor,font=button_text_font, image= self.discharge_img
        )
        discharge_button.grid(row=0, column=3, padx=2, pady=5)

        view_discharge_button = customtkinter.CTkButton(
            button_frame, text="View Discharged", width=button_width, height=button_height, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=self.view_discharged_patient_frame, corner_radius=button_corner_radius, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor,font=button_text_font, image= self.view_img
        )
        view_discharge_button.grid(row=0, column=4, padx=2, pady=5)

        # Main Sub-frame for Doctor List Table Placeholder
        table_frame = customtkinter.CTkFrame(self.second_frame, corner_radius=10, fg_color="lightgray")
        table_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Configure grid weights for the frame
        table_frame.grid_rowconfigure(0, weight=1)  # Table row
        table_frame.grid_columnconfigure(0, weight=1)

          # Add a table to the frame
        self.table = ttk.Treeview(
            table_frame,
            columns=('ID', 'Full_Name', 'Doctor\'s_Full_Name', 'Age', 'Mobile', 'Post_Code', 'Symptoms'),
            show='headings',
        )
        # Configure columns
        for col in ('ID', 'Full_Name', 'Doctor\'s_Full_Name', 'Age', 'Mobile', 'Post_Code', 'Symptoms'):
            self.table.column(col, anchor="center", width=100)
            self.table.heading(col, text=col.replace('_', ' '), anchor="center")
            
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
        
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with enriched patient data
        self.refresh_patient_table()
        
        
        #ComboBox to select view option
        self.view_option = customtkinter.StringVar(value="Select View Option")
        
        self.drop_down_menu = customtkinter.CTkOptionMenu(table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                                command=self.update_table_view)
        self.drop_down_menu.grid(row=1, column=0, padx=8, pady=10, sticky="w")


        return self.second_frame


    def refresh_patient_table(self):
        """Refresh the doctor table with updated data."""
        # Clear existing rows
        self.display_all_patients()


    def refresh_patient_frame(self):
        """Perform updates and refresh the frame."""
        for widget in self.second_frame.winfo_children():
            widget.destroy()
        # Rebuild the frame
        self.create_patient_management_frame() 





    def create_appointment_management_frame(self):
        """Creates and returns the doctor management frame."""
          # Create second frame
        

        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid(row=0, column=0, sticky="nsew")  # Ensure the frame is added to the grid

        self.second_frame.grid_forget()
        self.third_frame.grid_forget()


        # Configure grid for layout
        self.third_frame.grid_rowconfigure(1, weight=1)  # Row for doctor list table
        self.third_frame.grid_columnconfigure(0, weight=1)  # Entire frame adjusts dynamically

        # Top Sub-frame for Label and Buttons
        top_frame = customtkinter.CTkFrame(self.third_frame, corner_radius=0, fg_color="transparent", height=10)
        top_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
        top_frame.grid_columnconfigure(0, weight=1)  # Label on the left
        top_frame.grid_columnconfigure(1, weight=3)  # Buttons on the right

        # Patient List Label
        patient_list_label = customtkinter.CTkLabel(
            top_frame,
            text="Appointment",
            font=customtkinter.CTkFont("Times New Roman", size=20, weight="bold"),
            text_color="black"
        )
        patient_list_label.grid(row=0, column=0, sticky="w", padx=5, pady=10)

        # Buttons Frame
        button_frame = customtkinter.CTkFrame(top_frame, fg_color="transparent", height=10)
        button_frame.grid(row=0, column=1, sticky="e", padx=5, pady=10)
        #button_frame.grid_rowconfigure((0), weight=1)

        button_width = 105
        button_height = 28
        button_fg_color = "lightgray"
        button_text_color = "black"
        button_corner_radius = 2
        button_hover_color = ("gray70", "gray30")
        button_border_spacing = 4
        button_anchor = "center"
        button_compound = "left"
        button_text_font = customtkinter.CTkFont("Times New Roman", weight="bold", size=11)

        # Buttons for various actions
       

        add_button = customtkinter.CTkButton(
              button_frame, text="Add Appointment", width=button_width, height=button_height, command=self.add_appointment_frame, fg_color=button_fg_color, text_color=button_text_color, corner_radius=button_corner_radius, compound=button_compound, image=self.update_image, border_spacing=button_border_spacing, anchor=button_anchor, font=button_text_font, hover_color=button_hover_color
        )
        add_button.grid(row=0, column=0, padx=2, pady=5)

        view_button = customtkinter.CTkButton(
             button_frame, text="Remove Appointment", width=button_width, height=button_height, fg_color=button_fg_color, hover_color=button_hover_color, text_color=button_text_color, command=self.remove_appointment_frame, corner_radius=button_corner_radius, compound=button_compound, border_spacing=button_border_spacing, anchor=button_anchor,font=button_text_font, image= self.delete_img
        )
        view_button.grid(row=0, column=1, padx=2, pady=5)


        # Main Sub-frame for Doctor List Table Placeholder
        table_frame = customtkinter.CTkFrame(self.third_frame, corner_radius=10, fg_color="lightgray")
        table_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Configure grid weights for the frame
        table_frame.grid_rowconfigure(0, weight=1)  # Table row
        table_frame.grid_columnconfigure(0, weight=1)

          # Add a table to the frame
        # Add a table to the frame
        self.table = ttk.Treeview(
            table_frame,
            columns=("#", "Patient", "Doctor", "Date", "Time", "Notes"),
            show="headings",
        )
        # Configure columns
        self.table.column("#", anchor="center", width=50)  # Numbering column
        self.table.heading("#", text="No.", anchor="center")
        
        for col in ("Patient", "Doctor", "Date", "Time", "Notes"):
            self.table.column(col, anchor="center", width=150)
            self.table.heading(col, text=col, anchor="center")
        
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space
        
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with appointment data
        self.refresh_appointment_table()


        return self.third_frame


    def refresh_appointment_table(self):
        """Refresh the doctor table with updated data."""
        # Clear existing rows
        self.display_all_appointment()


    def refresh_appointment_frame(self):
        """Perform updates and refresh the frame."""
        for widget in self.third_frame.winfo_children():
            widget.destroy()

        # Rebuild the frame
        self.create_appointment_management_frame()
        self.third_frame.grid(row=0, column=1, sticky="nsew")  # Ensure it remains visible



    
    def create_system_frame(self):
      
        """Creates and returns the dashboard frame."""
        
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid(row=0, column=1, sticky="nsew")

        # Configure grid for fourth frame layout
        self.fourth_frame.grid_rowconfigure(0, weight=0)
        self.fourth_frame.grid_rowconfigure(1, weight=1)  # Charts row
        self.fourth_frame.grid_columnconfigure(0, weight=2)  # Left section (longer frame & table)
        self.fourth_frame.grid_columnconfigure(1, weight=3)  # Right section (charts)

        # Title Label
        label = customtkinter.CTkLabel(
            self.fourth_frame, text="Management Report", 
            font=customtkinter.CTkFont("Times New Roman", size=20, weight="bold")
        )
        label.grid(row=0, column=0, columnspan=2, padx=20, pady=(10, 10), sticky="w")

        # LEFT SECTION
        # Longer frame (left-top)
        self.longer_frame = customtkinter.CTkFrame(self.fourth_frame, corner_radius=10, fg_color="lightgray")
        self.longer_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
       


        #self.longer_frame.grid_rowconfigure(0, weight=1)  # Row for the table
        self.longer_frame.grid_rowconfigure(0, weight=1)  # Row 0 for tabview1 (appointments)
        self.longer_frame.grid_rowconfigure(1, weight=2)  # Row 1 for tabview2 (patients per doctor)
        self.longer_frame.grid_rowconfigure(2, weight=0)  # Row 2 for tabview3 (illness types)

        self.longer_frame.grid_columnconfigure(0, weight=1)  # Make column 0 stretchable (where all tabviews are placed)
        self.longer_frame.grid_columnconfigure(1, weight=0)  # Column 1 for scrollbar, no need for stretching
        self.longer_frame.grid_propagate(False)  # Prevents the frame from resizing to fit the widgets, allowing custom resizing


        self.tabview = customtkinter.CTkTabview(self.longer_frame,
                                                segmented_button_fg_color="#3B8ED0",
                                                 segmented_button_selected_color="#3B8ED0",
                                                 segmented_button_selected_hover_color="#3B8ED0",
                                                 text_color="white")
        self.tabview.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Add a tab
        self.tabview.add("Total No of Appointment per Month per Doctor ")  # Changed the tab name to something meaningful
        self.tabview.tab("Total No of Appointment per Month per Doctor ").grid_columnconfigure(0, weight=1)


        # Create the Treeview table inside the "Appointments" tab
        self.table = ttk.Treeview(
            self.tabview.tab("Total No of Appointment per Month per Doctor "),  # Attach to the specific tab
            height=5,
            columns=('ID', 'Doctor', 'Month', 'No_of_Appointment'),
            show='headings',
        )

        # Configure columns
        self.table.column('ID', width=8, anchor="center")
        self.table.heading('ID', text="ID")

        self.table.column('Doctor', width=60, anchor="center")
        self.table.heading('Doctor', text="Doctor")

        self.table.column('Month', width=60, anchor="center")
        self.table.heading('Month', text="Month")

        self.table.column('No_of_Appointment', width=80, anchor="center")
        self.table.heading('No_of_Appointment', text="Appointment")

        # Place the table in the tab
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add a vertical scrollbar to the table
        scrollbar = ttk.Scrollbar(self.tabview.tab("Total No of Appointment per Month per Doctor "), orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10)

        
        self.tabview2 = customtkinter.CTkTabview(self.longer_frame,
                                segmented_button_fg_color="#3B8ED0",
                                segmented_button_selected_color="#3B8ED0",
                                segmented_button_selected_hover_color="#3B8ED0",
                                text_color="white")
        self.tabview2.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        

        # Add a tab
        self.tabview2.add("Total No of Patients per Doctor")
        self.tabview2.tab("Total No of Patients per Doctor").grid_columnconfigure(0, weight=1)
        

        # Create Table (Treeview)
        self.table2 = ttk.Treeview(self.tabview2.tab("Total No of Patients per Doctor"),  # Put table in the tab
                                height=4,
                                columns=('ID', 'Doctor', 'No_of_Patients'),
                                show='headings')

        # Configure the columns and headings for the table
        self.table2.column('ID', width=8, anchor="center")
        self.table2.heading('ID', text="ID")

        self.table2.column('Doctor', width=60, anchor="center")
        self.table2.heading('Doctor', text="Doctor")

        self.table2.column('No_of_Patients', width=80, anchor="center")
        self.table2.heading('No_of_Patients', text="No of Patients")

        # Grid the table inside the tab
        self.table2.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Add a vertical scrollbar to the table
        scrollbar2 = ttk.Scrollbar(self.tabview2.tab("Total No of Patients per Doctor"), orient="vertical", command=self.table2.yview)
        self.table2.configure(yscrollcommand=scrollbar2.set)
        scrollbar2.grid(row=0, column=1, sticky="ns", pady=10)


        self.tabview3 = customtkinter.CTkTabview(self.longer_frame,
                                segmented_button_fg_color="#3B8ED0",
                                segmented_button_selected_color="#3B8ED0",
                                segmented_button_selected_hover_color="#3B8ED0",
                                text_color="white")
        self.tabview3.grid(row=2, column=0, padx=(20, 20), pady=(5, 20), sticky="nsew")
        

        # Add a tab
        self.tabview3.add("Patients Based on Illness Type")
        self.tabview3.tab("Patients Based on Illness Type").grid_columnconfigure(0, weight=1)
        



        self.table3 = ttk.Treeview(
            self.tabview3.tab("Patients Based on Illness Type"),
            height=6,
            columns=('Illness', 'No_of_Patients'),
            show='headings',
        )
           
        self.table3.column('Illness', width=80, anchor="center")
        self.table3.heading('Illness', text="Illness")
    
        self.table3.column('No_of_Patients', width=80, anchor="center")
        self.table3.heading('No_of_Patients', text="No of Patients")
          
        self.table3.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
        # Add a vertical scrollbar
        scrollbar3 = ttk.Scrollbar(self.tabview3.tab("Patients Based on Illness Type"), orient="vertical", command=self.table.yview)  # Apply the custom style)
        self.table3.configure(yscrollcommand=scrollbar.set)
        scrollbar3.grid(row=0, column=1, sticky="ns", pady=10)



        

        self.refresh_system_table()



        # RIGHT SECTION
        # Create a sub-frame for the right section charts
        self.charts_frame = customtkinter.CTkFrame(self.fourth_frame, corner_radius=10, fg_color="transparent")
        self.charts_frame.grid(row=1, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
      
        # Configure rows for equal height
        self.charts_frame.grid_rowconfigure(0, weight=1)  # First row
        self.charts_frame.grid_rowconfigure(1, weight=1)  # Second row

        # Configure columns for equal width
        self.charts_frame.grid_columnconfigure(0, weight=1)  # First column
        self.charts_frame.grid_columnconfigure(1, weight=1)  # Second column


        # Small chart frames (top-right section)
        self.column_chart_frame = customtkinter.CTkFrame(self.charts_frame, corner_radius=10, fg_color="lightgray")
        self.column_chart_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.column_chart_frame.grid_propagate(False)  # Prevent resizing
        self.column_chart(self.column_chart_frame)

        self.stacked_column_chart_frame = customtkinter.CTkFrame(self.charts_frame, corner_radius=10, fg_color="lightgray")
        self.stacked_column_chart_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.stacked_column_chart_frame.grid_propagate(False)  # Prevent resizing
        self.stacked_chart(self.stacked_column_chart_frame)
        
        

        # Horizontal bar chart (top-right section)
        self.horizontal_bar_chart_frame = customtkinter.CTkFrame(self.charts_frame, corner_radius=10, fg_color="lightgray")
        self.horizontal_bar_chart_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.horizontal_bar_chart_frame.grid_propagate(False)  # Prevent resizing
        self.horizontal_chart(self.horizontal_bar_chart_frame)

        # Pie chart (larger chart frame)
        self.pie_chart_frame = customtkinter.CTkFrame(self.charts_frame, corner_radius=10, fg_color="lightgray")
        self.pie_chart_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.pie_chart_frame.grid_propagate(False)  # Prevent resizing
       
        # Call the function to create the pie chart in the pie_chart_frame
        self.create_pie_chart(self.pie_chart_frame)

        return self.fourth_frame

    def refresh_system_table(self):
        """Refresh the doctor table with updated data."""
        # Clear existing rows
        self.populate_table()
        self.populate_table2()
        self.populate_table3()


    def refresh_system_frame(self):
        """Perform updates and refresh the frame."""
        for widget in self.fourth_frame.winfo_children():
            widget.destroy()

        # Rebuild the frame
        self.create_system_frame()
        self.fourth_frame.grid(row=0, column=1, sticky="nsew")  # Ensure it remains visible

    def get_appointments_summary(self):
        """
        Returns a list of dictionaries with doctor ID, full name, month, and appointment counts,
        formatted for populating a table.
        """ 
        

        appointment_summary = []

        for index, doctor  in enumerate(admin.doctors, start=1):
            monthly_counts = {month: 0 for month in range(1, 13)}  # Initialize counts for all months

            for appointment in doctor.get_appointments():
                appointment_date = appointment['date']  # Assuming appointments have a 'date' key

                # Extract the month from the date string
                try:
                    appointment_month = int(appointment_date.split('/')[0])  # Extract month as an integer
                    monthly_counts[appointment_month] += 1  # Increment the count for the specific month
                except (IndexError, ValueError):
                    print(f"Invalid date format for appointment: {appointment_date}")
                    continue

            # Create table-friendly entries for each month
            for month, count in monthly_counts.items():
                if count > 0:  # Only include months with appointments
                    appointment_summary.append({
                        'ID': index,  # Assuming doctors have an 'id' attribute
                        'Doctor': doctor.full_name(),
                        'Month': month_name[month],  # Convert month number to name
                        'No_of_Appointment': count
                    })

        return appointment_summary

    # Example usage for populating the table
    def populate_table(self):
        # Clear the table before inserting new data
        for row in self.table.get_children():
            self.table.delete(row)

        data = self.get_appointments_summary()

        for entry in data:
            self.table.insert('', 'end', values=(
                entry['ID'],
                entry['Doctor'],
                entry['Month'],
                entry['No_of_Appointment']
            ))



    def populate_table2(self):
        """
        Populates `self.table2` with doctor-patient count data.
        """
        # Clear existing data in the table
        for row in self.table2.get_children():
            self.table2.delete(row)

        # Get the data
        data = self.get_total_patients_per_doctor()


        # Populate the table with data
        for idx, (doctor, patient_count) in enumerate(data.items(), start=1):
            self.table2.insert("", "end", values=(idx, doctor, patient_count))

        # Optional: Print the data to verify
        print("Table populated with data:", data)


    
    def populate_table3(self):
        """
        Populates `self.table3` with illnesses and the number of patients for each illness.
        """
        # Clear existing data in the table
        for row in self.table3.get_children():
            self.table3.delete(row)

        # Retrieve illness data: { 'Flu': 5, 'Cold': 3, ... }
        illness_data = admin.get_patients_by_illness(admin.patients)

        # Insert the data into the table
        for illness, count in illness_data.items():
            self.table3.insert("", "end", values=(illness, count))



    def column_chart(self, parent_frame):
        # Number of doctors (assuming this method exists)
        specialty_count = self.get_doctors_by_specialty()  # Adjust this method as needed

        # Prepare data for the bar chart
        specialties = list(specialty_count.keys())  # List of specialties
        doctor_counts = list(specialty_count.values())  # Corresponding doctor counts

        # Create a Matplotlib figure with one subplot (1 row, 1 column)
        fig, axs = plt.subplots(figsize=(5, 4), dpi=100)  # Single bar chart for the number of doctors

        # 1. Bar Chart (Row 0, Column 0)
        axs.bar(specialties, doctor_counts, color="skyblue", width=0.3)
        axs.set_title("Number of Doctors by Specialty", fontweight="bold")
        axs.set_ylabel("Counts", fontweight="bold")
        axs.set_xlabel("Specialty", fontweight="bold")
        
        # 2. Adjust layout to avoid overlaps
        plt.subplots_adjust(
            left=0.2,   # Space from the left edge of the figure
            right=0.9,  # Space from the right edge of the figure
            top=0.9,    # Space from the top of the figure
            bottom=0.2, # Space from the bottom of the figure
            hspace=0.5,  # Vertical space between rows
            wspace=0.3   # Horizontal space between columns
        )
        
        # Interactive click handler for bar chart
        def on_click_bar(event):
            if event.inaxes == axs:  # Check if the click is inside the bar chart axes
                for i, bar in enumerate(axs.patches):  # Loop through all the bars (patches)
                    if bar.contains(event)[0]:  # Check if the click is on the bar
                        value = doctor_counts[i]  # Get the corresponding count
                        category = specialties[i]  # Get the corresponding specialty
                        messagebox.showinfo(
                            "Data Point", f"Specialty: {category}\nCount: {value}"
                        )

        # Embed the Matplotlib figure into the customtkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")

        # Connect the click event to the handler
        canvas.mpl_connect("button_press_event", on_click_bar)

    
 

    def horizontal_chart(self, parent_frame):
        # 1. Get the appointments data for the chart
        appointments_data = self.get_appointments_per_month_per_doctor()
        doctors = list(appointments_data.keys())
        months = range(1, 13)  # Representing months from January to December

        # 2. Prepare stacked data
        stacked_data = {month: [] for month in months}
        for month in months:
            for doctor in doctors:
                stacked_data[month].append(appointments_data[doctor][month])

        # 3. Create the stacked column chart
        bottom_stack = [0] * len(months)
        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)

        for i, doctor in enumerate(doctors):
            monthly_counts = [appointments_data[doctor][month] for month in months]
            ax.bar(
                months, 
                monthly_counts, 
                bottom=bottom_stack, 
                label=doctor,
                color=plt.cm.Set3(i / len(doctors))
            )
            bottom_stack = [bottom_stack[j] + monthly_counts[j] for j in range(len(months))]

        # 4. Set abbreviated month names (Jan, Feb, Mar, ...) on the x-axis
        month_abbr = [month_name[month][:3] for month in months]  # Slice to get first 3 letters
        ax.set_xticks(months)
        ax.set_xticklabels(month_abbr)

        # 5. Add labels and title
        ax.set_title("Monthly Appointments Per Doctor", fontweight="bold")
        ax.set_ylabel("Number of Appointments", fontweight="bold")
        ax.set_xlabel("Month", fontweight="bold")
        ax.legend(title="Doctors")

         # 2. Adjust layout to avoid overlaps
        plt.subplots_adjust(
            left=0.2,   # Space from the left edge of the figure
            right=0.9,  # Space from the right edge of the figure
            top=0.9,    # Space from the top of the figure
            bottom=0.2, # Space from the bottom of the figure
            hspace=0.5,  # Vertical space between rows
            wspace=0.3   # Horizontal space between columns
        )

        # 6. Click handler for stacked bar chart
        def on_click_stacked(event):
            if event.inaxes == ax:
                x_value = int(round(event.xdata))
                y_value = event.ydata

                if x_value not in range(1, 13):
                    return

                cumulative_height = 0
                for i, doctor in enumerate(doctors):
                    doctor_count = appointments_data[doctor][x_value]
                    cumulative_height += doctor_count

                    if y_value <= cumulative_height:
                        messagebox.showinfo(
                            "Data Point Details",
                            f"Month: {month_name[x_value][:3]}\nDoctor: {doctor}\nAppointments: {doctor_count}"
                        )
                        break

        # 7. Embed the Matplotlib figure into the customtkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")

        # Connect click handler
        canvas.mpl_connect("button_press_event", on_click_stacked)


    def stacked_chart(self, parent_frame):
        doctor_patient_count = self.get_total_patients_per_doctor()
        if not doctor_patient_count:
            print("No data available for the chart.")
        else:
            print(doctor_patient_count)

        # Prepare data for the chart
        doctors = list(doctor_patient_count.keys())  # Get list of doctor names
        patient_counts = list(doctor_patient_count.values())  # Get the list of patient counts for each doctor

        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        # 4. Horizontal Bar Chart (Row 1, Column 2)
        ax.barh(doctors, patient_counts, color='lightcoral', height=0.3)
        ax.set_title("Number of Patients Per Doctors", fontweight="bold")
        ax.set_xlabel("Number of Patients", fontweight="bold")
        #axs[1, 1].set_ylabel("Doctors", fontweight="bold")

        plt.subplots_adjust(
            left=0.2,   # Space from the left edge of the figure
            right=0.8,  # Space from the right edge of the figure
            top=0.9,    # Space from the top of the figure
            bottom=0.2, # Space from the bottom of the figure
            hspace=0.5,  # Vertical space between rows
            wspace=0.3   # Horizontal space between columns
        )

        # Interactive click handler for horizontal bar chart
        def on_click_horizontal(event):
            if event.inaxes == ax:  # Check if the click is inside the horizontal bar chart axes
               for i, hor_bar in enumerate(ax.patches):  # Loop through all the bars (patches)
                if hor_bar.contains(event)[0]:  # Check if the click is on the bar
                    value = patient_counts[i]  # Get the corresponding count
                    category = doctors[i]  # Get the corresponding specialty
                    messagebox.showinfo(
                        "Data Point", f"Doctor: {category}\nCount: {value}"
                    )

        # Embed the Matplotlib figure into the customtkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")

        canvas.mpl_connect("button_press_event", on_click_horizontal)



    def select_frame_by_name(self, name):
        print(f"Switching to frame: {name}")
        # set button color for selected button
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
       
        # List of all frames to ensure they are hidden
        all_frames = [
            "home_frame",
            "doctor_table_frame", 
            "registration_frame",
            "update_frame",
            "delete_frame",
            "view_doctor_frame",
            "assign_frame",
            "relocate_frame",
            "patient_table_frame"
        ]
        
        # Hide all frames
        for frame_name in all_frames:
            if hasattr(self, frame_name):
                frame = getattr(self, frame_name)
                frame.grid_forget()
                
            
                
                
    
        # show selected frame
        if name == "dashboard":
            if not self.dashboard_frame.winfo_ismapped():
                self.refresh_dashboard_frame()
            self.dashboard_frame.grid(row=0, column=1, sticky="nsew")
           
        else:
            self.dashboard_frame.grid_forget()

        if name == "home":
            if not self.home_frame.winfo_ismapped():  # Only refresh if the frame is not currently visible
                self.refresh_frame()
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        
        if name == "frame_2":
            if not self.second_frame.winfo_ismapped():
                self.refresh_patient_frame()
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

            

        if name == "frame_3":
            self.refresh_appointment_frame()
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
            
        if name == "frame_4":
            self.refresh_system_frame()
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

        
        if name == "frame_5":
            self.admin_update_frame()
            
        if name == "patients_table_frame":
            self.patients_table_frame.grid(row=0, column=1, sticky="nsew")
            
        
            
            
   
    def dashboard_button_event(self):
        self.select_frame_by_name("dashboard")

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        """Event handler for the Back button."""
        print("Back button clicked!")  # Debug: Confirm the button click works
        
        self.select_frame_by_name("frame_2")
       


    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
     
        
    def frame_4_button_event(self):
         self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
         self.select_frame_by_name("frame_5")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
        
    def view_doctors(self):
        """Fetch doctors from Admin and display them in the table."""
        # Hide other frames
        self.home_frame.grid_forget()
        
          # Create a new frame for displaying doctors
        self.doctor_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.doctor_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
    
        # Configure grid weights for the frame
        self.doctor_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.doctor_table_frame.grid_columnconfigure(0, weight=1)

        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14))
        style.map("Treeview", background=[("selected", "gray75")])
        
        # Add a table to the frame
        self.table = ttk.Treeview(
            self.doctor_table_frame,
            columns=('ID', 'Full_Name', 'Speciality'),
            show='headings',
        )
        # Configure columns alignment
        self.table.column('ID', anchor="center", width=100)  # Center-align ID column
        self.table.column('Full_Name', anchor="center", width=200)  # Left-align Full Name column
        self.table.column('Speciality', anchor="center", width=200)  # Left-align Speciality column
        
        # Configure headers alignment
        self.table.heading('ID', text='ID', anchor="center")  # Center-align header
        self.table.heading('Full_Name', text='Full Name', anchor="center")  # Left-align header
        self.table.heading('Speciality', text='Speciality', anchor="center")  # Left-align header
        
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space
        
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.doctor_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with doctor data
        for i, doctor in enumerate(admin.get_doctors(), start=1):
            full_name = f"{doctor.get_first_name()} {doctor.get_surname()}"
            speciality = doctor.get_speciality()
            self.table.insert('', 'end', values=(i, full_name, speciality))


    def register_doctor_frame(self):
        self.home_frame.grid_forget()

        # Create the registration frame
        self.registration_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.registration_frame.grid(row=0, column=1, sticky="n", padx=50, pady=20)  # Added padding to center
        
        # Ensure the parent container is configured to allow space for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        
        # Registration label
        self.registration_label = customtkinter.CTkLabel(self.registration_frame, text="Register Doctor", font=("Roboto", 24))
        self.registration_label.grid(row=0, column=0, pady=10, padx=50)
        
        # Entry fields for registration form
        self.name_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter First Name")
        self.name_entry.grid(row=1, column=0, pady=10, padx=50)
        
        self.surname_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Surname")
        self.surname_entry.grid(row=2, column=0, pady=10, padx=50)
        
        self.speciality_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Speciality")
        self.speciality_entry.grid(row=3, column=0, pady=10, padx=50)
        
        # Registration button
        self.register_button = customtkinter.CTkButton(self.registration_frame, width=80, text="Register", command=self.register_doctor)
        self.register_button.grid(row=4, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.registration_frame, width=80, text="Back", command=self.home_button_event
        )
        self.back_button.grid(row=4, column=0, pady=10, padx=20, sticky="e")
        
        
    def register_doctor(self):
        
        # Get user inputs from the registration form
        first_name = self.name_entry.get().capitalize()
        surname = self.surname_entry.get().capitalize()
        speciality = self.speciality_entry.get().capitalize()
        
        # Debugging to confirm fetched values
        print(f"First Name: '{first_name}', Surname: '{surname}', Speciality: '{speciality}'")
     
        # Validate fields only when the "Register" button is clicked
        if not first_name or not surname or not speciality:
            messagebox.showerror("Error", "All fields are required!")
            return
        
     
        # Call the method to add a doctor to admin.doctors
        result = admin.get_doctor_details(admin.doctors, first_name, surname, speciality)
     
        if result:
            # Registration successful
            print(f"Doctor {first_name} {surname} registered successfully!")
            messagebox.showinfo("Success", f"Doctor {first_name} {surname} registered successfully!")
            self.registration_frame.grid_forget()
            self.home_button_event()
        else:
            # Handle the case where doctor already exists
            messagebox.showerror("Error", "Doctor with this name already exists.")
            
            
            
    def update_doctor_frame(self):
        self.home_frame.grid_forget()
        
        # Create a new frame for displaying doctors
        self.doctor_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.doctor_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space

        # Create the registration frame
        self.update_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.update_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
        
        # Configure grid weights for the frame
        self.doctor_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.doctor_table_frame.grid_columnconfigure(0, weight=1)

        
        # Registration label
        self.update_label = customtkinter.CTkLabel(self.update_frame, text="Update Doctor", font=("Roboto", 24))
        self.update_label.grid(row=0, column=0, pady=10, padx=50)
        
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
        # Add a table to the frame
        self.table = ttk.Treeview(
            self.doctor_table_frame,
            columns=('ID', 'Full_Name', 'Speciality'),
            show='headings',
        )
        # Configure columns alignment
        self.table.column('ID', anchor="center", width=100)  # Center-align ID column
        self.table.column('Full_Name', anchor="center", width=200)  # Left-align Full Name column
        self.table.column('Speciality', anchor="center", width=200)  # Left-align Speciality column
    
        # Configure headers alignment
        self.table.heading('ID', text='ID', anchor="center")  # Center-align header
        self.table.heading('Full_Name', text='Full Name', anchor="center")  # Left-align header
        self.table.heading('Speciality', text='Speciality', anchor="center")  # Left-align header
    
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
    
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.doctor_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        
        # Place the table and scrollbar side by side using grid
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Table expands to fill the table frame
        scrollbar.grid(row=0, column=1, sticky="ns",  padx=(0, 10))  # Scrollbar on the right, fills vertical space
        
    
        # Populate the table with doctor data
        for i, doctor in enumerate(admin.get_doctors(), start=1):
            full_name = f"{doctor.get_first_name()} {doctor.get_surname()}"
            speciality = doctor.get_speciality()
            self.table.insert('', 'end', values=(i, full_name, speciality))
    
            
        self.id_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Doctor ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
        # Entry fields for registration form
        self.name_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New First Name")
        self.name_entry.grid(row=4, column=0, pady=10, padx=50)
        
        self.surname_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New Surname")
        self.surname_entry.grid(row=5, column=0, pady=10, padx=50)
        
        self.speciality_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New Speciality")
        self.speciality_entry.grid(row=6, column=0, pady=10, padx=50)
        
       # Update button
        self.update_button = customtkinter.CTkButton(self.update_frame, width=80, text="Update", command=self.update_doctor)
        self.update_button.grid(row=7, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.update_frame, width=80, text="Back", command=self.home_button_event
        )
        self.back_button.grid(row=7, column=0, pady=10, padx=20, sticky="e")

        

    def update_doctor(self):
        # Get user inputs from the update form
        doctor_id = self.id_entry.get()  # Assuming an entry field for doctor ID is present
        new_first_name = self.name_entry.get().strip()
        new_surname = self.surname_entry.get().strip()
        new_speciality = self.speciality_entry.get().strip()
    
        # Debugging to confirm fetched values
        print(f"Doctor ID: '{doctor_id}', First Name: '{new_first_name}', Surname: '{new_surname}', Speciality: '{new_speciality}'")
    
        # Validate the ID field
        if not doctor_id.isdigit():
            messagebox.showerror("Error", "Doctor ID must be a valid number!")
            return
    
        # Validate the other fields
        if not new_first_name and not new_surname and not new_speciality:
            messagebox.showerror("Error", "At least one field must be updated!")
            return
        
        # Confirmation prompt
        if not messagebox.askyesno("Confirm Update", f"Are you sure you want to update Doctor ID {doctor_id}?"):
            return
    
        # Call the admin method to update doctor details
        success, message = admin.update_doctor_details(
            doctor_id,
            new_first_name=new_first_name,
            new_surname=new_surname,
            new_speciality=new_speciality
        )
    
        # Handle the result
        if success:
            print(message)
            messagebox.showinfo("Success", message)
            #self.update_frame.grid_forget()
            #self.doctor_table_frame.grid_forget()
            #self.view_doctors()  # Refresh the doctor list view
            self.home_button_event()
        else:
            print(message)
            messagebox.showerror("Error", message)


    def delete_doctor_frame(self):
        self.home_frame.grid_forget()
        self.doctor_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.doctor_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
        
        # Create the delete frame
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.delete_frame.grid(row=0, column=2, sticky="n", padx=50, pady=20)  # Added padding to center
        
        # Configure grid weights for the frame
        self.doctor_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.doctor_table_frame.grid_columnconfigure(0, weight=1)
        
        
        # Delete label
        self.delete_label = customtkinter.CTkLabel(self.delete_frame, text="Delete Doctor", font=("Roboto", 24))
        self.delete_label.grid(row=0, column=0, pady=10, padx=50)
        
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
        # Add a table to the frame
        self.table = ttk.Treeview(
            self.doctor_table_frame,
            columns=('ID', 'Full_Name', 'Speciality'),
            show='headings',
        )
        # Configure columns alignment
        self.table.column('ID', anchor="center", width=100)  # Center-align ID column
        self.table.column('Full_Name', anchor="center", width=200)  # Left-align Full Name column
        self.table.column('Speciality', anchor="center", width=200)  # Left-align Speciality column
    
        # Configure headers alignment
        self.table.heading('ID', text='ID', anchor="center")  # Center-align header
        self.table.heading('Full_Name', text='Full Name', anchor="center")  # Left-align header
        self.table.heading('Speciality', text='Speciality', anchor="center")  # Left-align header
    
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
    
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.doctor_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        
        # Place the table and scrollbar side by side using grid
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Table expands to fill the table frame
        scrollbar.grid(row=0, column=1, sticky="ns",  padx=(0, 10))  # Scrollbar on the right, fills vertical space
        
    
        # Populate the table with doctor data
        for i, doctor in enumerate(admin.get_doctors(), start=1):
            full_name = f"{doctor.get_first_name()} {doctor.get_surname()}"
            speciality = doctor.get_speciality()
            self.table.insert('', 'end', values=(i, full_name, speciality))
  
            
        self.id_entry = customtkinter.CTkEntry(self.delete_frame, width=220, placeholder_text="Doctor ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
       # Delete button
        self.delete_button = customtkinter.CTkButton(self.delete_frame, width=80, text="Delete", command=self.delete_doctor)
        self.delete_button.grid(row=4, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.delete_frame, width=80, text="Back", command=self.home_button_event
        )
        self.back_button.grid(row=4, column=0, pady=10, padx=20, sticky="e")

        

    def delete_doctor(self):
        # Get user inputs from the update form
        doctor_id = self.id_entry.get()  # Assuming an entry field for doctor ID is present
    
        # Debugging to confirm fetched values
        print(f"Doctor ID: '{doctor_id}'")
    
        # Validate the ID field
        if not doctor_id.isdigit():
            messagebox.showerror("Error", "Doctor ID must be a valid number!")
            return
     
        # Confirmation prompt
        if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Doctor ID {doctor_id}?"):
            return
        
    
        # Call the admin method to update doctor details
        success, message = admin.delete_doctor(
            doctor_id)
    
        # Handle the result
        if success:
            print(message)
            messagebox.showinfo("Success", message)
            #self.delete_frame.grid_forget()
            #self.doctor_table_frame.grid_forget()
            #self.view_doctors()  # Refresh the doctor list view
            self.home_button_event()
        else:
            print(message)
            messagebox.showerror("Error", message)
            
            
            
            
    def assign_doctor_to_patient_frame(self):
        """sumary_line
        Assign patient frame 
        """
        
        self.home_frame.grid_forget()
        
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
        

        self.assign_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.assign_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
        
    
        self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.patient_table_frame.grid_columnconfigure(0, weight=1)
        
        self.assign_label = customtkinter.CTkLabel(self.assign_frame, text="Assign Doctor", font=("Roboto", 24))
        self.assign_label.grid(row=0, column=0, pady=10, padx=50)
        
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
         # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=('ID', 'Full Name', 'Doctor\'s Name', 'Age', 'Mobile', 'Post Code', 'Symptoms'),
            show='headings',
        )
      
        self.table.column('ID', anchor="center", width=20, stretch=True)
        self.table.heading('ID', text="ID", anchor="center")
             
        self.table.column('Full Name', anchor="center", width=120, stretch=True)
        self.table.heading('Full Name', text="Full Name", anchor="center")
 
        self.table.column('Doctor\'s Name', anchor="center", width=130, stretch=True)
        self.table.heading('Doctor\'s Name', text="Doctor\'s Name", anchor="center")
    
        self.table.column('Age', anchor="center", width=40, stretch=True)
        self.table.heading('Age', text="Age", anchor="center")
        
        self.table.column('Mobile', anchor="center", width=100, stretch=True)
        self.table.heading('Mobile', text="Mobile", anchor="center")
       
        self.table.column('Post Code', anchor="center", width=80, stretch=True)
        self.table.heading('Post Code', text="Post Code", anchor="center")
          
        # Configure the "Symptoms" column with a wider width
        self.table.column('Symptoms', anchor="center", width=150, stretch=True)
        self.table.heading('Symptoms', text="Symptoms", anchor="center")
          
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
     
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with enriched patient data
        self.display_all_patients()
        
            
        self.id_entry = customtkinter.CTkEntry(self.assign_frame, width=220, placeholder_text="Enter Patient ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
        # Fetch doctor data
        doctors = admin.get_doctors()
        doctor_list = [f"{idx}: {doctor.full_name()} ({doctor.get_speciality()})" for idx, doctor in enumerate(doctors, start=1)]
        
        #ComboBox to select view option
        self.option = customtkinter.StringVar(value="Select Doctor")
        
        self.doctor_dropdown = customtkinter.CTkComboBox(self.assign_frame, variable=self.option, values=doctor_list, width=220, state="readonly",)
        self.doctor_dropdown.grid(row=4, column=0, pady=10, padx=50)
        
        
        #ComboBox to select view option
        self.view_option = customtkinter.StringVar(value="Select View Option")
        
        self.drop_down_menu = customtkinter.CTkOptionMenu(self.patient_table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                                command=self.update_table_view)
        self.drop_down_menu.grid(row=2, column=0, padx=8, pady=10, sticky="w")
        
     
        self.assign_button = customtkinter.CTkButton(self.assign_frame, width=80, text="Assign", command=self.assign_doctor_to_patient)
        self.assign_button.grid(row=5, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.assign_frame, width=80, text="Back", command=self.home_button_event
        )
        self.back_button.grid(row=5, column=0, pady=10, padx=20, sticky="e")


    

        
        
        
    def assign_doctor_to_patient(self):
        #Get user inputs from the update form
        patient_id = self.id_entry.get()
        
        selected_doctor = self.doctor_dropdown.get()  # Doctor selection from dropdown
        
        # Validate doctor selection and extract doctor ID
        if selected_doctor:
             try:
                 # Attempt to split and extract the doctor ID
                 doctor_id_str = selected_doctor.split(":")[0]
                 doctor_id = int(doctor_id_str)
             except (ValueError, IndexError):
                 messagebox.showerror("Error", f"Invalid doctor selection: '{selected_doctor}'. Please select a valid doctor.")
                 return
        else:
             messagebox.showerror("Error", "Please select a doctor.")
             return
         
        if not patient_id.isdigit():
             messagebox.showerror("Error", "Patient ID must be a valid number!")
             return
         
        if not all([patient_id, selected_doctor]):
            messagebox.showerror("Error", "All fields are required!")
            return
        

        # Confirmation prompt
        if not messagebox.askyesno("Confirm Update", f"Are you sure you want to assign Patient ID {patient_id}?"):
            return
        
        # Debugging to confirm fetched values
        
        print(f"Patient ID: '{patient_id}',  Doctor: '{selected_doctor}'")
        
        
        # Call the admin function
        success, message = admin.assign_doctor_to_patient(
            admin.patients, 
            patient_id,
            admin.doctors, 
            doctor_id
        )
        
       # Handle the result
        if success:
           print(message)
           messagebox.showinfo("Success", message)
           #self.assign_frame.grid_forget()
           #self.patient_table_frame.grid_forget()
           #self.view_patients_frame()  # Refresh the Patient list view
           self.home_button_event()
        else:
           print(message)
           messagebox.showerror("Error", message)
           
           
           
    def relocate_doctor_to_patient_frame(self):
         self.home_frame.grid_forget()
         
         # Create a new frame for displaying patient
         self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
         self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
         
         # Create the relocate frame
         self.relocate_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
         self.relocate_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
         
         # Configure grid weights for the frame
         self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
         self.patient_table_frame.grid_columnconfigure(0, weight=1)
         
         # Delete label
         self.relocate_label = customtkinter.CTkLabel(self.relocate_frame, text="Relocate Doctor", font=("Roboto", 24))
         self.relocate_label.grid(row=0, column=0, pady=10, padx=50)
         
         # Style for ttk.Treeview
         style = ttk.Style()
         style.theme_use("default")  # Use default theme for ttk widgets
         
         style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
         style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
         style.map("Treeview", background=[("selected", "gray75")])
     
          # Add a table to the frame
         self.table = ttk.Treeview(
             self.patient_table_frame,
             columns=('ID', 'Full Name', 'Doctor\'s Name', 'Age', 'Mobile', 'Post Code', 'Symptoms'),
             show='headings',
         )
       
         self.table.column('ID', anchor="center", width=20, stretch=True)
         self.table.heading('ID', text="ID", anchor="center")
              
         self.table.column('Full Name', anchor="center", width=120, stretch=True)
         self.table.heading('Full Name', text="Full Name", anchor="center")
      
         self.table.column('Doctor\'s Name', anchor="center", width=130, stretch=True)
         self.table.heading('Doctor\'s Name', text="Doctor\'s Name", anchor="center")
     
         self.table.column('Age', anchor="center", width=40, stretch=True)
         self.table.heading('Age', text="Age", anchor="center")
         
         self.table.column('Mobile', anchor="center", width=100, stretch=True)
         self.table.heading('Mobile', text="Mobile", anchor="center")
        
         self.table.column('Post Code', anchor="center", width=80, stretch=True)
         self.table.heading('Post Code', text="Post Code", anchor="center")
           
         # Configure the "Symptoms" column with a wider width
         self.table.column('Symptoms', anchor="center", width=150, stretch=True)
         self.table.heading('Symptoms', text="Symptoms", anchor="center")
           
         self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
      
         # Add a vertical scrollbar
         scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
         self.table.configure(yscrollcommand=scrollbar.set)
         scrollbar.grid(row=0, column=1, sticky="ns")
         
         # Populate the table with enriched patient data
         self.display_all_patients()
             
         self.id_entry = customtkinter.CTkEntry(self.relocate_frame, width=220, placeholder_text="Enter Patient ID")
         self.id_entry.grid(row=3, column=0, pady=10, padx=50)
         
         # Fetch doctor data
         doctors = admin.get_doctors()
         doctor_list = [f"{idx}: {doctor.full_name()} ({doctor.get_speciality()})" for idx, doctor in enumerate(doctors, start=1)]
         
         #ComboBox to select view option
         self.option = customtkinter.StringVar(value="Select Doctor")
         
         self.doctor_dropdown = customtkinter.CTkComboBox(self.relocate_frame, variable=self.option, values=doctor_list, width=220, state="readonly",)
         self.doctor_dropdown.grid(row=4, column=0, pady=10, padx=50)
         
         
         #ComboBox to select view option
         self.view_option = customtkinter.StringVar(value="Select View Option")
         
         self.drop_down_menu = customtkinter.CTkOptionMenu(self.patient_table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                                 command=self.update_table_view)
         self.drop_down_menu.grid(row=2, column=0, padx=8, pady=10, sticky="w")
         
        # Delete button
         self.relocate_button = customtkinter.CTkButton(self.relocate_frame, width=80, text="Relocate", command=self.relocate_doctor_to_patient)
         self.relocate_button.grid(row=5, column=0, pady=10, padx=20, sticky="w") 
         
         # Add a back button
         self.back_button = customtkinter.CTkButton(
             self.relocate_frame, width=80, text="Back", command=self.home_button_event
         )
         self.back_button.grid(row=5, column=0, pady=10, padx=20, sticky="e")
         
         
    def relocate_doctor_to_patient(self):
        #Get user inputs from the update form
        patient_id = self.id_entry.get()
        
        selected_doctor = self.doctor_dropdown.get()  # Doctor selection from dropdown
        
        # Validate doctor selection and extract doctor ID
        if selected_doctor:
             try:
                 # Attempt to split and extract the doctor ID
                 doctor_id_str = selected_doctor.split(":")[0]
                 doctor_id = int(doctor_id_str)
             except (ValueError, IndexError):
                 messagebox.showerror("Error", f"Invalid doctor selection: '{selected_doctor}'. Please select a valid doctor.")
                 return
        else:
             messagebox.showerror("Error", "Please select a doctor.")
             return
         
        if not patient_id.isdigit():
             messagebox.showerror("Error", "Patient ID must be a valid number!")
             return
         
        if not all([patient_id, selected_doctor]):
            messagebox.showerror("Error", "All fields are required!")
            return
        

        # Confirmation prompt
        if not messagebox.askyesno("Confirm Update", f"Are you sure you want to relocate Patient ID {patient_id}?"):
            return
        
        # Debugging to confirm fetched values
        
        print(f"Patient ID: '{patient_id}',  Doctor: '{selected_doctor}'")
        
        
        # Call the admin function
        success, message = admin.relocate_doctor_to_patient(
            admin.patients, 
            patient_id,
            admin.doctors, 
            doctor_id
        )
        
       # Handle the result
        if success:
           print(message)
           messagebox.showinfo("Success", message)
           self.home_button_event()
           #self.relocate_frame.grid_forget()
           #self.patient_table_frame.grid_forget()
           #self.view_patients_frame()  # Refresh the Patient list view
        else:
           print(message)
           messagebox.showerror("Error", message)
          
                

    def view_patients_frame(self):
       """Fetch view patients table."""
       # Hide other frames
       self.second_frame.grid_forget()
   
       self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
       self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
   
       # Configure grid weights for the frame
       self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
       self.patient_table_frame.grid_columnconfigure(0, weight=1)
   
       # Style for ttk.Treeview
       style = ttk.Style()
       style.theme_use("default")  # Use default theme for ttk widgets
       
       style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
       style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
       style.map("Treeview", background=[("selected", "gray75")])
   
        # Add a table to the frame
       self.table = ttk.Treeview(
           self.patient_table_frame,
           columns=('ID', 'Full_Name', 'Doctor\'s_Full_Name', 'Age', 'Mobile', 'Post_Code', 'Symptoms'),
           show='headings',
       )
       # Configure columns
       for col in ('ID', 'Full_Name', 'Doctor\'s_Full_Name', 'Age', 'Mobile', 'Post_Code', 'Symptoms'):
           self.table.column(col, anchor="center", width=100)
           self.table.heading(col, text=col.replace('_', ' '), anchor="center")
         
       self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
    
       # Add a vertical scrollbar
       scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
       self.table.configure(yscrollcommand=scrollbar.set)
       scrollbar.grid(row=0, column=1, sticky="ns")
    
       # Populate the table with enriched patient data
       self.display_all_patients()
       
       #ComboBox to select view option
       self.view_option = customtkinter.StringVar(value="Select View Option")
       
       self.drop_down_menu = customtkinter.CTkOptionMenu(self.patient_table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                               command=self.update_table_view)
       self.drop_down_menu.grid(row=1, column=0, padx=8, pady=10, sticky="w")

       # Add a back button
       self.back_button = customtkinter.CTkButton(
           self.patient_table_frame, text="Back", command=self.frame_2_button_event
       )
       self.back_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")  # Align to the bottom-right
       
       
    def display_all_patients(self):
        """Display all patients in the table."""
        # Clear existing data
        for item in self.table.get_children():
            self.table.delete(item)
    
        # Populate with all patients
        for i, patient in enumerate(admin.get_patients(), start=1):
            self.table.insert('', 'end', values=(
                i,
                patient['full_name'],
                patient['doctor_name'],
                patient['age'],
                patient['mobile'],
                patient['post_code'],
                patient['symptoms'],
            ))
       
     
    def display_patients_by_surname(self):
        """Display patients grouped by surname in the table."""
        # Clear existing data
        for item in self.table.get_children():
            self.table.delete(item)
        
        # Populate with grouped patients
        grouped_patients = admin.grouped__patients_by_surname(admin.get_patients())
        for surname, patient_list in grouped_patients.items():
            for i, patient in enumerate(patient_list, start=1):
                self.table.insert('', 'end', values=(
                    i,
                    patient['full_name'],
                    patient['doctor_name'],
                    patient['age'],
                    patient['mobile'],
                    patient['post_code'],
                    patient['symptoms'],
                ))
        
                
    def update_table_view(self, choice):
        """Update table view based on ComboBox selection."""
        if choice == "View All Patients":
            self.display_all_patients()
            messagebox.showinfo("Patient View", "You are now viewing all patients.")
        elif choice == "View Patients by Surname":
            self.display_patients_by_surname()
            messagebox.showinfo("Patient View", "You are now viewing patients grouped by surname.")


    def register_patient_frame(self):
       self.second_frame.grid_forget()

       # Create the registration frame
       self.registration_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
       self.registration_frame.grid(row=0, column=1, sticky="n", padx=50, pady=20)  # Added padding to center
       
       # Ensure the parent container is configured to allow space for centering
       self.grid_rowconfigure(0, weight=1)
       self.grid_columnconfigure(1, weight=1)
       
       # Registration label
       self.registration_label = customtkinter.CTkLabel(self.registration_frame, text="Register Patient", font=("Roboto", 24))
       self.registration_label.grid(row=0, column=0, pady=10, padx=50)
       
       # Entry fields for registration form
       self.name_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter First Name")
       self.name_entry.grid(row=1, column=0, pady=10, padx=50)
       
       self.surname_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Surname")
       self.surname_entry.grid(row=2, column=0, pady=10, padx=50)
       
       self.age_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Age")
       self.age_entry.grid(row=3, column=0, pady=10, padx=50)
        
       self.mobile_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Mobile")
       self.mobile_entry.grid(row=4, column=0, pady=10, padx=50)
        
       self.post_code_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Post Code")
       self.post_code_entry.grid(row=5, column=0, pady=10, padx=50)
        
       self.symptoms_entry = customtkinter.CTkEntry(self.registration_frame, width=220, placeholder_text="Enter Symptoms (comma-separated)")
       self.symptoms_entry.grid(row=6, column=0, pady=10, padx=50)
       
       # Fetch doctor data
       doctors = admin.get_doctors()
       doctor_list = [f"{idx}: {doctor.full_name()} ({doctor.get_speciality()})" for idx, doctor in enumerate(doctors, start=1)]
       
       #ComboBox to select view option
       self.option = customtkinter.StringVar(value="Select Doctor")
       
       self.doctor_dropdown = customtkinter.CTkComboBox(self.registration_frame, variable=self.option, values=doctor_list, width=220, state="readonly",)
       self.doctor_dropdown.grid(row=7, column=0, pady=10, padx=50)
       
       # Registration button
       self.register_button = customtkinter.CTkButton(self.registration_frame, width=80, text="Register", command=self.register_patient)
       self.register_button.grid(row=8, column=0, pady=10, padx=20, sticky="w") 
       
       # Add a back button
       self.back_button = customtkinter.CTkButton(
           self.registration_frame, width=80, text="Back", command=self.frame_2_button_event
       )
       self.back_button.grid(row=8, column=0, pady=10, padx=20, sticky="e")


    def register_patient(self):
        print("Register button clicked")
        
        # Get user inputs from the registration form
        first_name = self.name_entry.get().capitalize()
        surname = self.surname_entry.get().capitalize()
        age = self.age_entry.get()
        mobile = self.mobile_entry.get()
        post_code = self.post_code_entry.get().upper()
        raw_symptoms = self.symptoms_entry.get()
        symptoms = [symptom.strip().capitalize() for symptom in raw_symptoms.split(',')]
        
        selected_doctor = self.doctor_dropdown.get()  # Doctor selection from 
        if selected_doctor:
            try:
                doctor_id = int(selected_doctor.split(":")[0])
            except ValueError:
                messagebox.showerror("Error", "Invalid doctor selection.")
                return
        else:
            messagebox.showerror("Error", "Please select a doctor.")
            return
    
        # Validate fields
        if not all([first_name, surname, age, mobile, post_code, raw_symptoms]):
            messagebox.showerror("Error", "All fields are required!")
            return
    
        if not age.isdigit() or int(age) <= 0:
            messagebox.showerror("Error", "Please enter a valid positive integer for age.")
            return
    
        if not mobile.isdigit() or len(mobile) < 10:
            messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
            return
        if selected_doctor:
            doctor_id = int(selected_doctor.split(":")[0])
        else:
            messagebox.showerror("Error", "Please select a doctor.")
            return
        
        # Debugging to confirm fetched values
        print(f"First Name: '{first_name}', Surname: '{surname}', Mobile: '{mobile}', Age: '{age}', Post Code: '{post_code}', Symptoms: '{symptoms}', Docotor: '{selected_doctor}', ")
     
        # Call the admin function
        result = admin.get_patient_details(
            admin.patients, 
            first_name, 
            surname, 
            int(age), 
            mobile, 
            post_code, 
            symptoms, 
            admin.doctors, 
            doctor_id
        )
        
        # Handle the result
        if result is None:
            messagebox.showerror("Error", "Patient with this name already exists.")
        elif isinstance(result, tuple):
            messagebox.showinfo("Success", "Patient registration successful!")
            #self.registration_frame.grid_forget()
            self.frame_2_button_event()
            #self.display_all_patients()
            #self.view_patients_frame()  # Update the patient list view
            
        else:
            messagebox.showerror("Error", result[1])  # Display error message from admin
        
    def update_patient_frame(self):
        self.second_frame.grid_forget()
        
        # Create a new frame for displaying patient
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
        
        # Create the registration frame
        self.update_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.update_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
        
        
        # Configure grid weights for the frame
        self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.patient_table_frame.grid_columnconfigure(0, weight=1)
        
        # Registration label
        self.update_label = customtkinter.CTkLabel(self.update_frame, text="Update Patient", font=("Roboto", 24))
        self.update_label.grid(row=0, column=0, pady=10, padx=50)
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
         # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=('ID', 'Full Name', 'Doctor\'s Name', 'Age', 'Mobile', 'Post Code', 'Symptoms'),
            show='headings',
        )
        self.table.column('ID', anchor="center", width=20, stretch=True)
        self.table.heading('ID', text="ID", anchor="center")
             
        self.table.column('Full Name', anchor="center", width=120, stretch=True)
        self.table.heading('Full Name', text="Full Name", anchor="center")
 
        self.table.column('Doctor\'s Name', anchor="center", width=130, stretch=True)
        self.table.heading('Doctor\'s Name', text="Doctor\'s Name", anchor="center")
    
        self.table.column('Age', anchor="center", width=40, stretch=True)
        self.table.heading('Age', text="Age", anchor="center")
        
        self.table.column('Mobile', anchor="center", width=100, stretch=True)
        self.table.heading('Mobile', text="Mobile", anchor="center")
       
        self.table.column('Post Code', anchor="center", width=80, stretch=True)
        self.table.heading('Post Code', text="Post Code", anchor="center")
          
        # Configure the "Symptoms" column with a wider width
        self.table.column('Symptoms', anchor="center", width=150, stretch=True)
        self.table.heading('Symptoms', text="Symptoms", anchor="center")
          
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
     
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
     
        # Populate the table with enriched patient data
        self.display_all_patients()
        
        self.id_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Patient ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
        # Entry fields for registration form
        self.name_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New First Name")
        self.name_entry.grid(row=4, column=0, pady=10, padx=50)
        
        self.surname_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New Surname")
        self.surname_entry.grid(row=5, column=0, pady=10, padx=50)
        
        self.age_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New Age")
        self.age_entry.grid(row=6, column=0, pady=10, padx=50)
         
        self.mobile_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New Mobile")
        self.mobile_entry.grid(row=7, column=0, pady=10, padx=50)
         
        self.post_code_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="New Post Code")
        self.post_code_entry.grid(row=8, column=0, pady=10, padx=50)
         
        self.symptoms_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Enter Symptoms (comma-separated)")
        self.symptoms_entry.grid(row=9, column=0, pady=10, padx=50)
        
        # Fetch doctor data
        doctors = admin.get_doctors()
        doctor_list = [f"{idx}: {doctor.full_name()} ({doctor.get_speciality()})" for idx, doctor in enumerate(doctors, start=1)]
        
        #ComboBox to select view option
        self.option = customtkinter.StringVar(value="Select Doctor")
        
        self.doctor_dropdown = customtkinter.CTkComboBox(self.update_frame, variable=self.option, values=doctor_list, width=220, state="readonly",)
        self.doctor_dropdown.grid(row=10, column=0, pady=10, padx=50)
            
        #ComboBox to select view option
        self.view_option = customtkinter.StringVar(value="Select View Option")
        
        self.drop_down_menu = customtkinter.CTkOptionMenu(self.patient_table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                                command=self.update_table_view)
        self.drop_down_menu.grid(row=1, column=0, padx=8, pady=10, sticky="w")

        
       # Update button
        self.update_button = customtkinter.CTkButton(self.update_frame, width=80, text="Update", command=self.update_patient)
        self.update_button.grid(row=11, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.update_frame, width=80, text="Back", command=self.frame_2_button_event
        )
        self.back_button.grid(row=11, column=0, pady=10, padx=20, sticky="e")

    def update_patient(self):
        
       #Get user inputs from the update form
       patient_id = self.id_entry.get()
       new_first_name = self.name_entry.get().capitalize()
       new_surname = self.surname_entry.get().capitalize()
       new_age = self.age_entry.get()
       new_mobile = self.mobile_entry.get()
       new_post_code = self.post_code_entry.get().upper()
       raw_symptoms = self.symptoms_entry.get()
       symptoms = [symptom.strip().capitalize() for symptom in raw_symptoms.split(',')]
       
       selected_doctor = self.doctor_dropdown.get()  # Doctor selection from dropdown

        # Validate doctor selection and extract doctor ID
       if selected_doctor:
            try:
                # Attempt to split and extract the doctor ID
                doctor_id_str = selected_doctor.split(":")[0]
                doctor_id = int(doctor_id_str)
            except (ValueError, IndexError):
                messagebox.showerror("Error", f"Invalid doctor selection: '{selected_doctor}'. Please select a valid doctor.")
                return
       else:
            messagebox.showerror("Error", "Please select a doctor.")
            return
   
       # Validate fields
       if not all([new_first_name, new_surname, new_age, new_mobile, new_post_code, raw_symptoms]):
           messagebox.showerror("Error", "All fields are required!")
           return
   
       if not new_age.isdigit() or int(new_age) <= 0:
           messagebox.showerror("Error", "Please enter a valid positive integer for age.")
           return
   
       if not new_mobile.isdigit() or len(new_mobile) < 10:
           messagebox.showerror("Error", "Please enter a valid 10-digit mobile number.")
           return
       if selected_doctor:
           doctor_id = int(selected_doctor.split(":")[0])
       else:
           messagebox.showerror("Error", "Please select a doctor.")
           return
       
       # Confirmation prompt
       if not messagebox.askyesno("Confirm Update", f"Are you sure you want to update Patient ID {patient_id}?"):
           return
       
       # Debugging to confirm fetched values
       print(f"First Name: '{new_first_name}', Surname: '{new_surname}', Mobile: '{new_mobile}', Age: '{new_age}', Post Code: '{new_post_code}', Symptoms: '{symptoms}', Doctor: '{selected_doctor}', ")
    
       # Call the admin function
       success, message = admin.update_patient_detail(
           admin.patients, 
           patient_id,
           admin.doctors, 
           doctor_id,
           new_first_name, 
           new_surname, 
           int(new_age), 
           new_mobile, 
           new_post_code, 
           symptoms, 
           
       )
       
      # Handle the result
       if success:
          print(message)
          messagebox.showinfo("Success", message)
          self.display_all_patients()
          #self.update_frame.grid_forget()
          #self.patient_table_frame.grid_forget()
          #self.view_patients_frame()  # Refresh the Patient 
          # list view
       else:
          print(message)
          messagebox.showerror("Error", message)
          
          
          
    def delete_patient_frame(self):
        self.second_frame.grid_forget()
        
        # Create a new frame for displaying patient
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
        
        # Create the delete frame
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.delete_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
        
        
        # Configure grid weights for the frame
        self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.patient_table_frame.grid_columnconfigure(0, weight=1)
        
        # Delete label
        self.delete_label = customtkinter.CTkLabel(self.delete_frame, text="Delete Patient", font=("Roboto", 24))
        self.delete_label.grid(row=0, column=0, pady=10, padx=50)
        
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
         # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=('ID', 'Full Name', 'Doctor\'s Name', 'Age', 'Mobile', 'Post Code', 'Symptoms'),
            show='headings',
        )
      
        self.table.column('ID', anchor="center", width=20, stretch=True)
        self.table.heading('ID', text="ID", anchor="center")
             
        self.table.column('Full Name', anchor="center", width=120, stretch=True)
        self.table.heading('Full Name', text="Full Name", anchor="center")
 
        self.table.column('Doctor\'s Name', anchor="center", width=130, stretch=True)
        self.table.heading('Doctor\'s Name', text="Doctor\'s Name", anchor="center")
    
        self.table.column('Age', anchor="center", width=40, stretch=True)
        self.table.heading('Age', text="Age", anchor="center")
        
        self.table.column('Mobile', anchor="center", width=100, stretch=True)
        self.table.heading('Mobile', text="Mobile", anchor="center")
       
        self.table.column('Post Code', anchor="center", width=80, stretch=True)
        self.table.heading('Post Code', text="Post Code", anchor="center")
          
        # Configure the "Symptoms" column with a wider width
        self.table.column('Symptoms', anchor="center", width=150, stretch=True)
        self.table.heading('Symptoms', text="Symptoms", anchor="center")
          
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
     
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with enriched patient data
        self.display_all_patients()
            
        self.id_entry = customtkinter.CTkEntry(self.delete_frame, width=220, placeholder_text="Patient ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
        #ComboBox to select view option
        self.view_option = customtkinter.StringVar(value="Select View Option")
        
        self.drop_down_menu = customtkinter.CTkOptionMenu(self.patient_table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                                command=self.update_table_view)
        self.drop_down_menu.grid(row=2, column=0, padx=8, pady=10, sticky="w")
        
       # Delete button
        self.delete_button = customtkinter.CTkButton(self.delete_frame, width=80, text="Delete", command=self.delete_patient)
        self.delete_button.grid(row=4, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.delete_frame, width=80, text="Back", command=self.frame_2_button_event
        )
        self.back_button.grid(row=4, column=0, pady=10, padx=20, sticky="e")
       
        
       
    def delete_patient(self):
        # Get user inputs from the update form
        patient_id = self.id_entry.get()  # Assuming an entry field for doctor ID is present
    
        # Debugging to confirm fetched values
        print(f"Patient ID: '{patient_id}'")
    
        # Validate the ID field
        if not patient_id.isdigit():
            messagebox.showerror("Error", "Patient ID must be a valid number!")
            return
        
        # Validate fields
        if not patient_id:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Confirmation prompt
        if not messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete patient ID {patient_id}?"):
            return
    
        
        # Call the admin method to update doctor details
        success, message = admin.delete_patient(
            patient_id)
    
        # Handle the result
        if success:
            print(message)
            messagebox.showinfo("Success", message)
            #self.delete_frame.grid_forget()
            #self.patient_table_frame.grid_forget()
            #self.view_patients_frame()  # Refresh the patient list view
            self.display_all_patients()
        else:
            print(message)
            messagebox.showerror("Error", message)
            
            
            
    def discharge_patient_frame(self):
        self.second_frame.grid_forget()
        
        # Create a new frame for displaying patient
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
       
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.delete_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
        
        
        # Configure grid weights for the frame
        self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.patient_table_frame.grid_columnconfigure(0, weight=1)
        
       
        self.delete_label = customtkinter.CTkLabel(self.delete_frame, text=" Discharge Patient", font=("Roboto", 24))
        self.delete_label.grid(row=0, column=0, pady=10, padx=50)
        
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
         # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=('ID', 'Full Name', 'Doctor\'s Name', 'Age', 'Mobile', 'Post Code', 'Symptoms'),
            show='headings',
        )
      
        self.table.column('ID', anchor="center", width=20, stretch=True)
        self.table.heading('ID', text="ID", anchor="center")
             
        self.table.column('Full Name', anchor="center", width=120, stretch=True)
        self.table.heading('Full Name', text="Full Name", anchor="center")
 
        self.table.column('Doctor\'s Name', anchor="center", width=130, stretch=True)
        self.table.heading('Doctor\'s Name', text="Doctor\'s Name", anchor="center")
    
        self.table.column('Age', anchor="center", width=40, stretch=True)
        self.table.heading('Age', text="Age", anchor="center")
        
        self.table.column('Mobile', anchor="center", width=100, stretch=True)
        self.table.heading('Mobile', text="Mobile", anchor="center")
       
        self.table.column('Post Code', anchor="center", width=80, stretch=True)
        self.table.heading('Post Code', text="Post Code", anchor="center")
          
        # Configure the "Symptoms" column with a wider width
        self.table.column('Symptoms', anchor="center", width=150, stretch=True)
        self.table.heading('Symptoms', text="Symptoms", anchor="center")
          
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
     
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with enriched patient data
        self.display_all_patients()
            
        self.id_entry = customtkinter.CTkEntry(self.delete_frame, width=220, placeholder_text="Patient ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
        #ComboBox to select view option
        self.view_option = customtkinter.StringVar(value="Select View Option")
        
        self.drop_down_menu = customtkinter.CTkOptionMenu(self.patient_table_frame, variable=self.view_option, values=["View All Patients", "View Patients by Surname"],
                                                                command=self.update_table_view)
        self.drop_down_menu.grid(row=2, column=0, padx=8, pady=10, sticky="w")
        
       # Delete button
        self.discharge_button = customtkinter.CTkButton(self.delete_frame, width=80, text="Discharge", command=self.discharge_patient)
        self.discharge_button.grid(row=4, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.delete_frame, width=80, text="Back", command=self.frame_2_button_event
        )
        self.back_button.grid(row=4, column=0, pady=10, padx=20, sticky="e")
       
            
       
    def discharge_patient(self):
        # Get user inputs from the update form
        patient_id = self.id_entry.get()  # Assuming an entry field for doctor ID is present
    
        # Debugging to confirm fetched values
        print(f"Patient ID: '{patient_id}'")
    
        # Validate the ID field
        if not patient_id.isdigit():
            messagebox.showerror("Error", "Patient ID must be a valid number!")
            return
        
        # Validate fields
        if not patient_id:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Confirmation prompt
        if not messagebox.askyesno("Confirm Discharge", f"Are you sure you want to discharge patient ID {patient_id}?"):
            return
    
        
        # Call the admin method to update doctor details
        success, message = admin.discharged(
            patient_id, admin.discharged_patients)
    
        # Handle the result
        if success:
            print(message)
            messagebox.showinfo("Success", message)
            #self.delete_frame.grid_forget()
            #self.patient_table_frame.grid_forget()
            #self.view_patients_frame()  # Refresh the patient list view
            self.display_all_patients()
        else:
            print(message)
            messagebox.showerror("Error", message)
            
            
            
    def view_discharged_patient_frame(self):
   
       # Hide other frames
       self.second_frame.grid_forget()
   
       # Create a new frame for displaying doctors
       self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
       self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
   
       # Configure grid weights for the frame
       self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
       self.patient_table_frame.grid_columnconfigure(0, weight=1)
   
       # Style for ttk.Treeview
       style = ttk.Style()
       style.theme_use("default")  # Use default theme for ttk widgets
       
       style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
       style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
       style.map("Treeview", background=[("selected", "gray75")])
   
        # Add a table to the frame
       self.table = ttk.Treeview(
           self.patient_table_frame,
           columns=('ID', 'Full_Name', 'Doctor\'s_Full_Name', 'Age', 'Mobile', 'Post_Code', 'Symptoms'),
           show='headings',
       )
       # Configure columns
       for col in ('ID', 'Full_Name', 'Doctor\'s_Full_Name', 'Age', 'Mobile', 'Post_Code', 'Symptoms'):
           self.table.column(col, anchor="center", width=100)
           self.table.heading(col, text=col.replace('_', ' '), anchor="center")
         
       self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
    
       # Add a vertical scrollbar
       scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
       self.table.configure(yscrollcommand=scrollbar.set)
       scrollbar.grid(row=0, column=1, sticky="ns")
    
       # Populate the table with enriched patient data
       self.display_all_discharged_patients()
       

       # Add a back button
       self.back_button = customtkinter.CTkButton(
           self.patient_table_frame, text="Back", command=self.frame_2_button_event
       )
       self.back_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")  # Align to the bottom-right
       
       
    def display_all_discharged_patients(self):
        """Display all discharged patients in the table."""
        # Clear existing data from the table
        for item in self.table.get_children():
            self.table.delete(item)
        
        # Check if there are any discharged patients
        if not admin.discharged_patients:
            messagebox.showinfo("No Patients", "There are no discharged patients to display.")
            return
    
        # Populate with all patients
        for i, patient in enumerate(admin.discharged_patients, start=1):
            self.table.insert('', 'end', values=(
                i, #index
               patient.full_name(),
               patient.get_doctor(),
               patient.get_age(),
               patient.get_mobile(),
               patient.get_postcode(),
               ', '.join(patient.get_symptoms())
            ))
        messagebox.showinfo("Patient View", "You are now viewing all discharged patients.")
            
    
    def add_appointment_frame(self):
        """Frame to add an appointment."""
        self.third_frame.grid_forget()
    
        # Create a new frame for displaying patient
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
    
        # Create the add appointment frame
        self.update_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.update_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
    
        # Configure grid weights for the patient table frame
        self.patient_table_frame.grid_rowconfigure(0, weight=1)
        self.patient_table_frame.grid_columnconfigure(0, weight=1)
    
        # Appointment Label
        self.appointment_label = customtkinter.CTkLabel(self.update_frame, text="Add Appointment", font=("Roboto", 24))
        self.appointment_label.grid(row=0, column=0, pady=10, padx=50)
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        style.configure(
            "Treeview",
            background="lightgray",
            foreground="black",
            rowheight=30,
            fieldbackground="lightgray",
            font=("Arial", 12, "bold"),
        )
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14))
        style.map("Treeview", background=[("selected", "gray75")])
    
        # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=('ID', 'Full Name', 'Doctor\'s Name', 'Age', 'Mobile', 'Post Code', 'Symptoms'),
            show='headings',
        )
        self.table.column('ID', anchor="center", width=20, stretch=True)
        self.table.heading('ID', text="ID", anchor="center")
        self.table.column('Full Name', anchor="center", width=120, stretch=True)
        self.table.heading('Full Name', text="Full Name", anchor="center")
        self.table.column('Doctor\'s Name', anchor="center", width=130, stretch=True)
        self.table.heading('Doctor\'s Name', text="Doctor\'s Name", anchor="center")
        self.table.column('Age', anchor="center", width=40, stretch=True)
        self.table.heading('Age', text="Age", anchor="center")
        self.table.column('Mobile', anchor="center", width=100, stretch=True)
        self.table.heading('Mobile', text="Mobile", anchor="center")
        self.table.column('Post Code', anchor="center", width=80, stretch=True)
        self.table.heading('Post Code', text="Post Code", anchor="center")
        self.table.column('Symptoms', anchor="center", width=150, stretch=True)
        self.table.heading('Symptoms', text="Symptoms", anchor="center")
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space
    
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
    
        # Populate the table with enriched patient data
        self.display_all_patients()
    
        # Input for Patient ID
        self.id_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Patient ID")
        self.id_entry.grid(row=3, column=0, pady=10, padx=50)
        
    
        # Date Display Label
        self.date_label = customtkinter.CTkLabel(self.update_frame, text="Selected Date: None", font=("Arial", 14))
        self.date_label.grid(row=4, column=0, pady=1, padx=50, sticky="w")
        
        # Button to open calendar for selecting date
        self.date_button = customtkinter.CTkButton(
            self.update_frame, width=220, text="Select Appointment Date", command=self.open_calender
        )
        self.date_button.grid(row=5, column=0, pady=10, padx=50, sticky="w")
        
        # Date Display Label (Updated to show current date or None)
        # Store selected date and time
    
    
        time_list = ["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
                     "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM"]
    
        # ComboBox to select time
        self.option = customtkinter.StringVar(value="Select Time")
        self.time_dropdown = customtkinter.CTkComboBox(self.update_frame, variable=self.option, values=time_list, width=220)
        self.time_dropdown.grid(row=7, column=0, pady=10, padx=50)
        
        # Fetch doctor data
        doctors = admin.get_doctors()
        doctor_list = [f"{idx}: {doctor.full_name()} ({doctor.get_speciality()})" for idx, doctor in enumerate(doctors, start=1)]
        
        #ComboBox to select view option
        self.option = customtkinter.StringVar(value="Select Doctor")
        
        self.doctor_dropdown = customtkinter.CTkComboBox(self.update_frame, variable=self.option, values=doctor_list, width=220, state="readonly",)
        self.doctor_dropdown.grid(row=8, column=0, pady=10, padx=50)
        
    
        # Text Box for Appointment Notes
        self.text_box = customtkinter.CTkTextbox(self.update_frame, width=220, height=120)
        self.text_box.insert("1.0", "Add appointment notes")  # Placeholder text
        self.text_box.grid(row=9, column=0, pady=10, padx=50)
    
        # Update button
        self.update_button = customtkinter.CTkButton(
            self.update_frame, width=80, text="Submit", command=self.add_appointment
        )
        self.update_button.grid(row=10, column=0, pady=10, padx=20, sticky="w")
    
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.update_frame, width=80, text="Back", command=self.frame_3_button_event
        )
        self.back_button.grid(row=10, column=0, pady=10, padx=20, sticky="e")
    
        # Store selected date and time
        self.selected_date = None
        self.selected_time = None
        
        
    def open_calender(self):
        """Open a calendar window for date selection."""
        self.calendar_window = customtkinter.CTkToplevel(self)
        self.calendar_window.title("Select Date")
        self.calendar_window.geometry("300x300")
        
     # Create the Calendar widget
        self.calender_frame = Calendar(self.calendar_window, selectmode='day', year=2025, month=1, day=1, font=("Arial", 12))
        self.calender_frame.grid(pady=20)
        
        
        # Function to handle date selection
        def select_date():
            # Get the selected date from the calendar
            self.selected_date = self.calender_frame.get_date()
            
            self.update_date_label()

            # Ensure the GUI is updated after configuring the label
            self.update_idletasks()  # Force the GUI to update immediately
            
            print("Selected Date:", self.selected_date)
            
            # Close the calendar window
            self.calendar_window.destroy()
        
            # Select button to confirm the date
        self.select_button = customtkinter.CTkButton(self.calendar_window, text="Select", command=select_date)
        self.select_button.grid(pady=10)
        
        self.calendar_window.mainloop()  # Keep the window open until the user selects a date
        
    def update_date_label(self):
        """Update the date label in add_appointment_frame."""
        if hasattr(self, "date_label"):  # Ensure the label exists
            if self.selected_date:
                self.date_label.configure(text=f"Selected Date: {self.selected_date}")
            else:
                self.date_label.configure(text="Selected Date: None")
        
    def add_appointment(self):
        """Confirm the appointment with the selected date and time."""
        try:
            # Retrieve and validate inputs
            patient_id = self.id_entry.get()
            selected_doctor = self.doctor_dropdown.get()  # Replace with logic to get the doctor's ID if needed
            notes = self.text_box.get("1.0", "end").strip()
            selected_date = self.selected_date
            selected_time = self.time_dropdown.get()
            
            # Validate doctor selection and extract doctor ID
            if selected_doctor:
                 try:
                     # Attempt to split and extract the doctor ID
                     doctor_id_str = selected_doctor.split(":")[0]
                     doctor_id = int(doctor_id_str)
                 except (ValueError, IndexError):
                     messagebox.showerror("Error", f"Invalid doctor selection: '{selected_doctor}'. Please select a valid doctor.")
                     return
            else:
                 messagebox.showerror("Error", "Please select a doctor.")
                 return
             
            if not patient_id.isdigit():
                 messagebox.showerror("Error", "Patient ID must be a valid number!")
                 return

            if not selected_date or selected_time == "Select Time":
                messagebox.showerror("Error", "Please select both a date and time before confirming.")
                return
    
            print(f"Patient ID: '{patient_id}',  Doctor: '{selected_doctor}'")
            
            # Call create_appointment to handle logic
            success, message = admin.create_appointment(
                admin.patients,  # Replace with the actual list of patients
                patient_id,
                selected_date,
                selected_time,
                notes,
                admin.doctors,  # Replace with the actual list of doctors
                doctor_id
            )
    
            # Display feedback based on the operation's result
            if success:
                messagebox.showinfo("Success", message)
                #self.update_frame.grid_forget()
                self.patient_table_frame.grid_forget()
                #self.view_appointment_frame()  # Refresh the Patient list view
                #self.patient_table_frame.grid_forget()
                self.frame_3_button_event()
                #self.display_all_appointment()
            else:
                print(message)
                messagebox.showerror("Error", message)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            
        
        
    def view_appointment_frame(self):
        """Fetch appointments from Admin and display them in the table."""
        # Hide other frames
        self.third_frame.grid_forget()
        
        # Create a new frame for displaying appointments
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
        
        # Configure grid weights for the frame
        self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.patient_table_frame.grid_columnconfigure(0, weight=1)
        
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure(
            "Treeview",
            background="lightgray",
            foreground="black",
            rowheight=30,
            fieldbackground="lightgray",
            font=("Arial", 12, "bold"),
        )
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14))
        style.map("Treeview", background=[("selected", "gray75")])
        
        # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=("#", "Patient", "Doctor", "Date", "Time", "Notes"),
            show="headings",
        )
        # Configure columns
        self.table.column("#", anchor="center", width=50)  # Numbering column
        self.table.heading("#", text="No.", anchor="center")
        
        for col in ("Patient", "Doctor", "Date", "Time", "Notes"):
            self.table.column(col, anchor="center", width=150)
            self.table.heading(col, text=col, anchor="center")
        
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space
        
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Populate the table with appointment data
        self.display_all_appointment()
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.patient_table_frame, text="Back", command=self.frame_3_button_event
        )
        self.back_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")  # Align to the bottom-right

    
    def display_all_appointment(self):
        
        """Display all appointments in the table with numbering."""
        # Clear existing data
        for item in self.table.get_children():
            self.table.delete(item)
        
        # Retrieve and display all appointments
        appointments = admin.view_all_appointments(admin.doctors)
        if not appointments:
            #messagebox.showerror("Error", "No appoinment found" )
            print("No appointments found.")
            return
        
        for i, appointment in enumerate(appointments, start=1):  # Add numbering (start=1)
            self.table.insert(
                '',
                'end',
                values=(
                    i,  # Row number
                    appointment["patient"],
                    appointment["doctor"],
                    appointment["date"],
                    appointment["time"],
                    appointment["notes"],
                ),
            )

        
    def remove_appointment_frame(self):
        self.third_frame.grid_forget()
        
        # Create a new frame for displaying patient
        self.patient_table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patient_table_frame.grid(row=0, column=1, sticky="nsew")  # Fill available space
        
        self.update_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.update_frame.grid(row=0, column=2, sticky="n", padx=20, pady=20)  # Added padding to center
        
        
        # Configure grid weights for the frame
        self.patient_table_frame.grid_rowconfigure(0, weight=1)  # Table row
        self.patient_table_frame.grid_columnconfigure(0, weight=1)

        self.update_label = customtkinter.CTkLabel(self.update_frame, text="Remove Appointment", font=("Roboto", 24))
        self.update_label.grid(row=0, column=0, pady=10, padx=50)
    
    
        # Style for ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")  # Use default theme for ttk widgets
        
        style.configure("Treeview", background="lightgray", foreground="black", rowheight=30, fieldbackground="lightgray", font=("Arial", 12, "bold"))
        style.configure("Treeview.Heading", background="lightgray", foreground="black", font=("Arial", 14) )
        style.map("Treeview", background=[("selected", "gray75")])
    
         # Add a table to the frame
        self.table = ttk.Treeview(
            self.patient_table_frame,
            columns=("#", "Patient", "Doctor", "Date", "Time", "Notes"),
            show='headings',
        )
        self.table.column('#', anchor="center", width=20, stretch=True)
        self.table.heading('#', text="No.", anchor="center")
             
        self.table.column('Patient', anchor="center", width=110, stretch=True)
        self.table.heading('Patient', text="Patient", anchor="center")
 
        self.table.column('Doctor', anchor="center", width=120, stretch=True)
        self.table.heading('Doctor', text="Doctor", anchor="center")
        
        self.table.column('Date', anchor="center", width=80, stretch=True)
        self.table.heading('Date', text="Date", anchor="center")
       
        self.table.column('Time', anchor="center", width=80, stretch=True)
        self.table.heading('Time', text="Time", anchor="center")
          
        # Configure the "Symptoms" column with a wider width
        self.table.column('Notes', anchor="center", width=200, stretch=True)
        self.table.heading('Notes', text="Notes", anchor="center")
          
        self.table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Expand to fill space # Expand to fill space
     
        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self.patient_table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
     
        # Populate the table with enriched patient data
        self.display_all_appointment()
        
        # Entry fields for registration form
        self.name_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Enter Doctor Name")
        self.name_entry.grid(row=3, column=0, pady=10, padx=50)
        
        self.date_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Enter Date")
        self.date_entry.grid(row=4, column=0, pady=10, padx=50)
        
        self.time_entry = customtkinter.CTkEntry(self.update_frame, width=220, placeholder_text="Enter Time")
        self.time_entry.grid(row=5, column=0, pady=10, padx=50)
        
       # Update button
        self.update_button = customtkinter.CTkButton(self.update_frame, width=80, text="Sumbit", command=self.remove_appointment)
        self.update_button.grid(row=6, column=0, pady=10, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.update_frame, width=80, text="Back", command=self.frame_3_button_event
        )
        self.back_button.grid(row=6, column=0, pady=10, padx=20, sticky="e")
        
        
        
    def remove_appointment(self):
        try:
            # Retrieve and validate inputs
            selected_doctor = self.name_entry.get()  # Get doctor name
            selected_date = self.date_entry.get()           # Get the selected date
            selected_time = self.time_entry.get()     # Get the selected time
    
            # Validate fields
            if not all([selected_doctor, selected_date, selected_time]):
                messagebox.showerror("Error", "All fields are required!")
                return
    
            print(f"Attempting to remove appointment for Doctor: '{selected_doctor}', Date: '{selected_date}', Time: '{selected_time}'")
    
            # Call the admin function to remove the appointment
            success, message = admin.remove_appointment(
                admin.doctors,  # Pass the list of doctors
                selected_doctor,
                selected_date,
                selected_time
            )
    
            # Display feedback based on the operation's result
            if success:
                messagebox.showinfo("Success", message)
                #self.update_frame.grid_forget()
                #self.patient_table_frame.grid_forget()
                #self.view_appointment_frame()  # Refresh the appointment view
                #self.display_all_patients()
                self.frame_3_button_event()
            else:
                messagebox.showerror("Error", message)
    
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def get_doctors_by_specialty(self):
        """
        Returns a dictionary of specialties and the number of doctors in each specialty.
        """
        specialty_count = {}
        for doctor in admin.doctors:
            specialty = doctor.get_speciality()  # Get the doctor's specialty
            print(specialty)
            if specialty not in specialty_count:
                specialty_count[specialty] = 1
            else:
                specialty_count[specialty] += 1
        return specialty_count
    

    def get_total_patients_per_doctor(self):
        """
        Returns a dictionary where keys are doctor names and values are the total number of patients for each doctor.
        """
        doctor_patient_count = {}
    
        # Iterate through the list of doctors
        for doctor in admin.doctors:
            # Get the list of patients for each doctor (from the passed `patients` argument)
            patient_count = sum(1 for patient in admin.patients if patient.get_doctor() == doctor.full_name())
            
            # Store the doctor and their patient count
            doctor_patient_count[doctor.full_name()] = patient_count

            print(f"Doctor: {doctor.full_name()}, Patient Count: {patient_count}")
            
        return doctor_patient_count
    
    def get_appointments_per_month_per_doctor(self):
        """
        Returns a dictionary with doctor names as keys and another dictionary as values, 
        representing months and their corresponding appointment counts.
        """
        
        appointment_data = {}
        for doctor in admin.doctors:
            monthly_counts = {month: 0 for month in range(1, 13)}  # Initialize counts for all months

            for appointment in doctor.get_appointments():
                print(appointment)
                appointment_date = appointment['date']  # Assuming appointments have a 'date' key

                # Extract the month from the date string
                try:
                    appointment_month = int(appointment_date.split('/')[0])  # Extract month as an integer
                    monthly_counts[appointment_month] += 1  # Increment the count for the specific month

                    print(appointment_month)
                except (IndexError, ValueError):
                    print(f"Invalid date format for appointment: {appointment_date}")
                    continue

            appointment_data[doctor.full_name()] = monthly_counts

        return appointment_data

        
    def report_frame(self):
        pass
        


    def admin_update_frame(self):
        #self.fourth_frame.grid_forget()

        # Create the registration frame
        self.registration_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=320, height=380)
        self.registration_frame.grid(row=0, column=1, sticky="n", padx=50, pady=20)  # Added padding to center
        
        # Ensure the parent container is configured to allow space for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Registration label
        self.admin_label = customtkinter.CTkLabel(self.registration_frame, text="Update Admin Details", font=("Roboto", 20))
        self.admin_label.grid(row=0, column=0, pady=10, padx=50)
        
        # Entry fields for registration form
        self.username_entry = customtkinter.CTkEntry(self.registration_frame, width=180, placeholder_text="Enter Username")
        self.username_entry.grid(row=1, column=0, pady=10, padx=50)
        
        self.password_entry = customtkinter.CTkEntry(self.registration_frame, width=180, placeholder_text="Enter Password")
        self.password_entry.grid(row=2, column=0, pady=10, padx=50)
        
        self.confirm_entry = customtkinter.CTkEntry(self.registration_frame, width=180, placeholder_text="Confirm Password")
        self.confirm_entry.grid(row=3, column=0, pady=10, padx=50)
        
        # Registration button
        self.admin_button = customtkinter.CTkButton(self.registration_frame, width=70, text="Submit", command=self.admin_update)
        self.admin_button.grid(row=4, column=0, pady=8, padx=20, sticky="w") 
        
        # Add a back button
        self.back_button = customtkinter.CTkButton(
            self.registration_frame, width=70, text="Back", command=self.frame_5_button_event
        )
        self.back_button.grid(row=4, column=0, pady=8, padx=20, sticky="e")


    def admin_update(self):
      
        # Get user inputs from the registration form
        new_username = self.username_entry.get()
        new_password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()
        
        # Debugging to confirm fetched values
        print(f"Username: '{new_username}', Password: '{new_password}', Confirm Password: '{confirm_password}'")
     
        # Validate fields only when the "Register" button is clicked
        if not new_username or not new_password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return
    
     
        # Call the method to add a doctor to admin.doctors
        success, message = admin.update_details(new_username, new_password, confirm_password)
     
        if success:
            # Update successful
            messagebox.showinfo("Success",message)
            self.dashboard_button_event()
            #self.registration_frame.grid_forget()

        else:
            # Handle the case where doctor already exists
            messagebox.showerror("Error", message)




        
      
    
    
    
if __name__ == '__main__':
    app = App()
    app.mainloop()