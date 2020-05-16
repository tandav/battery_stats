import datetime
import subprocess
import macos

_ = (
    subprocess
    .check_output(['ioreg', '-rn', 'AppleSmartBattery'], text=True)
    .splitlines()
)
for line in _:
    if '"MaxCapacity" = ' in line:
        MaxCapacity = int(line.split('=')[1])
    if '"CycleCount" = ' in line:
        CycleCount = int(line.split('=')[1])

with open('macbook_pro_16_inch_battery.csv', 'a') as fd:
    row = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{CycleCount},{MaxCapacity}\n"
    fd.write(row)


macos.notification(text=f'CycleCount: {CycleCount}\nMaxCapacity:{MaxCapacity}', title='Battery Stats')
