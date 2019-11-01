MESSAGE_CONTENTS_FILENAME = "text_messages/message.txt"
ORDERS_FILENAME = "user_data/orders.csv"
API_KEY = ""
ORDER_NUMBER_ROW = "Order Number"
ORDER_STATUS_ROW = "Order Status"
FIRST_NAME_ROW = "First Name (Billing)"
ORDER_ITEM_ROW = "Item Name"
NUMBER_OF_ITEMS_ROW = "Quantity"
PHONE_NUMBER_ROW = "Phone (Billing)"

with open("secret/apikey", 'r') as f:
    API_KEY = f.read()