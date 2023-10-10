// TODO: Add class docstring

#ifndef SENSORDATA_H
#define SENSORDATA_H

#include <iostream>

class SensorData {
private:
    // Instantiate attributes
    int id;
    int priority;
    int* data;
    unsigned long timeStamp;

public:
    // Constructor
    SensorData();
    // CHECK change timeStamp to unsigned long
    SensorData(int id, int priority, int* data, unsigned long timeStamp);
    // CHECK change canMessage to CAN_message_t
    SensorData(CAN_message_t canMessage);

    // CHECK add destructor
    // Destructor
    ~SensorData();

    int getTimeStamp() const;
    int getId() const;
    int getPriority() const;
    int* getData() const;

    void setId(int id);
    void setPriority(int priority);
    void setData(int* data);
    // CHECK allow for setting timestamp
    void setTimeStamp(int timeStamp);

    // CHECK change output to CAN_message_t
    CAN_message_t formatCAN() const;
};

#endif // SENSORDATA_H