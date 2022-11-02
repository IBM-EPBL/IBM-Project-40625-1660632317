/*Assignment 4:

//KUMAR A

//Reg_No:112819104018

//Write code and connections in wokwi for the ultrasonic sensor.

Whenever the distance is less than 100 cms send an "alert" to the IBM cloud and display in

the device recent events.

Upload document with wokwi share link and images of IBM cloud*/




// defines pins numbers

const int trigPin = 2;

const int echoPin = 5;

// defines variables

long duration;

int distance;

void setup() {

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output

  pinMode(echoPin, INPUT); // Sets the echoPin as an Input

  Serial.begin(9600); // Starts the serial communication

}

void loop() {

  // Clears the trigPin

  digitalWrite(trigPin, LOW);

  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds

  digitalWrite(trigPin, HIGH);

  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds

  duration = pulseIn(echoPin, HIGH);

  // Calculating the distance

  distance= duration*0.034/2;

  // Prints the distance on the Serial Monitor

  Serial.print("Distance: ");

  Serial.print(distance);

  Serial.println(" cm");

  if(distance <= 100){

    Serial.println("Alert Distance is less than 100 cm");

    

  }

}
