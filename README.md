# marvis

[![master](https://api.travis-ci.com/diselab/marvis.svg?branch=master)](https://travis-ci.com/diselab/marvis)

## Contributors

 - Malte Andersch
 - Arne Boockmeyer
 - Felix Gohla
 - Martin Michaelis
 - Benedikt Schenkel
 - Robert Schmid

## Installation

### Installation With Docker

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

### Installation Without Docker

Recommended python version: Python 3.7

In the case you do not want to use the prebuilt docker, a normal ns-3 installation with *NetAnim* Python bindings will work, too.
To easily install these have a look at our [python wheels repository](https://github.com/osmhpi/python-wheels).

You also need the following packages:
```shell script
sudo pip3 install pyroute2 nsenter docker paramiko
sudo pip3 install git+https://github.com/active-expressions/active-expressions-static-python
```

The Python libraries / directory provided by ns-3 and all other packages has to be in your `PYTHONPATH`, though.
To run an example testcase, go to the example folder and run:
```shell script
python3 basic_example.py
```

Marvis so far has only been tested with **Debian 10 Buster** and **Ubuntu 18.04 Bionic Beaver**.

## Contribution

We are always happy when somebody contributes to marvis.
Therefore please create a fork and create a pull request to our repository.
Make sure, that [`pylint`](https://www.pylint.org/) does not show any additional errors or warnings.
Also make sure that your code and your pull request is well documented.
The documentation should also contain how to test your feature, if it is more complex.
Afterwards we are going to test your new feature and review the code.
