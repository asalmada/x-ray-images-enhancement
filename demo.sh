#!/bin/bash

source bin/activate

echo "Running HEF for image images/004.jpg..."
python app.py -a hef -i images/004.jpg
echo "Done!"

echo "Running UM for image images/043.jpg..."
python app.py -a um -i images/043.jpg
echo "Done!"

echo "Running CLAHE for image images/001.tif..."
python app.py -a clahe -i images/001.tif < test_cases/clahe/40_4_1.in
echo "Done!"

deactivate
