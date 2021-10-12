# Simple CLI Image Processing
## Index
 * [Getting Started](#getting-started)

## Getting Started
1. Create Virtual Environment
```shell
python3 -m venv *virtual_environment_name*
```
2. Activate the virtual environment
```shell
. *virtual_environment_name*/bin/activate
```
3. Install the depedencies
```shell
pip install -r requirements.txt
```
4. Run the application by selecting one of the available command
* ```python3 main.py and <image> <image>```
* ```python3 main.py bright <image> -c <int>```
* ```python3 main.py div <image> -c <int>```
* ```python3 main.py vflip <image>```
* ```python3 main.py hflip <image>```
* ```python3 main.py or <image> <image>```
* ```python3 main.py rgb2grayscale <image>```
* ```python3 main.py subc <image> -c <int>```
* ```python3 main.py sub <image> <image>```
* ```python3 main.py sumc <image> -c <int>```
* ```python3 main.py sum <image> <image>```
* ```python3 main.py translation <image> -x <int> -y <int>```
* ```python3 main.py xor <image> <image>```
* ```python3 main.py zoomout <image> -x <int> -y <int>```
* ```python3 main.py zoomin <image> -x <int> -y <int>```
* ```python3 main.py negative <image>```
* ```python3 main.py multi <image> <image>```
* ```python3 main.py multic <image> -c <int>```
* ```python3 main.py rotation <image> -r <int>```

### Notes
| cmd      | purpose                        | example    |
|----------|--------------------------------|------------|
| \<image> | image location                 | ./test.png |
| -c       | a number needed to run the cmd | -c 10      |
| -x       | the magnitude of x translation | -x 5       |
| -y       | the magnitude of x translation | -y 10      |
| -r       | the magnitude of degree        | -r 90      |