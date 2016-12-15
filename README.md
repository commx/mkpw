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
By default, the script will generate three passwords with a length of 16 and print them to screen. The passwords contain lowercase and uppercase letters, digits and special characters by default and exclude ambigious characters (those who may confuse you like 0 and O). You can alter this behaviour by using the command line arguments.

For greater flexibility, you can use configuration files to personalise your preferred way of creating passwords. This will ease the need of specifying the command line arguments all the time, and you can still provide them if you wish. Command line arguments always have a higher precedence than configuration file options.

### Configuration files
The configuration files are simply INI-styled text files which define a section and some options that control the behaviour of mkpw. Not all options must be present, but can.

mkpw will find and read configurations in the following order:

1. `/etc/mkpw.cfg`
2. `/usr/local/etc/mkpw.cfg`
3. `$HOME/.mkpw.cfg`

If you want to specify a custom configuration file name, use the `MKPW_CONFIG_FILE` environment variable to achieve that. It also allows you to specify a custom section by exporting the filename and section, both separated by colon (e.g. `myfile.cfg:custom_section`).

#### Example configuration file

```ini
; This is a example configuration file for mkpw.

[default]
count = 3
length = 10
ambigious = no

[custom_section]
count = 10
length = 3
special = no
ambigious = yes
```

Execute mkpw with example.cfg and the custom section:

```
$ MKPW_CONFIG_FILE=example.cfg:custom_section mkpw
```

## Contributions
The tool is released under the Apache License 2.0. Contributions in any forms is highly welcome.
