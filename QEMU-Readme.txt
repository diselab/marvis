# cohydra

[![master](https://api.travis-ci.com/osmhpi/cohydra.svg?branch=master)](https://travis-ci.com/osmhpi/cohydra)

## Contributors

 - Malte Andersch
 - Arne Boockmeyer
 - Felix Gohla
 - Martin Michaelis
 - Benedikt Schenkel

## Installation

### Installation With Docker

Cohydra can be obtained via docker.
The easiest solution is using the VSCode *Remote - Containers* extension.
After cloning the repository and opening it in the container, your scenarios will by executing them with `python3.7`.

Otherwise, you can build the [Dockerfile](./Dockerfile) in the project's root directory yourself by running `make`. In the container, cohydra will be added to your
`PYTHONPATH`. But you need to make sure, that you run the container with privileges to access the host network in order to have access to the host's network interfaces. You of course need to modify the volume mount to allow cohydra access to your scenarios.

```sh
docker run -it --rm --cap-add=ALL -v /var/run/docker.sock:/var/run/docker.sock --net host --pid host --userns host --privileged osmhpi/cohydra:latest
```

The main image is based on the images in the [docker](./docker) directory.
The [`cohydra-base`](./docker/cohydra-base/Dockerfile) installs all neccessary dependencies for cohydra,
[`cohydra-dev`](./docker/cohydra-dev/Dockerfile) is for development purposes (docker-cli in the container).

### Installation Without Docker

In the case you do not want to use the prebuilt docker, a normal ns-3 installation with *NetAnim* Python bindings will work, too.
The Python libraries / directory provided by ns-3 has to be in your `PYTHONPATH`, though.
Cohydra so far has only been tested with **Debian 10 Buster** and **Ubuntu 18.04 Bionic Beaver**.

There is no installation via `pip`.


## Marvis Docu:

### Installation
+ Python3.7
    + sudo apt install python3.7-dev
    + sudo apt install -y python3-pip

+ NS-3
    + Download ns-3 python wheel from: https://github.com/osmhpi/python-wheels/releases
        + wget https://github.com/osmhpi/python-wheels/releases/download/2020-04-07-15-51-05/ns-3.30-cp37-cp37m-linux_x86_64.whl

+ Docker
    + sudo apt install docker.io

+ no tty present and no askpass program specified
    + /etc/sudoers, where username=your_username
    + Add `username ALL=(ALL) NOPASSWD: ALL`

## QEMU information

### QEMU installation
+ `sudo apt-get install qemu-system-x86 ` for x86 emulations or
+ `sudo apt-get install qemu-system` for other Systems

### qcow2 file creation
+ Download a Linux image and create a qcow2 file
    + `qemu-img create -f qcow2 xxx.qcow2`
+ Start the empty qcow2 file and install the downloaded OS (qemu-system must fit the selected OS ex. arm, x86, ...)
    + `qemu-system-x86_64 -boot d -cdrom image.iso -m 512 -hda xxx.qcow2`

### Example QEMU starting arguments for testing
+ Raspberry Pi image
    + `qemu-system-arm -M versatilepb -kernel pathTo/kernel-qemu-4.14.79-stretch -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" -hda pathTo/raspbian-stretch-lite.qcow -dtb pathTo/QEMU/versatile-pb.dtb -cpu arm1176 -m 256 -no-reboot -machine versatilepb -net nic -net user,hostfwd=tcp::2222-:22,hostfwd=tcp::22280-:80`
+ Lubuntu image (kvm needs root)
    + `sudo qemu-system-x86_64 -hda pathTo/lubuntu.qcow2 -m 512 -enable-kvm -no-reboot -net nic -serial mon:stdio -net user,hostfwd=tcp::2222-:22,hostfwd=tcp::22280-:80`

### Preparations for usage (setup on QEMU image)
+ SSH
    + Possible package: `openssh-client`
    +  If it won't start on system boot, a crontab can be used
        + `sudo crontab -e`
        + Add `@reboot service ssh restart`
    + Copy ssh key from Host to VM
        + ex. `ssh-copy-id -p 2222 -i pathTo/id_rsa lubuntu@127.0.0.1`
+ For the integration in Cohydra
    + Add an IP address and IP route (host side is taken care by Cohydra)
        + ex. `sudo crontab -e`
        + Add `@reboot sudo ip addr add 12.0.1.2 dev eth0`, where the IP and eth0 device may be changed
        + Add `@reboot sudo ip link set eth0 up`
        + Add `@reboot sudo ip route add 12.0.1.0/24 dev eth0 protocol kernel src 12.0.1.2`
    + Try deactivating `GRUB` or set the timeout to a low value to reduce booting time

