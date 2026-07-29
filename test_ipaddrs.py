import re


def is_valid_ipaddress(text):
    return re.findall(r'\d{3}\.\d{2,}\.\d{1}\.\d{1,}',text)

def test_ip():
    text = "Server IPs: 192.168.0.1, 10.0.0.256, 172.16.5.4"
    assert is_valid_ipaddress(text) == ["192.168.0.1", "172.16.5.4"]