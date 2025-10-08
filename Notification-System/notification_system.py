from abc import ABC, abstractmethod

class Notification:
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self, recipient):
        print(f"Sending notification to {recipient}: {self.message}")

class EmailNotification(Notification):
    def send(self, email):
        print(f"Sending email to {email}: {self.message}")

class SMSNotification(Notification):
    def send(self, phone_number):
        print(f"Sending SMS to {phone_number}: {self.message}")

class WhatsappNotification(Notification):
    def send(self, phone_number):
        print(f"Sending Whatsapp to {phone_number}: {self.message}")

class PushNotification(Notification):
    def send(self, phone_number):
        print(f"Sending Push Notification to {phone_number}: {self.message}")

class UrgentNotification(Notification):
    def __init__(self, message):
        super().__init__(message)
        self.channels = [
            EmailNotification(message),
            SMSNotification(message),
            WhatsappNotification(message),
            PushNotification(message)
        ]

    def send(self, *recipients):
        print("\n```````````````Urgent Notification```````````````")
        print(f"\n🚨 Sending URGENT notification through all channels:")
        for channel in self.channels:
            if isinstance(channel, EmailNotification):
                channel.send(recipients[0])  # email
            else:
                channel.send(recipients[1])  # phone number
        print("✅ Urgent notification sent successfully!\n")

def main():
    print("\n========== Notification System ==========\n")

    notifications = [
        EmailNotification("Welcome to Python OOP!"),
        SMSNotification("Your OTP is 9876"),
        WhatsappNotification("Hey, how are you?"),
        PushNotification("You’ve got a new message!"),
        UrgentNotification("This is an urgent system-wide alert!")
    ]

    recipients = [
        "alex@example.com",
        "+911234567890",
        "+911234567890",
        "+911234567890",
        ("team@allchannels.com", "+911234567890")  # tuple for UrgentNotification: (email, phone_number)
    ]

    # 🔁 Polymorphism in action
    print("\n~~~~~Sending notifications...~~~~")
    print("\n")
    for notify, recipient in zip(notifications, recipients):
        if isinstance(notify, UrgentNotification):
            notify.send(*recipient)                 # unpack tuple for UrgentNotification
            print("`````````````````````````````````````````````````")  
        else:
            notify.send(recipient)
            print("--------------------------------------")
          

    print("\n========== End of Notification Demo ==========\n")

if __name__ == '__main__':
    main()