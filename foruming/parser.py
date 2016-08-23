class parser():

    def __init__(self):
        import requests
        self.roothtml = '//*[@class="forum-table-row"]/'


    def getelement(self,xpath,omitroot=False,strip=False):
        if not omitroot:
            self.elements = self.plxml.xpath(self.roothtml+xpath)
        else:
            self.elements = self.plxml.xpath(xpath)
        if strip:
            try:
                for e in range(0,len(self.elements)):
                    self.elements[e] = str(self.elements[e]).replace('\n','')
                    self.elements[e] = str(self.elements[e]).replace('\r','')
                    self.elements[e] = str(self.elements[e]).replace('\t','')
            except:
                raise ValueError('Cannot strip element: element is not a str')

        return self.elements
        
    def parse(self,forum):
        import requests
        from lxml import html
        
        self.titles = None
        self.authors = None
        self.urls = None

        self.__forum = forum
        from lxml import html
        if type(self.__forum) == str:
            self.__url = 'https://forum.roblox.com/Forum/ShowForum.aspx?ForumID='+self.__forum
        elif type(self.__forum) == int:
            self.__url = 'https://forum.roblox.com/Forum/ShowForum.aspx?ForumID='+str(self.__forum)

        self.page = requests.get(self.__url)
        self.plxml = html.fromstring(self.page.content)
        
        self.threadelements = self.plxml.xpath('//tr[@class="forum-table-row"]')

        self.threads = []
        for t in range(0,len(self.threadelements)):
            self.threads.append(thread(index=t,parent=self))


        return self.threads
    
class thread():

    def __init__(self,url=None,index=None,parent=None):
        import requests
        from lxml import html
        self.roothtml = '//tr[@class="forum-post"]/'
        self.parent = parent
        self.index = index
        
        self.url = url
        self.author = None
        self.title = None
		
        self.postelements = []
        self.plxml = None
 
    def getelement(self,xpath,omitroot=False,strip=False):
        if not omitroot:
            self.elements = self.plxml.xpath(self.roothtml+xpath)
        else:
            self.elements = self.plxml.xpath(xpath)
        if strip:
            try:
                for e in range(0,len(self.elements)):
                    self.elements[e] = str(self.elements[e]).replace('\n','')
                    self.elements[e] = str(self.elements[e]).replace('\r','')
                    self.elements[e] = str(self.elements[e]).replace('\t','')
            except:
                raise ValueError('Cannot strip element: element is not a str')
        
        if len(self.elements) == len(self.postelements) or omitroot:
            return self.elements
        else:
            raise ValueError('Unable to properly parse page. This is because forum layout has likely been changed. Please notify the developer so this package can be updated accourdingly')
     

    def getposts(self):
        import requests
        from lxml import html
        self.page = requests.get(self.geturl())
        self.plxml = html.fromstring(self.page.content)
        
        self.postelements = self.plxml.xpath('//*[@class="forum-post"]')
        self.texts = None
        self.authors = None 
        self.postcounts = None
        self.joindates = None 
        self.timestamps = None 
        self.posts = []
        for p in range(0,len(self.postelements)):
            self.posts.append(post(p,self))

        return self.posts

    def geturl(self):
        if self.parent == None:
            return self.url
        elif self.parent.urls == None:
            self.parent.urls = ['https://forum.roblox.com'+x for x in  self.parent.getelement('td[2]/a/@href')]
        return self.parent.urls[self.index]

    def getparent(self):
        return self.parent

    def gettitle(self):
        if self.parent == None:
            if self.plxml == None:
                import requests
                from lxml import html
                self.page = requests.get(self.url)
                self.plxml = html.fromstring(self.page.content)
            if self.title == None:
                self.title = self.getelement('//*[@id="ctl00_cphRoblox_PostView1_ctl00_PostTitle"]/text()',strip=True,omitroot=True)[0]
            return self.title            
        else:
            if self.parent.titles == None:
                self.parent.titles = self.parent.getelement('td[2]/a/div/div/text()',strip=True)
            return self.parent.titles[self.index]

    def getauthor(self):
        if self.parent == None:
            if self.author == None:
                self.author = self.getposts()[0].getauthor()
            return self.author
        elif self.parent.authors == None:
            self.parent.authors = self.parent.getelement('td[4]/a/div/div/text()',strip=True)
        return self.parent.authors[self.index]
    
class post():

    def __init__(self,index,parent,url=None):
        self.parent = parent
        self.index = index
        self.url = url

    def getparent(self):
        return self.parent

    def gettext(self):
        if self.parent.texts == None:
            self.parent.texts = [x.text_content() for x in self.parent.getelement('td[2]/table/tr[2]/td/span')]
        return self.parent.texts[self.index]

    def getauthor(self):
        if self.parent.authors == None:
            self.parent.authors = self.parent.getelement('td[1]/table/tr[1]/td/a/text()')
        return self.parent.authors[self.index]

    def getauthorpostcount(self):
        if self.parent.postcounts == None:
            self.parent.postcounts = [x for x in self.parent.getelement('td[1]/table/tr[4]/td/span/text()')]
        return self.parent.postcounts[self.index]

    def getauthorjoindate(self):
        if self.parent.joindates == None:
            self.parent.joindates = [x for x in self.parent.getelement('td[1]/table/tr[3]/td/span/text()')]
        return self.parent.joindates[self.index]

    def gettimestamp(self):
        if self.parent.timestamps == None:
            self.parent.timestamps = self.parent.getelement('td[2]/table/tr[1]/td/span/text()')
        return self.parent.timestamps[self.index]
