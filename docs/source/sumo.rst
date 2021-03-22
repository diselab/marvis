***********************
Using SUMO With marvis
***********************

For simulating the movement of wireless network participants, marvis provides a connection to
the `SUMO <https://sumo.dlr.de/>`_ simulator.

There are two ways to use SUMO with marvis. In either way, marvis uses the `TraCI <https://sumo.dlr.de/docs/TraCI.html>`_
Python library to connect to the SUMO instance, running as server.

Variant 1: Install SUMO On Simulation Host
##########################################

You can install SUMO directly onto the simulation host. On Debian-based machines, this can be achievd by executing: ::

    sudo apt-get install sumo sumo-tools sumo-docs

**Important:** marvis relies on the TraCI Python library.
If you use marvis *without Docker*, you need to ensure that marvis can find the library.
Set the ``SUMO_HOME`` environment variable accordingly: ::

    $ export SUMO_HOME="/usr/share/sumo"

Run SUMO In Remote Mode
=======================

After that you can start the simulation and load your configuration files.
You have to provide a port for TraCI: ::

    $ sumo-gui --remote-port 8813 -c /path/to/configuration

Run SUMO In Local Mode
======================

**Prerequesite:** This assumes that **you are not using marvis in Docker**! From within the marvis-container, you cannot start SUMO automatically on the host.
To install marvis locally, please see :ref:`Local Installation Without Docker`.

Marvis can start the SUMO simulation for you. You can just pass a ``config_path`` to the initializer of the :class:`.SUMOMobilityInput`.
The testbed will use a version of SUMO **without GUI** because there is no way to start the SUMO simulation automatically from marvis with the GUI-version.


Variant 2: Using Docker
#######################

SUMO can also be used with Docker.
We provide Docker images at the `osmhpi/sumo repository <https://hub.docker.com/r/osmhpi/sumo>`_ that can be used.
After pulling the image, the simulation can be started with a new container.
Make sure to properly setup your *volume mounts*.

::

    $ docker run -it --rm \
        --net host \
        --pid host \
        --userns host \
        --privileged \
        --cap-add=ALL \
        --env="DISPLAY" \
        -v "/etc/group:/etc/group:ro" \
        -v "/etc/passwd:/etc/passwd:ro" \
        -v "/etc/shadow:/etc/shadow:ro" \
        -v "/etc/sudoers.d:/etc/sudoers.d:ro" \
        -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        --user=$(id -u) \
        -w /workspace \
        -v /path/to/configuration-folder:/workspace \
        osmhpi/sumo:latest \
        bash

Now you can proceed like in the local installation by entering the command to start SUMO in the container:
::

    sumo-gui --remote-port 8813 -c /workspace/path/to/scenario.sumocfg


Writing a SUMO Scenario With marvis
####################################

After installing and starting SUMO, the simulation be configured to use SUMO with the :class:`.SUMOMobilityInput` class.
Please configure the port and host accordingly.
Furthermore, nodes have to be mapped to SUMO IDs in order to be moved by the co-simulation.

Connect To A SUMO Remote Mode Instance
======================================

This example explains how to use marvis with a SUMO server.

*Note:* If you are using marvis with Docker, you can access a SUMO Remote Mode Instance running on the Docker host with `localhost`.
The container must be in the same network namespace, though. Please have a look at :ref:`Installation With Docker`.

.. code-block:: python

    from marvis.mobility_input import SUMOMobilityInput
    #...
    # Scenario creation
    #...
    port = 8813 # TraCI is listening on 8813.
    sumo = SUMOMobilityInput(name='Some title', sumo_host='hostname-or-ip', sumo_port=port)
    sumo.add_node_to_mapping(car, 'car0', obj_type='vehicle')
    scenario.add_mobility_input(sumo)
    #...
    # Simulation run
    #...

Connect To A SUMO Local Mode Instance
=====================================

This example shows how to start SUMO with marvis locally.

.. code-block:: python

    from marvis.mobility_input import SUMOMobilityInput
    #...
    # Scenario creation
    #...
    config = '/absolute/path/to/sumocfg.cfg'
    sumo = SUMOMobilityInput(name='Some title', config_path=config)
    sumo.add_node_to_mapping(car, 'car0', obj_type='vehicle')
    scenario.add_mobility_input(sumo)
    #...
    # Simulation run
    #...
