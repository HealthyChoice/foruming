class account():
    
    def __init__(self,username,password):
        import requests
        self.url = 'https://www.roblox.com/newlogin'
        self.__username = username
        self.__password = password
        self.__session = requests.Session()
        self.__login = self.__session.post(url=self.url,data={
            'Username':username,
            'Password':password
            }
        )
        self.lasturl=None
        if not 'home' in self.__login.url:
            raise ValueError('Could not create account session')
        print(self.__login.status_code)

    def getvalues(self,source):
        import requests
        from lxml import html
        self.plxml = html.fromstring(source)
        return self.plxml.xpath('//input[@id="__VIEWSTATE"]/@value')[0], self.plxml.xpath('//input[@id="__EVENTVALIDATION"]/@value')[0]

    def makethread(self,subject,body,id):
        self.__baseurl = 'https://forum.roblox.com/Forum/AddPost.aspx?ForumID='+str(id)
        self.__credentials = self.__session.get(self.__baseurl)
        self.viewstate,self.eventvalidation = self.getvalues(self.__credentials.content)
        self.__post = self.__session.post(self.__baseurl,data = {
            'ctl00$cphRoblox$Createeditpost1$PostForm$NewPostSubject':subject,
            'ctl00$cphRoblox$Createeditpost1$PostForm$PostBody':body,
            'ctl00$cphRoblox$Createeditpost1$PostForm$PostButton':' Post ',
            '__VIEWSTATE':self.viewstate,
            '__EVENTVALIDATION':self.eventvalidation
            }
        )
        if self.__post.status_code == 200:
            if '-1' in self.__post.url:
                raise ValueError('Could not create post: floodchecked')
            elif '-4' in self.__post.url:
                raise ValueError('Could not create post: doubleposted')
            else:
                self.lasturl = self.__post.url
        else:
            raise ValueError('Could not create post!')

    def reply(self,body,url):
        import requests
        from lxml import html
        self.__baseurl = url
        if 'ShowPost' in url:
            self.__baseurl = url.replace('ShowPost','AddPost')
        self.__credentials = self.__session.get(self.__baseurl)
        self.viewstate,self.eventvalidation = self.getvalues(self.__credentials.content)
        self.__reply = self.__session.post(self.__baseurl,data = {
            'ctl00$cphRoblox$Createeditpost1$PostForm$PostBody':body,
            'ctl00$cphRoblox$Createeditpost1$PostForm$PostButton':' Post ',
            '__VIEWSTATE':self.viewstate,
            '__EVENTVALIDATION':self.eventvalidation
            }
        )
        if self.__reply.status_code == 200:
            if '-1' in self.__reply.url:
                raise ValueError('Could not create post: floodchecked')
            elif '-4' in self.__reply.url:
                raise ValueError('Could not create post: doubleposted')
            else:
                self.lasturl = self.__reply.url
        else:
            raise ValueError('Could not create post!')

    def getusername(self):
        return self.__username

    def getpassword(self):
        return self.__password

    def getlastpost(self):
        return self.lasturl
