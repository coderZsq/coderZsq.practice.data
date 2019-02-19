#### ssh

```
$ ssh -p 22 parallels@172.16.23.91

The authenticity of host '172.16.23.91 (172.16.23.91)' can't be established.
ECDSA key fingerprint is SHA256:kQazyjG3fEbViREdwrb3tlvvHZO6DlR5YKztwgmzKY4.
Are you sure you want to continue connecting (yes/no)?
```

```
$ scp -P 22 parallels@172.16.23.91:Desktop/01.py .
$ scp -P 22 01.py parallels@172.16.23.91:Desktop
$ scp -P 22 -r parallels@172.16.23.91:Desktop/a demo
```

```
$ ssh-keygen
$ ssh-copy-id parallels@172.16.23.91
```

```
.ssh/config
Host Ubuntu
HostName 172.16.23.91
User parallels
Port 22
```

#### chmod

```
-rw-rw-r--  1 parallels parallels    0 Jan 29 10:40 01.py

$ chmod -rw 01.py
----------  1 parallels parallels    0 Jan 29 10:40 01.py

$ chmod +r 01.py
-r--r--r--  1 parallels parallels    0 Jan 29 10:40 01.py

$ chmod +w 01.py
-rw-rw-r--  1 parallels parallels    0 Jan 29 10:40 01.py

$ chmod +x 01.py
-rwxrwxr-x  1 parallels parallels    0 Jan 29 10:40 01.py*
$ ./01.py
hello world

$ chmod -x 01.py
-rw-rw-r--  1 parallels parallels   40 Jan 29 10:48 01.py

```

```
.
├── Parallels Shared Folders -> /media/psf
└── test
    └── 01.py

drwxrwxr-x  2 parallels parallels 4096 Jan 29 10:50 test/

$ chmod -x test/
drw-rw-r--  2 parallels parallels 4096 Jan 29 10:52 test/
$ cd test/
-bash: cd: test/: Permission denied

$ chmod +x test/
drwxrwxr-x  2 parallels parallels 4096 Jan 29 10:52 test/

$ chmod -rw test/
d--x--x--x  2 parallels parallels 4096 Jan 29 10:52 test/
$ cd test/
$ ls
ls: cannot open directory '.': Permission denied

$ chmod +r test/
dr-xr-xr-x  2 parallels parallels 4096 Jan 29 10:52 test/
$ cd test/
$ ls
01.py
$ touch 02.py
touch: cannot touch '02.py': Permission denied
```

#### group

```
$ groupadd dev
groupadd: Permission denied.
groupadd: cannot lock /etc/group; try again later.

$ sudo groupadd dev
$ cat /etc/group
dev:x:1001:

$ groupdel dev
groupdel: Permission denied.
groupdel: cannot lock /etc/group; try again later.

$ sudo groupdel dev
$ cat /etc/group

.
├── Parallels Shared Folders -> /media/psf
└── pythonstudy
drwxrwxr-x  2 parallels parallels 4096 Jan 29 11:13 pythonstudy/

$ sudo groupadd dev
$ chgrp -R dev pythonstudy/
chgrp: changing group of 'pythonstudy/': Operation not permitted
$ sudo chgrp -R dev pythonstudy/
drwxrwxr-x  2 parallels dev       4096 Jan 29 11:13 pythonstudy/
```

#### user 

```
$ sudo useradd -m -g dev zhangsan
$ ll /home/
total 16
drwxr-xr-x  4 root      root      4096 Jan 29 11:20 ./
drwxr-xr-x 24 root      root      4096 Aug 10  2017 ../
drwxr-xr-x 17 parallels parallels 4096 Jan 29 10:48 parallels/
drwxr-xr-x  2 zhangsan  dev       4096 Jan 29 11:20 zhangsan/

$ sudo passwd zhangsan
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

```
$ useradd lisi
useradd: Permission denied.
useradd: cannot lock /etc/passwd; try again later.

$ ll -l /etc/passwd
-rw-r--r-- 1 root root 2340 Jan 29 11:20 /etc/passwd

$ cat /etc/passwd | cat -n /etc/passwd
zhangsan:x:1001:1001::/home/zhangsan:

$ sudo useradd -g dev lisi
43	lisi:x:1002:1001::/home/lisi:

$ sudo userdel -r lisi
userdel: lisi mail spool (/var/mail/lisi) not found
userdel: lisi home directory (/home/lisi) not found

$ sudo useradd -m -g dev lisi
```

```
$ id lisi
uid=1002(lisi) gid=1001(dev) groups=1001(dev)
$ cat -n /etc/passwd | grep lisi
43	lisi:x:1002:1001::/home/lisi:
$ cat -n /etc/group | grep dev
35	plugdev:x:46:parallels
48	netdev:x:109:
69	dev:x:1001:

$ id zhangsan
uid=1001(zhangsan) gid=1001(dev) groups=1001(dev)
$ cat -n /etc/passwd | grep zhangsan
42	zhangsan:x:1001:1001::/home/zhangsan:

$ id
uid=1000(parallels) gid=1000(parallels) groups=1000(parallels),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
$ cat -n /etc/passwd | grep parallels
40	parallels:x:1000:1000:Parallels,,,:/home/parallels:/bin/bash
$ cat -n /etc/group | grep parallels
 5	adm:x:4:syslog,parallels
18	cdrom:x:24:parallels
21	sudo:x:27:parallels
23	dip:x:30:parallels
35	plugdev:x:46:parallels
52	lpadmin:x:113:parallels
67	parallels:x:1000:
68	sambashare:x:128:parallels
```
```
$ whoami
parallels

$ who
parallels tty7         2019-01-29 10:29 (:0)
parallels pts/6        2019-01-29 10:42 (172.16.23.170)
```

```
$ sudo usermod -G sudo zhangsan
$ cat -n /etc/group | grep parallels
 5	adm:x:4:syslog,parallels
18	cdrom:x:24:parallels
21	sudo:x:27:parallels,zhangsan
23	dip:x:30:parallels
35	plugdev:x:46:parallels
52	lpadmin:x:113:parallels
67	parallels:x:1000:
68	sambashare:x:128:parallels

$ ssh zhangsan@172.16.23.91
zhangsan@172.16.23.91's password:
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.10.0-28-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

530 packages can be updated.
332 updates are security updates.

New release '18.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Last login: Tue Jan 29 13:00:07 2019 from 172.16.23.170

$ sudo useradd -m -g dev wangwue
```

```
$ sudo usermod -s /bin/bash zhangsan
42	zhangsan:x:1001:1001::/home/zhangsan:/bin/bash
43	lisi:x:1002:1001::/home/lisi:
44	wangwu:x:1003:1001::/home/wangwu:
```

```
$ which passwd
/usr/bin/passwd
-rwsr-xr-x 1 root root 54256 May 17  2017 /usr/bin/passwd
$ ls -l /etc/passwd
-rw-r--r-- 1 root root 2413 Jan 29 13:12 /etc/passwd

$ which ls
$ ls -l /bin/ls
-rwxr-xr-x 1 root root 126584 Mar  3  2017 /bin/ls

$ which useradd
$ ls -l /usr/sbin/useradd
-rwxr-xr-x 1 root root 121568 May 17  2017 /usr/sbin/useradd
```

```
$ su parallels
parallels@parallels-vm:/home/zhangsan$
$ su - zhangsan
zhangsan@parallels-vm:~$
```

```
$ sudo chgrp dev pythonstudy/
drwxrwxr-x  2 parallels dev       4096 Jan 29 13:40 pythonstudy/
$ sudo chown zhangsan pythonstudy/
drwxrwxr-x  2 zhangsan  dev       4096 Jan 29 13:40 pythonstudy/
$ sudo chgrp parallels pythonstudy/
drwxrwxr-x  2 zhangsan  parallels 4096 Jan 29 13:40 pythonstudy/
```

```
.
├── 01.py
├── 123.txt
├── Parallels Shared Folders -> /media/psf
└── test
    └── a
        └── b
            └── c
                └── d
                
-rw-rw-r--  1 parallels parallels    0 Jan 29 13:52 01.py
chmod 754 01.py
-rwxr-xr--  1 parallels parallels    0 Jan 29 13:52 01.py*

-rw-rw-r--  1 parallels parallels    0 Jan 29 13:53 123.txt
$ chmod 640 123.txt
-rw-r-----  1 parallels parallels    0 Jan 29 13:53 123.txt

drwxrwxr-x  3 parallels parallels 4096 Jan 29 13:55 test/
$ chmod -R 755 test/
drwxr-xr-x  3 parallels parallels 4096 Jan 29 13:55 test/
drwxr-xr-x  3 parallels parallels 4096 Jan 29 13:55 a/
drwxr-xr-x  3 parallels parallels 4096 Jan 29 13:55 b/
drwxr-xr-x  3 parallels parallels 4096 Jan 29 13:55 c/
drwxr-xr-x  3 parallels parallels 4096 Jan 29 13:55 d/
```

#### system

```
$ date
Tue Jan 29 14:02:16 CST 2019

```
```
$ cal
    January 2019
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

$ cal -y
                            2019
      January               February               March
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
       1  2  3  4  5                  1  2                  1  2
 6  7  8  9 10 11 12   3  4  5  6  7  8  9   3  4  5  6  7  8  9
13 14 15 16 17 18 19  10 11 12 13 14 15 16  10 11 12 13 14 15 16
20 21 22 23 24 25 26  17 18 19 20 21 22 23  17 18 19 20 21 22 23
27 28 29 30 31        24 25 26 27 28        24 25 26 27 28 29 30
                                            31

       April                  May                   June
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6            1  2  3  4                     1
 7  8  9 10 11 12 13   5  6  7  8  9 10 11   2  3  4  5  6  7  8
14 15 16 17 18 19 20  12 13 14 15 16 17 18   9 10 11 12 13 14 15
21 22 23 24 25 26 27  19 20 21 22 23 24 25  16 17 18 19 20 21 22
28 29 30              26 27 28 29 30 31     23 24 25 26 27 28 29
                                            30

        July                 August              September
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6               1  2  3   1  2  3  4  5  6  7
 7  8  9 10 11 12 13   4  5  6  7  8  9 10   8  9 10 11 12 13 14
14 15 16 17 18 19 20  11 12 13 14 15 16 17  15 16 17 18 19 20 21
21 22 23 24 25 26 27  18 19 20 21 22 23 24  22 23 24 25 26 27 28
28 29 30 31           25 26 27 28 29 30 31  29 30


      October               November              December
Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
       1  2  3  4  5                  1  2   1  2  3  4  5  6  7
 6  7  8  9 10 11 12   3  4  5  6  7  8  9   8  9 10 11 12 13 14
13 14 15 16 17 18 19  10 11 12 13 14 15 16  15 16 17 18 19 20 21
20 21 22 23 24 25 26  17 18 19 20 21 22 23  22 23 24 25 26 27 28
27 28 29 30 31        24 25 26 27 28 29 30  29 30 31
```
```
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on
udev              482388         0    482388   0% /dev
tmpfs             100932      5020     95912   5% /run
/dev/sda1       64891708   4512724  57059640   8% /
tmpfs             504644       216    504428   1% /dev/shm
tmpfs               5120         4      5116   1% /run/lock
tmpfs             504644         0    504644   0% /sys/fs/cgroup
Home           244810132 215911872  28898260  89% /media/psf/Home
iCloud         244810132 215911872  28898260  89% /media/psf/iCloud
Photo Library  244810132 215911872  28898260  89% /media/psf/Photo Library
tmpfs             100932        80    100852   1% /run/user/1000
tmpfs             100932         0    100932   0% /run/user/1001

$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            472M     0  472M   0% /dev
tmpfs            99M  5.0M   94M   5% /run
/dev/sda1        62G  4.4G   55G   8% /
tmpfs           493M  216K  493M   1% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           493M     0  493M   0% /sys/fs/cgroup
Home            234G  206G   28G  89% /media/psf/Home
iCloud          234G  206G   28G  89% /media/psf/iCloud
Photo Library   234G  206G   28G  89% /media/psf/Photo Library
tmpfs            99M   80K   99M   1% /run/user/1000
tmpfs            99M     0   99M   0% /run/user/1001
```

```
$ du -h
4.0K	./test/a/b/c/d
8.0K	./test/a/b/c
12K		./test/a/b
16K		./test/a
20K		./test
24K		.
```
```
$ ps
  PID TTY          TIME CMD
 1213 pts/4    00:00:00 bash
 8625 pts/4    00:00:00 ps
 
$ ps au
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      1181  0.4 11.2 431940 113788 tty7    Ssl+ 10:58   0:48 /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root      1200  0.0  0.3  61444  3560 pts/4    S    13:33   0:00 su parallels
paralle+  1213  0.0  0.5  29644  5292 pts/4    S    13:33   0:00 bash
root      1668  0.0  0.1  23008  1532 tty1     Ss+  10:59   0:00 /sbin/agetty --noclear tty1 linux
paralle+  7358  0.0  0.5  29648  5192 pts/6    Ss+  11:12   0:00 -bash
paralle+  9244  0.0  0.3  44432  3164 pts/4    R+   14:15   0:00 ps au
zhangsan 29833  0.0  0.5  29536  5276 pts/4    Ss   13:12   0:00 -bash

$ ps aux
```

```
$ top

top - 14:16:59 up  3:18,  3 users,  load average: 0.07, 0.02, 0.00
Tasks: 200 total,   1 running, 199 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.5 us,  0.8 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1009288 total,   106600 free,   547836 used,   354852 buff/cache
KiB Swap:  1046524 total,   930956 free,   115568 used.   279776 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  784 root      20   0  222840   9744   3780 S   0.3  1.0   0:00.59 snapd
  972 root      20   0   43496     24      0 S   0.3  0.0   0:01.47 prltoolsd
 1181 root      20   0  431940 113788  14056 S   0.3 11.3   0:48.81 Xorg
 2574 paralle+  20   0  427956   6004   5688 S   0.3  0.6   0:18.16 prlcc
 9443 paralle+  20   0   48868   3696   3080 R   0.3  0.4   0:00.04 top
    1 root      20   0  185180   5000   3404 S   0.0  0.5   0:01.87 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd
    4 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H
    
$ q
```

```
$ kill -9 pid
```

#### find
```
.
├── 01.py
├── 123.txt
├── Parallels Shared Folders -> /media/psf
└── test
    └── a
        └── b
            └── c
                └── d

$ find . -name "*1*"
./01.py
./123.txt

$ find -name "*.py"
./01.py

$ find -name "1*"
./123.txt
```

#### ln

```
.
├── 01.py
├── a
│   └── b
│       └── c
└── Parallels Shared Folders -> /media/psf

$ mv 01.py a/b/c/
.
├── a
│   └── b
│       └── c
│           └── 01.py
└── Parallels Shared Folders -> /media/psf

$ ln -s a/b/c/01.py 01_r
lrwxrwxrwx  1 parallels parallels   11 Jan 29 14:32 01_r -> a/b/c/01.py*

$ ln -s /home/parallels/Desktop/a/b/c/01.py 01_d
lrwxrwxrwx  1 parallels parallels   35 Jan 29 14:38 01_d -> /home/parallels/Desktop/a/b/c/01.py*

.
├── 01_d -> /home/parallels/Desktop/a/b/c/01.py
├── 01_r -> a/b/c/01.py
├── a
│   └── b
│       └── c
│           └── 01.py
└── Parallels Shared Folders -> /media/psf

$ mv 01* a/
.
├── a
│   ├── 01_d -> /home/parallels/Desktop/a/b/c/01.py
│   ├── 01_r -> a/b/c/01.py x
│   └── b
│       └── c
│           └── 01.py
└── Parallels Shared Folders -> /media/psf

```

```
.
├── a
│   └── b
│       └── c
│           └── 01.py
└── Parallels Shared Folders -> /media/psf

$ ln /home/parallels/Desktop/a/b/c/01.py  01_hard
-rw-rw-r--  2 parallels parallels    0 Jan 29 14:45 01_hard

$ rm a/b/c/01.py
.
├── 01_hard
├── a
│   └── b
│       └── c
└── Parallels Shared Folders -> /media/psf
-rw-rw-r--  1 parallels parallels    0 Jan 29 14:45 01_hard

```

#### tar

```
.
├── 01.py
├── 02.py
├── 03.py
└── Parallels Shared Folders -> /media/psf

$ tar -cvf py.tar 01.py 02.py 03.py
-rw-rw-r-- 1 parallels parallels 10K Jan 29 15:01 py.tar

$ mkdir tar
$ mv py.tar tar/

.
├── 01.py
├── 02.py
├── 03.py
├── Parallels Shared Folders -> /media/psf
└── tar
    └── py.tar
    
$ tar -xvf py.tar

.
├── 01.py
├── 02.py
├── 03.py
├── Parallels Shared Folders -> /media/psf
└── tar
    ├── 01.py
    ├── 02.py
    ├── 03.py
    └── py.tar
    
$ tar -zcvf py.tar.gz *.py
-rw-rw-r-- 1 parallels parallels  139 Jan 29 15:08 py.tar.gz

$ mv py.tar.gz gz/
.
├── 01.py
├── 02.py
├── 03.py
├── gz
│   └── py.tar.gz
├── Parallels Shared Folders -> /media/psf
└── tar
    ├── 01.py
    ├── 02.py
    ├── 03.py
    └── py.tar

$ tar -zxvf py.tar.gz
.
├── 01.py
├── 02.py
├── 03.py
├── gz
│   ├── 01.py
│   ├── 02.py
│   ├── 03.py
│   └── py.tar.gz
├── Parallels Shared Folders -> /media/psf
└── tar
    ├── 01.py
    ├── 02.py
    ├── 03.py
    └── py.tar
    
$ tar -jcvf py.tar.bz2 *.py
-rw-rw-r-- 1 parallels parallels  150 Jan 29 15:15 py.tar.bz2
$ tar -jxvf py.tar.bz2 -C bz2/

.
├── 01.py
├── 02.py
├── 03.py
├── bz2
│   ├── 01.py
│   ├── 02.py
│   └── 03.py
├── gz
│   ├── 01.py
│   ├── 02.py
│   ├── 03.py
│   └── py.tar.gz
├── Parallels Shared Folders -> /media/psf
├── py.tar.bz2
└── tar
    ├── 01.py
    ├── 02.py
    ├── 03.py
    └── py.tar
```

#### ifconfig

```
$ sudo ifconfig en0 down
$ sudo ifconfig en0 up
```

#### arp

```
$ arp -a

? (172.16.22.1) at 9c:37:f4:83:d5:d6 on en0 ifscope [ethernet]
? (172.16.23.120) at 68:db:ca:e4:7e:1d on en0 ifscope [ethernet]
? (172.16.23.123) at 9c:e3:3f:9a:64:28 on en0 ifscope [ethernet]
? (172.16.23.126) at 34:23:87:0:2f:25 on en0 ifscope [ethernet]
```