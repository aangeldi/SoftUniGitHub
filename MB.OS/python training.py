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


destination_mac = "0180C200000E" 
source_mac = "3CCE15000005" 
TPI = "8100" 
TCI = "E07F" #(User priority(3bits), Canonical format indicator(1 bit), VLAN ID(12 bits))
ether_type = "88F7"

#Sync message header: 
message_type = "10"
version_ptp = "02" 
message_length  = "002C" #44 
domain_number = "00"
reserved_1byte = "00"
flags = "0208"
correctionField = "0000000000000000"
reserved_4bytes = "00000000"
sourcePortIdentity = "3CCE15FFFE0000050001"
sequence_id = 0
logMessageInterval = "00FF" #255(0.5s)
reserved_10bytes = "00000000000000000000"


for seq_id in range(16, 22, 1):
    sequence_id = str(hex(seq_id))
    print(sequence_id)
    


gts_sync_message = ""
gts_message_hex = []

#0180C200000E  3CCE15000005 8100 E07F 88F7 10 02 00 2C 00 00 02 08 00 00 00 00 00 00 00 00 00 00 00 00 3C CE 15 FF FE 00 00 05 00 01 00 02 00 FF 00 00 00 00 00 00 00 00 00 00
#0180C200000E  3CCE15000005 8100 E07F 88F7 10 02 00 2C 00 00 02 08 00 00 00 00 00 00 00 00 00 00 00 00 3C CE 15 FF FE 00 00 05 00 01 00 03 00 FF 00 00 00 00 00 00 00 00 00 00

gts_sync_message = destination_mac + source_mac + TPI + TCI + ether_type + message_type + version_ptp + message_length + domain_number + reserved_1byte + flags + correctionField + reserved_4bytes + sourcePortIdentity + sequence_id + logMessageInterval + reserved_10bytes
canoe_inst.print_in_py_canoe(f"Message: 0x{gts_sync_message}")

hex_sign = "0x"
for i in range(0,len(gts_sync_message), 2):
    byte_value = (hex_sign + gts_sync_message[i] + gts_sync_message[i + 1])
    gts_message_hex.append(byte_value)
 
canoe_inst.print_in_py_canoe(f"Message:{gts_message_hex}")


#convert string to hex
an_integer = int(gts_message_hex[1], 16)
hex_value = hex(an_integer)
#convert hex to bin
bin_value = bin(int(hex_value, 16))[2:]
print(bin_value[0])
 
 
canoe_inst.test_case("Check values")
canoe_inst.test_step("Check hex_value")
canoe_inst.requirement("12345")
canoe_inst.check_value("hex_value", hex_value,"0x80")


# # Stop CANoe Measurement
# canoe_inst.stop_measurement()