import psutil
import time
import os

def get_cpu_power_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_power_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_nic_power_usage():
    net_info = psutil.net_io_counters()
    return net_info.bytes_sent + net_info.bytes_recv

def get_disk_io_power_usage():
    disk_info = psutil.disk_io_counters()
    return disk_info.read_bytes + disk_info.write_bytes

def get_tdp():
    temps = []
    try:
        for i in range(5):  # Assume up to 5 thermal zones
            with open(f"/sys/class/thermal/thermal_zone{i}/temp", "r") as f:
                temp = f.read()
                temps.append(int(temp) / 1000.0)
        return temps
    except:
        return None

def simulate_system_load(target_utilization):
    print("Simulating system load...")
    load = os.cpu_count() * target_utilization / 100
    start_time = time.time()
    while time.time() - start_time < 10:
        psutil.cpu_percent(interval=0.1)

def collect_telemetry_data(target_utilization):
    simulate_system_load(target_utilization)
    
    cpu_usage = get_cpu_power_usage()
    memory_usage = get_memory_power_usage()
    nic_usage = get_nic_power_usage()
    disk_usage = get_disk_io_power_usage()
    tdp = get_tdp()

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "nic_usage": nic_usage,
        "disk_usage": disk_usage,
        "tdp": tdp
    }

if __name__ == "__main__":
    target_utilization = 100  # Target system utilization in percentage
    telemetry_data = collect_telemetry_data(target_utilization)
    
    print("Telemetry Data:")
    print(f"CPU Usage: {telemetry_data['cpu_usage']}%")
    print(f"Memory Usage: {telemetry_data['memory_usage']}%")
    print(f"NIC Usage: {telemetry_data['nic_usage']} bytes")
    print(f"Disk Usage: {telemetry_data['disk_usage']} bytes")
    print(f"TDP: {telemetry_data['tdp']} °C")
