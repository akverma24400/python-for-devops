# Reads live CPU/memory/disk with psutil and checks each against a threshold.

import psutil

def system_health():
    try:
        cpu_threshold = int(input("Enter CPU threshold :"))
        memory_threshold = int(input("Enter Memory threshold :"))
        disk_threshold = int(input("Enter Disk threshold :"))

        current_cpu = psutil.cpu_percent(interval=1)
        current_memory = psutil.virtual_memory().percent
        current_disk = psutil.disk_usage("/").percent

        if current_cpu > cpu_threshold:
            print(f"CPU usage is above threshold: {current_cpu}% > {cpu_threshold}% WARNING")
        else:   
            print(f"CPU usage is within threshold: {current_cpu}% <= {cpu_threshold}% SAFE" )

        if current_memory > memory_threshold:
            print(f"Memory usage is above threshold: {current_memory}% > {memory_threshold}% WARNING")
        else:
            print(f"Memory usage is within threshold: {current_memory}% <= {memory_threshold}% SAFE")

        if current_disk > disk_threshold:
            print(f"Disk usage is above threshold: {current_disk}% > {disk_threshold}% WARNING ")
        else:
            print(f"Disk usage is within threshold: {current_disk}% <= {disk_threshold}% SAFE")

    except Exception as e:
        print(f"An error occurred: {e}")

system_health()
        

""" THRESHOLDS = {
    "CPU": 85.0,
    "Memory": 85.0,
    "Disk": 75.0,
}


def collect_metrics():
    return {
        "CPU": psutil.cpu_percent(interval=1),
        "Memory": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage("/").percent,
    }


def evaluate(name, value, threshold):
    if value > threshold:
        return f"WARNING (above {threshold:.0f}%)", False
    return "Healthy", True


def main():
    try:
        metrics = collect_metrics()
    except Exception as exc:  # psutil can fail on odd platforms/permissions
        print("Could not read system metrics:", exc)
        return

    print("=== System Health Report ===")
    all_healthy = True
    for name, value in metrics.items():
        status, healthy = evaluate(name, value, THRESHOLDS[name])
        all_healthy = all_healthy and healthy
        print(f"{name:7}: {value:5.1f}%  -> {status}")

    print("Overall:", "Healthy" if all_healthy else "NEEDS ATTENTION")


if __name__ == "__main__":
    main() """