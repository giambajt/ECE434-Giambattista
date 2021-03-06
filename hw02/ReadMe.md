### Measuring a gpio pin on an Oscilloscope using togglegpio.sh
1. Min voltage is 0V and Max voltage is 3.3V
2. O-scope says frequency is 4.12 Hz which is a period of 0.245 seconds
3. It's almost 2.5x off of the 100ms period
4. They most likely differ because linux is preempting togglegpio.sh
5. htop says that the CPU is using anywhere from 3-5%
6. ToggleGPIO.sh Table

 Sleep Time (s)  | Period (s) | CPU Usage (%)
-----------|-------------|----------
0.1|0.245|4
0.05|0.141|5.5
0.01|0.0588|12.5
0.001|0.045|19
0.0001|0.041|20.3
0.00001|0.04|20

7. The period becomes less and less stable as the frequency increases
8. The period is even less stable
9. The period was doubled by removing a few lines from the while loop
10. Using a sleep of 0.0001 the frequency went up about 17 Hz from the last question
11. 70 Hz seems to be the fastest I can get it

### Python Toggling
1. The frequency is around 6.2 KHz and the period is 0.000161 seconds
2. around 95% of the CPU
3. Comparison Table

Shell fastest frequency (Hz) | Python Fastest Frequency (kHz) | C Fastest Frequency (kHz)
----------------------------|-------------------------------|--------------------------
70|6.2|158

### GPIOD Toggling

Python 1 bit frequency (kHz) | Python 2 bit Frequency (kHz) | C 1 bit frequency (kHz) | C 2 bit frequency (kHz)
----------|---------|--------|----------
57| 53 | 280 | 265 



# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  7/7 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  2/2 | gpiod
|      | Security
|  1/1 | ssh port
|  1/1 | iptables
|  1/1 | fail2ban
| 20/20   | **Total**

Nice Videos