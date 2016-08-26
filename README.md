# Foruming
A general purpose module for botting on the roblox forums. It will handle all the valildation tokens and html parser that makes botting all the more tedious

Specifically, you can do the following: 

-Create an account session by only supplying a username and password

-Create posts by only supplying the subject, body, and forum id

-Get lists of all the threads on the forum, with access to title, url, author, etc

-Get lists of all the posts in a threa, along with the author, text, etc

All of this seems simple enough but is in fact incredibly tedious to write functions for over and over again. This package will save me and you a great deal of time

# something something logs

this package is in beta. Currenlty there is no documentation which would make it pretty much unusable at the moment. I don't even know why I'm bothering to upload and publicize it. Oh well

im on vacation now, ill probably add the docs and work out the kinks when i get home, stay tuned.

# HOW TO INSTALL

Judging by the target userbase for this package, you are probably too dumb or techincally illiterate to know how to properly install python packages, so will do this just like we do in 'special school*

before you install you will need the following:

the python interpreter: if you didnt realize you'd need this by now then leave this page now

setuptools: special tool for installing packages. if you installed pip along with the python interpreter like you should've, 'pip install setuptools' should get them for you. if you have problems with this, google it, because setuptools and pip are separate from my package and will have widespread support among the python community

Follow these steps to install once you have the other tools installed

1. download the package: The simplest way to do this is click 'Download as ZIP'
2. extract it: the package will be in a compressed format by default, so it must be extracted. simply use 7zip or winrar to extract the zip file to an accessible spot on your computer, like your desktop
3. run the setup file: Open a terminal/command prompt in the directory you extracted and run this command: "python3 setup.py install". You shold probably run as administrator if you're on windows, or put 'sudo' in front of the aforementioned command if you use linux. If you use mac consider suicide
4. realize you've accomplished absolutely nothing in your life and likely never will: This step may take longer to complete than the others

There. that's literally it. If you cannot follow these simple steps you are very certianly mentally challenged

Troubleshooting:
if python3 setup.py install doesnt work, you can try 'pip3 install .' instead
If that still doesn't work, simply save any programs you write that use the module in the same folder with the module scripts, although if you do this you are most certainly a script kiddie.

To ensure that you haven't fucked up, open a python shell and type 'import foruming'. If the shell doesnt yell at you, you've done everything right. Congradulations on your demonstration of basic cognitive function.

reminder: this module is for python3. disgusting python2 peasants can get their filth-ridden hands off of my git page. their kind is not welcome here
