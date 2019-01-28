#### SSH

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