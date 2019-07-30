## Find inspiration in practice

### magnet
> Practice building a server-end & data-end through python.

#### Get Started

- Step 1. you need a **Python3** environment.
- Step 2. you need a **pip3** environment.
- Step 3. you need to create **virtualenvs**.
- Step 4. **pip install** following libs.

```
(magnet) [root@izuf69ibpdra8ui5a6edjtz magnet]# pipenv graph
cfscrape==2.0.7
  - requests [required: >=2.0.0, installed: 2.22.0]
    - certifi [required: >=2017.4.17, installed: 2019.6.16]
    - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
    - idna [required: >=2.5,<2.9, installed: 2.8]
    - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.3]
Flask==1.1.1
  - click [required: >=5.1, installed: 7.0]
  - itsdangerous [required: >=0.24, installed: 1.1.0]
  - Jinja2 [required: >=2.10.1, installed: 2.10.1]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - Werkzeug [required: >=0.15, installed: 0.15.4]
gunicorn==19.9.0
lxml==4.3.4
selenium==3.141.0
  - urllib3 [required: Any, installed: 1.25.3]
```

- Step 5. run the **following command** to launch server.

```
$ . run.sh
```

#### Content
- **Douban**: web crawler from **douban.com**.
- **Thunder**: web crawler from **22tu.cc**.
- **Beiwo**: web crawler from **beiwo888.com**.
- **Piaohua**: web crawler from **piaohua.com**.
- **Baidu**: web crawler from **baidu.com**.