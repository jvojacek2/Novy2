let SmerDoprava = 0
let zmenenSmer = 0
function TurnLeft () {
    SmerDoprava = 0
    maqueen.motorStop(maqueen.Motors.M1)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
}
function ZmenSmer () {
    if (0 == SmerDoprava) {
        TurnRight()
    } else {
        TurnLeft()
    }
}
function TurnRight () {
    SmerDoprava = 1
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    maqueen.motorStop(maqueen.Motors.M2)
}
basic.forever(function () {
    if (true && 10 > maqueen.Ultrasonic(PingUnit.Centimeters)) {
        ZmenSmer()
        zmenenSmer = control.eventTimestamp()
    }
})
