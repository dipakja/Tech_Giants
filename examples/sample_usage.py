from main import collect_telemetry_data

if __name__ == "__main__":
    target_utilization = 80
    telemetry_data = collect_telemetry_data(target_utilization)
    
    print("Sample Telemetry Data:")
    print(f"CPU Usage: {telemetry_data['cpu_usage']}%")
    print(f"Memory Usage: {telemetry_data['memory_usage']}%")
    print(f"NIC Usage: {telemetry_data['nic_usage']} bytes")
    print(f"TDP: {telemetry_data['tdp']} °C")
