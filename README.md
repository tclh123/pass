# Pass

## Install

```
$ make install
```

Then, `venv/bin/pass` to run,
Or, 

```
$ make make_ln
$ pass
usage: pass [-h] {status,st,platform,pl,account,ac} ...

optional arguments:
  -h, --help            show this help message and exit

  commands:
    {status,st,platform,pl,account,ac}
```

## Usage

### Platform

```
$ pass pl -h
usage: pass pl [-h] [-v] [-n NAME] [-u URL] {add,list,rm}

Alias of platform

positional arguments:
  {add,list,rm}

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         enable additional output
  -n NAME, --name NAME  platform's name
  -u URL, --url URL     platform's url
```

```
$ pass pl list
taobao => http://www.taobao.com/
```

### Account

```
(lh)vagrant@vagrant ~/github/pass $ pass ac -h
usage: pass ac [-h] [-v] [-u UID] [-p PASSWD] [-P PLATFORM] [-n NAME]
               [-e EMAIL] [--phone PHONE]
               {add,list,rm}

Alias of account

positional arguments:
  {add,list,rm}

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         enable additional output
  -u UID, --uid UID     account's uid
  -p PASSWD, --passwd PASSWD
                        account's passwd
  -P PLATFORM, --platform PLATFORM
                        account's platform
  -n NAME, --name NAME  account's name
  -e EMAIL, --email EMAIL
                        account's email
  --phone PHONE         account's phone
```

```
$ pass ac list
逆风(lh@gmail.com), taobao, email: lh@gmail.com, pwd: l*********h
```
