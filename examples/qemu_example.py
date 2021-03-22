#!/usr/bin/env python3

from cohydra import ArgumentParser, Scenario, Network, DockerNode, QEMUNode, SwitchNode

def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0")

    node1 = DockerNode('pong', docker_build_dir='./docker/pong')
    node2 = QEMUNode('lubuntu', password='8559', ip='12.0.5.2', image_path='/home/julian/Master/GIT/hector_iot_testing_framework/VMs/lubuntu.qcow2',
            username='lubuntu', system='qemu-system-x86_64', guest_interface='ens3', mac_address='52:54:00:12:34:56', qemu_options='-m 512 -enable-kvm')
    #node3 = QEMUNode('rasp', password='raspberry', ip='12.0.6.2', image_path='/home/julian/Master/GIT/hector_iot_testing_framework/VMs/raspbian-stretch-lite.qcow',
    #        username='pi', system='qemu-system-arm', guest_interface='eth0', mac_address='52:54:00:12:34:55',
    #        qemu_options='-M versatilepb -kernel /home/julian/Master/GIT/hector_iot_testing_framework/QEMU/kernel-qemu-4.14.79-stretch -append \"root=/dev/sda2 panic=1 rootfstype=ext4 rw\" -dtb /home/julian/Master/GIT/hector_iot_testing_framework/QEMU/versatile-pb.dtb -cpu arm1176 -m 256 -machine versatilepb')
    switch = SwitchNode('switch-1')

    net.connect(node1, switch, delay='40ms')
    net.connect(node2, switch, delay='30ms')
    #net.connect(node3, switch, delay='20ms')
    
    scenario.add_network(net)
    
    with scenario as sim:
        # To simulate forever, just do not specifiy the simulation_time parameter.
        sim.simulate() #simulation_time=180
    

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
