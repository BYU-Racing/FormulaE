// TODO: Add doc string


#ifndef SENSOR_H
#define SENSOR_H

#include "../SensorID.h"

class Sensor {
protected:
    // Instantiate attributes
    int* inputPins;
    int waitTime;
    unsigned long previousUpdateTime = 0;
    int sensorID;
    int priority;

public:
    // Constructor
    Sensor(int id, int freq, int prio, int* inputPins);

    // Destructor
    virtual ~Sensor();  // Make the destructor virtual

    // Declare a pure virtual function
    virtual int* readInputs() = 0;

    // Method to check if it's ready to read
    virtual bool readyToCheck() = 0;
};

#endif // SENSOR_H
