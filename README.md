# Data analysis
- Document here the project: Hack4Nature
- Description: Project Description
- Data Source:
- Type of analysis:
- Important links: https://developers.google.com/maps/documentation/urls/get-started#map-action
- conserning the google map api: the price of 1 kilo request is 1,6... dollar, the maximum size of a request map is explained in this text:
*" Image sizes
The size parameter, in conjunction with center, defines the coverage area of a map. It also defines the output size of the map in pixels, when multiplied with the scale value (which is 1 by default).

This table shows the maximum allowable values for the size parameter at each scale value.

scale=1|	scale=2

640x640|	640x640 (returns 1280x1280 pixels)
"

reference: https://developers.google.com/maps/documentation/maps-static/start#Imagesizes
price is taken from the google cloud account




#
superficies de marseille: 240.6 KM²


Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for Hack4Nature in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/Hack4Nature`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "Hack4Nature"
git remote add origin git@github.com:{group}/Hack4Nature.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
Hack4Nature-run
```

# Install

Go to `https://github.com/{group}/Hack4Nature` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/Hack4Nature.git
cd Hack4Nature
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
Hack4Nature-run
```
