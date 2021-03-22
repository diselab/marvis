Search.setIndex({docnames:["api","api/marvis.argparse","api/marvis.channel","api/marvis.channel.channel","api/marvis.channel.csma","api/marvis.channel.wifi","api/marvis.command_executor","api/marvis.command_executor.base","api/marvis.command_executor.console","api/marvis.command_executor.docker","api/marvis.command_executor.local","api/marvis.command_executor.lxd","api/marvis.command_executor.ssh","api/marvis.command_executor.util","api/marvis.context","api/marvis.events","api/marvis.events.Event","api/marvis.interface","api/marvis.network","api/marvis.node","api/marvis.node.base","api/marvis.node.docker","api/marvis.node.external","api/marvis.node.interface","api/marvis.node.lxd","api/marvis.node.qemu","api/marvis.node.ssh","api/marvis.node.switch","api/marvis.scenario","api/marvis.simulation","api/marvis.util","api/marvis.visualization","api/marvis.visualization.netanimvisualization","api/marvis.visualization.visualization","api/marvis.workflow","getting-started","index","installation","sumo"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.index":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["api.rst","api/marvis.argparse.rst","api/marvis.channel.rst","api/marvis.channel.channel.rst","api/marvis.channel.csma.rst","api/marvis.channel.wifi.rst","api/marvis.command_executor.rst","api/marvis.command_executor.base.rst","api/marvis.command_executor.console.rst","api/marvis.command_executor.docker.rst","api/marvis.command_executor.local.rst","api/marvis.command_executor.lxd.rst","api/marvis.command_executor.ssh.rst","api/marvis.command_executor.util.rst","api/marvis.context.rst","api/marvis.events.rst","api/marvis.events.Event.rst","api/marvis.interface.rst","api/marvis.network.rst","api/marvis.node.rst","api/marvis.node.base.rst","api/marvis.node.docker.rst","api/marvis.node.external.rst","api/marvis.node.interface.rst","api/marvis.node.lxd.rst","api/marvis.node.qemu.rst","api/marvis.node.ssh.rst","api/marvis.node.switch.rst","api/marvis.scenario.rst","api/marvis.simulation.rst","api/marvis.util.rst","api/marvis.visualization.rst","api/marvis.visualization.netanimvisualization.rst","api/marvis.visualization.visualization.rst","api/marvis.workflow.rst","getting-started.rst","index.rst","installation.rst","sumo.rst"],objects:{"":{marvis:[0,0,0,"-"]},"marvis.argparse":{ArgumentParser:[1,1,1,""]},"marvis.argparse.ArgumentParser":{add_argument:[1,2,1,""],add_argument_group:[1,2,1,""],add_mutually_exclusive_group:[1,2,1,""],add_subparsers:[1,2,1,""],convert_arg_line_to_args:[1,2,1,""],error:[1,2,1,""],exit:[1,2,1,""],format_help:[1,2,1,""],format_usage:[1,2,1,""],format_version:[1,2,1,""],get_default:[1,2,1,""],parse_args:[1,2,1,""],parse_known_args:[1,2,1,""],print_help:[1,2,1,""],print_usage:[1,2,1,""],print_version:[1,2,1,""],register:[1,2,1,""],run:[1,2,1,""],set_defaults:[1,2,1,""]},"marvis.channel":{channel:[3,0,0,"-"],csma:[4,0,0,"-"],wifi:[5,0,0,"-"]},"marvis.channel.channel":{Channel:[3,1,1,""]},"marvis.channel.channel.Channel":{interfaces:[3,3,1,""],network:[3,3,1,""],nodes:[3,2,1,""],ns3_nodes_container:[3,3,1,""],prepare:[3,2,1,""]},"marvis.channel.csma":{CSMAChannel:[4,1,1,""]},"marvis.channel.csma.CSMAChannel":{csma_helper:[4,3,1,""],delay:[4,3,1,""],devices_container:[4,3,1,""],nodes:[4,2,1,""],prepare:[4,2,1,""],speed:[4,3,1,""]},"marvis.channel.wifi":{WiFiChannel:[5,1,1,""]},"marvis.channel.wifi.WiFiChannel":{WiFiDataRate:[5,1,1,""],WiFiStandard:[5,1,1,""],antennas:[5,3,1,""],channel:[5,3,1,""],channel_width:[5,3,1,""],data_rate:[5,3,1,""],devices_container:[5,3,1,""],frequency:[5,3,1,""],nodes:[5,2,1,""],prepare:[5,2,1,""],standard:[5,3,1,""],tx_power:[5,3,1,""],wifi:[5,3,1,""],wifi_mac_helper:[5,3,1,""]},"marvis.channel.wifi.WiFiChannel.WiFiDataRate":{DSSS_RATE_11Mbps:[5,3,1,""],DSSS_RATE_1Mbps:[5,3,1,""],DSSS_RATE_2Mbps:[5,3,1,""],DSSS_RATE_5_5Mbps:[5,3,1,""],ERP_OFDM_RATE_12Mbps:[5,3,1,""],ERP_OFDM_RATE_18Mbps:[5,3,1,""],ERP_OFDM_RATE_24Mbps:[5,3,1,""],ERP_OFDM_RATE_36Mbps:[5,3,1,""],ERP_OFDM_RATE_48Mbps:[5,3,1,""],ERP_OFDM_RATE_54Mbps:[5,3,1,""],ERP_OFDM_RATE_6Mbps:[5,3,1,""],ERP_OFDM_RATE_9Mbps:[5,3,1,""],OFDM_RATE_12Mbps:[5,3,1,""],OFDM_RATE_18Mbps:[5,3,1,""],OFDM_RATE_24Mbps:[5,3,1,""],OFDM_RATE_36Mbps:[5,3,1,""],OFDM_RATE_48Mbps:[5,3,1,""],OFDM_RATE_54Mbps:[5,3,1,""],OFDM_RATE_6Mbps:[5,3,1,""],OFDM_RATE_9Mbps:[5,3,1,""],OFDM_RATE_BW_12Mbps:[5,3,1,""],OFDM_RATE_BW_18Mbps:[5,3,1,""],OFDM_RATE_BW_24Mbps:[5,3,1,""],OFDM_RATE_BW_27Mbps:[5,3,1,""],OFDM_RATE_BW_3Mbps:[5,3,1,""],OFDM_RATE_BW_4_5Mbps:[5,3,1,""],OFDM_RATE_BW_6Mbps:[5,3,1,""],OFDM_RATE_BW_9Mbps:[5,3,1,""]},"marvis.channel.wifi.WiFiChannel.WiFiStandard":{WIFI_802_11a:[5,3,1,""],WIFI_802_11ac:[5,3,1,""],WIFI_802_11ax:[5,3,1,""],WIFI_802_11b:[5,3,1,""],WIFI_802_11g:[5,3,1,""],WIFI_802_11n:[5,3,1,""],WIFI_802_11n_5G:[5,3,1,""],WIFI_802_11p:[5,3,1,""]},"marvis.command_executor":{base:[7,0,0,"-"],console:[8,0,0,"-"],docker:[9,0,0,"-"],local:[10,0,0,"-"],lxd:[11,0,0,"-"],ssh:[12,0,0,"-"],util:[13,0,0,"-"]},"marvis.command_executor.base":{CommandExecutor:[7,1,1,""],ExitCode:[7,4,1,""]},"marvis.command_executor.base.CommandExecutor":{counter:[7,3,1,""],execute:[7,2,1,""],get_logger:[7,2,1,""],name:[7,3,1,""]},"marvis.command_executor.base.ExitCode":{args:[7,3,1,""],with_traceback:[7,2,1,""]},"marvis.command_executor.console":{ConsoleCommandExecutor:[8,1,1,""]},"marvis.command_executor.console.ConsoleCommandExecutor":{execute:[8,2,1,""],get_logger:[8,2,1,""]},"marvis.command_executor.docker":{DockerCommandExecutor:[9,1,1,""]},"marvis.command_executor.docker.DockerCommandExecutor":{container:[9,3,1,""],execute:[9,2,1,""],get_logger:[9,2,1,""]},"marvis.command_executor.local":{LocalCommandExecutor:[10,1,1,""],log_file:[10,5,1,""]},"marvis.command_executor.local.LocalCommandExecutor":{execute:[10,2,1,""],get_logger:[10,2,1,""]},"marvis.command_executor.lxd":{LXDCommandExecutor:[11,1,1,""],create_handler:[11,5,1,""]},"marvis.command_executor.lxd.LXDCommandExecutor":{container:[11,3,1,""],execute:[11,2,1,""],get_logger:[11,2,1,""]},"marvis.command_executor.ssh":{SSHCommandExecutor:[12,1,1,""],log_file:[12,5,1,""]},"marvis.command_executor.ssh.SSHCommandExecutor":{client:[12,3,1,""],execute:[12,2,1,""],get_logger:[12,2,1,""],sudo:[12,3,1,""]},"marvis.command_executor.util":{LogFile:[13,1,1,""],apply_user_and_shell:[13,5,1,""],split_shell_arguments:[13,5,1,""],stringify_shell_arguments:[13,5,1,""]},"marvis.command_executor.util.LogFile":{log:[13,2,1,""]},"marvis.context":{Context:[14,1,1,""],DeferredItem:[14,1,1,""],NoContext:[14,1,1,""],SimpleContext:[14,1,1,""],ThreadLocalStack:[14,1,1,""],defer:[14,5,1,""]},"marvis.context.Context":{add_error:[14,2,1,""],cancel:[14,2,1,""],cleanup:[14,2,1,""],current:[14,2,1,""],defer:[14,2,1,""],fails:[14,3,1,""]},"marvis.context.DeferredItem":{args:[14,3,1,""],cancel:[14,2,1,""],cleanup:[14,2,1,""],ctx:[14,3,1,""],func:[14,3,1,""],kwargs:[14,3,1,""],name:[14,3,1,""]},"marvis.context.NoContext":{add_error:[14,2,1,""],cancel:[14,2,1,""],cleanup:[14,2,1,""],current:[14,2,1,""],defer:[14,2,1,""]},"marvis.context.SimpleContext":{add_error:[14,2,1,""],cancel:[14,2,1,""],cleanup:[14,2,1,""],current:[14,2,1,""],defer:[14,2,1,""]},"marvis.context.ThreadLocalStack":{pop:[14,2,1,""],push:[14,2,1,""],stack:[14,2,1,""],top:[14,2,1,""]},"marvis.events":{Event:[16,0,0,"-"],e:[15,5,1,""],event:[15,5,1,""],execute_events_on_simulation_end:[15,5,1,""]},"marvis.events.Event":{Event:[16,1,1,""],EventPart:[16,1,1,""],e:[16,5,1,""],event:[16,5,1,""],event_worker:[16,5,1,""],execute_events_on_simulation_end:[16,5,1,""]},"marvis.events.Event.Event":{after:[16,2,1,""],check_if:[16,2,1,""],execute:[16,2,1,""],s:[16,2,1,""],start:[16,2,1,""],start_on_simulation_end:[16,2,1,""],start_on_simulation_start:[16,2,1,""],when:[16,2,1,""]},"marvis.interface":{Interface:[17,1,1,""]},"marvis.interface.Interface":{address:[17,3,1,""],bridge_name:[17,2,1,""],connect_tap_to_bridge:[17,2,1,""],disconnect_tap_from_bridge:[17,2,1,""],ifname:[17,3,1,""],mac_address:[17,3,1,""],node:[17,3,1,""],ns3_device:[17,3,1,""],number:[17,3,1,""],pcap_file_name:[17,2,1,""],remove_bridge:[17,2,1,""],setup_bridge:[17,2,1,""],setup_qemu_host_address:[17,2,1,""],setup_veth_container_end:[17,2,1,""],setup_veth_pair:[17,2,1,""],tap_name:[17,2,1,""],veth_name:[17,2,1,""]},"marvis.network":{Network:[18,1,1,""],network_address_helper:[18,5,1,""]},"marvis.network.Network":{address_helper:[18,3,1,""],channels:[18,3,1,""],color:[18,3,1,""],connect:[18,2,1,""],network:[18,3,1,""],prepare:[18,2,1,""]},"marvis.node":{"interface":[23,0,0,"-"],"switch":[27,0,0,"-"],base:[20,0,0,"-"],docker:[21,0,0,"-"],external:[22,0,0,"-"],lxd:[24,0,0,"-"],qemu:[25,0,0,"-"],ssh:[26,0,0,"-"]},"marvis.node.base":{Node:[20,1,1,""]},"marvis.node.base.Node":{add_interface:[20,2,1,""],channels:[20,3,1,""],color:[20,3,1,""],command_executor:[20,3,1,""],execute_command:[20,2,1,""],get_custom_mac:[20,2,1,""],go_offline:[20,2,1,""],go_online:[20,2,1,""],interfaces:[20,3,1,""],name:[20,3,1,""],ns3_node:[20,3,1,""],position:[20,3,1,""],prepare:[20,2,1,""],set_position:[20,2,1,""],wants_ip_stack:[20,2,1,""]},"marvis.node.docker":{DockerNode:[21,1,1,""],expand_volume_shorthand:[21,5,1,""],log_to_file:[21,5,1,""]},"marvis.node.docker.DockerNode":{add_interface:[21,2,1,""],build_docker_image:[21,2,1,""],command:[21,3,1,""],command_executor:[21,3,1,""],container:[21,3,1,""],container_pid:[21,3,1,""],cpus:[21,3,1,""],docker_build_dir:[21,3,1,""],docker_image:[21,3,1,""],docker_image_tag:[21,2,1,""],dockerfile:[21,3,1,""],environment_variables:[21,3,1,""],execute_command:[21,2,1,""],exposed_ports:[21,3,1,""],get_custom_mac:[21,2,1,""],go_offline:[21,2,1,""],go_online:[21,2,1,""],memory:[21,3,1,""],prepare:[21,2,1,""],pull:[21,3,1,""],set_position:[21,2,1,""],setup_host_interfaces:[21,2,1,""],start_docker_container:[21,2,1,""],stop_docker_container:[21,2,1,""],volumes:[21,3,1,""],wants_ip_stack:[21,2,1,""]},"marvis.node.external":{ExternalNode:[22,1,1,""]},"marvis.node.external.ExternalNode":{add_interface:[22,2,1,""],bridge:[22,3,1,""],command_executor:[22,3,1,""],execute_command:[22,2,1,""],get_custom_mac:[22,2,1,""],go_offline:[22,2,1,""],go_online:[22,2,1,""],ifname:[22,3,1,""],prepare:[22,2,1,""],remove_remote_address:[22,2,1,""],set_position:[22,2,1,""],setup_remote_address:[22,2,1,""],wants_ip_stack:[22,2,1,""]},"marvis.node.interface":{InterfaceNode:[23,1,1,""]},"marvis.node.interface.InterfaceNode":{add_interface:[23,2,1,""],command_executor:[23,3,1,""],execute_command:[23,2,1,""],get_custom_mac:[23,2,1,""],go_offline:[23,2,1,""],go_online:[23,2,1,""],ifname:[23,3,1,""],prepare:[23,2,1,""],set_position:[23,2,1,""],wants_ip_stack:[23,2,1,""]},"marvis.node.lxd":{LXDNode:[24,1,1,""],log_to_file:[24,5,1,""]},"marvis.node.lxd.LXDNode":{add_interface:[24,2,1,""],command_executor:[24,3,1,""],container:[24,3,1,""],create_container:[24,2,1,""],custom_configuration:[24,3,1,""],delete_container:[24,2,1,""],execute_command:[24,2,1,""],get_custom_mac:[24,2,1,""],go_offline:[24,2,1,""],go_online:[24,2,1,""],image:[24,3,1,""],image_server:[24,3,1,""],prepare:[24,2,1,""],set_position:[24,2,1,""],setup_host_interfaces:[24,2,1,""],start_container:[24,2,1,""],wants_ip_stack:[24,2,1,""]},"marvis.node.qemu":{QEMUNode:[25,1,1,""]},"marvis.node.qemu.QEMUNode":{add_interface:[25,2,1,""],command_executor:[25,3,1,""],copy_qemu_image:[25,2,1,""],execute_command:[25,2,1,""],get_custom_mac:[25,2,1,""],get_pid:[25,2,1,""],go_offline:[25,2,1,""],go_online:[25,2,1,""],guest_interface:[25,3,1,""],image_path:[25,3,1,""],ip:[25,3,1,""],local_command_executor:[25,3,1,""],mac_address:[25,3,1,""],password:[25,3,1,""],prepare:[25,2,1,""],proc_id:[25,3,1,""],qemu_options:[25,3,1,""],remove_remote_address:[25,2,1,""],set_position:[25,2,1,""],setup_host_interfaces:[25,2,1,""],setup_remote_address:[25,2,1,""],start_qemu:[25,2,1,""],stop_qemu_vm:[25,2,1,""],system:[25,3,1,""],username:[25,3,1,""],wait_for_connection:[25,2,1,""],wants_ip_stack:[25,2,1,""]},"marvis.node.ssh":{SSHNode:[26,1,1,""],default_ip:[26,5,1,""]},"marvis.node.ssh.SSHNode":{add_interface:[26,2,1,""],execute_command:[26,2,1,""],get_custom_mac:[26,2,1,""],go_offline:[26,2,1,""],go_online:[26,2,1,""],prepare:[26,2,1,""],remove_remote_address:[26,2,1,""],set_position:[26,2,1,""],setup_remote_address:[26,2,1,""],wants_ip_stack:[26,2,1,""]},"marvis.node.switch":{SwitchNode:[27,1,1,""]},"marvis.node.switch.SwitchNode":{add_interface:[27,2,1,""],bridge_device:[27,3,1,""],execute_command:[27,2,1,""],get_custom_mac:[27,2,1,""],go_offline:[27,2,1,""],go_online:[27,2,1,""],prepare:[27,2,1,""],set_position:[27,2,1,""],wants_ip_stack:[27,2,1,""]},"marvis.scenario":{Scenario:[28,1,1,""]},"marvis.scenario.Scenario":{add_mobility_input:[28,2,1,""],add_network:[28,2,1,""],channels:[28,2,1,""],context:[28,3,1,""],networks:[28,3,1,""],nodes:[28,2,1,""],set_visualization:[28,2,1,""],simulation:[28,3,1,""],visualization:[28,3,1,""],workflow:[28,2,1,""],workflows:[28,3,1,""]},"marvis.simulation":{Simulation:[29,1,1,""]},"marvis.simulation.Simulation":{docker_client:[29,3,1,""],hosts:[29,3,1,""],log_directory:[29,3,1,""],prepare:[29,2,1,""],scenario:[29,3,1,""],simulate:[29,2,1,""],started:[29,3,1,""],workflows:[29,3,1,""]},"marvis.util":{network_color_for:[30,5,1,""],once:[30,5,1,""],unique:[30,5,1,""],unique_generator:[30,5,1,""]},"marvis.visualization":{netanimvisualization:[32,0,0,"-"],visualization:[33,0,0,"-"]},"marvis.visualization.netanimvisualization":{NetAnimVisualization:[32,1,1,""]},"marvis.visualization.netanimvisualization.NetAnimVisualization":{animation_interface:[32,3,1,""],get_visualization:[32,2,1,""],prepare_node:[32,2,1,""],set_node_position:[32,2,1,""],set_node_size:[32,2,1,""],set_output_directory:[32,2,1,""],set_visualization:[32,2,1,""]},"marvis.visualization.visualization":{NoVisualization:[33,1,1,""],Visualization:[33,1,1,""]},"marvis.visualization.visualization.NoVisualization":{get_visualization:[33,2,1,""],prepare_node:[33,2,1,""],set_node_position:[33,2,1,""],set_node_size:[33,2,1,""],set_output_directory:[33,2,1,""],set_visualization:[33,2,1,""]},"marvis.visualization.visualization.Visualization":{get_visualization:[33,2,1,""],node_size:[33,3,1,""],output_directory:[33,3,1,""],prepare_node:[33,2,1,""],set_node_position:[33,2,1,""],set_node_size:[33,2,1,""],set_output_directory:[33,2,1,""],set_visualization:[33,2,1,""]},"marvis.workflow":{Workflow:[34,1,1,""]},"marvis.workflow.Workflow":{current_waiting_events:[34,3,1,""],sleep:[34,2,1,""],start:[34,2,1,""],stop:[34,2,1,""],stop_event:[34,3,1,""],task:[34,3,1,""],wait_until:[34,2,1,""],wait_until_true:[34,2,1,""]},marvis:{"interface":[17,0,0,"-"],argparse:[1,0,0,"-"],channel:[2,0,0,"-"],command_executor:[6,0,0,"-"],context:[14,0,0,"-"],events:[15,0,0,"-"],network:[18,0,0,"-"],node:[19,0,0,"-"],scenario:[28,0,0,"-"],simulation:[29,0,0,"-"],util:[30,0,0,"-"],visualization:[31,0,0,"-"],workflow:[34,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","exception","Python exception"],"5":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:exception","5":"py:function"},terms:{"0ms":4,"100mbp":4,"128m":21,"4ghz":5,"5ghz":5,"64kbp":4,"abstract":[1,3,7,20,33],"case":37,"catch":[10,29],"class":[1,3,4,5,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,28,29,32,33,34,38],"default":[1,23,26,32,33],"enum":5,"export":38,"float":[5,20,21,22,23,24,25,26,27,29,32,33,34],"function":[1,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,30,34],"import":[32,33,38],"int":[5,7,18,30],"new":[28,32,33,37,38],"null":[8,14,33],"return":[1,3,4,5,7,14,17,20,21,22,23,24,25,26,27,28,30,32,33],"static":[14,32,33,34],"super":33,"true":[1,20,21,22,23,24,25,26,27,34],"var":37,But:37,For:[3,4,25,38],IDs:38,Not:[20,21,22,23,24,25,26,27],The:[1,3,4,5,7,8,9,10,11,12,13,14,17,18,20,21,22,23,24,25,26,27,28,29,30,32,33,34,37,38],There:[33,37,38],These:[18,34],Use:[3,5,29],Using:36,VMs:25,With:36,__traceback__:7,abc:[32,33],abort:29,absolut:[21,25,38],access:[25,37,38],accordingli:38,achievd:38,activ:34,add:[14,20,21,22,23,24,25,26,27,28,37,38],add_argu:1,add_argument_group:1,add_error:14,add_help:1,add_interfac:[17,20,21,22,23,24,25,26,27],add_mobility_input:[28,38],add_mutually_exclusive_group:1,add_network:28,add_node_to_map:38,add_subpars:1,added:37,adding:17,addit:[24,25],address:[17,18,21,22,24,25,26],address_help:18,after:[16,37,38],afterward:[1,25],afunct:14,againt:34,alia:24,all:[3,4,5,18,20,21,22,23,24,25,26,27,28,29,33,34,37,38],allow:[21,25,34,37],alphanumer:[21,23,25],alread:22,alreadi:[18,25],also:[17,18,22,26,29,38],alwai:21,amount:21,ani:[14,17],anim:32,animation_interfac:32,anoth:[5,14],anotherfunct:14,antenna:5,api:36,append:[7,8,9,10,11,12,20,21,22,23,24,25,26,27],apply_user_and_shel:13,apt:38,arg:[1,7,14,25,27],arg_lin:1,argument:[1,14,18,25],argument_default:1,argumentpars:1,arm:25,arn:34,assign:[14,17,18,21,22,25,26],assum:38,automat:[25,38],avail:[5,30],awai:[1,7],back:[20,21,22,23,24,25,26,27],band:5,base:[1,3,4,5,8,9,10,11,12,13,14,16,17,18,21,22,23,24,25,26,27,28,29,30,32,33,34,37,38],bash:[7,8,9,10,11,12,38],beaver:37,becaus:38,been:37,befor:[22,24],behaviour:19,behind:23,being:[24,29,34],belong:[3,14,28],below:37,best:5,between:[5,18,27],bind:37,bionic:37,bitrat:5,block:34,blue:30,blueprint:28,boockmey:34,bool:[1,12,20,21,22,23,24,25,26,27],bridg:[17,21,22,23,24,25,26],bridge_devic:27,bridge_nam:17,build:[18,21,37],build_docker_imag:21,buster:37,cabl:[3,4,18],calcul:[26,30],call:[1,14,18,20,21,22,23,24,25,26,27,33,34],callabl:[1,14,28,34],can:[5,6,7,14,17,18,21,25,28,29,36,37,38],cancel:14,cannel:20,cannot:38,cap:[37,38],capabl:3,car0:38,car:38,card:[3,17,20],care:29,cfg:38,channel:[17,18,20,21,22,23,24,25,26,27,28],channel_typ:18,channel_width:5,charact:[21,23,25],check:[24,29],check_if:16,choos:5,cleanup:14,cli:37,client:[12,29],clone:37,code:[7,32],cohydra:25,collid:5,collis:[3,4],color:[18,20,30],com:34,combin:6,come:34,command:[6,7,8,9,10,11,12,13,16,20,21,22,23,24,25,26,27,34,38],command_executor:[20,21,22,23,24,25],commandexecutor:[6,7,8,9,10,11,12],common:37,commun:[17,25],compar:[18,34],compon:19,comput:[20,21],condit:[16,34],conect:18,config:38,config_path:38,configur:[18,21,24,28,38],configureloc:17,conflict_handl:1,connect:[2,3,4,5,12,17,18,20,21,22,23,24,25,26,27,36],connect_tap_to_bridg:17,consid:[5,22],consist:[21,23,25],consolecommandexecutor:8,constraint:17,contain:[3,7,9,11,14,17,18,21,24,32,34,36,37,38],container_pid:21,content:36,context:[21,28],conthost:17,continu:29,control:17,convert_arg_line_to_arg:1,copi:25,copy_qemu_imag:25,copy_vm:25,correct:5,correctli:17,could:[5,18],counter:7,cours:[5,37],cpu:21,creat:[5,23,24,25,28,32,34,37],create_contain:24,create_handl:11,creation:[18,38],creator:[21,24],csma:[3,18],csma_help:4,csmachannel:[4,18],ctrl:29,ctx:14,current:[14,25,28,32,33],current_waiting_ev:34,custom:[24,25],custom_configur:24,dasylab:34,data:5,data_r:5,dbm:5,debian:[37,38],debug:[1,8],decor:34,def:34,default_ip:26,defer:14,deferreditem:14,defin:[1,31],delai:4,delet:[17,24,25],delete_contain:24,depend:[5,37],describ:29,descript:[1,14],dest:1,destroi:17,detail:32,determin:29,dev:37,develop:37,devic:[4,5,17,22,23,25,26,27],devices_contain:[4,5],diagramm:[1,3,4,5,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,28,29,32,33,34],dict:[14,17,21,24],dictionari:[21,24],dictonari:21,directli:38,directori:[21,24,29,32,33,37],disconnect:[17,20,21,22,23,24,25,26,27],disconnect_tap_from_bridg:17,diselab:37,displai:[33,38],do_another_th:34,do_someth:34,doc:38,docker:[18,24,29,36],docker_build_dir:21,docker_cli:29,docker_fil:21,docker_imag:21,docker_image_tag:21,dockercommandexecutor:9,dockerfil:[21,37],dockernod:[17,21],doe:[14,33],domain:[3,4],don:18,done:34,down:14,dry:8,dsss_rate_11mbp:5,dsss_rate_1mbp:5,dsss_rate_2mbp:5,dsss_rate_5_5mbp:5,dsssrate11mbp:5,dsssrate1mbp:5,dsssrate2mbp:5,dsssrate5_5mbp:5,durat:34,dure:[6,21,22,26,34],each:[21,33],easi:23,easiest:37,either:[1,17,38],enabl:[25,37],enforc:21,ensur:38,enter:[25,38],entri:21,env:38,environ:[21,38],environment_vari:21,epilog:1,equal:[25,34],equival:[3,4,17],erp_ofdm_rate_12mbp:5,erp_ofdm_rate_18mbp:5,erp_ofdm_rate_24mbp:5,erp_ofdm_rate_36mbp:5,erp_ofdm_rate_48mbp:5,erp_ofdm_rate_54mbp:5,erp_ofdm_rate_6mbp:5,erp_ofdm_rate_9mbp:5,erpofdmrate12mbp:5,erpofdmrate18mbp:5,erpofdmrate24mbp:5,erpofdmrate36mbp:5,erpofdmrate48mbp:5,erpofdmrate54mbp:5,erpofdmrate6mbp:5,erpofdmrate9mbp:5,err:14,error:[1,14],etc:38,eth0:[22,23,26],eth:[20,21,22,23,24,25,26],ethernet:4,evalu:34,event:34,event_work:16,eventpart:16,everi:[16,34],exampl:[1,17,18,21,25,28,29,34,38],except:[1,7,14],execpt:10,execut:[7,8,9,10,11,12,14,16,20,21,22,23,24,25,26,27,28,29,34,37,38],execute_command:[20,21,22,23,24,25,26,27],execute_events_on_simulation_end:[15,16],executor:[7,8,9,10,11,12,20,21,22,23,24,25],exist:[22,25],exit:[1,7],exitcod:7,expand:21,expand_volume_shorthand:21,expected_result:34,explain:38,expos:21,exposed_port:21,express:[16,34],extens:37,extern:[17,23,25,26,36],externalnod:[22,26],fail:14,fals:[12,13,21,24],far:37,fault:[34,36],featur:[20,21,22,23,24,25,26,27],fetch:24,file:[1,7,8,9,10,11,12,17,21,24,25,29,32,38],find:38,first:5,flag:1,folder:38,follow:[28,32],form:21,format:[25,32],format_help:1,format_usag:1,format_vers:1,formatter_class:1,found:[5,24],frequenc:5,from:[5,20,21,22,23,24,25,26,27,32,33,37,38],fromfile_prefix_char:1,func:[14,28,30],further:[5,34],furthermor:38,gener:[18,25],get:[28,33,36,38],get_custom_mac:[20,21,22,23,24,25,26,27],get_default:1,get_logg:[7,8,9,10,11,12],get_pid:25,get_visu:[32,33],ghcr:37,github:34,give:[32,33],given:[18,25,26],global:34,global_var:16,global_vari:34,go_offlin:[20,21,22,23,24,25,26,27],go_onlin:[20,21,22,23,24,25,26,27],goe:10,green:30,grep:25,group:38,guest:[17,25],guest_interfac:25,gui:38,hand:32,handl:[20,21,22,23,24,25,26,27],hardwar:[22,36],has:[20,21,31,37],have:[17,37,38],help:13,helper:[4,5,18],helpformatt:1,here:[5,17],host:[10,12,17,21,22,24,25,26,29,36,37],hostnam:[21,24,38],how:38,http:[5,24,34],hue:30,hybrid:36,identifi:17,ieee_802:5,ifnam:[17,22,23,26],ignor:[5,33],imag:[21,24,25,37,38],image_path:25,image_serv:24,implement:[14,25],includ:[22,23],incomplet:5,incorpor:1,index:[18,30,36],indic:[12,20,21,22,23,24,25,26,27,29,34],influxdb:29,info:[1,25,34],inform:5,inherit:[1,3,4,5,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,28,29,32,33,34],initi:[29,38],inject:[34,36],insert:18,insid:[21,23],instal:[20,21,22,23,24,25,26,27,36],instanc:[18,21,24,25,30],instanti:[3,17],instead:29,instruct:34,intent:14,interfac:[3,20,21,22,24,25,26,27,31,32,37],interfacenod:23,intern:[3,13,17,20,21,27,30],ipv4:18,ipv6:18,item:[14,21],iter:[29,30],its:36,just:[8,38],kei:[21,24],key_valu:21,keyword:[14,18],kind:[8,22,28],kwarg:[1,14,18,27],label:[21,24],lambda_expr:16,lan:[3,4],later:[14,17],latest:[37,38],layer:5,level:[1,10,11,12,13],lib:37,librari:[37,38],like:[14,34,38],line:13,link:3,linuxcontain:24,list:[3,4,5,14,18,20,21,22,23,24,25,26,27,28,34],listen:38,load:38,local:[23,24,25,34,36],local_command_executor:25,local_var:16,local_vari:34,localcommandexecutor:10,localhost:38,log:[1,3,4,5,7,8,9,10,11,12,13,14,17,21,24,29],log_directori:[21,24,29],log_fil:[10,12],log_path:[21,24],log_to_fil:[21,24],logfil:[10,12,13],logger:[1,7,8,9,10,11,12,13,25],logger_arg:1,login:26,look:38,lxc:24,lxd:37,lxdcommandexecutor:11,lxdnode:24,mac:[5,17,25],mac_address:[17,25],machin:[17,23,25,38],mai:17,main:[1,19,25,37],make:[5,37,38],manag:[17,25],mani:18,manipul:36,manual:[18,20,21,22,23,24,25,26,27,29,34],map:[21,29,38],marvi:37,mask:18,maximum:5,mbit:5,mean:21,memmori:21,memori:21,messag:1,method:30,mhz:5,mobility_input:[28,38],mobilityinput:28,mobitl:[20,21,22,23,24,25,26,27],mode:17,model:[9,11,20,21,22,23,24,25,26,27],modifi:[29,37],modul:36,monitor:29,more:[5,18,25],mount:[37,38],move:38,movement:38,multipl:31,must:[18,21,23,25,38],name:[1,7,8,9,10,11,12,14,17,20,21,22,23,24,25,26,27,38],namespac:[1,17,38],neccesari:[20,27],neccessari:[18,37],necessari:18,need:[14,17,18,22,34,37,38],net:[37,38],netanim:[32,37],netmask:18,network:[0,3,4,5,17,20,21,22,23,24,25,26,27,28,29,30,36,37,38],network_address:18,network_address_help:18,network_color_for:30,network_index:18,new_node_s:[32,33],new_output_directori:[32,33],nic:23,nocontext:[14,33],node:[2,3,4,5,7,17,18,28,29,32,33,38],node_s:33,none:[1,3,4,5,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,26,27,28,29,32,33,34],normal:37,note:38,noth:[14,33],novisu:33,now:38,ns3:22,ns3_devic:17,ns3_node:20,ns3_nodes_contain:3,number:[5,14,17,20,21,22,23,24,25,26,27,30],number_of_network:30,obj_typ:38,object:[1,3,7,8,13,14,16,17,18,20,28,29,32,33,34],obtain:37,ofdm_rate_12mbp:5,ofdm_rate_18mbp:5,ofdm_rate_24mbp:5,ofdm_rate_36mbp:5,ofdm_rate_48mbp:5,ofdm_rate_54mbp:5,ofdm_rate_6mbp:5,ofdm_rate_9mbp:5,ofdm_rate_bw_12mbp:5,ofdm_rate_bw_18mbp:5,ofdm_rate_bw_24mbp:5,ofdm_rate_bw_27mbp:5,ofdm_rate_bw_3mbp:5,ofdm_rate_bw_4_5mbp:5,ofdm_rate_bw_6mbp:5,ofdm_rate_bw_9mbp:5,ofdmrate12mbp:5,ofdmrate12mbpsbw10mhz:5,ofdmrate18mbp:5,ofdmrate18mbpsbw10mhz:5,ofdmrate24mbp:5,ofdmrate24mbpsbw10mhz:5,ofdmrate27mbpsbw10mhz:5,ofdmrate36mbp:5,ofdmrate3mbpsbw10mhz:5,ofdmrate48mbp:5,ofdmrate4_5mbpsbw10mhz:5,ofdmrate54mbp:5,ofdmrate6mbp:5,ofdmrate6mbpsbw10mhz:5,ofdmrate9mbp:5,ofdmrate9mbpsbw10mhz:5,off:24,offer:31,onc:30,one:[3,4,18,25],onli:[21,23,25,30,37],onto:[20,21,22,23,24,25,26,27,38],open:[21,24,37],oppertun:[32,33],option:[1,17,18,21,25],option_str:1,order:[17,34,37,38],org:[5,24],osmhpi:38,other:[5,27],otherwis:37,out:[8,20,21,22,23,24,25,26,27],output:[7,8,9,10,11,12,21,24,25,32,33],output_directori:33,over:[12,29],overal:[1,30],overrid:[1,21],packag:[22,27],page:36,pair:[17,21,24],paramet:[1,3,4,5,7,8,9,10,11,12,14,17,18,20,21,22,23,24,25,26,27,28,29,30,32,33,34],paramiko:12,parent:1,pars:1,parse_arg:1,parse_known_arg:1,parser:1,particip:38,pass:[1,5,14,18,24,34,38],passwd:38,password:[25,26],path:[7,8,9,10,11,12,13,21,24,25,38],pcap:17,pcap_file_nam:17,peer:17,per:30,physic:[3,4,5,18,22,26],pick:5,pid:[21,25,37,38],pip:37,plan:34,pleas:[5,22,34,38],pop:14,port:[21,38],posit:[14,20,21,22,23,24,25,26,27,32,33],possibl:21,power:5,prebuilt:37,prefix:[20,21,22,23,24,25,26,27],prefix_char:1,prepar:[3,4,5,18,20,21,22,23,24,25,26,27,28,29,32,33],prepare_nod:[32,33],prepend:13,prerequesit:38,prevent:1,print:[1,8],print_help:1,print_usag:1,print_vers:1,privileg:[37,38],proc_id:25,proce:38,process:25,produc:32,prog:1,project:[14,37],properli:[34,38],properti:[3,4,5,14,17,21],provid:[18,34,37,38],proxy_arp:25,pull:[21,24,38],purpos:[7,8,14,29,37],push:14,put:[21,24],pylxd:11,python3:37,python:[1,34,37,38],pythonpath:37,qemu:17,qemu_opt:25,qemunod:25,queue:16,rais:[1,10],random:17,raspberri:26,rate:5,raw:5,reach:[17,25],reachabl:26,read:5,real:22,receiv:4,recommend:37,red:30,refer:[28,36],regist:1,registri:21,registry_nam:1,rel:[21,25],relat:[32,33],reli:38,remot:[12,22,25,26,37],remov:[22,25,26],remove_bridg:17,remove_remote_address:[22,25,26],repetit:1,repositori:[37,38],repres:[20,21,22,23,24,25,26,27],requir:[25,37],resembl:[3,4,8,17],result:[16,33],retriev:[7,8,9,10,11,12,28],return_cod:16,return_valu:16,root:37,rout:[22,27],run:[1,6,7,8,9,10,11,12,14,20,21,22,23,24,25,26,28,29,30,37],runtim:[21,29],same:38,scenario:[0,1,29,32,34,36,37],script:[21,22,23,24],search:36,second:[16,29,34],see:[5,17,21,34,38],self:7,send:5,sequenc:34,server:[24,38],set:[1,5,7,17,20,21,22,23,24,25,26,27,28,29,32,33,38],set_default:1,set_node_posit:[32,33],set_node_s:[32,33],set_output_directori:[32,33],set_posit:[20,21,22,23,24,25,26,27],set_visu:[28,32,33],setup:[17,21,22,24,25,26,38],setup_bridg:17,setup_host_interfac:[21,24,25],setup_log:1,setup_qemu_host_address:17,setup_remote_address:[22,25,26],setup_veth_container_end:17,setup_veth_pair:17,shadow:38,shall:[20,21,22,23,24,25,26,27],share:38,shell:[7,8,9,10,11,12,13,20],should:[1,18,21,24],show:38,side:[17,25],simpl:[1,14,23],simplecontext:14,simul:[0,1,3,4,5,6,10,14,18,19,20,21,22,23,24,25,26,27,28,33,34,36,37],simulation_tim:[28,29],singl:18,site:17,size:[32,33],sleep:34,snap:37,sock:37,socket:37,solut:37,some:[8,34,37,38],someth:[10,21],sourc:[1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,32,33,34],space:34,spatial:5,specif:[14,25,30,34],specifi:[7,20,21,22,23,24,25,26,27],spectrum:30,speed:4,split_shell_argu:13,ssh:25,sshclient:12,sshcommandexecutor:12,sshnode:26,stack:[14,20,21,22,23,24,25,26,27],standard:[5,21],start:[16,18,21,24,25,28,29,34,36,38],start_contain:24,start_docker_contain:21,start_on_simulation_end:16,start_on_simulation_start:16,start_qemu:25,startup:21,statu:1,stderr:[1,7,8,9,10,11,12,21,24],stderr_logfil:[7,8,9,10,11,12],stdout:[7,8,9,10,11,12,21,24],stdout_logfil:[7,8,9,10,11,12],step:[20,27],stop:[10,21,25,34],stop_docker_contain:21,stop_ev:34,stop_qemu_vm:25,store:[7,14],str:[1,4,7,8,9,10,11,12,14,17,18,20,21,22,23,24,25,26,27,32,33],stream:[5,21,24],string:[1,5,21],stringify_shell_argu:13,subclass:[1,18],subnet:[18,26],successfulli:[25,30],sudo:[12,13,38],sudoer:38,sumo:36,sumo_hom:38,sumo_host:38,sumo_port:38,sumocfg:38,sumomobilityinput:38,suppli:[20,21,22,23,24,25,26,27],support:[18,20,21,22,23,24,25,26,27,34],sure:[5,10,37,38],switchnod:27,system:25,tag:21,take:[26,29],tap:[17,21,24,25],tap_mod:17,tap_nam:17,task:34,tbd:35,tear:14,teardown:[14,28],termin:25,test:37,testb:[0,34,38],than:25,them:[1,18,21,24,29,37],therefor:[14,33,37],thereful:6,thi:[1,3,4,5,7,8,9,10,11,12,14,17,18,20,21,22,23,24,25,26,27,29,34,38],though:[37,38],thread:34,threadlocalstack:14,time:[4,21],timeout:[25,29],timestamp:13,titl:38,tmp:38,togeth:18,too:[5,37],tool:38,top:14,torn:14,traci:38,transmiss:4,transmit:4,tupl:21,two:[5,38],tx_power:5,type:[3,4,5,7,8,9,10,11,12,17,20,21,22,23,24,25,26,27,28],ubuntu:37,understand:21,uniqu:[17,20,25,30],unique_gener:30,universal_newlin:10,unix:38,unnam:[7,8],unqiu:17,untest:18,until:[25,29,34],updat:[20,21,22,23,24,25,26,27],usag:1,use:[1,5,7,8,9,10,11,12,14,18,21,22,24,25,32,33,34,37,38],used:[1,2,6,14,17,18,20,22,24,26,28,29,38],useful:[6,8,14,21,22,23,24],useloc:17,user:[7,8,9,10,11,12,13,20,21,22,23,24,25,26,27,31,38],usern:[37,38],usernam:[25,26],uses:[27,36,38],using:[5,32,37,38],usr:38,valid:[1,4,5],valu:[1,4,5,21,24,25,30,34],variabl:[21,34,38],variant:36,vcpu:21,vehicl:38,verbos:1,version:[1,38],veth:[17,21,24],veth_nam:17,via:[4,25,26,37],virtual:[21,25],visual:[18,20,28],volum:[21,37,38],volumes_and_port:21,vscode:37,wai:[23,28,38],wait:[25,34],wait_for_connect:25,wait_until:34,wait_until_tru:34,want:[14,37],wants_ip_stack:[20,21,22,23,24,25,26,27],warn:[3,10,17,18,20,21,22,23,24,25,26,27,34],whatev:14,when:[16,20,21,22,23,24,25,26,27,34],where:25,whether:[1,12,20,21,22,23,24,25,26,27,29],which:[29,32],width:5,wifi:20,wifi_802_11a:5,wifi_802_11ac:5,wifi_802_11ax:5,wifi_802_11b:5,wifi_802_11g:5,wifi_802_11n:5,wifi_802_11n_5g:5,wifi_802_11p:5,wifi_mac_help:5,wifichannel:[5,18],wifidatar:5,wifistandard:5,wiki:5,wikipedia:5,wireless:[5,38],with_traceback:7,within:[17,20,21,22,23,24,25,26,27,37,38],without:[36,38],work:[20,21,22,23,24,25,26,27,34,37],workflow:[6,21,22,23,24,28,29],workflow_function_nam:34,workspac:38,would:[3,4],write:[0,21,24,36],wrong:10,x11:38,x86_64:25,xml:32,you:[1,5,7,14,17,22,34,37,38],your:[5,14,17,37,38],yourself:[3,17,29,37]},titles:["API Reference","marvis.argparse","marvis.channel","marvis.channel.channel","marvis.channel.csma","marvis.channel.wifi","marvis.command_executor","marvis.command_executor.base","marvis.command_executor.console","marvis.command_executor.docker","marvis.command_executor.local","marvis.command_executor.lxd","marvis.command_executor.ssh","marvis.command_executor.util","marvis.context","marvis.events","marvis.events.Event","marvis.interface","marvis.network","marvis.node","marvis.node.base","marvis.node.docker","marvis.node.external","marvis.node.interface","marvis.node.lxd","marvis.node.qemu","marvis.node.ssh","marvis.node.switch","marvis.scenario","marvis.simulation","marvis.util","marvis.visualization","marvis.visualization.netanimvisualization","marvis.visualization.visualization","marvis.workflow","Getting Started","marvis - It\u2019s A Testbed! :)","Installation","Using SUMO With marvis"],titleterms:{"switch":27,Using:38,With:[37,38],api:0,argpars:1,base:[7,20],channel:[2,3,4,5],command_executor:[6,7,8,9,10,11,12,13],connect:38,consol:8,context:14,csma:4,docker:[9,21,37,38],event:[15,16],extern:22,get:35,host:38,indic:36,instal:[37,38],instanc:38,interfac:[17,23],local:[10,37,38],lxd:[11,24],marvi:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,38],mode:38,netanimvisu:32,network:18,node:[19,20,21,22,23,24,25,26,27],qemu:25,refer:0,remot:38,run:38,scenario:[28,38],simul:[29,38],ssh:[12,26],start:35,sumo:38,tabl:36,testb:36,util:[13,30],variant:38,visual:[31,32,33],wifi:5,without:37,workflow:34,write:38}})