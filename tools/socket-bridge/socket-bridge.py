import argparse
import http.server
import socketserver
import subprocess

def generate_ids():
    """
    The following defines the codes used for communication with switchable sockets. Key of each entry is 
    the base ID, scraped from one physical socket. Value is another dict where each entry defines the value
    that needs to be XORed on the ID to get to one channel's code. Channels a-d additionally need to be XORed 
    with on/off codes to switch the respective channel/ID combination on/off. Channels On/Off need to be XORed
    with the on code and switch all channels belonging to the ID on and off, respectively. 
    """
    id_vectors = [
        {'0b011000010111000100000000000000000': {'a': '0b1110001000000', 'b': '0b1100001000110','c': '0b1010001001110','d': '0b0110001011110','on': '0b0100001011000','off': '0b1000001001000'}}, 
        {'0b011101101101100000000000000000000': {'a': '0b1110100111100', 'b': '0b1100100111000','c': '0b1010100110100','d': '0b0110100101100','on': '0b0100100101000','off': '0b1000100110000'}}, 
        {'0b000010001000001000000000000000000': {'a': '0b1110100000100', 'b': '0b1100100000000','c': '0b1010100001000','d': '0b0110100011000','on': '0b0100100011100','off': '0b1000100010000'}}, 
        {'0b000011101100100000000000000000000': {'a': '0b1110110011100', 'b': '0b1100110011000','c': '0b1010110010100','d': '0b0110110001100','on': '0b0100110001000','off': '0b1000110001100'}} 
    ] 
    ids = []
    # TODO implement flexible ID parts if more than 16 channels are needed
    for base_id in id_vectors:
        for channel in ['a', 'b', 'c', 'd']:
            # perform XOR operation to get all 16 ID/channel combinations
            ids.append(int(list(base_id.keys())[0],2) ^ int(list(base_id.values())[0][channel],2))
    return ids

on = int('0b1000000000',2) # on code
off = int('0b10',2) # off code
protocol = 13 # rc-swich protocol used by sample sockets (Mumbi RCS-20GS)
ids = generate_ids()

class SwitchableSocketBridge(http.server.SimpleHTTPRequestHandler):

    def do_PUT(self): # web server behavior definition
        if self.path.startswith('/socket/'):
            path = self.path.split('/')
            try:
                switch_id = int(path[2]) # 0 <= switch_id <= 34
            except ValueError:
                self.send_response(400, "Socket ID not integer between 0 and 15")
                self.end_headers()
                return
            switch_toggle = path[3] # on or off
            if switch_id > 15:
                self.send_response(400, "Socket ID not integer between 0 and 15")
                self.end_headers()
                return
            if switch_toggle == 'on':
                subprocess.run(["./transmit", str(ids[switch_id] ^ on), str(protocol)]) # send ID XOR channel XOR on
                self.send_response(200, "OK")
                self.end_headers()
            elif switch_toggle == 'off':
                subprocess.run(["./transmit", str(ids[switch_id] ^ off), str(protocol)]) # send ID XOR channel XOR off
                self.send_response(200, "OK")
                self.end_headers()
            else:
                self.send_response(400, "Toggle state neither on nor off")
                self.end_headers()
        else:
            self.send_response(400, 'Path not /socket/<id>/<on|off>')
            self.end_headers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', action='store', default=8080, type=int, nargs='?', help='specify port (default 80)')
    args = parser.parse_args()
    with socketserver.TCPServer(('', args.port), SwitchableSocketBridge) as httpd: 
        print('HTTP server at port', args.port)
        httpd.serve_forever() ## start web server
