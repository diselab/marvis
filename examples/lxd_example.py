#!/usr/bin/env python3

from marvis import ArgumentParser, Network, DockerNode, LXDNode, Scenario


def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0")

    node1 = DockerNode('ping', docker_build_dir='./docker/ping')
    node2 = LXDNode('pong', image='alpine/3.10')
    channel = net.create_channel(delay="200ms")
    channel.connect(node1)
    channel.connect(node2)

    scenario.add_network(net)

    with scenario as sim:
        # To simulate forever, just do not specifiy the simluation_time parameter.
        sim.simulate()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
