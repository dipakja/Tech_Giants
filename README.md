# Power Manager Telemetry

## Description

In the era of 5G and edge computing, the deployment of devices across different locations has increased, leading to higher power consumption. To address this issue, the government is pushing enterprises and industries to reduce power usage with the goal of achieving net-zero power consumption. Additionally, the increasing price of electricity makes it crucial to understand the total power drawn by a system. This project aims to collect power telemetry data from a system's CPU, memory, NIC, and TDP to measure and record power utilization based on system utilization percentages.

## Pre-requisites

- Computer Systems Basics (CPU, memory, storage, NIC)
- Good hands-on experience with Linux
- Programming skills in Python and/or C
- Familiarity with Kubernetes/Docker

## Outcomes

- Ability to get telemetry data from the system (CPU, memory, NIC, and TDP)
- Run traffic to consume 100% utilization of the system using containers
- Collect telemetry data
- Create a solution to run, utilize a system, and get telemetry data

## Requirements

- Python 3.x
- psutil library (for telemetry data collection)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/power-manager-telemetry.git
    cd power-manager-telemetry
    ```

2. **Install the required Python packages**:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the telemetry data collection script**:

    ```sh
    python power_manager_telemetry.py
    ```

2. **Specify the target system utilization percentage** (default is 100%):

    ```sh
    python power_manager_telemetry.py --target-utilization 100
    ```

## Script Details

### `power_manager_telemetry.py`

This script collects telemetry data from the system and measures power utilization. It performs the following tasks:

- Collects CPU power usage using `psutil`.
- Collects memory power usage using `psutil`.
- Collects NIC power usage using `psutil`.
- Collects TDP (Thermal Design Power) by reading system thermal data.
- Simulates system load to achieve the target utilization percentage.
- Records telemetry data and prints the results.

### Telemetry Data Collection Functions

- `get_cpu_power_usage()`: Returns the CPU usage percentage.
- `get_memory_power_usage()`: Returns the memory usage percentage.
- `get_nic_power_usage()`: Returns the total bytes sent and received by the NIC.
- `get_tdp()`: Returns the system's TDP in degrees Celsius.
- `simulate_system_load(target_utilization)`: Simulates system load to achieve the target utilization percentage.
- `collect_telemetry_data(target_utilization)`: Collects and returns telemetry data based on the target utilization percentage.

## Example Output

```sh
Simulating system load...
Telemetry Data:
CPU Usage: 99.5%
Memory Usage: 65.3%
NIC Usage: 1234567 bytes
TDP: 45.2 °C
