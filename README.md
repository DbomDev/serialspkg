# Serial-Generator
I was thinking today that I need again Serial lists for my purchase onyl Programms and online I can't find a free serial list generator, so I amde this Project.

## Setup
First you need Install the required Packages so the Program can work.

```pip install random
pip install json
pip install time
pip install pathlib
```

After We done this we are going to setup what we want have for serials. First we want to set the lengh of our serial keyes by settiing the variable `serial_lengh = 20` to our decided lengh of the Serial Key.

Then we can decide how many Serials we want to generate. For that we edit the variable `serial_amout = 5000` to the amout of Serials we want to generate.

When you want have a custom tag at the start of all of your serials, then just put in this variable `start_text = ""` your start. If you dont't want have a custom tag at the start of all of your Serials then just leave it blank.

In this variable `chars = 'abcdefghijklmnopqrstuvwxyz'` we have all of our characters which can be used for the Serials, you can add everything you want.

### Example
```
serial_lengh = 30
serial_amout = 1000

start_text = "myTag_"
chars = 'abcdefghijklmnopqrstuvwxyz123456789_.-'

```

## Credits
Credits are required (DbomDev).
