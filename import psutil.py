import psutil
ram= psutil.virtual_memory().percent
cpu= psutil.cpu_percent(interval=5)
print(f"ram percent,{ram}%")
print(f"cpu percent,{cpu}%")

if ram > 75:
    print("ram is high")
else:
    print("ram is normal")
if cpu > 75:
    print("cpu is high")
else:
    print("cpu is normal")
