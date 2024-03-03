#ifndef DIGITALSENSOR_H
#define DIGITALSENSOR_H

#include "Sensor.h"
#include <Arduino.h>

class DigitalSensor : public Sensor {
private:
    // Additional attributes specific to DigitalSensor

    int sensorValue = 0;

public:
    // Constructor
    DigitalSensor(int id, int time, int pin);

    // Implement the pure virtual functions from the base class
    int readInputs() override;

    // Additional methods for DigitalSensor
    int getPins();
    int getWaitTime();
    int getDataLength();
    int getId();

    int rescale(int data);
    int* buildData(int value);
    int* buildError();
};

#endif // DIGITALSENSOR_H