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