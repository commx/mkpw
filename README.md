# mkpw
mkpw is a small tool to generate safe passwords.

## Installation
Make sure that you have [Python](https://www.python.org) installed. You'll need at least Python 2.7 to run this tool.

Next, download the [`mkpw.py`](https://github.com/commx/mkpw/raw/master/mkpw.py) [right-click, save link as…] script and install it somewhere on your computer. Make sure to make it executable by setting the appropriate permissions. I'd recommend setting up a shell alias (you could also provide a symlink to the script on any path visible in `PATH`), so you can execute the script directly as `mkpw`.

```
$ curl -o mkpw.py https://github.com/commx/mkpw/raw/master/mkpw.py
$ chmod +x mkpw.py
```

### Creating a shell alias
This shall work on most UNIX-like shells, including bash. The example below is for bash.

```
$ echo 'alias mkpw=/path/to/mkpw.py' >> ~/.bashrc
```

## Features
By default, the script will generate a password with four segments with five characters each.  It includes upper- and lowercase letters, digits and a set of special characters.  Ambigious characters are excluded by default, but can be included by using the --with-ambigious option.

```
usage: mkpw [-h] [-s, --segments SEGMENTS]
            [-l, --segment-length SEGMENT_LENGTH] [--with-ambigious] [-x]
            [--sep SEP] [--version]
            [count]

Make safe passwords.

positional arguments:
  count

optional arguments:
  -h, --help            show this help message and exit
  -s, --segments SEGMENTS
                        number of segments
  -l, --segment-length SEGMENT_LENGTH
                        number of characters in segment
  --with-ambigious      include ambigious characters
  -x                    exclude special characters
  --sep SEP             segment separator string
  --version             show program's version number and exit
```

## Contributions
The tool is released under the Apache License 2.0. Contributions in any forms is highly welcome.
