"""
Send the Thursday text out to remind people to order.
"""
import time
from composemessages import Messenger
from sendmessage import sendSingleMessage


def sendThursdayNotification(messageFileName):
    """
    Send the notification with the message text being
    stored in the {messageFileName} file.
    """
    with open(messageFileName, 'r') as n:
        notification = n.read()

    unique_numbers = {}
    m = Messenger()
    phoneNumbers = m.phoneNumbers
    firstNames = m.firstNames

    for number, name in zip(phoneNumbers, firstNames):
        unique_numbers[number] = name

    totalMessages = 0
    for number in unique_numbers:
        time.sleep(1)
        custom_notification = notification.replace("{NAME}", unique_numbers[number])
        sendSingleMessage(custom_notification, number)
        totalMessages += 1

    print("Total messages sent: {}".format(totalMessages))

def main():
    """
    Program entry point when being run.
    """
    sendThursdayNotification('text_messages/notification.txt')

if __name__ == '__main__': main()