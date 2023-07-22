# Personal-HealthCareAssistant
from tkinter import *   #creating graphical user interfaces 
from tkinter import Toplevel  #create additional windows apart from the main application window.
import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image        # working with images in Python
from tkinter import messagebox        #displaying various types of message boxes
import random                   #generating random numbers,
import smtplib          #simple way to send emails 
import webbrowser       #opening URLs in web browsers.

def open_new_window():
    new_window = Toplevel()
    new_window.geometry('700x600')
    new_window.title('HealthCare')
    root.withdraw()
    # Add widgets to the new window as desired
    appointments_btn = Button(new_window, text='Book Appointments', bg='#0d2b45', fg='white',command=handle_appointment)
    appointments_btn.pack(pady=(50, 20), padx=100)
    appointments_btn.config(font=('Helvetica', 16), relief='groove')

    health_tips_btn = Button(new_window, text='Health Tips', bg='#0d2b45', fg='white', command=handle_health_tips)
    health_tips_btn.pack(pady=20, padx=100)
    health_tips_btn.config(font=('Helvetica', 16), relief='groove')
    
    checkme_btn = Button(new_window, text='CheckMe', bg='#0d2b45', fg='white', command=handle_check_me)
    checkme_btn.pack(pady=20, padx=100)
    checkme_btn.config(font=('Helvetica', 16), relief='groove')

    hospital_btn = Button(new_window, text='Hospitals Information', bg='#0d2b45', fg='white', command=handle_hospitals)
    hospital_btn.pack(pady=20, padx=100)
    hospital_btn.config(font=('Helvetica', 16), relief='groove')

    hospital_near_me = Button(new_window, text='Hospitals Near Me', bg='#0d2b45', fg='white', command= hospital_nearme)
    hospital_near_me.pack(pady=20, padx=100)
    hospital_near_me.config(font=('Helvetica', 16), relief='groove')

def handle_appointment():
    hospitals = {
        "Ruby Hall Clinic": "https://www.rubyhall.com",
        "Jehangir Hospital": "https://www.jehangirhospital.com",
        "Sancheti Hospital": "https://www.sanchetihospital.org",
        "Deenanath Mangeshkar Hospital": "https://www.dmhospital.org",
        "Sahyadri Super Speciality Hospital": "https://www.sahyadrihospital.com",
        "Aditya Birla Memorial Hospital": "https://www.adityabirlahospital.com",
        "Columbia Asia Hospital": "https://www.columbiaasia.com",
        "KEM Hospital": "https://kemhospitalpune.org/"
    }

    def open_hospital_website(hospital_url):
        webbrowser.open_new(hospital_url)

    app_book = Toplevel()
    app_book.title('Book Appointment')
    app_book.geometry('300x300')
    # app_book.iconbitmap("D:\Python\Tkinter\images.ico")
    #bg image
       # Create the "Go to Website" button
    def book_appointment():
        selected_hospital = hospital_dropdown.get()
        hospital_url = hospitals.get(selected_hospital)
        open_hospital_website(hospital_url)

    # Create the drop-down list to select a hospital
    hospital_dropdown = StringVar()
    hospital_dropdown.set("Select a hospital")

    drop_down = OptionMenu(app_book, hospital_dropdown, *hospitals.keys())
    drop_down.pack(pady=10)

    book_button = Button(app_book, text="Go to Website", command=book_appointment)
    book_button.pack()
    # button to close the window
    close_button = Button(app_book, text='Close', command=app_book.destroy)
    close_button.pack(pady=10)
    app_book.mainloop()
  
def handle_health_tips():
    # Add code to handle health tips button click
    tips_window = Toplevel()
    tips_window.title('Health Tips')
    tips_window.geometry('400x450')
    # tips_window.iconbitmap("D:\Python\Tkinter\healt_tips.ico")
    # bg image
    
    # Create a list of health tips with descriptions
    health_tips = {
        'Get plenty of sleep': 'Getting 7-8 hours of sleep each night is important for physical and mental health.',
        'Exercise regularly': 'Regular exercise can help improve cardiovascular health, boost mood, and maintain a healthy weight.',
        'Eat a balanced diet': 'A balanced diet that includes a variety of nutrient-rich foods can help prevent chronic diseases.',
        'Stay hydrated': 'Drinking plenty of water helps keep the body hydrated and can improve physical and cognitive performance.',
        'Wash your hands frequently': 'Washing your hands regularly can help prevent the spread of germs and reduce the risk of infection.',
        'Reduce stress': 'Chronic stress can have negative effects on both physical and mental health. Finding ways to manage stress, such as through meditation or exercise, can help improve overall health.',
        'Limit screen time': 'Excessive screen time can contribute to eyestrain, headaches, and poor sleep. It is recommended to take breaks from screens every hour and limit total screen time each day.',
        'Avoid smoking and tobacco use': 'Smoking and other tobacco use can increase the risk of many health problems, including cancer and heart disease. Quitting smoking or never starting in the first place is important for long-term health.',
        'Get regular check-ups': 'Regular check-ups with a healthcare provider can help identify and prevent health problems before they become serious.',
        'Maintain social connections': 'Social connections can have a positive impact on mental health and well-being. Spending time with loved ones, joining social groups or clubs, and volunteering can all help build social connections.',
        'Limit alcohol consumption': 'Drinking too much alcohol can have negative effects on health, including liver disease and increased risk of accidents. It is recommended to limit alcohol consumption to moderate levels (up to one drink per day for women, up to two drinks per day for men).',
        'Practice good posture': 'Good posture can help prevent back pain and improve overall physical health. It is important to maintain good posture while sitting, standing, and moving throughout the day.'
    }

    # Create a label to display the health tips
    tips_label = Label(tips_window, text='Here are some health tips:')
    tips_label.pack(pady=20)
    # Create a listbox
    tips_listbox = Listbox(tips_window, height=13)
    tips_listbox.pack(padx=40)
    # Add the health tips to the listbox
    for tip in health_tips:
        tips_listbox.insert(END, tip)
    #label to display the tip description
    tip_description = Label(tips_window, wraplength=400, justify='left')
    tip_description.pack(pady=10)
    # Create a function to update the tip description when a new tip is selected
    def update_tip_description(event):
        selected_tip = tips_listbox.get(tips_listbox.curselection())
        tip_description.config(text=health_tips[selected_tip])
    # Bind the listbox to the update_tip_description function
    tips_listbox.bind('<<ListboxSelect>>', update_tip_description)
    # button to close the window
    close_button = Button(tips_window, text='Close', command=tips_window.destroy)
    close_button.pack(pady=10)

def handle_check_me():
    check_me_window = Toplevel()
    check_me_window.title('Check Me')
    check_me_window.geometry('400x350')
    # check_me_window.iconbitmap("D:\Python\Tkinter\check_me.ico")
    
    sugar_level_label = Label(check_me_window, text='Sugar Level:')
    sugar_level_label.grid(row=1, column=0, padx=10, pady=10)
    sugar_level_entry = Entry(check_me_window)
    sugar_level_entry.grid(row=1, column=1)

    weight_label = Label(check_me_window, text='Weight(kg):')
    weight_label.grid(row=2, column=0, padx=10, pady=10)
    weight_entry = Entry(check_me_window)
    weight_entry.grid(row=2, column=1)

    height_label = Label(check_me_window, text='Height(cm):')
    height_label.grid(row=3, column=0, padx=10, pady=10)
    height_entry = Entry(check_me_window)
    height_entry.grid(row=3, column=1)

    result_label = Label(check_me_window, text='')
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def check_me():
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = round(weight * (100 ** 2) / (height ** 2), 3)
        sugar_level = float(sugar_level_entry.get())

        result = f'BMI: {bmi}\n'
        if bmi < 18.5:
            result += 'Your BMI is underweight. Please consult a doctor.'
        elif bmi < 24.9:
            result += 'Your BMI is normal. Keep it up!'
        elif bmi < 29.9:
            result += 'Your BMI is overweight. Please exercise regularly.'
        else:
            result += 'Your BMI is obese. Please consult a doctor.'

        result += '\n'

        if sugar_level < 80 or sugar_level > 140:
            result += 'Your sugar level is not within the normal range. Please consult a doctor.'

        result_label.config(text=result)

    check_button = Button(check_me_window, text='Check', command=check_me)
    check_button.grid(row=5, column=0, columnspan=2, pady=10)

    close_button = Button(check_me_window, text='Close', command=check_me_window.destroy)
    close_button.grid(row=6, column=0, columnspan=2, pady=10)

def handle_hospitals():
    hospitals = [
        {
            "name": "Ruby Hall Clinic",
            
            "doctors": [
                {"name": "Dr. Nirmala Castellino", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Parvez K.Grant", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr Rashmi Aderao", "speciality": "Dermatology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                {"name": "Dr. Rajendra Patil", "speciality": "Anesthesia", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Murarji Ghadge", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Sunita Tandulwadkar", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. Nitin Pai", "speciality": "IVF and Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Devashish Desai", "speciality": "Infectious Diseases", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. A.N. Sadre", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
            ],
        },
        {
            "name": "Noble Hospitals",
           
            "doctors": [
                {"name": "Dr. Sangeeta Chandrashekhar ", "speciality": "Anesthesiology", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Vishal Chaudhari", "speciality": "Bone & Joint", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr.Minish Jain", "speciality": "Cancer Care", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                {"name": "Dr. Prasad Shah", "speciality": "Cardiology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Akshay Raut", "speciality": "Dental & Maxillofacial Surgery", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Nudurat Kamal", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. Pramod Kadam", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Anuja Athale", "speciality": "Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Ramesh Dumbre", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
            ],
        },
   {
            "name": "Sancheti Hospital ",
           
            "doctors": [
                {"name": "Dr. Narendra Vaidya", "speciality": "Orthopedist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Rajeev Joshi", "speciality": "Orthopaedics Orthopedist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr. Sudheer Jadhav", "speciality": "", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                 {"name": "Dr. Sangeeta Chandrashekhar ", "speciality": "Anesthesiology", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Vishal Chaudhari", "speciality": "Bone & Joint", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr.Minish Jain", "speciality": "Cancer Care", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                {"name": "Dr. Prasad Shah", "speciality": "Cardiology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Akshay Raut", "speciality": "Dental & Maxillofacial Surgery", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Nudurat Kamal", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. Pramod Kadam", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Anuja Athale", "speciality": "Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Ramesh Dumbre", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
            ],
        },
     {
            "name": "Deenanath Mangeshkar Hospital",
           
            "doctors": [
               {"name": "Dr. Nirmala Castellino", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Parvez K.Grant", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr Rashmi Aderao", "speciality": "Dermatology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                {"name": "Dr. Rajendra Patil", "speciality": "Anesthesia", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Murarji Ghadge", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Sunita Tandulwadkar", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. Nitin Pai", "speciality": "IVF and Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Devashish Desai", "speciality": "Infectious Diseases", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. A.N. Sadre", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
            ],
        },
        {
            "name": "Sahyadri Super Speciality Hospital",
           
            "doctors": [
                 {"name": "Dr. Narendra Vaidya", "speciality": "Orthopedist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Rajeev Joshi", "speciality": "Orthopaedics Orthopedist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr. Sudheer Jadhav", "speciality": "", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                 {"name": "Dr. Nitin Pai", "speciality": "IVF and Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Devashish Desai", "speciality": "Infectious Diseases", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. A.N. Sadre", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
                 {"name": "Dr. Parvez K.Grant", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr Rashmi Aderao", "speciality": "Dermatology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},      
                {"name": "Dr. Murarji Ghadge", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Sunita Tandulwadkar", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"}              
               
            ],
        },
          {
            "name": "Aditya Birla Memorial Hospital ",
           
            "doctors": [
                {"name": "Dr. Murarji Ghadge", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Sunita Tandulwadkar", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. Nitin Pai", "speciality": "IVF and Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Devashish Desai", "speciality": "Infectious Diseases", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. A.N. Sadre", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
                {"name": "Dr. Narendra Vaidya", "speciality": "Orthopedist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Rajeev Joshi", "speciality": "Orthopaedics Orthopedist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr. Sudheer Jadhav", "speciality": "", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"}
            ],
        },
       {
            "name": "KEM Hospital (King Edward Memorial Hospital)",
           
            "doctors": [
                {"name": "Dr. Nirmala Castellino", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Parvez K.Grant", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr Rashmi Aderao", "speciality": "Dermatology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                {"name": "Dr. Rajendra Patil", "speciality": "Anesthesia", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"},     
                 {"name": "Dr. Narendra Vaidya", "speciality": "Orthopedist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Rajeev Joshi", "speciality": "Orthopaedics Orthopedist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr. Sudheer Jadhav", "speciality": "", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
            ],
        },
         {
            "name": "Columbia Asia Hospital",
            
            "doctors": [
                {"name": "Dr. Nirmala Castellino", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Parvez K.Grant", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr Rashmi Aderao", "speciality": "Dermatology", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 4 PM)"},
                {"name": "Dr. Rajendra Patil", "speciality": "Anesthesia", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Murarji Ghadge", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Sunita Tandulwadkar", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. A.N. Sadre", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
            ],
        },
        {
            "name": "Jehangir Hospital",
            
            "doctors": [
                {"name": "Dr. Nirmala Castellino", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. Parvez K.Grant", "speciality": "Cardiologist", "OPD Day(OPD Timings)": "Mon to Thu(4 PM - 8 PM)"},
                {"name": "Dr. Murarji Ghadge", "speciality": "ENT", "OPD Day(OPD Timings)": "Mon to Sat(4 PM - 8 PM)"},
                {"name": "Dr. Sunita Tandulwadkar", "speciality": "Gynaecology", "OPD Day(OPD Timings)": "Mon to Thu(9 AM - 1 PM)"},              
                {"name": "Dr. Nitin Pai", "speciality": "IVF and Endoscopy", "OPD Day(OPD Timings)": "Mon to Sat(10 AM - 1 PM)"}, 
                {"name": "Dr. Devashish Desai", "speciality": "Infectious Diseases", "OPD Day(OPD Timings)": "Mon to Sat(9 AM - 5 PM)"},
                {"name": "Dr. A.N. Sadre", "speciality": "Kidney Transplant", "OPD Day(OPD Timings)": "Mon to Sat(11 AM - 1 PM)"},
            ],
        },

    ]

    hospitals_window = Toplevel()
    hospitals_window.title("Hospitals Information")
    hospitals_window.geometry("500x400")

    hospitals_listbox = Listbox(hospitals_window, height=10,width=45)
    hospitals_listbox.pack(padx=30)

    # Add hospitals to the listbox
    for hospital in hospitals:
        hospitals_listbox.insert(END, hospital["name"])

    def show_hospital_info():
        selected_hospital = hospitals_listbox.get(ANCHOR)

        hospital_info = Toplevel()
        hospital_info.title(selected_hospital)
        hospital_info.geometry("600x400")
        
        # Table headers
        headers = ["Doctor Name", "Speciality", "OPD Day(OPD Timings)"]
        for i, header in enumerate(headers):
            header_label = Label(hospital_info, text=header, font=("Helvetica", 14, "bold"))
            header_label.grid(row=0, column=i, padx=10, pady=10)

        # Find the selected hospital in the hospitals list
        selected_hospital_info = next((hospital for hospital in hospitals if hospital["name"] == selected_hospital), None)

        if selected_hospital_info:
            # Table rows for doctors
            for row, doctor in enumerate(selected_hospital_info["doctors"]):
                doctor_name = Label(hospital_info, text=doctor["name"])
                doctor_name.grid(row=row + 1, column=0, padx=10, pady=5)

                speciality = Label(hospital_info, text=doctor["speciality"])
                speciality.grid(row=row + 1, column=1, padx=10, pady=5)

                contact = Label(hospital_info, text=doctor["OPD Day(OPD Timings)"])
                contact.grid(row=row + 1, column=2, padx=10, pady=5)
        else:
            # case when the selected hospital is not found in the hospitals list
            error_label = Label(hospital_info, text="Hospital information not found.")
            error_label.pack(pady=20)

    show_info_button = Button(hospitals_window, text="Show Info", command=show_hospital_info)
    show_info_button.pack(pady=10)

    close_button = Button(hospitals_window, text='Close', command=hospitals_window.destroy)
    close_button.pack(pady=10)

def hospital_nearme():
    webbrowser.open_new('https://www.google.com/maps/search/hospitals+near+me')

root = Tk()
#  change title
root.title('HealthCare')
root.geometry('700x600')
root.configure()
appointments_btn = Button(root, text='HealtCare Assistant', bg='#0d2b45', fg='white',command=open_new_window)
appointments_btn.pack(pady=(50, 20), padx=100)
appointments_btn.config(font=('Helvetica', 16), relief='groove')
root.mainloop()
