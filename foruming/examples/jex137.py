#This is an example of usage of the foruming package
#This script will automatically reply to any post that contains a keyword, 
#similar to the jex137/sisa8447 bots that used to be active on the Off topic forum

import foruming

acc = foruming.account('USERNAME','PASSWORD')
par = foruming.parser()

keyword = 'KEYWORD'
response = 'RESPONSE'

while True:
    threads = par.parse(18)
    for thread in threads:
        posts = thread.getposts()
        for post in posts:
            if keyword in post.gettext():
                reply(response,thread.geturl())
                time.sleep(30)
