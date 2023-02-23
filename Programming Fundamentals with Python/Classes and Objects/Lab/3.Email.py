class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []
while command != "Stop":
    sender, receiver, content = command.split()
    emil = Email(sender, receiver, content)
    emails.append(emil)
    command = input()

indexes = [int(x) for x in input().split(", ")]

for idx, emil in enumerate(emails):
    if idx in indexes:
        Email.send(emil)
    print(Email.get_info(emil))

# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}:" \
#                f"{self.content}. Sent: {self.is_sent}"
#
#
# emails = []
#
# data = input()
#
# while data != 'Stop':
#     senders, receiver, content = data.split()
#     email = Email(senders, receiver, content)
#     emails.append(email)
#     data = input()
#
# indexes = [int(el) for el in input().split(", ")]
#
# for index, email in enumerate(emails):
#     if index in indexes:
#         emails[index].send()
#     get = Email.get_info(email)
#     print(get)
#     # print(f'{email.sender} says to {email.receiver}: '
#     #       f'{email.content}. Sent: {email.is_sent}')
