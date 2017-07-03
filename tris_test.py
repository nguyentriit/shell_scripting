#!/usr/bin/env python

import subprocess

def tris_shownetwork():
	subprocess.call("cat /etc/sysconfig/network-scripts/ifcfg-eth0",shell=True)


def singing():
	for i in range(5):
		print "La la la"
def math():
	sum = 1+1
	print "%s"%sum

def diskusage():
	du = subprocess.call(["df","-h"])
	print "%s"%du

def main():
	tris_shownetwork()
	singing()
	math()	
	diskusage()

#main()



if __name__ == "__main__":
	main()	





Lahawk just added this line
