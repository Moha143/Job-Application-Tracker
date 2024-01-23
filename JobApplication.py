from datetime import datetime


class JobApplication:
    def __init__(self, company_name, position_title, address, contact_name, phone_number,
                 job_pay, date_applied, interview_1_date, interview_2_date,
                 notes):
        self.company_name = company_name
        self.position_title = position_title
     
        self.address = address
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.job_pay = job_pay
        self.date_applied = date_applied
        self.interview_1_date = interview_1_date
        self.interview_2_date = interview_2_date
        
        self.days_since_applying = ""
      
       
        try:
            delta = datetime.now() - datetime.strptime(self.date_applied, '%Y-%m-%d')
            self.days_since_applying = delta.days
        except (TypeError, ValueError):
            print("can't parse interview_1_date", self.interview_1_date)
      
       
      
        self.notes = notes

    def to_list(self):
        return [self.company_name,
                self.position_title,
             
                self.address,
                self.contact_name,
                self.phone_number,
                self.job_pay,
                self.date_applied,
                self.interview_1_date,
                self.interview_2_date,
             
                self.days_since_applying,
                
               
                self.notes]
