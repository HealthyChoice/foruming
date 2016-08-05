class account():
    
    def __init__(self,username,password):
        import requests
        url = 'https://www.roblox.com/newlogin'
        self.__username = username
        self.__password = password
        self.__session = requests.Session()
        self.__login = self.__session.post(url=url,data={
            'Username':username,
            'Password':password
            }
        )
        if not 'home' in self.__login.url:
            raise ValueError('Could not create account session')
        print(self.__login.status_code)

    def makethread(self,subject,body,id):
        self.__baseurl = 'https://forum.roblox.com/Forum/AddPost.aspx?ForumID='+id
        self.__credentials = self.__session.get(self.__baseurl)
    def getusername(self):
        return self.__username

    def getpassword(self):
        return self.__password
