import os
import csv

from JobApplication import JobApplication

# create file
if not os.path.exists("jobs.csv"):
    with open("jobs.csv", "w") as file:
        pass


# todo: replace with db
def load_job_applications():
    with open("jobs.csv", 'r') as file:
        data = list(csv.reader(file))

    if len(data) == 0:
        insert_dummy_data()
        with open("jobs.csv") as file:
            data = list(csv.reader(file))

    print("applications", data)
    applications = []
    for application in data:
        print(application)
        try:
            company_name = application[0]
            position_title = application[1]
            address = application[2]
            contact_name = application[3]
            phone_number = application[4]
            job_pay = application[5]
            date_applied = application[6]
            interview_1_date = application[7]
            interview_2_date = application[8]
            notes = application[9]
            applications.append(JobApplication(company_name, position_title, address, contact_name,
                                               phone_number, job_pay, date_applied, interview_1_date, interview_2_date,
                                               notes))
        except IndexError:
            print("can't parse line", application)
    return applications


# todo: replace with db
def save_job_applications(job_applications: list[JobApplication]):
    with open("jobs.csv", 'w') as file:
        csv_writer = csv.writer(file)
        for application in job_applications:
            csv_writer.writerow([application.company_name,
                                 application.position_title,

                                 application.address,
                                 application.contact_name,
                                 application.phone_number,
                                 application.job_pay,
                                 application.date_applied,
                                 application.interview_1_date,
                                 application.interview_2_date,

                                 application.notes])


def insert_dummy_data():
    dummy_data = [
        JobApplication('Tijaabo', 'Software Engineer', 'Mogadishu',
                       'Maxamed', '6100000000', 2000.00, '2024-01-01', '2024-02-01', '2024-03-01',  'Tijaabo'),
    ]
    save_job_applications(dummy_data)
