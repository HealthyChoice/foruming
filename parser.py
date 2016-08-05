class parser():

    def __init__(self):
        import requests
        self.roothtml = '//*[@id="ctl00_cphRoblox_ThreadView1_ctl00_ThreadList"]/'
       
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
        
        print(self.elements)
        if len(self.elements) == len(self.threadelements):
            return self.elements
        else: 
            raise ValueError('Unable to properly parse page. This is because forum layout has likely been changed. Please notify the developer so this package can be updated accourdingly')
        
    def parse(self,forum):
        import requests
        from lxml import html

        self.__forum = forum
        from lxml import html
        if type(self.__forum) == str:
            self.__url = 'https://forum.roblox.com/Forum/ShowForum.aspx?ForumID='+self.__forum
        elif type(self.__forum) == int:
            self.__url = 'https://forum.roblox.com/Forum/ShowForum.aspx?ForumID='+str(self.__forum)

        self.page = requests.get(self.__url)
        self.plxml = html.fromstring(self.page.content)
        
        self.threadelements = self.plxml.xpath('//tr[@class="forum-table-row"]')
        print(len(self.threadelements))
        self.urls = ['https://forum.roblox.com'+x for x in self.getelement('tr/td[2]/a/@href')]
        self.titles = self.getelement('tr/td[2]/a/div/div/text()',strip=True)
        self.authors = self.getelement('tr/td[4]/a/div/div/text()',strip=True)
        self.lastpostURLs = self.getelement('tr/td[7]/a/@href')
        self.lastposts = []

        for lastpost in self.lastpostURLs:
            self.lastposts.append(thread(self,'https://forum.roblox.com'+lastpost))

        self.lastposters = self.getelement('tr/td[7]/a/div[2]/text()')

        self.threads = []
        for t in range(0,len(self.threadelements)):
            self.threads.append(thread(self,self.urls[t],self.__forum,self.titles[t],self.authors[t],self.lastposts[t],self.lastposters[t]))

        #reply number and view count functionality saved for a later version
        #self.replies = self.pxml.xpath(self.roothmtl+'//*[@class="normalTextSmaller"]')

        return self.threads
            
    def parsethread(self,thread):
        pass
    
    def parsepost(self,post):
        pass
    
class thread():

    def __init__(self,parent,url,forum=None,title=None,author=None,lastpost=None,lastposter=None):
        import requests
        from lxml import html
        self.roothtml = '//table[@id="ctl00_cphRoblox_PostView1_ctl00_PostList"]/'
        self.__url = url
        self.__forum = forum
        self.__title = title
        self.__author = author
        self.__lastpost = lastpost
        self.__lastposter = lastposter
    '''
    def getelement(self,xpath):
        self.elements = self.plxml.xpath(self.roothtml+xpath)
        print(len(self.elements))
        print(self.elements)
        if len(self.elements) == len(self.postelements):
            return self.elements
        else:
            raise ValueError('Unable to properly parse page. This is because forum layout has likely been changed. Please notify the developer so this package can be updated accourdingly')
    '''
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
        
        print(self.elements)
        print(len(self.elements))
        if len(self.elements) == len(self.postelements):
            return self.elements
        else:
            raise ValueError('Unable to properly parse page. This is because forum layout has likely been changed. Please notify the developer so this package can be updated accourdingly')
     

    def getposts(self):
        import requests
        from lxml import html
        self.page = requests.get(self.__url)
        self.plxml = html.fromstring(self.page.content)
        
        self.postelements = self.plxml.xpath('//*[@class="forum-post"]')
        self.texts = [x.text_content() for x in self.getelement('tr/td[2]/table/tr[2]/td/span')]
        self.authors = self.getelement('//tr[@class="forum-post"]/td[1]/table/tr[1]/td/a/text()',omitroot=True)
        self.authorpostcounts = [x for x in self.getelement('/tr/td[1]/table/tr[4]/td/span/text()')]
        self.authorjoindates = [x for x in self.getelement('tr/td[1]/table/tr[3]/td/span/text()')]
        self.timestamps = self.getelement('tr/td[2]/table/tr[1]/td/span/text()')
        self.posts = []
        for p in range(0,len(self.postelements)):
            self.posts.append(post(self,self.texts[p],self.authors[p],self.authorpostcounts[p],self.authorjoindates[p],self.timestamps[p]))


        return self.posts

    def geturl(self):
        return self.__url

    def getforum(self):
        return self.__forum

    def gettitle(self):
        return self.__title

    def getauthor(self):
        return self.__author

    def getlastpost(self):
        return self.__lastpost
    
    def getlastposter(self):
        return self.__lastposter
    
class post():

    def __init__(self,parent,text,author,authorpostcount,authorjoindate,timestamp):
        self.__parent = parent
        self.__text = text
        self.__author = author
        self.__authorpostcount = authorpostcount
        self.__authorjoindate = authorjoindate
        self.__timestamp = timestamp

    def getparent(self):
        return self.__parent
    def gettext(self):
        return self.__text

    def getauthor(self):
        return self.__author

    def getauthorpostcount(self):
        return self.__authorpostcount

    def getauthorjoindate(self):
        return self.__authorjoindate

    def gettimestamp(self):
        return self.__timestamp
