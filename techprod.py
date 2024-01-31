import matplotlib.pyplot as plt
# here is some code based upon practice examples I found in the book. 
Customer_1 = {}
Customer_2 = {}
'''To add AI training to your program, you can use machine learning techniques to train a model that can make predictions or recommendations based on customer behavior and item purchases. Here's a step-by-step guide on how you can incorporate AI training into your program:
Collect and preprocess data: Gather data on customer purchases, including the items they bought and the order in which they purchased them. Clean and preprocess the data to remove any inconsistencies or errors.
Define the problem: Determine the specific task you want the AI model to perform. For example, you might want the model to predict the next item a customer is likely to purchase based on their previous purchases.'''

computer_items = ["webcam", "Computer", "keyboard", "Mouse", "Monitor", "Printer", "Speakers", "Microphone", "Headphones", "Router", "Modem", "Ethernet Cable", "HDMI Cable", "VGA Cable", "Power Cable", "Power Strip", "Surge Protector", "USB Cable", "USB Hub", "USB Flash Drive", "External Hard Drive", "Internal Hard Drive", "Motherboard", "CPU", "GPU", "RAM", "Case", "Case Fan", "CPU Fan", "Thermal Paste", "Optical Drive", "Operating System", "Software", "Anti-Virus", "Anti-Malware", "Anti-Spyware", "Anti-Adware", "Anti-Ransomware", "Anti-Rootkit", "Anti-Phishing", "Anti-Keylogger", "Anti-Screenlogger", "Anti-Trojan", "Anti-Worm", "Anti-Rootkit", "Anti-Exploit", "Anti-Spa"]
# now we are attempting to create a list of items that a customer might want to purchase; and if they buy one item; what would determine the next
# for example; if they buy a computer; they will need a monitor, keyboard, mouse, and speakers.
class BuysItem:
    def __init__(self):
        self.customer = {}
        self.computer_items = ["webcam", "Computer", "keyboard", "Mouse", "Monitor", "Printer", "Speakers", "Microphone", "Headphones", "Router", "Modem", "Ethernet Cable", "HDMI Cable", "VGA Cable", "Power Cable", "Power Strip", "Surge Protector", "USB Cable", "USB Hub", "USB Flash Drive", "External Hard Drive", "Internal Hard Drive", "Motherboard", "CPU", "GPU", "RAM", "Case", "Case Fan", "CPU Fan", "Thermal Paste", "Optical Drive", "Operating System", "Software", "Anti-Virus", "Anti-Malware", "Anti-Spyware", "Anti-Adware", "Anti-Ransomware", "Anti-Rootkit", "Anti-Phishing", "Anti-Keylogger", "Anti-Screenlogger", "Anti-Trojan", "Anti-Worm", "Anti-Rootkit", "Anti-Exploit", "Anti-Spa"]
        #This is where I put the confidence value to these list of items; so that the program can determine what the next item is that the customer might want to purchase.
        computer_items = [
            ("webcam", 0.8),
            ("Computer", 0.9),
            ("keyboard", 0.7),
            ("Mouse", 0.65),
            ("Monitor", 0.9),
            ("Printer", 0.8),
            ("Speakers", 0.7),
            ("Microphone", 0.6),
            ("Headphones", 0.6),
            
        ]
   


##########################################################################################
        def plot_confidence_values(self):
                items = [item[0] for item in self.computer_items]
                confidence_values = [item[1] for item in self.computer_items]

                plt.bar(items, confidence_values)
                plt.xlabel('Computer Items') # also need to add the significance values to the graph
                plt.ylabel('Confidence Values')
                plt.title('Confidence Values of Computer Items')
                plt.show()

        # Create an instance of the BuysItem class
        buys_item = BuysItem()

        # Call the plot_confidence_values method to generate the plot
        buys_item.plot_confidence_values()

##########################################################################################
        
    def add_customer(self, customer_id):
        self.customer[customer_id] = {}

    def add_item(self, customer_id, item):
        if item in self.computer_items:
            self.customer[customer_id][item] = True
            if item == "Computer" or item == "keyboard": 
                self.computer_items.append(("Mouse", 0.90))  # Increase confidence for keyboard by 0.1
                print("The item has been added to your list of items purchased.")
        else:
            print("Invalid item.")
            
        if item == "Mouse":
            self.computer_items.append(("keyboard", 0.90))
            print("The item has been added to your list of items purchased. Would you like to add anything else?")
        else:
             print("Invalid item.")
       
        if item == "Monitor":
             self.computer_items.append(("Computer", 0.90, "keyboard", 0.90, "Mouse", 0.90, "Speakers", 0.90))
             print("The item has been added to your list of items purchased. Would you like to add anything else?")
        else:
             print("Invalid itme.")         


    def get_next_items(self, customer_id):
        items_purchased = self.customer[customer_id].keys()
        next_items = []
        for item in self.computer_items:
            if item not in items_purchased:
                next_items.append(item)
        return next_items
    
##########################################################################################
    def current_values(self, customer_id, computer_items): # use this as an attempt to get current purchase values
        print("The current items in your list are:", computer_items)
        return self.customer[customer_id]
########################################################################################## 
   
class returnsItem:
        def _init_(self,customer_id):
            self.customer = {}
            self.customer_items = ["webcam", "Computer", "keyboard", "Mouse", "Monitor", "Printer", "Speakers", "Microphone", "Headphones", "Router", "Modem", "Ethernet Cable", "HDMI Cable", "VGA Cable", "Power Cable", "Power Strip", "Surge Protector", "USB Cable", "USB Hub", "USB Flash Drive", "External Hard Drive", "Internal Hard Drive", "Motherboard", "CPU", "GPU", "RAM", "Case", "Case Fan", "CPU Fan", "Thermal Paste", "Optical Drive", "Operating System", "Software", "Anti-Virus", "Anti-Malware", "Anti-Spyware", "Anti-Adware", "Anti-Ransomware", "Anti-Rootkit", "Anti-Phishing", "Anti-Keylogger", "Anti-Screenlogger", "Anti-Trojan", "Anti-Worm", "Anti-Rootkit", "Anti-Exploit", "Anti-Spa"]  
            # I want to attempt to make a loop or a function that will get a confidence value for each of the items based on the item tat has been recently purchased.
            #IMPORTANT ^ 
            computer_items = [
            ("webccam", 0.8)
            ]
            
            remove_item = input("What item would you like to return? ")
            if remove_item in self.customer_items:
                self.customer[customer_id][remove_item] = False
                print("The item has been removed from your list of items purchased.")
            else:
                print("That item is not in the list of items purchased.")
                print("Please enter a valid item.")    


#  buys_item.plot_confidence_values()
#  Will have to add the confidence values for this as well. 