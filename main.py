import PySimpleGUI as sg
import time
import functions
from JobApplication import JobApplication

sg.theme("green")

todays_date = sg.Text(time.strftime("%b %d, %Y"), key="date")
add_button = sg.Button("Add")
remove_button = sg.Button("Delete")

table_headings = ["Company Name", "Position Title", "Address", "Contact Name", "Phone Number",
                  "Job Pay", "Date Applied", "Interview 1 Date", "Interview 2 Date",
                  "Days Since Applying",
                  "Notes"]
jobs_table = sg.Table(headings=table_headings, key="jobs_table", vertical_scroll_only=False,
                      values=[application.to_list() for application in functions.load_job_applications()])

layout = [[todays_date], [add_button, remove_button,], [jobs_table]]

window = sg.Window("Job Application Tracker", layout=layout, resizable=True)

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            job_applications = functions.load_job_applications()
            company_name_label = sg.Text("Company Name")
            position_title_label = sg.Text("Position Title")
         
            address_label = sg.Text("Address")
            contact_name_label = sg.Text("Contact Name")
            phone_number_label = sg.Text("Phone Number")
            job_pay_label = sg.Text("Job Pay")
            date_applied_label = sg.Text("Date Applied")
            interview_1_date_label = sg.Text("Interview 1 Date")
            interview_2_date_label = sg.Text("Interview 2 Date")
           
            notes_label = sg.Text("Notes")

            company_name_input = sg.Input(key="company_name")
            position_title_input = sg.Input(key="position_title")
          
            address_input = sg.Input(key="address")
            contact_name_input = sg.Input(key="contact_name")
            phone_number_input = sg.Input(key="phone_number")
            job_pay_input = sg.Input(key="job_pay")
            date_applied_input = sg.InputText(key="date_applied")
            date_applied_calendar_input = sg.CalendarButton("Select Date", target="date_applied", format="%Y-%m-%d")
            interview_1_date_input = sg.InputText(key="interview_1_date")
            interview_1_calendar_input = sg.CalendarButton("Select Date", target="interview_1_date", format="%Y-%m-%d")
            interview_2_date_input = sg.InputText(key="interview_2_date")
            interview_2_calendar_input = sg.CalendarButton("Select Date", target="interview_2_date", format="%Y-%m-%d")
          
          
            notes_input = sg.Input(key="notes")

            ok_button = sg.Button("Ok", key="ok")
            cancel_button = sg.Button("Cancel", key="cancel")

            column1 = sg.Column([[company_name_label],
                                 [position_title_label],
                             
                                 [address_label],
                                 [contact_name_label],
                                 [phone_number_label],
                                 [job_pay_label],
                                 [date_applied_label],
                                 [interview_1_date_label],
                                 [interview_2_date_label],
                               
                                 [notes_label]])
            column2 = sg.Column([[company_name_input],
                                 [position_title_input],
                               
                                 [address_input],
                                 [contact_name_input],
                                 [phone_number_input],
                                 [job_pay_input],
                                 [date_applied_input, date_applied_calendar_input],
                                 [interview_1_date_input, interview_1_calendar_input],
                                 [interview_2_date_input, interview_2_calendar_input],
                                 [notes_input]])
            add_window = sg.Window("Add Job Application", layout=[[column1, column2], [ok_button, cancel_button]])
            while True:
                add_event, add_values = add_window.read()
                print(add_event, add_values)

                match add_event:
                    case "ok":
                        company_name = add_values['company_name']
                        position_title = add_values['position_title']

                        if company_name == '' or position_title == '':
                            sg.popup("Please enter a company name and position title")
                            continue

                        date_applied = add_values['date_applied']
                        if date_applied == '':
                            date_applied = time.strftime("%Y-%m-%d")

                        job_application = JobApplication(company_name, position_title,
                                                        add_values['address'],
                                                         add_values['contact_name'], add_values['phone_number'],
                                                         add_values['job_pay'], date_applied,
                                                         add_values['interview_1_date'], add_values['interview_2_date']
                                                        , add_values['notes'])
                        job_applications.append(job_application)
                        functions.save_job_applications(job_applications)

                        add_window.close()
                        window['jobs_table'].update(values=[i.to_list() for i in job_applications])
                    case "cancel":
                        add_window.close()
                        break
                    case sg.WIN_CLOSED:
                        break
        case "Delete":
            selected = values['jobs_table']
            job_applications = functions.load_job_applications()
            for index_to_delete in reversed(selected):
                job_applications.pop(index_to_delete)
            functions.save_job_applications(job_applications)
            window['jobs_table'].update(values=[job_application.to_list() for job_application in job_applications])

        case "Edit":
            pass
        case sg.WIN_CLOSED:
            break
