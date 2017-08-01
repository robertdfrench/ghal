#!/usr/bin/env python
import tox
import shlex
import sys


class Toxic(object):
    SAFE_COMMANDS = {}

    @classmethod
    def command(cls, func):
        cls.SAFE_COMMANDS[func.func_name] = func
        func.func_globals['sh'] = cls.sh
        return func

    @classmethod
    def sh(cls, command_string):
        cmd = shlex.split(command_string)
        tox.cmdline(cmd)


    @classmethod
    def run_command(cls, name):
        if name not in cls.SAFE_COMMANDS:
            raise Exception("No such command '%s'" % name)
        cls.SAFE_COMMANDS[name]()


    @classmethod
    def display_help(cls):
        for command in cls.SAFE_COMMANDS:
            docs = cls.SAFE_COMMANDS[command].func_doc.lstrip()
            print("%s => %s" % (command, docs))

    @classmethod
    def main(cls):
        if len(sys.argv) < 2:
            cls.display_help()
        else:
            cls.run_command(sys.argv[1])


@Toxic.command
def unit_tests():
    """ Run the inexpensive tests """
    sh("pytest")


@Toxic.command
def pep8_check():
    """ Enforce pep8 """
    sh("flake8")


@Toxic.command
def linter():
    """ Lintify """
    sh("pylint ghal")


if __name__ == "__main__":
    Toxic.main()
