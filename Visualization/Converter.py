import pandas as pd
from bitstring import BitArray
import numpy as np

import Config
from Config import *


"""
Assumptions:
1. Data is sent in IEEE 64 bit floating point binary representation
2. Time is sent as number of milliseconds since the start
3. We have control over how we encode data and timestamps
4. We have control over how we encode the entire signal (metadata)
5. CSV File has one signal per line and optionally one field per column
6. Signals follow CAN Bus Protocol Draft format

Corrections #TODO
1. Time is an unsigned long in milliseconds from power on
2. Data is a 2 byte ADC range from zero to max, unique for each sensor. Only the first 10 bits are meaningful
3. ID is an int from 0 to (total number of sensors)
4. Each run starts with a delimiter
5. Input file is a CSV
"""


def readData(filename):
    """
    Read data from a csv file filename into a dictionary
    Parameters:
        filename (string): name of the file to read
    Returns:
        all_data (dictionary): data from the csv stored, converted, and parsed in a dictionary

    CAN BUS Protocol
    1. Start of frame:  (1 bit)     Always 1. Denotes the start of frame transmission
    2. ID:              (11 bits)   A (unique) identifier which also represents the message priority
    3. Stuff bit:       (1 bit)     A bit of the opposite polarity to maintain synchronisation
    4. IDE:             (1 bit)     Identifier extension bit. Must be dominant (0)
    5. Reserved bit     (1 bit)     Reserved bit. Must be dominant (0)
    6. Message length:  (4 bits)    Number of bytes of data (0–8 bytes)
    7. Timestamp:       (16 bits)   Timestamp (number of milliseconds from start)
    7. Data field:      (8-64 bits) 1-8 bytes. Data to be transmitted (length in bytes dictated by DLC field)
    8. CRC:             (15 bits)   Cyclic redundancy check
    9. CRC delimiter:   (1 bit)     Must be recessive (1)
    10. ACK slot:       (1 bit)     Transmitter sends recessive (1) and any receiver can assert a dominant (0)
    11. ACK delimiter:  (1 bit)     Must be recessive (1)
    12. End-of-frame:   (1 bit)     (EOF) Must be recessive (1)
    13. IFS:            (3 bits)    Inter-frame spacing. Must be recessive (1)
    Total Signal:       (65-121 bits)

    Toy Signal
    1. ID (11 bits)
    2. Timestamp (16 bits)
    3. Data (64 bits)
    Total: 91 bits
    """

    # read data
    df = pd.read_csv(filename, sep=',', usecols=['ID', 'Timestamp', 'Data'])

    # convert from binary to decimal
    df['ID'] = convertID(df['ID'])
    df['Timestamp'] = convertTime(df['Timestamp'])
    df['Data'] = convertData(df['Data'])

    # construct
    all_data = {}
    for i in range(len(sensors)):
        all_data.update({i: df[df["ID"] == sensors[i]]})

    # return all the data in the csv
    return all_data


def parseBits(signals):
    """
    Check a binary string to make sure it matches the CANBus format, then turn it into a dataframe
    Parameters:
        signals (list): list of strings of binary digits
    Returns:
        processed (dataframe): data parsed into rows and columns
    """
    protocol = [['Start of frame', 1],
                ['ID', 11],
                ['Stuff bit', 1],
                ['IDE', 1],
                ['Reserved bit', 1],
                ['Message length', 4],
                ['Timestamp', 16],
                ['Data field', 64],
                ['CRC', 15],
                ['CRC delimiter', 1],
                ['ACK slot', 1],
                ['ACK delimiter', 1],
                ['EOF', 1],
                ['IFS', 3],
                ['Total', 121], ]

    processed = []
    for signal in signals:

        # check data type
        if type(signal) is not str:
            raise TypeError(f"Signal is not of type string. Instead received {type(signal)}."
                            f"\nSignal: {signal}")

        # check signal length
        if len(signal) != protocol[-1][1]:
            raise ValueError(f"Signal is not the right length. Expected {protocol[-1][1]} but received {len(signal)}."
                             f"\nSignal: {signal}")

        # create a list of signals divided into fields
        parsed = []
        for field in protocol[:-1]:
            parsed.append(signal[:field[1]])
            signal = signal[field[1]:]
        processed.append(parsed)

    # return the full data frame
    return pd.DataFrame(processed)


def convertTime(timestamp):
    """
    Convert binary timestamp into human-readable text
    Parameters:
        timestamp (string or dataframe): time as a string of binary digits
    Returns:
        time (int or dataframe): formatted time
    """
    # case if parameter is a string
    if type(timestamp) is str:
        return int(str(timestamp), 2) / 1000.

    # case if parameter is a dataframe
    return pd.DataFrame([int(str(time), 2) / 1000. for time in timestamp])


def convertID(id_sensor):
    """
    Convert a binary ID into an integer
    Parameters:
        id_sensor (string or dataframe of strings): sensor id in binary
    Returns:
        id (int or dataframe of ints): sensor id in decimal
    """
    # case if parameter is a string
    if type(id_sensor) is str:
        return sensors[int(str(id_sensor), 2)]

    # case if parameter is a dataframe
    return pd.DataFrame([sensors[int(str(i), 2)] for i in id_sensor])


def convertData(data):
    # TODO update data conversion for 12 bit data
    """
    Convert binary data into a float
    Parameters:
        data (string or dataframe of strings): data in binary as a string
    Returns:
        data (int or dataframe of ints): data in decimal
    """
    # case if parameter is a string
    if type(id) is str:
        return BitArray(bin=str(data)).float

    # case if parameter is a dataframe
    return pd.DataFrame([BitArray(bin=str(d)).float for d in data])


def convert_position(speed, time, angle):
    """
    Convert timestamped speed and steering wheel angle to current
    track position.
    :param speed: (list) a list of speeds in miles per hour as floats
    :param time: (list) as list of timestamps in seconds as floats
    :param angle: (list) a list of wheel angles in degrees as floats
    :return: x and y positions (list, list) of floats
    """
    # convert MPH to MPS and make distance traveled per second
    distance = [s * 0.000278 * t for s, t in zip(speed, time)]
    theta = 0
    x = 0
    y = 0

    x_val = [0] * len(distance)
    y_val = [0] * len(distance)
    angle = [np.deg2rad(a) for a in angle]

    for i in range(len(distance)):
        theta += angle[i]

        x += distance[i] * np.cos(theta)
        x_val[i] = x

        y += distance[i] * np.sin(theta)
        y_val[i] = y

    return x_val, y_val


def convert_sensor_data(sensor, data):
    """
    Convert raw sensor data to a float accounting for weights and biases
    :param sensor: (string) the name of the sensor
    :param data: (int) the raw data from the sensor
    :return: (float) the converted data
    """
    weight = "W_" + sensor
    bias = "B_" + sensor
    return (data - Config.biases[bias]) * Config.weights[weight]