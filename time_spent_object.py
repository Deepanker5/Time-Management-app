class time_spent:
    def __init__(self, subject, day, time):
        self.subject = subject
        self.day = day
        self.time_spent = time

    def serialize(self):
        return{
            "Day:": self.day,
            "Subject:": self.subject,
            "Time_spent:": self.time_spent
        }