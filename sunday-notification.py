"""
Run this program to send the text notification
to let people know when their order will arrive.
"""
import time
import config
import composemessages
from sendmessage import sendSingleMessage

def main():
    """
    Send the messages
    """
    messenger = composemessages.Messenger()
    messages = messenger.messages
    phoneNumbers = messenger.validPhoneNumbers

    for msg, number in zip(messages, phoneNumbers):
        time.sleep(1)
        sendSingleMessage(msg, number)

if __name__ == '__main__': main()