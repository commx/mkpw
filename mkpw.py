#!/usr/bin/env python

"""
mkpw is a small tool to generate safe passwords.

By default, three passwords are generated that match the following criterias:
  1. The password must include lowercase letters
  2. The password must include uppercase letters
  3. The password must include digits
  4. The password must include at least one special character
  5. The password must be at least 16 characters long

You can override this default by providing configuration files, or the command line arguments.

Copyright 2016 Christian Kröger <commx@commx.ws>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import sys

from argparse import ArgumentParser
from string import ascii_lowercase, ascii_uppercase, digits

try:
    from secrets import choice as rand_choice
except ImportError:
    from random import choice as rand_choice

try:
    from configparser import ConfigParser, NoOptionError, NoSectionError
except ImportError:
    from ConfigParser import ConfigParser, NoOptionError, NoSectionError


# ambigious characters
ambigious_chars = '01OIl|B8G6S5Z2'

# special characters to be used for generating passwords
special_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

# configuration file paths, in that order
config_file_paths = [
    '/etc/mkpw.cfg',
    '/usr/local/etc/mkpw.cfg',
    os.path.expanduser('~/.mkpw.cfg')
]

config_defaults = {
    'count': 3,
    'length': 16,
    'exclude': None,
    'ambigious': False,
    'lowercase': True,
    'uppercase': True,
    'digits': True,
    'special': True,
    'choices': None
}


def main():
    config = ConfigParser()
    section = 'default'

    if 'MKPW_CONFIG_FILE' in os.environ:
        name = os.environ['MKPW_CONFIG_FILE']
        if ':' in name:
            name, section = name.split(':')[:2]

        config_file_paths.append(name)

    # read files
    config.read(config_file_paths)

    # override the command line arguments
    for key in ('count', 'length', 'exclude', 'ambigious', 'lowercase', 'uppercase', 'digits', 'special', 'choices'):
        if key in ('count', 'length'):
            meth = config.getint
        elif key in ('ambigious', 'lowercase', 'uppercase', 'digits', 'special'):
            meth = config.getboolean
        else:
            meth = config.get

        try:
            config_defaults[key] = meth(section, key)
        except ValueError:
            return sys.exit('Error: Value of %r in section %r of configuration file is invalid.' % (key, section))
        except (NoOptionError, NoSectionError):
            pass

    parser = ArgumentParser(description='Make safe passwords.')
    parser.add_argument('count', type=int, default=config_defaults['count'], nargs='?',
                        help='number of passwords to make')
    parser.add_argument('-l, --length', type=int, default=config_defaults['length'], dest='length',
                        help='length of desired passwords')
    parser.add_argument('--exclude', dest='exclude', action='store', default=config_defaults['exclude'],
                        help='exclude given characters from choices')
    parser.add_argument('--exclude-ambigious', dest='ambigious', action='store_false',
                        default=config_defaults['ambigious'], help='exclude lowercase letters')
    parser.add_argument('--exclude-lowercase', dest='lowercase', action='store_false',
                        default=config_defaults['lowercase'], help='exclude lowercase letters')
    parser.add_argument('--exclude-uppercase', dest='uppercase', action='store_false',
                        default=config_defaults['uppercase'], help='exclude uppercase letters')
    parser.add_argument('--exclude-digits', dest='digits', action='store_false', default=config_defaults['digits'],
                        help='exclude digits')
    parser.add_argument('--exclude-special', dest='special', action='store_false', default=config_defaults['special'],
                        help='exclude special characters')
    parser.add_argument('--choices', dest='choices', action='store', default=config_defaults['choices'],
                        help='use the given characters instead of the character classes')

    args = parser.parse_args()

    for _ in range(args.count):
        while True:
            s = make_password(args)

            # ensure that the password includes characters of any class
            if not args.choices:
                if args.lowercase and not any(x.islower() for x in s):
                    continue
                if args.uppercase and not any(x.isupper() for x in s):
                    continue
                if args.digits and not any(x.isdigit() for x in s):
                    continue
                if args.special and not any(x in special_chars for x in s):
                    continue

            break

        print(s)


def make_password(args):
    """
    Create a password.

    :param args: ArgumentParser args
    :return: password string
    """
    if not args.choices and not args.lowercase and not args.uppercase and not args.digits and not args.special:
        return sys.exit('Error: All possible character classes have been excluded and no choices have been specified.')
    elif args.choices:
        choices = ''.join(set(args.choices))
    else:
        choices = ''

        if args.lowercase:
            choices += ascii_lowercase
        if args.uppercase:
            choices += ascii_uppercase
        if args.digits:
            choices += digits
        if args.special:
            choices += special_chars

    if not args.ambigious:
        choices = ''.join(x for x in choices if x not in ambigious_chars)
    if args.exclude:
        choices = ''.join(x for x in choices if x not in args.exclude)
    if not choices:
        return sys.exit('Error: All possible choices were excluded.')

    return ''.join(rand_choice(choices) for _ in range(args.length))


if __name__ == '__main__':
    main()