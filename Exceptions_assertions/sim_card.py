class PrepaidPhoneError(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg

class PrepaidPhone:
    def __init__(self, limit = 100):
        self.limit = limit
        
    def get_limit(self):
        return self.limit
    
    def add_to_limit(self, add_limit):
        self.limit += add_limit
        
    def call(self, call_limit):
        try:
            if self.limit == 0:
                raise Exception("You have an empty account. Call has been interrupted.")
            self.limit -= call_limit
            if self.limit < 0:
                raise PrepaidPhoneError("You have reached the limit.Re-charging phone.")
            print("Call finished. Actual account money status: \n" + str(self.get_limit()))
        except Exception as e:
            print(e)
            print("You have to re-charege your prepaid phone. No mone detected!!!!")
        except PrepaidPhoneError as e:
            print(e)
            self.add_to_limit(abs(self.limit))
            print(self.limit)

prepaidphone = PrepaidPhone()
prepaidphone.call(60)
prepaidphone.call(60)
