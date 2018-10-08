// Author: Kathy Grimes
// Node version: v10.11.0
// run this program by typing in terminal: node hwk4.js

// This js program reads 10 temp/hum sensor values, 1 every 10 seconds
// from the DHT22 sensor data pin on GPIO 4 of the Raspberry Pi 3
// The program prints out each reading as well as the lowest, highest, and average

// Please make sure the bcm2835, node, and node-gyp is installed before running this program
// Please make sure GPIO 4 of the Raspberry Pi is connected to the DHT22 sensor data pin

// Used https://github.com/momenso/node-dht-sensor for general setup and calling of sensor function
var sensor = require('node-dht-sensor');

var reading_value_number = 0;
var lowest_temp_f  = 300.0;
var lowest_hum     = 110.0;
var highest_temp_f = -300.;
var highest_hum    = -1.0;
var average_temp_f = 0;
var average_hum    = 0;


//while(reading_value_number < 10) {
function read_sensor() {
  sensor.read(22,4,function(err, temperature, humidity) {
		if(!err) {
		  //increment reading_value_number
		  reading_value_number = reading_value_number + 1;

		  //changing temperature in celsius to fahrenheit
		  var temp_f = temperature*9/5 + 32;

		  //outputting current reading onto console/terminal
		  console.log(reading_value_number + ' - Temp ' + temp_f.toFixed(1) + ' degF, ' + 
			      humidity.toFixed(1) + '% Hum');
		  
		  //checking for lowest temperature
		  if(temp_f < lowest_temp_f) {
		    lowest_temp_f = temp_f;
		  }

		  //checking for highest temperature
		  if(temp_f > highest_temp_f) {
		    highest_temp_f = temp_f;
		  }
		  
		  //cheking for lowest humidity
		  if(humidity < lowest_hum) {
		    lowest_hum = humidity;
		  }

		  //checking for highest humidity
		  if(humidity > highest_hum) {
		    highest_hum = humidity;
		  }
		  
		  //computing average temperature with past temperature values
		  average_temp_f = (average_temp_f*(reading_value_number-1)+temp_f)/reading_value_number;

		  //computing average humidity with past humidity values
		  average_hum = (average_hum*(reading_value_number-1)+humidity)/reading_value_number;
		  
		}
		if(reading_value_number == 10) {
		  //stop intervalObj as we have the required number of readings
		  clearInterval(intervalObj);
		  
		  //outputting lowest, highest, and average temperature and humidity values
		  console.log('Lowest Temp ' + lowest_temp_f.toFixed(1) + ' degF');
		  console.log('Lowest Hum '  + lowest_hum.toFixed(1) + '%');
		  console.log('Highest Temp ' + highest_temp_f.toFixed(1) + ' degF');
		  console.log('Highest Hum '  + highest_hum.toFixed(1) + '%');
		  console.log('Average Temp ' + average_temp_f.toFixed(1) + ' degF');
		  console.log('Average Hum '  + average_hum.toFixed(1) + '%');
		  
		}
	      });
}
	    
// run read_sensor function every 10 seconds - https://nodejs.org/en/docs/guides/timers-in-node/
const intervalObj = setInterval(read_sensor, 10000); 
