#include "SensorData.h"
// TODO: add docstrings for each method

SensorData::SensorData() {
    id = 0;
    priority = 0;
    data = {0};
    timeStamp = 0;
}

SensorData::SensorData(int inId, int inPriority, int* inData, unsigned long inTimeStamp) {
    id = inId;
    priority = inPriority;
    data = inData;
    timeStamp = inTimeStamp;
}

// TODO: Implement this method
SensorData::SensorData(CAN_Message_t canMessage) {
    //Need can message template to know where to find each attribute
}

int SensorData::getTimeStamp() const {
    return timeStamp;
}

int SensorData::getId() const {
    return id;
}

int SensorData::getPriority() const {
    return priority;
}

int* SensorData::getData() const {
    return data;
}

void SensorData::setId(int inId) {
    id = inId;
}

void SensorData::setPriority(int inPriority) {
    priority = inPriority;
}

void SensorData::setData(int* inData) {
    data = inData;
}

// CHECK: Implement this method
void SensorData::setTimeStamp(int inTimeStamp) {
    timeStamp = inTimeStamp;
}

// TODO: Implement this method
std::string SensorData::formatCAN() const {
    return "";
}