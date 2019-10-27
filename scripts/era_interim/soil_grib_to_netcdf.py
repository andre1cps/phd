#!/usr/bin/env python

"""
This script transforms grib files into netcdf files. It will be create a unique
netcdf file for each grib file.

Example of usage:

(climate36) >>> INPUT_FOLDER=/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/
(climate36) >>> OUTPUT_FOLDER=/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/
(climate36) >>> python soil_grib_to_netcdf.py $INPUT_FOLDER $OUTPUT_FOLDER
"""

# Load packages.
import sys
import os
import glob

import xarray as xr

# Dictionary for the variable choice.                            
var_dict = {"5": "Volumetric soil water layer 1",
            "6": "Volumetric soil water layer 2",
            "7": "Volumetric soil water layer 3",
            "8": "Volumetric soil water layer 4",
            "1": "Soil temperature level 1",
            "2": "Soil temperature level 2",
            "3": "Soil temperature level 3",
            "4": "Soil temperature level 4"}

# Master folder.
INPUT_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]

# List all sub directories.
SUB_FOLDERS = sorted([x[0] for x in os.walk(INPUT_FOLDER)])[1:]

# Loop over sub folders.
for SUB_FOLDER, var_number in zip(SUB_FOLDERS, range(len(SUB_FOLDERS))):

    # For grib reading.
    var_name = var_dict[str(var_number + 1)]

    # Message.
    print("\n* Into the folder", SUB_FOLDER + ":")
    
    # List all grib files.
    IN_FILES_PATHS = sorted(glob.glob(SUB_FOLDER + "/" + "*.grb"))

    # List all files names (with "grb" extension).
    IN_FILES_NAMES = [os.path.split(FILE_PATH)[-1] for FILE_PATH in IN_FILES_PATHS]

    # The same as before (without any extension).
    FILES_NAMES = [os.path.splitext(FILE_NAME)[0] for FILE_NAME in IN_FILES_NAMES]

    # Add netcdf extension.
    OUT_FILES_NAMES = [FILE_NAME + ".nc" for FILE_NAME in FILES_NAMES]

    # Absolute.
    OUT_FILES_PATHS = [SUB_FOLDER + "/" + FILE_NAME for FILE_NAME in OUT_FILES_NAMES]

    #  A dictionary of keyword arguments to pass on to the
    #  backend. This may be useful when backend options would improve
    #  performance or allow user control of dataset processing.

    if "temperature" in SUB_FOLDER:
        backend_kwargs = {"filter_by_keys": {"units": "K"}}
        
    else:
        backend_kwargs = {}
    
    # Loop over input files.
    for IN_FILE_PATH, OUT_FILE_PATH, OUT_FILE_NAME in zip(
            IN_FILES_PATHS, OUT_FILES_PATHS, OUT_FILES_NAMES
    ):

        # Check whether the netcdf file already exists.
        if os.path.isfile(OUT_FILE_PATH):

            # Message.
            print("   * The file", OUT_FILE_NAME,
                  "has already been created ...")

        else:
            # Message.
            print("   * Creating", OUT_FILE_NAME, "...")
                
            # Read grib data.
            DATASET = xr.open_dataset(IN_FILE_PATH,
                                      engine="cfgrib",
                                      backend_kwargs=backend_kwargs)

            # Export netcdf file.
            DATASET.to_netcdf(OUT_FILE_PATH)
