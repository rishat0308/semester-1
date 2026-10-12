# Week 1.2, Session 2: Task 6

temperature = int(input('Enter the temperature of the machine: '))
pressure = int(input('Enter the pressure of the machine: '))
status = int(input("Enter the machine's operational status (1 for operating, 0 for stopped): "))

# temperature

tempstatus = ''
if temperature > 80:
    print('Temperature is too high.')
    tempstatus = 'high'
elif temperature >= 50 and temperature <= 80:
     print('Temperature is within safe limits.')
     tempstatus = 'normal'
elif temperature < 50:
    print('Temperature is low and no action is needed.')
    tempstatus = 'normal'

# pressure

pressurestatus = ''
if pressure > 100:
    print('High pressure, maintenance is required.')
    pressurestatus = 'high'
elif pressure >= 70 and pressure <= 100:
    print('Pressure is stable.')
    pressurestatus = 'normal'
elif pressure < 70:
    print('Low pressure, system is operating normally.')
    pressurestatus = 'normal'

# determine status

if status == 1:
    if tempstatus == 'high' or pressurestatus == 'high':
        print('Machine is running in unsafe conditions, shutting down is recommend.')
    else:
        print('Machine is running normally.')
else:
    print('Machine is not currently running, no immediate action is needed.')

