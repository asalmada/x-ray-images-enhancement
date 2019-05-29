# X-Ray Images Enhancement

## Abstract
The main objective of this project is to improve the visualization of fractured bones using three image enhancement algorithms: **contrast limited adaptive histogram equalization** (CLAHE), **unsharping mask** (UM) and  **high-frequency emphasis filtering** (HEF) After implementing these algorithms, we will discuss about the results and the difficulties found during the development of the project.

## Example Image

![alt text](https://www.nsf.gov/news/mmg/media/images/pr05005xray1_f.jpg "Unprocessed image of a chest x-ray film")
##### Courtesy: National Science Foundation

Unprocessed images of x-ray films, like this one of a chest, made by *Nikola Zivaljevic, M.D.* and found at the [National Sciente Foundation Multimedia Gallery](https://www.nsf.gov/news/mmg/mmg_disp.jsp?med_id=52110), will be used in this project.

## Images Source

Besides the first image (001.tif), found at the [National Sciente Foundation Multimedia Gallery](https://www.nsf.gov/news/mmg/mmg_disp.jsp?med_id=52110), all the other images used were founded at the [National Library of Medicine MedPix](https://medpix.nlm.nih.gov/home), a free open source database with over 59,000 indexed and curated images, organized, reviewed, approved, and curated free of charge for personal use and for local teaching at institutions.

## Authors

- André Scheibel de Almada 9292952
- Cho Young Lim 6436060
- Eduardo Garcia Misiuk 9293230

# Dependencies
## Packages
### Python
`apt-get install python3`

### venv
`apt-get install python3-venv`

## Libraries
Setup the repository by following the instructions from [installation](installation) section.  
After activating the environment, install these libraries.

### numpy
`pip install numpy`

### scipy
`pip install scipy`

### imageio
`pip install imageio`

# Installation
Clone the repository with `git clone https://github.com/asalmada/x-ray-images-enhancement`.  
Run `python3 -m venv x-ray-images-enhancement` to install the environment in the repository.

## Environment
To activate, run `source bin/activate` and to deactivate, run `deactivate`.
