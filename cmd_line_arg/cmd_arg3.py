import argparse
"""msg = "THESE IS USING ArgumentParser"
parser = argparse.ArgumentParser(description = msg)
parser.parse_args()
"""

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--Output", help = "Show Output")
args = parser.parse_args()

if args.Output:
	print("Displaying Output as: % s" % args.Output)
