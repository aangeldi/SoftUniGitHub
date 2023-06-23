#Import CANoe module
from py_canoe import CANoe
from time import sleep as wait
import calendar
import time


# create CANoe object
canoe_inst = CANoe()


canoe_inst.test_author("Dimitar Angelov", "dimitar.angelov@mercedes-benz.com")

      
# open CANoe configuration. Replace canoe_cfg with yours.
canoe_inst.open(canoe_cfg=r'C:\MBOS\Mastercheck_V182_intern\ConverterConfig.cfg')

canoe_inst.enable_write_window_output_file(r"C:\.py_canoe\write_out.txt")
wait(1)
canoe_inst.write_text_in_write_window(f"SAMO CSKA")

# print installed CANoe application version
canoe_inst.get_canoe_version_info()

# print User name
canoe_inst.get_username()

# pcheck_sw_hw_verssions
canoe_inst.check_sw_hw_verssions()



# # check SW verssion
# canoe_inst.sw_verssion(sw)

# # check HW verssion
# canoe_inst.hw_verssion(hw)



current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
canoe_inst.print_in_py_canoe(f"Current timestamp: {time_stamp}")


# # Start CANoe measurement
# canoe_inst.start_measurement()


# # get signal value. Replace arguments with your message and signal data.
# sig_val = canoe_inst.get_signal_value('CAN', 1, 'LightState', 'FlashLight')
# print(sig_val)

# # set signal value. Replace arguments with your message and signal data.
# canoe_inst.set_signal_value('CAN', 1, 'LightState', 'FlashLight', 1)

# # send diagnostic request. Replace arguments with your diagnostics data.
# resp = canoe_inst.send_diag_request('Door', '10 01')
# print(resp)




###########################################################################
#TestCase: Check Sequence counter
canoe_inst.check_sync_fup_SC(canoe_inst.send_sync_fup(1, 3, "ETH"))
###########################################################################


###########################################################################
#TestCase: Check CRCS

    
crc = canoe_inst.calculate_crc8x_fast("ETH", "CRC_Time_0", canoe_inst.send_sync_fup(1, 3, "ETH"))
print(f"Full Crc = 0x{crc:x}, dec = {crc}")

###########################################################################
 
 
#canoe_inst.test_case("Check values")
#canoe_inst.test_step("Check hex_value")
#canoe_inst.requirement("12345")
#canoe_inst.check_value("hex_value", hex_value,"0x80")


# # Stop CANoe Measurement
# canoe_inst.stop_measurement()