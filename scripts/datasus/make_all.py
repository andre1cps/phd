#!/usr/bin/env python
#File: make_all.py
#
# Script intended to read all data from hospitalizations in a given Brazilian State.
# Later you can manipulate this data using "datasus" module.
#
# Example of usage in a linux terminal:
#
# >>> directory="/media/alex/ALEXDATA/data_sets/HEALTH/HOSPITALIZATION/MT/"
# >>> output="/media/alex/ALEXDATA/data_sets/HEALTH/HOSPITALIZATION/MT/DATASUS_MT.csv"
# >>> python make_all.py $directory $output 

# Load system package.
import sys

directory = sys.argv[1] # Where is the data?
output = sys.argv[2]    # Output file path with csv extension.

# My repository.
repository = "/home/alex/Dropbox/repositories/doctoral_thesis/libraries/"

# Include once my repository in the path for searching libraries.
if repository not in sys.path:
    sys.path.append(repository)
    
# Import my libraries.
import datasus.tools as sus

# Read all data. All diseases for all locations in the selected state.
SUS = sus.data_frame(directory)

# Export to a csv file.
SUS.to_csv(output)
