var jf = require("johnny-five");
var circuito = new jf.Board();
var led1, led2, motor, celda, turno;

circuito.on("ready", prender);

function prender () {
	var config = { pin: "A0", freq: 50 }
	celda = new jf.Sensor(config);

	led1 = new jf.Led(11);
	led2 = new jf.Led(13);
	//led1.blink(500);
	//led2.blink(1000);

	motor = new jf.Servo(9);
	motor.to(90);

	ondear();
	
}

function ondear () {
	console.log("Luz: "+ celda.value);

	var luz = celda.value;

	if (luz > 700 && luz < 900) {
		motor.to(90);
		led1.off();
		led2.off();
        if (turno == 1) {
        	turno = 0;
        	motor.to(70);
        } else {
        	turno = 1;
        	motor.to(110);
        }

	} else if (luz > 900) {
		motor.to(180);
		led1.off();
		led2.off();
	} else {
		motor.to(30);
		led1.on();
		led2.on();
	}

	setTimeout(ondear, 1000);
}