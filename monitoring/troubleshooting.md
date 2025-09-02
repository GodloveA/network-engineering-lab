# Monitoring & Troubleshooting

## 1. Tools
- Ping & Traceroute for connectivity
- Wireshark for packet analysis
- SNMP/NetFlow for performance monitoring

## 2. Example Troubleshooting Workflow
1. **User reports internet is down**
   - Check default gateway reachability: `ping 192.168.1.1`
   - Verify DNS resolution: `nslookup google.com`
   - Run traceroute to check routing issues: `tracert 8.8.8.8`
   - Inspect firewall logs for blocked traffic
