// TODO doc string
#include "AnalogSensor.h"

//Constructor
AnalogSensor::AnalogSensor(int id, int freq, int prio, int* inPins){
    int sensorID = id;
    int waitTime = freq;
    int priority = prio;
    int* inputPins = {inPins};
    int sensorValue = 0;
};

//readInputs
int* AnalogSensor::readInputs() {

    //Update previous update time
    previousUpdateTime = millis();

    //Grab Sensor Value
    sensorValue = analogRead(inputPins[0]);

    //Return a pointer to the private value
    return &sensorValue;
    
};


//readyToCheck
bool AnalogSensor::readyToCheck() {
    //millis gets arduino time
    return (waitTime <= millis() - previousUpdateTime);
};