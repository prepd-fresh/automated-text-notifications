"""
Send texts to Prep'd Fresh customers
By: Ben Miller
"""
import messagebird
import csv
import config as c

class Messenger:
    """
    The Messenger object will collect the appropriate data,
    compose the messages, and then send them.
    """
    def __init__(self):
        
        self.orderNumbers = []
        self.orderStatus = []
        self.firstNames = []
        self.orderItems = []
        self.numberOfItems = []
        self.phoneNumbers = []
        self.messages = []
        self.validPhoneNumbers = []
        self.extractOrders()
        self.composeMessages()

    def lintPhoneNumbers(self):
        """
        Lint the phone numbers to be processed
        """
        for i in range(len(self.phoneNumbers)):
            self.phoneNumbers[i] = self.phoneNumbers[i].replace("+","").strip(" ").replace("-","")
            if (self.phoneNumbers[i][0] != '1'):
                self.phoneNumbers[i] = '1' + self.phoneNumbers[i]
        
    def extractOrders(self):
        """
        Extract the user data from the order data
        """
        with open(c.ORDERS_FILENAME, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                self.orderNumbers.append(row[c.ORDER_NUMBER_ROW])
                self.orderStatus.append(row[c.ORDER_STATUS_ROW])
                self.firstNames.append(row[c.FIRST_NAME_ROW])
                self.orderItems.append(row[c.ORDER_ITEM_ROW].replace(",",""))
                self.numberOfItems.append(row[c.NUMBER_OF_ITEMS_ROW])
                self.phoneNumbers.append(row[c.PHONE_NUMBER_ROW])

        self.lintPhoneNumbers()

    def composeMessages(self):
        """
        Create the messages that will be sent
        """
        with open(c.MESSAGE_CONTENTS_FILENAME, 'r') as f:
            defaultMessage = f.read()

        ordersDictionary = {}

        for i in range(len(self.orderNumbers)):
            if (self.orderNumbers[i] not in ordersDictionary):
                ordersDictionary[self.orderNumbers[i]] = self.orderStatus[i] + "," + self.phoneNumbers[i] + "," + self.firstNames[i] + "," + "(" + self.numberOfItems[i] + ") " + self.orderItems[i]
            else:
                ordersDictionary[self.orderNumbers[i]] = ordersDictionary[self.orderNumbers[i]] + "," + "(" + self.numberOfItems[i] + ") " + self.orderItems[i]

        totalMessages = []
        for key in ordersDictionary:
            newMessageContents = ordersDictionary[key].split(',')
            if (newMessageContents[0] != 'Failed'):
                newMessage = defaultMessage.replace('{NAME}', newMessageContents[2])
                self.validPhoneNumbers.append(newMessageContents[1])

                totalOrders = ""
                for i in range(3, len(newMessageContents)):
                    if (i == 3):
                        totalOrders += newMessageContents[i]
                    elif (i == len(newMessageContents) - 1):
                        totalOrders += (", and " + newMessageContents[i])
                    else:
                        totalOrders += (", " + newMessageContents[i])
                newMessage = newMessage.replace('{ORDER}', totalOrders)
                self.messages.append(newMessage)

def main():
    m = Messenger()

if __name__ == '__main__': main()
