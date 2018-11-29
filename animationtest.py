import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import dht11
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# Create figur for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
#zs = []

#read data using pin 14
instance = dht11.DHT11(pin=17)
result = instance.read()

# This function is called periodically from FuncAnimation
def animate(zs, xs, ys):
    result = instance.read()
    if result.is_valid():
        temp_c = result.temperature
        humid = result.humidity
    # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(temp_c)
        #zs.append(humid)    

    # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=40, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('DHT11 Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    if xs == 5:
        xs.clear
#Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)

plt.show()