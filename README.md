# Dev Cells for Rolls Royce
This is a dynamic web application which will be used to assess engineers and managers progress and ensure they are being supported in their career aspirations.
## Setting up the project (Windows)
1. Create Virtual Environment. Only needs to be done on inital clone of project.
```shell
py -m venv venv
```
2. Set Execution Policy
```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
3. Activate Virtual Environment
```shell
venv\scripts\activate
```
4. Install requirements.
```shell
pip install -r requirements.txt
```
5. Move directory into project area.
```shell
cd dc_source
```

## Setting up the project (MacOs)
1. Create Virtual Environment. Only needs to be done on inital clone of project.
```shell
python3 -m venv venv
```
2. Activate Virtual Environment
```shell
source ./venv/bin/activate
```
3. Install requirements.
```shell
pip install -r requirements.txt
```
4. Move into project area.
```shell
cd dc_source
```
