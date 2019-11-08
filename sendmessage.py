"""
Send a single text message via. the messagebird API
"""
import messagebird
import config as c

def sendSingleMessage(message, phoneNumber, blacklist="user_data/blacklist.txt"):
    """
    Send the message {message} to the number {phoneNumber}
    If the number is in the blacklist, don't send the message
    """
    black_list = open(blacklist, "r")
    black_listed_nums = black_list.readlines()

    for number in black_listed_nums:
        if phoneNumber in number or number in phoneNumber:
            print("Sorry, the number: {} is in the black list.".format(phoneNumber))
            return

    print("Sending \"{}\" to {}".format(message, phoneNumber))
    try:
        client = messagebird.Client(c.API_KEY)
        # send the message
        client.message_create('FromMe', phoneNumber, message, {'reference':'Foobar'})
    except messagebird.client.ErrorException as err:
        print("An error occured while requesting a Message object.\n")
        for error in err.errors:
            print("Error:\nCode : {}".format(error.code))
            print("Description: {}".format(error.description))
            print("Parameter : {}\n".format(error.parameter))