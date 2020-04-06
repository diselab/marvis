Search.setIndex({docnames:["api","api/cohydra.argparse","api/cohydra.channel","api/cohydra.channel.channel","api/cohydra.channel.csma","api/cohydra.channel.wifi","api/cohydra.command_executor","api/cohydra.command_executor.base","api/cohydra.command_executor.console","api/cohydra.command_executor.docker","api/cohydra.command_executor.local","api/cohydra.command_executor.ssh","api/cohydra.command_executor.util","api/cohydra.context","api/cohydra.events","api/cohydra.events.Event","api/cohydra.interface","api/cohydra.network","api/cohydra.node","api/cohydra.node.base","api/cohydra.node.docker","api/cohydra.node.external","api/cohydra.node.ssh","api/cohydra.node.switch","api/cohydra.scenario","api/cohydra.simulation","api/cohydra.util","api/cohydra.visualisation","api/cohydra.visualisation.netanimvisualisation","api/cohydra.visualisation.visualisation","api/cohydra.workflow","getting-started","index","installation"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.index":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["api.rst","api/cohydra.argparse.rst","api/cohydra.channel.rst","api/cohydra.channel.channel.rst","api/cohydra.channel.csma.rst","api/cohydra.channel.wifi.rst","api/cohydra.command_executor.rst","api/cohydra.command_executor.base.rst","api/cohydra.command_executor.console.rst","api/cohydra.command_executor.docker.rst","api/cohydra.command_executor.local.rst","api/cohydra.command_executor.ssh.rst","api/cohydra.command_executor.util.rst","api/cohydra.context.rst","api/cohydra.events.rst","api/cohydra.events.Event.rst","api/cohydra.interface.rst","api/cohydra.network.rst","api/cohydra.node.rst","api/cohydra.node.base.rst","api/cohydra.node.docker.rst","api/cohydra.node.external.rst","api/cohydra.node.ssh.rst","api/cohydra.node.switch.rst","api/cohydra.scenario.rst","api/cohydra.simulation.rst","api/cohydra.util.rst","api/cohydra.visualisation.rst","api/cohydra.visualisation.netanimvisualisation.rst","api/cohydra.visualisation.visualisation.rst","api/cohydra.workflow.rst","getting-started.rst","index.rst","installation.rst"],objects:{"":{cohydra:[0,0,0,"-"]},"cohydra.argparse":{ArgumentParser:[1,1,1,""]},"cohydra.argparse.ArgumentParser":{add_argument:[1,2,1,""],add_argument_group:[1,2,1,""],add_mutually_exclusive_group:[1,2,1,""],add_subparsers:[1,2,1,""],convert_arg_line_to_args:[1,2,1,""],error:[1,2,1,""],exit:[1,2,1,""],format_help:[1,2,1,""],format_usage:[1,2,1,""],get_default:[1,2,1,""],parse_args:[1,2,1,""],parse_intermixed_args:[1,2,1,""],parse_known_args:[1,2,1,""],parse_known_intermixed_args:[1,2,1,""],print_help:[1,2,1,""],print_usage:[1,2,1,""],register:[1,2,1,""],run:[1,2,1,""],set_defaults:[1,2,1,""]},"cohydra.channel":{channel:[3,0,0,"-"],csma:[4,0,0,"-"],wifi:[5,0,0,"-"]},"cohydra.channel.channel":{Channel:[3,1,1,""]},"cohydra.channel.channel.Channel":{interfaces:[3,3,1,""],network:[3,3,1,""],nodes:[3,2,1,""],ns3_nodes_container:[3,3,1,""],prepare:[3,2,1,""]},"cohydra.channel.csma":{CSMAChannel:[4,1,1,""]},"cohydra.channel.csma.CSMAChannel":{csma_helper:[4,3,1,""],delay:[4,3,1,""],devices_container:[4,3,1,""],nodes:[4,2,1,""],prepare:[4,2,1,""],speed:[4,3,1,""]},"cohydra.channel.wifi":{WiFiChannel:[5,1,1,""]},"cohydra.channel.wifi.WiFiChannel":{WiFiDataRate:[5,1,1,""],WiFiStandard:[5,1,1,""],antennas:[5,3,1,""],channel:[5,3,1,""],channel_width:[5,3,1,""],data_rate:[5,3,1,""],devices_container:[5,3,1,""],frequency:[5,3,1,""],nodes:[5,2,1,""],prepare:[5,2,1,""],standard:[5,3,1,""],tx_power:[5,3,1,""],wifi:[5,3,1,""]},"cohydra.channel.wifi.WiFiChannel.WiFiDataRate":{DSSS_RATE_11Mbps:[5,3,1,""],DSSS_RATE_1Mbps:[5,3,1,""],DSSS_RATE_2Mbps:[5,3,1,""],DSSS_RATE_5_5Mbps:[5,3,1,""],ERP_OFDM_RATE_12Mbps:[5,3,1,""],ERP_OFDM_RATE_18Mbps:[5,3,1,""],ERP_OFDM_RATE_24Mbps:[5,3,1,""],ERP_OFDM_RATE_36Mbps:[5,3,1,""],ERP_OFDM_RATE_48Mbps:[5,3,1,""],ERP_OFDM_RATE_54Mbps:[5,3,1,""],ERP_OFDM_RATE_6Mbps:[5,3,1,""],ERP_OFDM_RATE_9Mbps:[5,3,1,""],OFDM_RATE_12Mbps:[5,3,1,""],OFDM_RATE_18Mbps:[5,3,1,""],OFDM_RATE_24Mbps:[5,3,1,""],OFDM_RATE_36Mbps:[5,3,1,""],OFDM_RATE_48Mbps:[5,3,1,""],OFDM_RATE_54Mbps:[5,3,1,""],OFDM_RATE_6Mbps:[5,3,1,""],OFDM_RATE_9Mbps:[5,3,1,""]},"cohydra.channel.wifi.WiFiChannel.WiFiStandard":{WIFI_802_11a:[5,3,1,""],WIFI_802_11ac:[5,3,1,""],WIFI_802_11ax:[5,3,1,""],WIFI_802_11b:[5,3,1,""],WIFI_802_11g:[5,3,1,""],WIFI_802_11n:[5,3,1,""],WIFI_802_11n_5G:[5,3,1,""]},"cohydra.command_executor":{base:[7,0,0,"-"],console:[8,0,0,"-"],docker:[9,0,0,"-"],local:[10,0,0,"-"],ssh:[11,0,0,"-"],util:[12,0,0,"-"]},"cohydra.command_executor.base":{CommandExecutor:[7,1,1,""],ExitCode:[7,4,1,""]},"cohydra.command_executor.base.CommandExecutor":{counter:[7,3,1,""],execute:[7,2,1,""],get_logger:[7,2,1,""],name:[7,3,1,""]},"cohydra.command_executor.base.ExitCode":{args:[7,3,1,""],with_traceback:[7,2,1,""]},"cohydra.command_executor.console":{ConsoleCommandExecutor:[8,1,1,""]},"cohydra.command_executor.console.ConsoleCommandExecutor":{execute:[8,2,1,""],get_logger:[8,2,1,""]},"cohydra.command_executor.docker":{DockerCommandExecutor:[9,1,1,""]},"cohydra.command_executor.docker.DockerCommandExecutor":{container:[9,3,1,""],execute:[9,2,1,""],get_logger:[9,2,1,""]},"cohydra.command_executor.local":{LocalCommandExecutor:[10,1,1,""],log_file:[10,5,1,""]},"cohydra.command_executor.local.LocalCommandExecutor":{execute:[10,2,1,""],get_logger:[10,2,1,""]},"cohydra.command_executor.ssh":{SSHCommandExecutor:[11,1,1,""],log_file:[11,5,1,""]},"cohydra.command_executor.ssh.SSHCommandExecutor":{client:[11,3,1,""],execute:[11,2,1,""],get_logger:[11,2,1,""],sudo:[11,3,1,""]},"cohydra.command_executor.util":{LogFile:[12,1,1,""],split_shell_arguments:[12,5,1,""],stringify_shell_arguments:[12,5,1,""]},"cohydra.command_executor.util.LogFile":{log:[12,2,1,""]},"cohydra.context":{Context:[13,1,1,""],DeferredItem:[13,1,1,""],NoContext:[13,1,1,""],SimpleContext:[13,1,1,""],ThreadLocalStack:[13,1,1,""],defer:[13,5,1,""]},"cohydra.context.Context":{add_error:[13,2,1,""],cancel:[13,2,1,""],cleanup:[13,2,1,""],current:[13,2,1,""],defer:[13,2,1,""],fails:[13,3,1,""]},"cohydra.context.DeferredItem":{args:[13,3,1,""],cancel:[13,2,1,""],cleanup:[13,2,1,""],ctx:[13,3,1,""],func:[13,3,1,""],kwargs:[13,3,1,""],name:[13,3,1,""]},"cohydra.context.NoContext":{add_error:[13,2,1,""],cancel:[13,2,1,""],cleanup:[13,2,1,""],current:[13,2,1,""],defer:[13,2,1,""]},"cohydra.context.SimpleContext":{add_error:[13,2,1,""],cancel:[13,2,1,""],cleanup:[13,2,1,""],current:[13,2,1,""],defer:[13,2,1,""]},"cohydra.context.ThreadLocalStack":{pop:[13,2,1,""],push:[13,2,1,""],stack:[13,2,1,""],top:[13,2,1,""]},"cohydra.events":{Event:[15,0,0,"-"],e:[14,5,1,""],event:[14,5,1,""],execute_events_on_simulation_end:[14,5,1,""]},"cohydra.events.Event":{Event:[15,1,1,""],EventPart:[15,1,1,""],e:[15,5,1,""],event:[15,5,1,""],event_worker:[15,5,1,""],execute_events_on_simulation_end:[15,5,1,""]},"cohydra.events.Event.Event":{after:[15,2,1,""],check_if:[15,2,1,""],execute:[15,2,1,""],s:[15,2,1,""],start:[15,2,1,""],start_on_simulation_end:[15,2,1,""],start_on_simulation_start:[15,2,1,""],when:[15,2,1,""]},"cohydra.interface":{Interface:[16,1,1,""]},"cohydra.interface.Interface":{address:[16,3,1,""],bridge_name:[16,2,1,""],connect_tap_to_bridge:[16,2,1,""],disconnect_tap_from_bridge:[16,2,1,""],ifname:[16,3,1,""],mac_address:[16,3,1,""],node:[16,3,1,""],ns3_device:[16,3,1,""],pcap_file_name:[16,2,1,""],remove_bridge:[16,2,1,""],setup_bridge:[16,2,1,""],setup_veth_container_end:[16,2,1,""],setup_veth_pair:[16,2,1,""],tap_name:[16,2,1,""],veth_name:[16,2,1,""]},"cohydra.network":{Network:[17,1,1,""],network_address_helper:[17,5,1,""]},"cohydra.network.Network":{address_helper:[17,3,1,""],channels:[17,3,1,""],color:[17,3,1,""],connect:[17,2,1,""],network:[17,3,1,""],prepare:[17,2,1,""]},"cohydra.node":{"switch":[23,0,0,"-"],base:[19,0,0,"-"],docker:[20,0,0,"-"],external:[21,0,0,"-"],ssh:[22,0,0,"-"]},"cohydra.node.base":{Node:[19,1,1,""]},"cohydra.node.base.Node":{add_interface:[19,2,1,""],channels:[19,3,1,""],color:[19,3,1,""],command_executor:[19,3,1,""],execute_command:[19,2,1,""],go_offline:[19,2,1,""],go_online:[19,2,1,""],interfaces:[19,3,1,""],name:[19,3,1,""],ns3_node:[19,3,1,""],position:[19,3,1,""],prepare:[19,2,1,""],set_position:[19,2,1,""],wants_ip_stack:[19,2,1,""]},"cohydra.node.docker":{DockerNode:[20,1,1,""],expand_volume_shorthand:[20,5,1,""],log_to_file:[20,5,1,""]},"cohydra.node.docker.DockerNode":{add_interface:[20,2,1,""],build_docker_image:[20,2,1,""],command:[20,3,1,""],command_executor:[20,3,1,""],container:[20,3,1,""],container_pid:[20,3,1,""],cpus:[20,3,1,""],docker_build_dir:[20,3,1,""],docker_image:[20,3,1,""],docker_image_tag:[20,2,1,""],dockerfile:[20,3,1,""],environment_variables:[20,3,1,""],execute_command:[20,2,1,""],exposed_ports:[20,3,1,""],go_offline:[20,2,1,""],go_online:[20,2,1,""],memory:[20,3,1,""],prepare:[20,2,1,""],pull:[20,3,1,""],set_position:[20,2,1,""],setup_host_interfaces:[20,2,1,""],start_docker_container:[20,2,1,""],stop_docker_container:[20,2,1,""],volumes:[20,3,1,""],wants_ip_stack:[20,2,1,""]},"cohydra.node.external":{ExternalNode:[21,1,1,""]},"cohydra.node.external.ExternalNode":{add_interface:[21,2,1,""],bridge:[21,3,1,""],command_executor:[21,3,1,""],execute_command:[21,2,1,""],go_offline:[21,2,1,""],go_online:[21,2,1,""],ifname:[21,3,1,""],prepare:[21,2,1,""],remove_remote_address:[21,2,1,""],set_position:[21,2,1,""],setup_remote_address:[21,2,1,""],wants_ip_stack:[21,2,1,""]},"cohydra.node.ssh":{SSHNode:[22,1,1,""],default_ip:[22,5,1,""]},"cohydra.node.ssh.SSHNode":{add_interface:[22,2,1,""],execute_command:[22,2,1,""],go_offline:[22,2,1,""],go_online:[22,2,1,""],prepare:[22,2,1,""],remove_remote_address:[22,2,1,""],set_position:[22,2,1,""],setup_remote_address:[22,2,1,""],wants_ip_stack:[22,2,1,""]},"cohydra.node.switch":{SwitchNode:[23,1,1,""]},"cohydra.node.switch.SwitchNode":{add_interface:[23,2,1,""],bridge_device:[23,3,1,""],execute_command:[23,2,1,""],go_offline:[23,2,1,""],go_online:[23,2,1,""],prepare:[23,2,1,""],set_position:[23,2,1,""],wants_ip_stack:[23,2,1,""]},"cohydra.scenario":{Scenario:[24,1,1,""]},"cohydra.scenario.Scenario":{add_mobility_input:[24,2,1,""],add_network:[24,2,1,""],channels:[24,2,1,""],context:[24,3,1,""],networks:[24,3,1,""],nodes:[24,2,1,""],simulation:[24,3,1,""],workflow:[24,2,1,""],workflows:[24,3,1,""]},"cohydra.simulation":{Simulation:[25,1,1,""]},"cohydra.simulation.Simulation":{docker_client:[25,3,1,""],hosts:[25,3,1,""],log_directory:[25,3,1,""],prepare:[25,2,1,""],scenario:[25,3,1,""],simulate:[25,2,1,""],started:[25,3,1,""],workflows:[25,3,1,""]},"cohydra.util":{network_color_for:[26,5,1,""],once:[26,5,1,""],unique:[26,5,1,""],unique_generator:[26,5,1,""]},"cohydra.visualisation":{netanimvisualisation:[28,0,0,"-"],visualisation:[29,0,0,"-"]},"cohydra.visualisation.netanimvisualisation":{NetAnimVisualisation:[28,1,1,""]},"cohydra.visualisation.netanimvisualisation.NetAnimVisualisation":{get_visualisation:[28,2,1,""],prepare_node:[28,2,1,""],set_node_position:[28,2,1,""],set_node_size:[28,2,1,""],set_visualisation:[28,2,1,""]},"cohydra.visualisation.visualisation":{NoVisualisation:[29,1,1,""],Visualisation:[29,1,1,""]},"cohydra.visualisation.visualisation.NoVisualisation":{get_visualisation:[29,2,1,""],prepare_node:[29,2,1,""],set_node_position:[29,2,1,""],set_node_size:[29,2,1,""],set_visualisation:[29,2,1,""]},"cohydra.visualisation.visualisation.Visualisation":{get_visualisation:[29,2,1,""],node_size:[29,3,1,""],prepare_node:[29,2,1,""],set_node_position:[29,2,1,""],set_node_size:[29,2,1,""],set_visualisation:[29,2,1,""]},"cohydra.workflow":{Workflow:[30,1,1,""]},"cohydra.workflow.Workflow":{current_waiting_events:[30,3,1,""],sleep:[30,2,1,""],start:[30,2,1,""],stop:[30,2,1,""],stop_event:[30,3,1,""],task:[30,3,1,""],wait_until:[30,2,1,""],wait_until_true:[30,2,1,""]},cohydra:{"interface":[16,0,0,"-"],argparse:[1,0,0,"-"],channel:[2,0,0,"-"],command_executor:[6,0,0,"-"],context:[13,0,0,"-"],events:[14,0,0,"-"],network:[17,0,0,"-"],node:[18,0,0,"-"],scenario:[24,0,0,"-"],simulation:[25,0,0,"-"],util:[26,0,0,"-"],visualisation:[27,0,0,"-"],workflow:[30,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","attribute","Python attribute"],"4":["py","exception","Python exception"],"5":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:attribute","4":"py:exception","5":"py:function"},terms:{"0ms":4,"100mbp":4,"128m":20,"4ghz":5,"5ghz":5,"64kbp":4,"abstract":[1,3,7,19,29],"case":33,"catch":[10,25],"class":[1,3,4,5,7,8,9,10,11,12,13,15,16,17,19,20,21,22,23,24,25,28,29,30],"default":[1,22,28,29],"enum":5,"float":[5,19,20,21,22,23,25,28,29,30],"function":[1,10,11,12,13,15,16,17,19,20,21,22,23,26,30],"import":[28,29],"int":[5,7,17,26],"new":[28,29,33],"null":[8,13,29],"return":[1,3,4,5,7,13,16,19,20,21,22,23,24,26,28,29],"static":[13,28,29,30],"super":29,"true":[1,19,20,21,22,23,30],"var":33,But:33,For:[3,4],Not:[19,20,21,22,23],The:[1,3,4,5,7,8,9,10,11,12,13,16,17,19,20,21,22,23,24,25,26,28,29,30,33],There:[29,33],These:[17,30],Use:[3,5,25],With:32,__traceback__:7,abc:[28,29],abort:25,absolut:20,access:33,activ:30,add:[13,19,20,21,22,23,24,33],add_argu:1,add_argument_group:1,add_error:13,add_help:1,add_interfac:[16,19,20,21,22,23],add_mobility_input:24,add_mutually_exclusive_group:1,add_network:24,add_subpars:1,added:33,adding:16,address:[16,17,20,21,22],address_help:17,after:[15,33],afterward:1,afunct:13,againt:30,all:[3,4,5,17,19,20,21,22,23,24,25,29,30,33],allow:[20,30,33],allow_abbrev:1,alphanumer:20,alread:21,alreadi:17,also:[16,17,19,20,21,22,23,25],alwai:20,amount:20,ani:[13,16],anoth:13,anotherfunct:13,antenna:5,api:32,append:[7,8,9,10,11,19,20,21,22,23],arg:[1,7,13,23],arg_lin:1,argument:[1,13,17],argument_default:1,argumentpars:1,arn:30,assign:[13,16,17,20,21,22],avail:[5,26],awai:[1,7],back:[19,20,21,22,23],band:5,base:[1,3,4,5,8,9,10,11,12,13,15,16,17,20,21,22,23,24,25,26,28,29,30,33],bash:[7,8,9,10,11],beaver:33,been:33,befor:21,behaviour:18,being:[25,30],belong:[3,13,24],below:33,best:5,between:[5,17,23],bind:33,bionic:33,bitrat:5,block:30,blue:26,blueprint:24,boockmey:30,bool:[1,11,19,20,21,22,23],bridg:[16,20,21,22],bridge_devic:23,bridge_nam:16,build:[17,20,33],build_docker_imag:20,buster:33,cabl:[3,4,17],calcul:[22,26],call:[1,13,17,19,20,21,22,23,29,30],callabl:[1,13,24,30],can:[5,6,7,13,16,17,20,24,25,32,33],cancel:13,cannel:19,cap:33,capabl:3,card:[3,16,19],care:25,channel:[16,17,19,20,21,22,23,24],channel_typ:17,channel_width:5,charact:20,check:25,check_if:15,choos:5,cleanup:13,cli:33,client:[11,25],clone:33,code:7,cohydra:33,collid:5,collis:[3,4],color:[17,19,26],com:30,combin:6,come:30,command:[6,7,8,9,10,11,12,15,19,20,21,22,23,30],command_executor:[19,20,21],commandexecutor:[6,7,8,9,10,11],compar:[17,30],compon:18,comput:[19,20],condit:[15,30],conect:17,configur:[17,20,24],conflict_handl:1,connect:[2,3,4,5,11,16,17,19,20,21,22,23,32],connect_tap_to_bridg:16,consid:21,consist:20,consolecommandexecutor:8,constraint:16,contain:[3,7,9,13,16,17,20,28,30,32,33],container_pid:20,content:32,context:[20,24],continu:25,control:16,convert_arg_line_to_arg:1,correct:5,correctli:16,could:[5,17],counter:7,cours:[5,33],cpu:20,creat:[5,24,28,30,33],creation:17,creator:20,csma:[3,17],csma_help:4,csmachannel:[4,17],ctrl:25,ctx:13,current:[13,24,28,29],current_waiting_ev:30,dasylab:30,data:5,data_r:5,dbm:5,debian:33,debug:[1,8],decor:30,def:30,default_ip:22,defer:13,deferreditem:13,defin:[1,27],delai:4,delet:16,depend:[5,33],describ:25,descript:[1,13],dest:1,destroi:16,detail:28,determin:25,dev:33,develop:33,devic:[4,5,16,21,22,23],devices_contain:[4,5],diagramm:[1,3,4,5,7,8,9,10,11,12,13,15,16,17,19,20,21,22,23,24,25,28,29,30],dict:[13,16,20],dictionari:20,dictonari:20,differ:27,directori:[20,25,33],disconnect:[16,19,20,21,22,23],disconnect_tap_from_bridg:16,displai:29,do_another_th:30,do_someth:30,docker:[17,25,32],docker_build_dir:20,docker_cli:25,docker_fil:20,docker_imag:20,docker_image_tag:20,dockercommandexecutor:9,dockerfil:[20,33],dockernod:[16,20],doe:[13,29],domain:[3,4],don:17,done:30,down:13,dry:8,dsss_rate_11mbp:5,dsss_rate_1mbp:5,dsss_rate_2mbp:5,dsss_rate_5_5mbp:5,dsssrate11mbp:5,dsssrate1mbp:5,dsssrate2mbp:5,dsssrate5_5mbp:5,durat:30,dure:[6,20,21,22,30],each:[20,29],easiest:33,either:1,enabl:33,enforc:20,entri:20,environ:20,environment_vari:20,epilog:1,equal:30,equival:[3,4,16],erp_ofdm_rate_12mbp:5,erp_ofdm_rate_18mbp:5,erp_ofdm_rate_24mbp:5,erp_ofdm_rate_36mbp:5,erp_ofdm_rate_48mbp:5,erp_ofdm_rate_54mbp:5,erp_ofdm_rate_6mbp:5,erp_ofdm_rate_9mbp:5,erpofdmrate12mbp:5,erpofdmrate18mbp:5,erpofdmrate24mbp:5,erpofdmrate36mbp:5,erpofdmrate48mbp:5,erpofdmrate54mbp:5,erpofdmrate6mbp:5,erpofdmrate9mbp:5,err:13,error:[1,13],eth0:[21,22],eth:[19,20,21,22],ethernet:4,evalu:30,event:30,event_work:15,eventpart:15,everi:[15,30],exampl:[1,16,17,20,24,25,30],except:[1,7,13],execpt:10,execut:[7,8,9,10,11,13,15,19,20,21,22,23,24,25,30,33],execute_command:[19,20,21,22,23],execute_events_on_simulation_end:[14,15],executor:[7,8,9,10,11,19,20,21],exist:21,exit:[1,7],exitcod:7,expand:20,expand_volume_shorthand:20,expected_result:30,expos:20,exposed_port:20,express:[15,30],extens:33,extern:[16,22,32],externalnod:[21,22],extra_host:20,fail:13,fals:[11,20],far:33,fault:[30,32],featur:[19,20,21,22,23],file:[1,7,8,9,10,11,16,20,25,28],first:5,flag:1,follow:24,form:20,format:28,format_help:1,format_usag:1,formatter_class:1,found:5,frequenc:5,from:[5,19,20,21,22,23,28,29,33],fromfile_prefix_char:1,func:[13,24,26],further:[5,30],gener:17,get:[24,29,32],get_default:1,get_logg:[7,8,9,10,11],get_visualis:[28,29],github:30,give:[28,29],given:[17,22],global:30,global_var:15,global_vari:30,go_offlin:[19,20,21,22,23],go_onlin:[19,20,21,22,23],goe:10,green:26,handl:[19,20,21,22,23],hardwar:[21,32],has:[19,20,27,33],have:[16,33],help:12,helper:[4,5,17],helpformatt:1,here:[5,16],host:[10,11,20,21,22,25,33],hostnam:20,http:[5,30],hue:26,hybrid:32,ieee_802:5,ifnam:[16,21,22],ignor:[5,29],imag:[20,33],implement:13,includ:21,incorpor:1,index:[17,26,32],indic:[11,19,20,21,22,23,25,30],influxdb:25,info:[1,30],inform:5,inherit:[1,3,4,5,7,8,9,10,11,12,13,15,16,17,19,20,21,22,23,24,25,28,29,30],initi:25,inject:[30,32],insert:17,insid:20,instal:[19,20,21,22,23,32],instanc:[17,20,26],instanti:[3,16],instead:25,instruct:30,intent:13,interfac:[3,19,20,21,22,23,27,33],intern:[3,12,16,19,20,23,26],ipv6:17,item:[13,20],iter:[25,26],its:32,just:8,kei:20,key_valu:20,keyword:[13,17],kind:[8,21,24],kwarg:[1,13,17,23],label:20,lambda_expr:15,lan:[3,4],later:[13,16],latest:33,level:[1,10,11,12],librari:33,like:[13,30],line:12,link:3,list:[3,4,5,13,17,19,20,21,22,23,24,30],local:[30,32],local_var:15,local_vari:30,localcommandexecutor:10,log:[1,3,4,5,7,8,9,10,11,12,13,16,20,25],log_directori:[20,25],log_fil:[10,11],log_path:20,log_to_fil:20,logfil:[10,11,12],logger:[1,7,8,9,10,11,12],logger_arg:1,login:22,mac:16,mac_address:16,mai:16,main:[1,18,33],make:[5,33],mani:17,manipul:32,manual:[17,19,20,21,22,23,25,30],map:[20,25],mask:17,maximum:5,mbit:5,mean:20,memmori:20,memori:20,messag:1,method:26,mhz:5,mobility_input:24,mobilityinput:24,model:[9,19],modifi:[25,33],modul:32,monitor:25,more:[5,17],mount:33,multipl:27,must:[17,20],name:[1,7,8,9,10,11,13,16,19,20,21,22,23],namespac:[1,16],neccesari:[19,23],neccessari:[17,33],necessari:17,need:[13,16,17,21,30,33],net:33,netanim:[28,33],netmask:17,network:[0,3,4,5,16,19,20,21,22,23,24,25,26,32,33],network_address:17,network_address_help:17,network_color_for:26,network_index:17,new_node_s:[28,29],nocontext:[13,29],node:[2,3,4,5,7,16,17,24,25,28,29],node_s:29,none:[1,3,4,5,7,8,9,10,11,13,15,16,17,19,20,21,22,23,24,25,29,30],normal:33,noth:[13,29],novisualis:29,ns3:21,ns3_devic:16,ns3_node:19,ns3_nodes_contain:3,number:[5,13,19,20,21,22,23,26],number_of_network:26,object:[1,3,7,8,12,13,15,16,17,19,24,25,28,29,30],obtain:33,ofdm_rate_12mbp:5,ofdm_rate_18mbp:5,ofdm_rate_24mbp:5,ofdm_rate_36mbp:5,ofdm_rate_48mbp:5,ofdm_rate_54mbp:5,ofdm_rate_6mbp:5,ofdm_rate_9mbp:5,ofdmrate12mbp:5,ofdmrate18mbp:5,ofdmrate24mbp:5,ofdmrate36mbp:5,ofdmrate48mbp:5,ofdmrate54mbp:5,ofdmrate6mbp:5,ofdmrate9mbp:5,onc:26,one:[3,4,17],onli:[20,26,33],onto:[19,20,21,22,23],open:[20,33],oppertun:[28,29],option:[1,16,17,20],option_str:1,order:[16,30,33],org:5,osmhpi:33,other:[5,23],otherwis:33,out:[8,19,20,21,22,23],output:[7,8,9,10,11,20],over:[11,25],overal:[1,26],overrid:[1,20],packag:[21,23],page:32,pair:[16,20],paramet:[1,3,4,5,7,8,9,10,11,13,16,17,19,20,21,22,23,24,25,26,28,29,30],paramiko:11,parent:1,pars:1,parse_arg:1,parse_intermixed_arg:1,parse_known_arg:1,parse_known_intermixed_arg:1,parser:1,pass:[1,13,17,30],password:22,path:[7,8,9,10,11,12,20],pcap:16,pcap_file_nam:16,peer:16,per:26,physic:[3,4,5,17,21,22],pick:5,pid:[20,33],pip:33,plan:30,pleas:[5,21,30],pop:13,port:20,posit:[13,19,20,21,22,23,28,29],possibl:20,power:5,prebuilt:33,prefix:[19,20,21,22,23],prefix_char:1,prepar:[3,4,5,17,19,20,21,22,23,24,25,28,29],prepare_nod:[28,29],prepend:12,prevent:1,print:[1,8],print_help:1,print_usag:1,privileg:33,produc:28,prog:1,project:[13,33],properli:30,properti:[3,4,5,13,16,20],provid:[17,30,33],pull:20,purpos:[7,8,13,25,33],push:13,put:20,python3:33,python:[1,30,33],pythonpath:33,queue:15,rais:[1,10],random:16,raspberri:22,rate:5,raw:5,reach:16,reachabl:22,read:5,real:21,receiv:4,recommend:33,red:26,refer:[24,32],regist:1,registri:20,registry_nam:1,rel:20,relat:[28,29],remot:[11,21,22,33],remov:[21,22],remove_bridg:16,remove_remote_address:[21,22],repetit:1,repositori:33,repres:[19,20,21,22,23],requir:33,resembl:[3,4,8,16],result:[15,29],retriev:[7,8,9,10,11,24],return_cod:15,return_valu:15,root:33,rout:[21,23],run:[1,6,7,8,9,10,11,13,19,20,21,22,24,25,26,33],runtim:[20,25],scenario:[0,1,25,30,32,33],script:[20,21],search:32,second:[15,25,30],see:[5,16,20,30],self:7,send:5,sequenc:30,set:[1,5,7,16,19,20,21,22,23,25,28,29],set_default:1,set_node_posit:[28,29],set_node_s:[28,29],set_posit:[19,20,21,22,23],set_visualis:[28,29],setup:[16,20,21,22],setup_bridg:16,setup_host_interfac:20,setup_log:1,setup_remote_address:[21,22],setup_veth_container_end:16,setup_veth_pair:16,shall:[19,20,21,22,23],shell:[7,8,9,10,11,19],should:[1,17,20],side:16,simpl:[1,13],simplecontext:13,simul:[0,1,3,4,5,6,10,13,17,18,19,20,21,22,23,24,29,30,32,33],simulation_tim:[24,25],singl:17,site:16,size:[28,29],sleep:30,sock:33,socket:33,solut:33,some:[8,30,33],someth:[10,20],sourc:[1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,28,29,30],space:30,spatial:5,specif:[13,26,30],specifi:[7,19,20,21,22,23],spectrum:26,speed:4,split_shell_argu:12,sshclient:11,sshcommandexecutor:11,sshnode:22,stack:[13,19,20,21,22,23],standard:[5,20],start:[15,20,24,25,30,32],start_docker_contain:20,start_on_simulation_end:15,start_on_simulation_start:15,startup:20,statu:1,stderr:[1,7,8,9,10,11,20],stderr_logfil:[7,8,9,10,11],stdout:[7,8,9,10,11,20],stdout_logfil:[7,8,9,10,11],step:[19,23],stop:[10,20,30],stop_docker_contain:20,stop_ev:30,store:[7,13,25],str:[1,4,7,8,9,10,11,13,16,17,19,20,21,22,23],stream:[5,20],string:[1,20],stringify_shell_argu:12,subclass:[1,17],subnet:[17,22],successfulli:26,sudo:11,suppli:[19,20,21,22,23],support:[17,19,20,21,22,23,30],sure:[5,10,33],switchnod:23,tag:20,take:[22,25],tap:[16,20],tap_nam:16,task:30,tbd:31,tear:13,teardown:[13,24],test:33,testb:[0,30],them:[1,17,20,25,33],therefor:[13,29,33],thereful:6,thi:[1,3,4,5,7,8,9,10,11,13,16,17,19,20,21,22,23,25,30],though:33,thread:30,threadlocalstack:13,time:[4,20],timeout:25,timestamp:12,togeth:17,too:33,top:13,torn:13,transmiss:4,transmit:4,tupl:20,two:5,tx_power:5,type:[3,4,5,7,8,9,10,11,16,19,20,21,22,23,24],ubuntu:33,understand:20,uniqu:[16,19,26],unique_gener:26,unnam:[7,8],unqiu:16,untest:17,until:[25,30],updat:[19,20,21,22,23],usag:1,use:[1,5,7,8,9,10,11,13,17,20,21,28,29,30,33],used:[1,2,6,13,16,17,19,21,22,24,25],useful:[6,8,13,20,21],user:[7,8,9,10,11,19,20,21,22,23,27],usern:33,usernam:22,uses:[23,32],using:[5,28,33],valid:[1,4,5],valu:[1,4,5,20,26,30],variabl:[20,30],vcpu:20,verbos:1,veth:[16,20],veth_nam:16,via:[4,22,33],virtual:20,visualis:[17,19],visualist:[19,20,21,22,23,28,29],volum:[20,33],volumes_and_port:20,vscode:33,wai:24,wait:30,wait_until:30,wait_until_tru:30,want:[13,33],wants_ip_stack:[19,20,21,22,23],warn:[3,10,16,17,19,20,21,22,23,30],whatev:13,when:[15,19,20,21,22,23,30],where:25,whether:[1,11,19,20,21,22,23,25],which:[25,28],width:5,wifi:19,wifi_802_11a:5,wifi_802_11ac:5,wifi_802_11ax:5,wifi_802_11b:5,wifi_802_11g:5,wifi_802_11n:5,wifi_802_11n_5g:5,wifichannel:[5,17],wifidatar:5,wifistandard:5,wiki:5,wikipedia:5,wireless:5,with_traceback:7,within:[16,19,20,21,22,23,33],without:32,work:[19,20,21,22,23,30,33],workflow:[6,20,21,24,25],workflow_function_nam:30,would:[3,4],write:[0,20],wrong:10,xml:28,you:[1,5,7,13,16,21,30,33],your:[5,13,16,33],yourself:[3,16,25,33]},titles:["API Reference","cohydra.argparse","cohydra.channel","cohydra.channel.channel","cohydra.channel.csma","cohydra.channel.wifi","cohydra.command_executor","cohydra.command_executor.base","cohydra.command_executor.console","cohydra.command_executor.docker","cohydra.command_executor.local","cohydra.command_executor.ssh","cohydra.command_executor.util","cohydra.context","cohydra.events","cohydra.events.Event","cohydra.interface","cohydra.network","cohydra.node","cohydra.node.base","cohydra.node.docker","cohydra.node.external","cohydra.node.ssh","cohydra.node.switch","cohydra.scenario","cohydra.simulation","cohydra.util","cohydra.visualisation","cohydra.visualisation.netanimvisualisation","cohydra.visualisation.visualisation","cohydra.workflow","Getting Started","cohydra - It\u2019s A Testbed! :)","Installation"],titleterms:{"switch":23,With:33,api:0,argpars:1,base:[7,19],channel:[2,3,4,5],cohydra:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32],command_executor:[6,7,8,9,10,11,12],consol:8,context:13,csma:4,docker:[9,20,33],event:[14,15],extern:21,get:31,indic:32,instal:33,interfac:16,local:[10,33],netanimvisualis:28,network:17,node:[18,19,20,21,22,23],refer:0,scenario:24,simul:25,ssh:[11,22],start:31,tabl:32,testb:32,util:[12,26],visualis:[27,28,29],wifi:5,without:33,workflow:30}})