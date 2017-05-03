# vim:set ff=unix expandtab ts=4 sw=4:
import unittest
import pathlib
import inspect
import os
import sys
from string import Template
from subprocess import call,check_call,check_output

class InDirTest(unittest.TestCase):
    def __init__(self,args):
        st=inspect.stack()
        self.caller_dir_path=pathlib.Path(os.path.dirname(os.path.abspath(inspect.getfile(st[-1].frame))))
        super().__init__(args)

    def myDirPath():
        return pathlib.Path.cwd()

        
    def tmpDirPath():
        return(__class__.myDirPath().joinpath("tmp"))
        

    def run(self,*args):
        testDirPath=__class__.tmpDirPath().joinpath(self.id())
        testDirName=testDirPath.as_posix()

        self.oldDirName=os.getcwd()
        __class__.rootDir=pathlib.Path(self.oldDirName).parent.parent
        check_output(["rm","-rf",testDirName])
        check_output(["mkdir","-p",testDirName])
        print("testDirName")
        print(testDirName)
        
        os.chdir(testDirName)
        
        try:
            super().run(*args)
        finally:
            os.chdir(self.oldDirName)
