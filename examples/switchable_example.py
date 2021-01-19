#!/usr/bin/env python3

from cohydra import ArgumentParser, Network, DockerNode, Scenario
from cohydra.node import SwitchableWrapper

def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0", base="0.0.0.2", delay="200ms")
    net.block_ip_address("10.0.0.1")

    node1 = DockerNode('ping', docker_build_dir='./docker/ping')
    node2 = DockerNode('pong', docker_build_dir='./docker/pong')
    switchableNode2 = SwitchableWrapper(node2, '1', "http://raspberrypi.local:8080")
    net.connect(node1, "10.0.0.17")
    net.connect(node2)

    scenario.add_network(net)

    @scenario.workflow
    def toggle_node2(workflow):
        while True: 
            workflow.sleep(5)
            switchableNode2.switch_on()
            workflow.sleep(5)
            switchableNode2.switch_off()

    with scenario as sim:
        # To simulate forever, just do not specifiy the simulation_time parameter.
        sim.simulate(simulation_time=60)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
