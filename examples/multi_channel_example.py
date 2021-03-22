#!/usr/bin/env python3

from marvis import ArgumentParser, Network, DockerNode, SwitchNode, Scenario

def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0")

    node1 = DockerNode('ping', docker_build_dir='./docker/ping')
    node2 = SwitchNode('bridge-1')
    node3 = DockerNode('pong', docker_build_dir='./docker/pong')

    channel1 = net.create_channel(delay="200ms")
    channel1.connect(node1)
    channel1.connect(node2)

    channel2 = net.create_channel(delay="200ms")
    channel2.connect(node2)
    channel2.connect(node3)

    scenario.add_network(net)
    with scenario as sim:
        # To simulate forever, just do not specifiy the simulation_time parameter.
        sim.simulate(simulation_time=60)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
