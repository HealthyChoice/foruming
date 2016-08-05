import foruming

Pars = foruming.parser()
threads = Pars.parse(18)
for thread in threads:
    print(thread.gettitle(),thread.getauthor(),thread.geturl())

posts = threads[1].getposts()
print([post.gettext() for post in posts])
print(posts[0].getparent().geturl())
