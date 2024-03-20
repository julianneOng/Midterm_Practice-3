class Phone_Book:
    def __init__(self):
        self.__data = {}  
    
    def addphonebook(self, name = None,  phone_number = None):
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, phone_number]
                print("Contact added successfully")
            else:
                print("Name and Phone Number already exists")
        


    def deletephonebook(self, name = None):
        if name != None:
            if name not in self.__data:
                print("Contact deleted successfully")
                del self.__data[name]
            else:
                print("Contact not found.")
        

    

    def searchphonebook(self, query = None, sort_field = None):
        if query != None:
            search_arr = []
            for key, val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
                        
            result = set()
            for word in query.lower().split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)
            
            ans = []
            for i in result:
                ans.append(search_arr[i][:-1])
            
            indx = 0
            if sort_field == "name":
                indx = 0
            indx = 1
            if sort_field == "phone_number":
                indx = 1
            
            ans.sort(key= lambda x : x[indx])

        else:
            return []

    def console(self):
        while True:
            try:
                print("Phone Book:\n1. Add contact\n2. Look up contact\n3. Delete contact\n4. Exit")
                n = int(input("Enter your choice: "))
                if n == 1:
                    name = input("Enter contact name: ")
                    phone_number = input("Enter phone number: ")
                    if len(name) == 0:
                        name = None
                    if len(phone_number) == 0:
                        phone_number = None
                    self.addphonebook(name, phone_number)
                    
                
                
                if n == 2:
                    query = input("Enter contact name:  ")
                    sort_by = input("John's phone number is ")
                    if len(query) == 0:
                        query = None
                    if len(sort_by) == 0:
                        sort_by = None
                    self.searchphonebook(query, sort_by)

                if n == 3:
                    name = input("Enter contact name: ")
                    if len(name) == 0:
                        name = None
                       
                    self.deletephonebook(name)
                
                if n == 4:
                    break

            except Exception as e:
                pass



phone_book = Phone_Book()
phone_book.console()
