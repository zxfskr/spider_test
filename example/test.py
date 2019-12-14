import dns.query
import dns.tsigkeyring
import dns.update
import dns.resolver
import sys

import dns


# resolver = dns.resolver.Resolver()
# resolver.nameservers = ["172.18.61.253"]
# resolver.nameserver_ports = {
#     "172.18.61.253": 53
# }
# answer = resolver.query("fig.test.video")
# print(answer.response.to_text())
SERVER = "47.112.142.132"
PORT = 53
dns_query = dns.message.make_query("fig.test.video", "A")
response = dns.query.udp(dns_query, SERVER, port=PORT)
# print(dir(response.answer))
# print(response.answer)
ip_list = []
for i in response.answer:
    # print(i.to_text())
    # print(dir(i))
    tmp = i.to_rdataset()
    print(dir(tmp.to_text()))
    print(tmp.to_text().split()[-1])
    break
# print(ip_list)


"""
dig @8.8.8.8 www.baidu.com
dig @47.112.142.132 fig.test.video
"""