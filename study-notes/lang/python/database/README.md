#### mysql

```
$ mysql -uroot -p
```

```
$ exit/quit/ctrl+d
```

```
mysql> select version();
+-----------+
| version() |
+-----------+
| 5.6.42    |
+-----------+
1 row in set (0.00 sec)
```

```
mysql>  select now();

mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2019-02-19 17:35:28 |
+---------------------+
1 row in set (0.00 sec)
```

```
mysql>  show databases;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.19 sec)
```

```
mysql> create database coderzsq;
Query OK, 1 row affected (0.00 sec)
```

```
mysql> show create database coderzsq;
+----------+---------------------------------------------------------------------+
| Database | Create Database                                                     |
+----------+---------------------------------------------------------------------+
| coderzsq | CREATE DATABASE `coderzsq` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+----------+---------------------------------------------------------------------+
1 row in set (0.00 sec)
```

```
mysql> create database coderzsq_new charset=utf8;
mysql> show create database coderzsq_new;
+--------------+-----------------------------------------------------------------------+
| Database     | Create Database                                                       |
+--------------+-----------------------------------------------------------------------+
| coderzsq_new | CREATE DATABASE `coderzsq_new` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+--------------+-----------------------------------------------------------------------+
1 row in set (0.00 sec)

```

```
mysql> drop database coderzsq;
Query OK, 0 rows affected (0.03 sec)
```