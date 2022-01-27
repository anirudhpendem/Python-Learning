import getopt, sys

argumentList = sys.argv[1:]

options = "hmo:"

long_options = ["Help","My_file","output ="]

try:

	arguments, values = getopt.getopt(argumentList,options,long_options)

	for currentArgument, currentValue in arguments:

		 if currentArgument in ("-h", "--Help"):
		 	print ("Displaying Help")

		 elif currentArgument in ("-m", "--My_file"):
		 	print ("Displaying file_name:", sys.argv[0])

		 elif currentArgument in ("-o", "--Output"):
		 	print (("Enabling special output mode (% s)") % (currentValue))

except getopt.error as err:
	print(str(err))
