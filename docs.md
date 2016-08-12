This is a formal documentation of all the end-user functions that can be used with this package

foruming.parser()

    parse(FORUM-ID) -returns a list of thread objects for each thread on the forum page of the given forum supplied
  
foruming.thread(THREAD-URL)

    getposts() -return a list of post objects for each post in the given thread
    
    getparent() -retunrs the id of the forum the thread is located in
    
    geturl() -returns the thread's url
    
    getauthor() -returns the author of the thread
    
    gettitle() -returns the title or subject of the thread
    
    
foruming.post()

    getparent() -returns the thread object that the post is in
    
    gettext() -returns the message of the post
    
    getauthor() -returns the author of the post
    
    getauthorpostcount() -returns the author's post count
    
    getauthorjoindate() -returns the author's joindate
    
    gettimestamp() -returns the time the post was made
    
    
foruming.account(USERNAME,PASSWORD)

    makethread(SUBJECT,BODY,FORUMID) -creates a post with the specified subject and body on the forum specified
    
    reply(REPLY,THREAD-URL) -creates a reply with the body specified on the thread specified
    
    getlaspost() -returns the url where the last thread or reply was made
    
    getusername() -returns the username of the  account
    
    getpassword() -returns the password of the account
