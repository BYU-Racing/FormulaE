/*
 * Created by David Reinhardt
 * Code to be uploaded to one of the Teensys to get them
 * to send Signals over CANBus
 * Goal: Receive a Signal over CAN and turn on an LED
 */
#include <Arduino.h>
#include <FlexCAN_T4.h>

#define LED 2
FlexCAN_T4<CAN3, RX_SIZE_256, TX_SIZE_16> receiver;

void canSniff(const CAN_message_t &msg) {

}

void setup() {
  //SETUP LED PIN
  pinMode(LED, OUTPUT);

  //TODO: SETUP CANBUS PINS
  Serial.begin(1152000); delay(400);
  receiver.begin();
  receiver.setClock(CLK_60MHz);
  receiver.onReceive(canSniff);
}

void loop() {
  if(0){ //TODO: MAKE THIS IF STATEMENT DEPEND ON SIGNALS COMING FROM THE CANBUS
    digitalWrite(LED, HIGH);
  }else{
    digitalWrite(LED, LOW);
  }

}