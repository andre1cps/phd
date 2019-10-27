#!/bin/bash
# Script intended to read all files of soil variables of ERA-INTERIM and create
# separated files for each variable.

# Original folder with data.
INPUT_FOLDER="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/all_together/"

# Where data will be copied.
OUTPUT_FOLDER1="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/volumetric_soil_water_1/"
OUTPUT_FOLDER2="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/volumetric_soil_water_2/"
OUTPUT_FOLDER3="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/volumetric_soil_water_3/"
OUTPUT_FOLDER4="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/volumetric_soil_water_4/"
OUTPUT_FOLDER5="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/soil_temperature_level_1/"
OUTPUT_FOLDER6="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/soil_temperature_level_2/"
OUTPUT_FOLDER7="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/soil_temperature_level_3/"
OUTPUT_FOLDER8="/media/alex/ALEXDATA/data_sets/ERA_INTERIM/soil/soil_temperature_level_4/"

# Run auxiliary script.
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER1 1 
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER2 2
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER3 3
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER4 4
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER5 5
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER6 6
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER7 7
python soil_separation_of_variables.py $INPUT_FOLDER $OUTPUT_FOLDER8 8 
