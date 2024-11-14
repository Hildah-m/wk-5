class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self._battery_life = battery_life  # Protected attribute

    def make_call(self, contact):
        print(f"Calling {contact} from {self.model}.")

    def send_message(self, contact, message):
        print(f"Sending message to {contact}: {message}")

    def charge(self):
        print(f"{self.model} is charging.")
        self._battery_life = 100  # Charging sets battery to 100%

# Derived class: SmartphoneWithCamera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_quality):
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality  # New attribute for camera quality

    def take_photo(self):
        if self._battery_life > 10:
            print(f"Taking a photo with {self.camera_quality} camera.")
            self._battery_life -= 10  # Each photo reduces battery life by 10%
        else:
            print("Battery too low to take a photo. Please charge.")

# Creating an instance of SmartphoneWithCamera
my_phone = SmartphoneWithCamera("Apple", "iPhone 13", 80, "12MP")
my_phone.make_call("Mukami")       # Calls Alice
my_phone.send_message("Hilda", "Hello!")  # Sends message to Bob
my_phone.take_photo()             # Takes a photo
print("Battery life:", my_phone._battery_life)  # Checking battery life
my_phone.charge()                 # Charges the phone
