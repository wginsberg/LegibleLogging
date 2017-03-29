#!/usr/bin/env python

import sys
import re

ANSI_DEFAULT = '\\033[0m'

# Read config
config_matcher = re.compile(r'^(.*?)(\s*)(\S+)$')
rules = {}
with open('config.txt', 'r') as f:
	for line in f:
		if len(line) < 3:
			continue
		result = config_matcher.match(line)
		if not result:
			continue
		pattern, colour = result.group(1), result.group(3)
		rules["(%s)" % pattern] = colour

# Do subsitution on stdin
for line in sys.stdin:
	subbed = line
	for pattern, colour in rules.iteritems():
		subbed = re.sub(pattern, "%s\\1%s" % (colour, ANSI_DEFAULT), subbed)
	sys.stdout.write(subbed)
