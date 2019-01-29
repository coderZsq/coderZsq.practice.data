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