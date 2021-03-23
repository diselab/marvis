# marvis

[![Github Actions CI](https://github.com/diselab/marvis/actions/workflows/main.yml/badge.svg)](https://github.com/diselab/marvis/actions/workflows/main.yml)


## Installation

### Installation Using Docker

Marvis can be obtained via docker.
The easiest solution is using the VSCode *Remote - Containers* extension.
After cloning the repository and opening it in the container, your scenarios will by executing them with `python3`.

Otherwise, you can build the [Dockerfile](./Dockerfile) in the project's root directory yourself by running `make`. In the container, marvis will be added to your
`PYTHONPATH`. But you need to make sure, that you run the container with privileges to access the host network in order to have access to the host's network interfaces. You of course need to modify the volume mount to allow marvis access to your scenarios.

```sh
docker run -it --rm --cap-add=ALL -v /var/run/docker.sock:/var/run/docker.sock --net host --pid host --userns host --privileged ghcr.io/diselab/marvis:latest
```

The main image [`ghcr.io/diselab/marvis`](./docker/Dockerfile) is based on the images in the [docker](./docker) directory.
The [`ghcr.io/diselab/marvis:base`](./docker/marvis-base/Dockerfile) image installs all neccessary dependencies for marvis,
[`ghcr.io/diselab/marvis:dev`](./docker/marvis-dev/Dockerfile) is for development purposes (docker-cli in the container).

### Installation Without Using Docker

In the case you do not want to use the prebuilt Docker, a normal ns-3
installation with *NetAnim* Python bindings will work, too. Marvis has
so far been tested with **Debian 10 Buster**, **Ubuntu 18.04 Bionic
Beaver** and **Ubuntu 20.04 Focal Fossa**.

The following instructions describe how to install marvis system-wide.
If you want to install marvis for your user only (`pip3 install --user
…`), in a virtualenv, or in a pipenv, feel free to do so. However, we
won't cover instructions in how to get the
`PYTHONPATH`/virtualenv/pipenv together with privilege escalation (sudo)
working.

First, make sure you have the required packages to build dependencies
installed:

```shell script
apt install \
  build-essential \
  cargo \
  git \
  libssl-dev \
  python3-dev \
  python3-pip \
  python3-setuptools \
  python3-wheel \
  rustc
```

The recommended Python version is Python 3.7. Python 3.8 is right now not supported (if you are running Ubuntu 20.04, make sure to install Python 3.7). 
Also, make sure you have pip3 version 20 or up
(if not, try `pip3 install --upgrade pip`).

#### User Installation

If you do not plan to modify the source code of marvis yourself,
marvis can be installed with the following command:

```shell script
# without ns-3
pip3 install git+https://github.com/diselab/marvis.git

# including ns-3
pip3 install 'git+https://github.com/diselab/marvis.git#egg=cohydra[ns-3]'
```

The second of the commands above, will use our
[Python Wheels repository](https://github.com/osmhpi/python-wheels)
for easier installation of binary dependencies, such as ns-3.

To run an example testcase, download this repository, go to the example folder and run:
```shell script
python3 basic_example.py
```

#### Developer Installation

If you do plan to modify the source code of marvis, clone this
repository and to install dependencies, run, e.g.:

```shell script
# without ns-3
pip3 install -e .

# including ns-3
pip3 install -e '.[ns-3]'

# including dev tools, if you want to contribute <3
pip3 install -e '.[dev]'

# including ns-3 and dev tools
pip3 install -e '.[ns-3,dev]'
```

In this case, where you do not install marvis itself but just its
dependencies, the code of marvis needs to be in your `PYTHONPATH`.
E.g.:

```shell script
export PYTHONPATH=$PYTHONPATH:$PWD/path/to/marvis-repo
```


## Contribution

We are always happy when somebody contributes to marvis.
Therefore please create a fork and create a pull request to our repository.
Make sure, that [`pylint`](https://www.pylint.org/) does not show any additional errors or warnings.
Also make sure that your code and your pull request is well documented.
The documentation should also contain how to test your feature, if it is more complex.
Afterwards we are going to test your new feature and review the code.


## Contributors

 - Malte Andersch
 - Felix Gohla
 - Martin Michaelis
 - Benedikt Schenkel
 - and the [diselab-Team](https://diselab.berlin)
