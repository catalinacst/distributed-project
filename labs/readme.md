# Simple Exercises to remember the socket methods and recommendations

This code is just a small probe of concepts to test again the socket.* implementations and threading.


# Debug 
If you want to run, you will need to run python3.6 **client and server**. 

You can run netstat or lsof to check the socket states: 
```sh
$ netstat -atn
$ lsof -i -n 
```
or if you want to check each time, you can watch each certain time: 

```sh
$ watch -n 1 'lsof -i -n |grep python'
```

you will get something like :  

>Every 1.0s: lsof -i -n |grep python                                                                                                  arth3missec: Wed Feb  6 19:16:12 2019

>python3  5336 c1b3r    3u  IPv4 6843386      0t0  TCP 127.0.0.1:46954->127.0.0.1:3030 (ESTABLISHED)

>python3 30390 c1b3r    3u  IPv4 6811170      0t0  TCP *:3030 (LISTEN)

>python3 30390 c1b3r   15u  IPv4 6811171      0t0  TCP 127.0.0.1:3030->127.0.0.1:46954 (ESTABLISHED)

