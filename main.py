def TurnLeft():
    global SmerDoprava
    SmerDoprava = 0
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)

def ZmenSmer():
    if 0 == SmerDoprava:
        TurnRight()
    else:
        TurnLeft()

def TurnRight():
    global SmerDoprava
    SmerDoprava = 1
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
SmerDoprava = 0
zmenenSmer = 0

def on_every_interval():
    global zmenenSmer
    if 0 == zmenenSmer:
        ZmenSmer()
        zmenenSmer = 0
loops.every_interval(500, on_every_interval)

def on_forever():
    global zmenenSmer
    if 0 == zmenenSmer and 10 > maqueen.ultrasonic(PingUnit.CENTIMETERS):
        ZmenSmer()
        zmenenSmer = control.event_timestamp()
basic.forever(on_forever)

def on_forever2():
    if 2000 + zmenenSmer < control.event_timestamp():
        ZmenSmer()
basic.forever(on_forever2)
