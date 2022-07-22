def maqSlightLeft():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
     

def maqSlightRight():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)

def maqForward(x):
    if x == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 220)

def maqStop():
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)

def maqBackward(x):
    if x == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 220)
    else:
        t = 5700 * x
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 255)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 220)
        basic.pause(t)
        maqStop()

def maqTurnLeft():
    music.play_tone(330,music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    for i in range(3):
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        basic.pause(100)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        basic.pause(100)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    basic.pause(660)
    maqStop()

def maqTurnRight():
    music.play_tone(262,music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    for i in range(3):
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        basic.pause(100)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        basic.pause(100)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    basic.pause(660)
    maqStop()

def on_forever():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)==0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)==0:   
        maqForward(0)

    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)==1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)==0: 
        maqSlightLeft()

    elif  maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT)==0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT)==1:
        maqSlightRight()

basic.forever(on_forever)