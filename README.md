# office-traffic-light
System to show your status in the office build of an old floppy drive an a Raspberry Pi

## basic idea

My colleague bought himself a light that he can pin utside of his office to indicate if you are allowed to come-in or not. It's basically an RGB LED connected to the USB port and has a software to change the colors.
So I thought I could achieve the goal the geek way, so I have build a mechanical indicator from a floppy drive and a RaspberryPi.

Just using the stepper with an arm as indicator and programmed a web-interface with django. The django framework might be over-kill for the task but I used the chance to look into django.

## hardware

1. find an old FDD drive, open it and attach somehow the arm to the stepper
2. connect the 5V & GND of the RPI GPIO to the 5V input of the drive. Don't worry the stepper does not pull to much current, so the RPI wont mind
3. Connect an other GND to any of odd (lower row) pins of the FDD, they are all GND
4. Connect GPIO17 to pin 20 of the FDD (Head Step)
5. Connect GPIO18 to pin 18 of the FDD (Direction Select)
6. use a jumper to shortcut pins 11 & 12 of the FDD (Drive Select 1)

- RPI GPIO layout: http://elinux.org/Rpi_Low-level_peripherals#Interfacing_with_GPIO_pins
- FDD PIN layout: http://www.interfacebus.com/PC_Floppy_Drive_PinOut.html

I'm using one of the very old RPI-1 B models. And it works fine

## software

1. install python, pip and django (https://docs.djangoproject.com/en/1.10/topics/install/)
2. clone or download the code from this repro
3. run the development server: python manage.py runserver 0.0.0.0:8000
4. you should now be able to access the control: `http://<your rpi ip>:8000`
username: admin password: officelight
5. to administrate the users and status choices: `http://<your rpi ip>:8000/admin`

Every choice has a string and a number. The number is the head-position. That head-position is the track number of the FDD. Most 3.5-inch FDD do 80 tracks, but some would also do 83 (0-82).


