import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class power_system():
    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D8)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    def __init__(self):
        #for some reason when running, code did not recognize imported files - redundant placement seems to fix it
        '''import os
        import time
        import busio
        import digitalio
        import board
        import adafruit_mcp3xxx.mcp3008 as MCP
        from adafruit_mcp3xxx.analog_in import AnalogIn'''

        # create analog input channels on 5 pins on analog to digital converter (ADC)
        self.batt = AnalogIn(self.mcp, MCP.P0)
        self.panelXPlus = AnalogIn(self.mcp, MCP.P1)
        self.panelXMinus = AnalogIn(self.mcp, MCP.P2)
        self.panelYPlus = AnalogIn(self.mcp, MCP.P3)
        self.panelYMinus = AnalogIn(self.mcp, MCP.P4)

        #stores the initial voltage read at startup, will be used later for monitoring change in voltage
        self.startV = self.batt.voltage


    #return voltages as a float
    #battery should be between 3.3 and 4.2V, solar panels may produce anything more than 0.0V (but we only tested as high as ~6V)
    def getBattV(self):
        return 2 * self.batt.voltage
    def getPanelXPlusV(self):
        return 2 * self.panelXPlus.voltage
    def getPanelXMinusV(self):
        return 2 * self.panelXMinus.voltage
    def getPanelYPlusV(self):
        return 2 * self.panelYPlus.voltage
    def getPanelYMinusV(self):
        return 2 * self.panelYMinus.voltage

    #determines which panel produces the most voltage at current time, used for "sun-sensor" feature
    def mostV(self):
        volts = [self.getPanelXPlusV(),self.getPanelXMinusV(),self.getPanelYPlusV(),self.getPanelYMinusV()]
        index = 0
        maxV = 0
        for volt in volts:
            #print("comparison: " + str(volt) + "?> " + str(volts[maxV]))
            if volt > volts[maxV]:
                maxV = index
            index = index + 1
        return maxV + 1

    def getBattPercent(self):
        battP = self.getBattV()
        return (-6.7827687744) * (battP ** 7) + 131.855152886*(battP ** 6) - 974.187788027*(battP ** 5) + 2991.80245381*(battP ** 4) - 24198.6246108*(battP ** 2) + 59006.2602871*(battP) - 46129.135888

    #returns the voltages of all 5 devices in the format:
    #Battery voltage: _V
    #Panel 1 voltage: _V
    #Panel 2 voltage: _V
    #Panel 3 voltage: _V
    #Panel 4 voltage: _V
    def __repr__(self):
        return 'Battery voltage: ' + str(2 * self.batt.voltage) + 'V\nPanel 1 voltage: ' + str(2 * self.panel1.voltage) + 'V\nPanel 2 voltage: ' + str(2 * self.panel2.voltage) + 'V\nPanel 3 voltage: ' + str(2 * self.panel3.voltage) + 'V\nPanel 4 voltage: ' + str(2 * self.panel4.voltage) + 'V'

#more redundant package imports
'''import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn'''

#ps = PowerSystem()

#while(True):
    #time.sleep(1)
    #print(ps)
#print(ps.mostV())
