import scapy
import pyshark

def capture_traffic(interface="Wi-Fi",capture_duration=10):
    capture=pyshark.LiveCapture(interface=interface)
    print(f"Starting capture on {interface} for {capture_duration} seconds")
    capture.sniff(timeout=capture_duration)
    print("capture completed")
    return capture

def analyze_captured_packets(packets):
    for packet in packets:
        try:
            print(f"Packet:{packet.number}")
            print(f"Time:{packet.sniff_time}")
            print(f"Source IP:{packet.ip.src}")
            print(f"Destination Ip:{packet.ip.dest}")
            print(f"Protocol: {packet.highest_layer}")
            print(f"Length: {packet.length}")
            print('-' * 50)
        except AttributeError as e:
            print(f"Packet: {packet.number} - {e}")
            print('-' * 50)


def main():
    packets=capture_traffic(interface="Wi-Fi" , capture_duration=10)

    analyze_captured_packets(packets)


if __name__=="__main__":
    main()
