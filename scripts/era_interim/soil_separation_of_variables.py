#!/usr/bin/env python

"""
Auxiliary script for ""soil_separation_of_variables.sh"

The possible choices for the "VARIABLE_NAME" are numbers between 1 and 8, 
which represent the following variables to be separated:

(1): Volumetric soil water layer 1 (0-7 cm) [m**3 m**-3]
(2): Volumetric soil water layer 2 (7-28 cm) [m**3 m**-3]
(3): Volumetric soil water layer 3 (28-100 cm) [m**3 m**-3]
(4): Volumetric soil water layer 4 (100-255 cm) [m**3 m**-3]
(5): Soil temperature level 1 (0-7 cm) [K]
(6): Soil temperature level 2 (7-28 cm) [K]
(7): Soil temperature level 3 (28-100 cm) [K]
(8): Soil temperature level 4 (100-255 cm) [K]
"""

# Load packages.
import sys
import glob
import os
import pygrib

# Input arguments.
FOLDER_INPUT = sys.argv[1]  # Where grouped data live.
FOLDER_OUTPUT = sys.argv[2] # Where the separated date will be located.
CHOICE = sys.argv[3]        # This is a number between 1 and 8, see the list
                            # above.

# Dictionary for the variable choice.                            
var_dict = {"1": "Volumetric soil water layer 1",
            "2": "Volumetric soil water layer 2",
            "3": "Volumetric soil water layer 3",
            "4": "Volumetric soil water layer 4",
            "5": "Soil temperature level 1",
            "6": "Soil temperature level 2",
            "7": "Soil temperature level 3",
            "8": "Soil temperature level 4"}

var_name = var_dict[CHOICE]

# List all files in the "FOLDER_INPUT".
FILES_PATHS = sorted(glob.glob(FOLDER_INPUT + "*grb"))

# List all files names.
FILES_NAMES = [os.path.split(FILE_PATH)[-1] for FILE_PATH in FILES_PATHS]

# Message.
print("\n* Into the folder", FOLDER_OUTPUT + ":")

# Loop over files.
for FILE_PATH, FILE_NAME in zip(FILES_PATHS, FILES_NAMES):

    # Name for the output file.
    YEAR = FILE_NAME[5: 9]
    MONTH = FILE_NAME[10: 12]
    FILE_NAME_OUTPUT = var_name.lower().replace(" ", "_") + "_" + \
                       YEAR + "_" + MONTH + ".grb"

    # Absolute path.                   
    FILE_PATH_OUTPUT = FOLDER_OUTPUT + FILE_NAME_OUTPUT                   

    # Check whether the file exists.
    if os.path.isfile(FILE_PATH_OUTPUT):

        # Message.
        print("    * The file", FILE_NAME_OUTPUT,
              "has already been created ...")
        
    else:
    
        # Message.
        print("    * Creating", FILE_NAME_OUTPUT, "...")

        # Read data.
        grbs = pygrib.open(FILE_PATH)

        # List of all gribs messages.
        GRBS = grbs.select(name=var_name)

        # Loop over gribs messages.
        for GRB in GRBS:
            with open(FILE_PATH_OUTPUT, "ab") as GRBOUT:
                msg = GRB.tostring()
                GRBOUT.write(msg)

        # Close grib file.
        grbs.close()
