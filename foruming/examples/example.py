#This is an example of usage of the foruming package
#This script will print out every thread subjecct and contained post on a given forum page(roblox talk by default), including usernames

import foruming

lendivider = 150

parser = foruming.parser()
threads = parser.parse(13)

for thread in threads:
        print('='**lendivider)
        print(thread.gettitle())
        print('='*lendivider)
        posts = thread.getposts()
        for post in posts:
                print(post.getauthor()+': '+post.gettext())
                print('-'*lendivider)
