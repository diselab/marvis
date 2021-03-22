#!/usr/bin/env python3

from marvis import ArgumentParser, Network, DockerNode, SwitchNode, Scenario


class Example(object):
    def __init__(self):
        self.some_value = 21


def main():
    scenario = Scenario()

    net = Network("10.0.0.0", "255.255.255.0")

    bridge = SwitchNode('br-1')

    server = DockerNode('server', docker_image='httpd:2.4')
    channel_server = net.create_channel(data_rate="1000Mbps")
    channel_server.connect(server)
    channel_server.connect(bridge)

    client1 = DockerNode('client-1', docker_build_dir='./docker/curl-webserver', cpus=0.5, memory="128m")
    channel_client1 = net.create_channel(delay="50ms", data_rate="100Mbps")
    channel_client1.connect(client1)
    channel_client1.connect(bridge)

    client2 = DockerNode('client-2', docker_build_dir='./docker/curl-webserver', cpus=0.5, memory="128m")
    channel_client2 = net.create_channel(delay="20ms", data_rate="100Mbps")
    channel_client2.connect(client2)
    channel_client2.connect(bridge)

    example = Example()

    @scenario.workflow
    def test(workflow):
        workflow.wait_until(lambda: example.some_value, 6, globals(), locals())
        server.go_offline()
        workflow.sleep(10)
        server.go_online()

    @scenario.workflow
    def test2(workflow):
        workflow.sleep(10)
        client1.execute_command('curl server -v')
        example.some_value = 6

    scenario.add_network(net)
    with scenario as sim:
        # To simulate forever, just do not specifiy the time parameter.
        sim.simulate(simluation_time=60)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.run(main)
