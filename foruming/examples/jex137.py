#

import foruming

acc = foruming.account('USERNAME','PASSWORD')
par = foruming.parser()

keyword = 'test'
response = 'response'

while True:
    threads = par.parse(18)
    for thread in threads:
        posts = thread.getposts()
        for post in posts:
        if keyword in post.gettext():
            reply('response',thread.geturl())
            time.sleep(30)
