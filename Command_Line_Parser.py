# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:47:18 2016

@author: Natalia Tucholska
"""
from optparse import OptionParser

parser = OptionParser(conflict_handler="resolve")
parser.set_conflict_handler("resolve")

args = ["-f", "foo.txt"]
options,args = parser.parse_args()
print('stuff is {}'.format(options))
parser.add_option("-f", "--file", action = "store", dest = "verbose", type = "string", help = "write report to File")
print(parser.parse_args(args))
parser.add_option("-n", type = "int", dest = "num")
args2 = ["-n", "10"]
print(parser.parse_args(args2))
parser.add_option("--cat", dest = "verbose", action = "store", type = "string", help = "displays parsed output from File")
args3 = ["--cat", "foo.txt"]
print(parser.parse_args(args3))
parser.add_option("--sort", dest = "verbose", action = "store", type = "string", help = "takes in File and outputs lines in sorted alphabetical order")
args6 = ["--sort", "-o", "foo.txt"]
print(parser.parse_args(args6))
parser.add_option("--sort", "-r", "-o", dest = "verbose", action = "store", type = "string", help = "writes the line sorted contents to an outfile")
args7 = ["--sort", "-r", "-o", "foo.txt"]
print(parser.parse_args(args7))