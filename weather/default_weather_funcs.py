import sys, os

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

import traci


# SNOW DEFAULT FUNCTIONS
def SnowChangeAccelD(weather_val, veh_id, param):
    if (weather_val <= 12.5):
        traci.vehicle.setAccel(veh_id, param)
    else:
        traci.vehicle.setAccel(veh_id, param / (0.08 * weather_val))


def SnowChangeDecelD(weather_val, veh_id, param):
    if (weather_val <= 12.5):
        traci.vehicle.setDecel(veh_id, param)
    else:
        traci.vehicle.setDecel(veh_id, param / (0.08 * weather_val))


def SnowChangeMaxSpeedD(weather_val, veh_id, param):
    if (weather_val <= 12.5):
        traci.vehicle.setMaxSpeed(veh_id, param)
    else:
        traci.vehicle.setMaxSpeed(veh_id, param / (0.08 * weather_val))


def SnowChangeMinGapD(weather_val, veh_id, param):
    traci.vehicle.setMinGap(veh_id, param * 0.1 * weather_val)


def SnowChangeSpeedD(weather_val, veh_id, param):
    traci.vehicle.setSpeedFactor(veh_id, 0.93)


def SnowChangeColorD(weather_val, veh_id, param):
    color_values = list(param)
    color_values[0] = 255
    color_values[1] = 0
    color_values[2] = 144
    traci.vehicle.setColor(veh_id, tuple(color_values))


# RAIN DEFAULT FUNCTIONS
def RainChangeAccelD(weather_val, veh_id, param):
    pass


def RainChangeDecelD(weather_val, veh_id, param):
    if weather_val <= 35:
        traci.vehicle.setDecel(veh_id, param * 0.95)
    elif weather_val <= 70:
        traci.vehicle.setDecel(veh_id, param * 0.85)
    else:
        traci.vehicle.setDecel(veh_id, param * 0.75)


def RainChangeMaxSpeedD(weather_val, veh_id, param):
    pass


def RainChangeMinGapD(weather_val, veh_id, param):
    pass


def RainChangeHeadwayTime(weather_val, veh_id, param):
    if weather_val <= 35:
        traci.vehicle.setTau(veh_id, param * 1.2)
    elif weather_val <= 70:
        traci.vehicle.setTau(veh_id, param * 1.5)
    else:
        traci.vehicle.setTau(veh_id, param * 2)


def RainChangeSpeedD(weather_val, veh_id, param):
    if weather_val <= 35:
        traci.vehicle.setSpeedFactor(veh_id, 0.96)
    elif weather_val <= 70:
        traci.vehicle.setSpeedFactor(veh_id, 0.92)
    else:
        traci.vehicle.setSpeedFactor(veh_id, 0.88)


def RainChangeColorD(weather_val, veh_id, param):
    color_values = list(param)
    color_values[0] /= 2
    color_values[1] /= 3
    color_values[2] = 255
    traci.vehicle.setColor(veh_id, tuple(color_values))
