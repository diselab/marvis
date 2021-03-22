Installation
============

Running marvis requires some dependencies. We therefore recommend using the Docker images provided below.

Installation With Docker
************************

Marvis can be obtained via docker.
The easiest solution is using the VSCode *Remote - Containers* extension.
After cloning the repository and opening it in the container, your scenarios will by executing them with :code:`python3`.

Otherwise, you can build the [Dockerfile](./Dockerfile) in the project's root directory yourself by running :code:`make`.
In the container, marvis will be added to your :code:`PYTHONPATH`.
But you need to make sure, that you run the container with privileges to access the host network in order to have access to the host's network interfaces.
The Docker socket is mounted into the container to enable creating new containers from within the simulation.
You of course need to modify the volume mount to allow marvis access to your scenarios:

::
    $ docker run -it --rm --cap-add=ALL \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /var/lib/lxd:/var/lib/lxd \
        -v /var/snap/lxd/common/lxd:/var/snap/lxd/common/lxd \
        --net host \
        --pid host \
        --userns host \
        --privileged \
        ghcr.io/diselab/marvis:latest

The main image is based on the images in the :src:`docker <docker>` directory.
The :src:`marvis-base <docker/marvis-base/Dockerfile>` installs all neccessary dependencies for marvis,
:src:`marvis-dev <docker/marvis-dev/Dockerfile>` is for development purposes (docker-cli in the container).

Local Installation Without Docker
*********************************

In the case you do not want to use the prebuilt docker, a normal ns-3 installation with *NetAnim* Python bindings will work, too.
The Python libraries / directory provided by ns-3 has to be in your :code:`PYTHONPATH`, though.
Marvis so far has only been tested with **Debian 10 Buster**, **Ubuntu 18.04 Bionic Beaver** and **ns-3.33**.

There is no installation via :code:`pip`.
