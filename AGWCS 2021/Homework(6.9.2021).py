#Base class
class Private:

  #Base function
    def __init__(self):
      self.Name = "Name: John Doe" #Public Information
      self.__Password = "123456" #Private Information
    
  #Getter
    def getPassword(self):
      print("Password: " + self.__Password)

  #Setter
    def setPassword(self, newPassword):
      self.__Password = newPassword
    
 
# Driver code
obj = Private()
print(obj.Name) #This is public information. It can be accessed freely.
#print(obj.__Password) This statement, if uncommented, will result in a traceback error. The information is private.
obj.getPassword() #This method will display the private variable.
obj.setPassword("132456") #heh heh heh im in...Anyways, this public method WILL change the private variable. 
obj.getPassword() #The password indeed has been changed to the new password that was previously set.
