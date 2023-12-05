import subprocess
import re

ip_server = '192.168.1.1'


def startProcess(server):
    try:
        result = subprocess.run(['iperf', '-c', server], capture_output=True, text=True, check=True)
        return result.stdout, None
    except subprocess.CalledProcessError as e:
        return None, f"Error: {e.stderr}"


def parse(text):
    result = []

    
    intervals = re.findall(r'\[\s*(\d+)\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+\.\d+)\s+MBytes\s+(\d+\.\d+)\s+Mbits/sec', text)

    for interval in intervals:
        result_dict = {
           
            'Interval': interval[1],
            'Transfer': float(interval[2]),
            'Bitrate': float(interval[3])
        }

        result.append(result_dict)

    return result


result_unparsed, error = startProcess(ip_server)

result_list = parse(result_unparsed)

print(result_list)
