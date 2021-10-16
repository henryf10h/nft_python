

# RETURN SPECIFIC LINE IN A FILE. EACH LINE IS ONE TOKEN URI.
def ipfs_to_id(_id):
    with open("./uris","r") as file:
         for i in enumerate(file):
             if i[0] == _id:
                print(i[1])
                return i[1]
 
if __name__ == '__main__':
    ipfs_to_id()


  