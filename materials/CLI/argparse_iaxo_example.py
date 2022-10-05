import os,sys, time
import stat

delay = 30
repeat = 10

narg = len(sys.argv)
cfgFile = ""
sectionName = ""
jobName = ""
email = ""
logPath = ""
idOffset = 0

duration = "7-00:00:00"

if narg < 2:
    print ""
    print "----------------------------------------------------------------"
    print ""
    print " This program launches restG4 jobs to slurm	    "
    print ""
    print " The usual restG4 command is : restG4 RML_FILE [SECTION_NAME]"
    print ""
    print " Values in brackets [] are optional"
    print ""
    print " Usage : restG4ToSlurm.py -c RML_FILE "
    print ""
    print " - Options : "
    print " ----------- "
    print ""
    print " -n or --sectionName SECTION_NAME :"
    print " Defines the name of the section to be used from RML_FILE"
    print ""
    print " -e or --email MAIL :"
    print " It allows to specify the e-mail for batch system job notifications"
    print ""
    print " -i or --initialRun VALUE :"
    print " An integer number to introduce the first run number."
    print ""
    print " -r or --repeat REPEAT_VALUE :"
    print " This option defines the number of simulations we will launch (default is 10)"
    print ""
    print " -d or --delay DELAY_TIME :"
    print " Time delay between launching 2 reapeated jobs (default is 30 seconds)"
    print " Random seed is connected to the time stamp."
    print ""
    print " -j or --jobName JOB_NAME :"
    print " JOB_NAME defines the name of scripts and output files stored under slurmJobs/"
    print ""
    print " -o or --onlyScripts :"
    print " It will just generate the slurm scripts without launching to the queue"
    print ""
    print "----------------------------------------------------------------"
    print ""
    sys.exit(1)

onlyScripts=0

for x in range(narg-1):
    if ( sys.argv[x+1] == "--repeat" or sys.argv[x+1] == "-r" ):
        repeat = int(sys.argv[x+2])

    if ( sys.argv[x+1] == "--cfgFile" or sys.argv[x+1] == "-c" ):
        cfgFile = sys.argv[x+2]

    if ( sys.argv[x+1] == "--logPath" or sys.argv[x+1] == "-l" ):
        logPath = sys.argv[x+2]

    if ( sys.argv[x+1] == "--idOffset" or sys.argv[x+1] == "-i" ):
        idOffset = int(sys.argv[x+2])

    if ( sys.argv[x+1] == "--delay" or sys.argv[x+1] == "-d" ):
        delay = int( sys.argv[x+2] )

    if ( sys.argv[x+1] == "--sectionName" or sys.argv[x+1] == "-n" ):
        sectionName = sys.argv[x+2]

    if ( sys.argv[x+1] == "--jobName" or sys.argv[x+1] == "-j" ):
        jobName = sys.argv[x+2]

    if ( sys.argv[x+1] == "--email" or sys.argv[x+1] == "-e" ):
        email = sys.argv[x+2]

    if ( sys.argv[x+1] == "--onlyScripts" or sys.argv[x+1] == "-o" ):
        onlyScripts = 1

if cfgFile == "":
    print  ( "RML file was not provided. Use -c file.rml" )
    sys.exit(1)
