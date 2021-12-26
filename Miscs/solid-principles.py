# Single Responsisbility Principle

class TelePhoneDirectory:

    def __init__(self):
        pass
        
    
    def add_contact(self, name, phone):
        pass
        
       
    def edit_contact(self, phone):
        pass
        
    def delete_contact(self, phone):
        passs
        
    
    def search_contact(self, phone):
        pass
        
    def search_contact_by_name(self, name):
        pass 
        
myTelephoneDirectory = TelePhoneDirectory()
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.add_entry("Vikas", 678452)
print(myTelephoneDirectory)        
        
        
class StoreData:

    def __init__(self):
        pass
        
    def to_file(self, file_name, data):
        pass
        
    def ppersitent_to_database(self, data):
        pass
        
        
        
store_data = StoreData()
store_data.to_file(os.pwd(), myTelephoneDirectory)    


# Open(extenstion) - Close(modification) Principle


class CATEGORIES(enum):
    FURNITUE = 1
    KITCHEN = 2
    BUILDING_MATERIALS = 3
    CLOTHING = 4
    FITNESS =5 
    FOOD = 6
    
    
class DiscontCalculator(self):
    
    def __init__(self):
        pass
        
    def special_sale_discount_price(self):
        pass
        
    def festival_sale_discount_price(self):
        pass
        
    def seasonal_sale_discount_price(self):
        pass
        
    def custom_sale_discount_price(self):
        pass
        
        
        
class FurnitureMaintance(DiscontCalculator):

    def __init__(self):
        pass
        
    def custom_sale_discount_price(self):
        pass 
    

class KitchenMaintance(DiscontCalculator):

    def __init__(self):
        pass
        
    def custom_sale_discount_price(self):
        pass 


class ClothingMaintance(DiscontCalculator):

    def __init__(self):
        pass
        
    def custom_sale_discount_price(self):
        pass 



# Interface Segregation Principle
# - No client should be forced to depend on methods it does not use

class CallingDevice():
  @abstractmethod
  def make_calls():
    pass

class MessagingDevice():
  @abstractmethod
  def send_sms():
    pass

class InternetbrowsingDevice():
  @abstractmethod
  def browse_internet():
    pass

class SmartPhone(CallingDevice, MessagingDevice, InternetbrowsingDevice):
  def make_calls():
    #implementation
    pass

  def send_sms():
    #implementation
    pass

  def browse_internet():
    #implementation
    pass

class LandlinePhone(CallingDevice):
  def make_calls():
    #implementation
    pass
