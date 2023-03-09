# HV_test_iseg
Controller for I-seg THQ Power Supply for HV test

Need Pyserial to be installed 

Minimum Python V3 

How to run : 
```
py run_HV_test.py -v 5 -s 10 -e 100 -p 5

-v:entering voltage for USB interface

-s: Start voltage of test

-e: End Voltage of test

-p: Voltage step size

```


To change the thresold current:  open run_HV_test.py and change "C1=0.5E-3" to desied value

0.5E-3 = 0.5 mA 

for gui

click on `run.cmd`
