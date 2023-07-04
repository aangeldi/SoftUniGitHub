"""Python package for controlling Vector CANoe tool"""

__version__ = "0.0.9"

# Import Python Libraries here
import os
import sys
import logging
import pythoncom
import win32com.client
from typing import Union
from logging import handlers
from time import sleep as wait
import calendar
import time
from tkinter import *
import re



class CANoe:
    
    r"""The CANoe class represents the CANoe application.
    The CANoe class is the foundation for the object hierarchy.
    You can reach all other methods from the CANoe class instance.

    Examples:
        >>> # Example to open CANoe configuration, start measurement, stop measurement and close configuration.
        >>> canoe_inst = CANoe(py_canoe_log_dir=r'D:\.py_canoe')
        >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
        >>> canoe_inst.start_measurement()
        >>> wait(10)
        >>> canoe_inst.stop_measurement()
        >>> canoe_inst.quit()
    """

    def __init__(self, py_canoe_log_dir=r'C:\.py_canoe') -> None:
        """
        Args:
            py_canoe_log_dir (str): directory to store py_canoe log. default 'D:\\.py_canoe'
        """
        self.failed_reqs = [4, 5]
        self.__canoe_app_obj = None
        self.__CANOE_COM_APP_NAME = 'CANoe.Application'
        self.__BUS_TYPES = {'CAN': 1, 'J1939': 2, 'TTP': 4, 'LIN': 5, 'MOST': 6, 'Kline': 14}
        self.APP_DELAY = 1
        self.log = logging.getLogger('CANOE_LOG')
        self.__py_canoe_log_initialisation(py_canoe_log_dir)
        self.__sys_vars_obj_dictionary = {}
        self.__networks_obj_dictionary = {}
        self.__network_devices_obj_dictionary = {}
        self.__diag_ecu_qualifiers_dictionary = {}
        self.__replay_blocks_obj_dictionary = {}
        self.__simulation_nodes_obj_dictionary = {}
        self.CRC_Time_0 = 0
        self.prec_origin_timestamp_1 = 0
        self.prec_origin_timestamp_2 = 0
        self.prec_origin_timestamp_3 = 0
        self.prec_origin_timestamp_4 = 0
        self.prec_origin_timestamp_5 = 0
        self.prec_origin_timestamp_6 = 0
        self.prec_origin_timestamp_7 = 0
        self.prec_origin_timestamp_8 = 0
        self.prec_origin_timestamp_9 = 0
        self.prec_origin_timestamp_10 = 0
        self.data_id = 00
        self.data_crc = 00
        self.crc_time_0 = 00
        self.crc_time_1 = "00"
        self.gts_sync_message = ""
        self.gts_fup_message = ""
        self.sync_fup_data = {"sync":[], "fup":[]}
        self.destination_mac = "0180C200000E" 
        self.source_mac = "3CCE150000C5" 
        self.tpi = "8100" 
        self.tci = "E07F" #(user priority(3bits), canonical format indicator(1 bit), vlan id(12 bits))
        self.ether_type = "88F7"
        self.message_type_sync = "10"
        self.message_type_fup = "18"
        self.version_ptp = "02" 
        self.message_length_sync  = "002C" #44 
        self.message_length_fup  = "0066" #102
        self.domain_number = "00"
        self.reserved_1byte = "00"
        self.flags_sync = "0208"
        self.flags_fup = "0008"
        self.correctionfield = "0000000000000000"
        self.reserved_4bytes = "00000000"
        self.sourceportidentity = "3CCE15FFFE0000050001"
        self.sequence_id = ""
        self.control_sync = "00"
        self.control_fup = "02"
        self.logmessageinterval = "FF" #255(0.5s)
        self.reserved_10bytes = "00000000000000000000"
        #Follow_Up information TLV [IEEE 802.1AS]
        self.tlv_type1 = "0003"
        self.length_field1 = "001C"
        self.organization_id1 = "0080C2"
        self.organization_sub_type1 = "000001"
        self.cumulative_scaled_rate_offset  = "00000001"
        self.gm_time_base_indicator  = "0000"
        self.last_gm_phase_change = "000000000000000000000000"
        self.caled_last_gm_freq_change = "00000000"

        #Follow_Up information TLV [AUTOSAR]
        self.tlv_type2 = "0003"
        self.length_field2 = "0016"
        self.organization_id2 = "1A75FB"
        self.organization_sub_type2 = "605676"

        #AUTOSAR TLV Sub-TLV:Status Secured
        self.type_status_secured = "50"
        self.length_status_secured = "02"
        self.status = "00"
        self.crc_status = "A9"

        #AUTOSAR TLV Sub-TLV:UserData Secured
        self.type_user_data_secured = "60"
        self.length = "05"
        self.user_data_length = "01"
        self.user_byte_0 = "20"
        self.user_byte_1 = "00"
        self.user_byte_2 = "00"
        self.crc_user_data = "E2"

        self.type_time_secured = "28"
        self.length_time_secured = "03"
        self.crc_time_flags = "37"
        self.hex_sign = "0x"         
        self.sec = 10

        self.ETHDataId = [
        [204, 214, 224, 234, 244, 3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103],    # [CC,D6,E0,EA,F4,03,0D,17,21,2B,35,3F,49,53,5D,67]	time domain 0
        None,  # time domain 1
        None,  # time domain 2
        None,  # time domain 3
        [0x1A, 0x96, 0x17, 0x93, 0x14, 0x90, 0x11, 0x8D, 0x0E, 0x8A, 0x0B, 0x87, 0x08, 0x84, 0x05, 0x81],  # [1A,96,17,93,14,90,11,8D,0E,8A,0B,87,08,84,05,81]	time domain 4
        [0x71, 0x66, 0x5B, 0x50, 0x45, 0x3A, 0x2F, 0x24, 0x19, 0x0E, 0x03, 0xF3, 0xE8, 0xDD, 0xD2, 0xC7],  # [71,66,5B,50,45,3A,2F,24,19,0E,03,F3,E8,DD,D2,C7]	time domain 5
        [0xA0, 0x19, 0x8D, 0x06, 0x7A, 0xEE, 0x67, 0xDB, 0x54, 0xC8, 0x41, 0xB5, 0x2E, 0xA2, 0x1B, 0x8F],  # [A0,19,8D,06,7A,EE,67,DB,54,C8,41,B5,2E,A2,1B,8F]	time domain 6
        [0x12, 0xFC, 0xEB, 0xDA, 0xC9, 0xB8, 0xA7, 0x96, 0x85, 0x74, 0x63, 0x52, 0x41, 0x30, 0x1F, 0x0E],  # [12,FC,EB,DA,C9,B8,A7,96,85,74,63,52,41,30,1F,0E]	time domain 7
        [0x41, 0x0D, 0xD4, 0xA0, 0x6C, 0x38, 0x04, 0xCB, 0x97, 0x63, 0x2F, 0xF6, 0xC2, 0x8E, 0x5A, 0x26],  # [41,0D,D4,A0,6C,38,04,CB,97,63,2F,F6,C2,8E,5A,26]	time domain 8
        [0x09, 0x6D, 0xD1, 0x3A, 0x9E, 0x07, 0x6B, 0xCF, 0x38, 0x9C, 0x05, 0x69, 0xCD, 0x36, 0x9A, 0x03],  # [09,6D,D1,3A,9E,07,6B,CF,38,9C,05,69,CD,36,9A,03]	time domain 9
        [0xDA, 0x4E, 0xBD, 0x31, 0xA0, 0x14, 0x83, 0xF2, 0x66, 0xD5, 0x49, 0xB8, 0x2C, 0x9B, 0x0F, 0x7E],  # [DA,4E,BD,31,A0,14,83,F2,66,D5,49,B8,2C,9B,0F,7E]	time domain 10
        [0xA1, 0x40, 0xDA, 0x79, 0x18, 0xB2, 0x51, 0xEB, 0x8A, 0x29, 0xC3, 0x62, 0xFC, 0x9B, 0x3A, 0xD4],  # [A1,40,DA,79,18,B2,51,EB,8A,29,C3,62,FC,9B,3A,D4]	time domain 11
        [0xFA, 0x8B, 0x1C, 0xA8, 0x39, 0xC5, 0x56, 0xE2, 0x73, 0x04, 0x90, 0x21, 0xAD, 0x3E, 0xCA, 0x5B],  # [FA,8B,1C,A8,39,C5,56,E2,73,04,90,21,AD,3E,CA,5B]	time domain 12
        [0x6C, 0x8D, 0xAE, 0xCF, 0xF0, 0x16, 0x37, 0x58, 0x79, 0x9A, 0xBB, 0xDC, 0xFD, 0x23, 0x44, 0x65],  # [6C,8D,AE,CF,F0,16,37,58,79,9A,BB,DC,FD,23,44,65]	time domain 13
        [0xFB, 0x24, 0x48, 0x6C, 0x90, 0xB4, 0xD8, 0xFC, 0x25, 0x49, 0x6D, 0x91, 0xB5, 0xD9, 0xFD, 0x26],  # [FB,24,48,6C,90,B4,D8,FC,25,49,6D,91,B5,D9,FD,26]	time domain 14
        [0x1B, 0x0E, 0xFC, 0xEF, 0xE2, 0xD5, 0xC8, 0xBB, 0xAE, 0xA1, 0x94, 0x87, 0x7A, 0x6D, 0x60, 0x53]   # [1B,0E,FC,EF,E2,D5,C8,BB,AE,A1,94,87,7A,6D,60,53]	time domain 15
        ]

        self.FRDataId = [
        [209, 133, 57, 232, 156, 80, 4, 179, 103, 27, 202, 126, 50, 225, 149, 73],              # [D1,85,39,E8,9C,50,04,B3,67,1B,CA,7E,32,E1,95,49]	time domain 0
        None,      # time domain 1
        [0xCC, 0xE3, 0xFA, 0x16, 0x2D, 0x44, 0x5B, 0x72, 0x89, 0xA0, 0xB7, 0xCE, 0xE5, 0xFC, 0x18, 0x2F] # [CC,E3,FA,16,2D,44,5B,72,89,A0,B7,CE,E5,FC,18,2F]	time domain 2 (PT)
        ]

        self.CANDataId_SYNC = [
        [225, 102, 230, 107, 235, 112, 240, 117, 245, 122, 250, 127, 4, 132, 9, 137],  # [E1,66,E6,6B,EB,70,F0,75,F5,7A,FA,7F,04,84,09,89]	time domain 0
        None,       # time domain 1
        [0x89, 0x4C, 0x0F, 0xCD, 0x90, 0x53, 0x16, 0xD4, 0x97, 0x5A, 0x1D, 0xDB, 0x9E, 0x61, 0x24, 0xE2]  # [89,4C,0F,CD,90,53,16,D4,97,5A,1D,DB,9E,61,24,E2]	time domain 2 (PT)
        ]

        self.CANDataId_FUP = [
        [143, 78, 13, 199, 134, 69, 4, 190, 125, 60, 246, 181, 116, 51, 237, 172],      # [8F,4E,0D,C7,86,45,04,BE,7D,3C,F6,B5,74,33,ED,AC]	time domain 0
        None,     # time domain 1
        [0x7F, 0xE5, 0x50, 0xB6, 0x21, 0x87, 0xED, 0x58, 0xBE, 0x29, 0x8F, 0xF5, 0x60, 0xC6, 0x31, 0x97]  # [7F,E5,50,B6,21,87,ED,58,BE,29,8F,F5,60,C6,31,97]	time domain 2 (PT)
        ]

         # *****************************************************************************
        # * Generated on Thu Feb 11 12:46:28 2016,
        # * by pycrc v0.8.1, http://www.tty1.net/pycrc/
        # * using the configuration:
        # *    Width        = 8
        # *    Poly         = 0x2f
        # *    XorIn        = 0xff
        # *    ReflectIn    = False
        # *    XorOut       = 0xff
        # *    ReflectOut   = False
        # *    Algorithm    = table-driven
        # *
        # * Static table used for the table_driven implementation.
        # *****************************************************************************
        self.crc8x_table = [
        0x00, 0x2f, 0x5e, 0x71, 0xbc, 0x93, 0xe2, 0xcd, 0x57, 0x78, 0x09, 0x26, 0xeb, 0xc4, 0xb5, 0x9a,
        0xae, 0x81, 0xf0, 0xdf, 0x12, 0x3d, 0x4c, 0x63, 0xf9, 0xd6, 0xa7, 0x88, 0x45, 0x6a, 0x1b, 0x34,
        0x73, 0x5c, 0x2d, 0x02, 0xcf, 0xe0, 0x91, 0xbe, 0x24, 0x0b, 0x7a, 0x55, 0x98, 0xb7, 0xc6, 0xe9,
        0xdd, 0xf2, 0x83, 0xac, 0x61, 0x4e, 0x3f, 0x10, 0x8a, 0xa5, 0xd4, 0xfb, 0x36, 0x19, 0x68, 0x47,
        0xe6, 0xc9, 0xb8, 0x97, 0x5a, 0x75, 0x04, 0x2b, 0xb1, 0x9e, 0xef, 0xc0, 0x0d, 0x22, 0x53, 0x7c,
        0x48, 0x67, 0x16, 0x39, 0xf4, 0xdb, 0xaa, 0x85, 0x1f, 0x30, 0x41, 0x6e, 0xa3, 0x8c, 0xfd, 0xd2,
        0x95, 0xba, 0xcb, 0xe4, 0x29, 0x06, 0x77, 0x58, 0xc2, 0xed, 0x9c, 0xb3, 0x7e, 0x51, 0x20, 0x0f,
        0x3b, 0x14, 0x65, 0x4a, 0x87, 0xa8, 0xd9, 0xf6, 0x6c, 0x43, 0x32, 0x1d, 0xd0, 0xff, 0x8e, 0xa1,
        0xe3, 0xcc, 0xbd, 0x92, 0x5f, 0x70, 0x01, 0x2e, 0xb4, 0x9b, 0xea, 0xc5, 0x08, 0x27, 0x56, 0x79,
        0x4d, 0x62, 0x13, 0x3c, 0xf1, 0xde, 0xaf, 0x80, 0x1a, 0x35, 0x44, 0x6b, 0xa6, 0x89, 0xf8, 0xd7,
        0x90, 0xbf, 0xce, 0xe1, 0x2c, 0x03, 0x72, 0x5d, 0xc7, 0xe8, 0x99, 0xb6, 0x7b, 0x54, 0x25, 0x0a,
        0x3e, 0x11, 0x60, 0x4f, 0x82, 0xad, 0xdc, 0xf3, 0x69, 0x46, 0x37, 0x18, 0xd5, 0xfa, 0x8b, 0xa4,
        0x05, 0x2a, 0x5b, 0x74, 0xb9, 0x96, 0xe7, 0xc8, 0x52, 0x7d, 0x0c, 0x23, 0xee, 0xc1, 0xb0, 0x9f,
        0xab, 0x84, 0xf5, 0xda, 0x17, 0x38, 0x49, 0x66, 0xfc, 0xd3, 0xa2, 0x8d, 0x40, 0x6f, 0x1e, 0x31,
        0x76, 0x59, 0x28, 0x07, 0xca, 0xe5, 0x94, 0xbb, 0x21, 0x0e, 0x7f, 0x50, 0x9d, 0xb2, 0xc3, 0xec,
        0xd8, 0xf7, 0x86, 0xa9, 0x64, 0x4b, 0x3a, 0x15, 0x8f, 0xa0, 0xd1, 0xfe, 0x33, 0x1c, 0x6d, 0x42
        ]




    def __py_canoe_log_initialisation(self, py_canoe_log_dir=r'C:\.py_canoe'):
        if not os.path.exists(py_canoe_log_dir):
            os.makedirs(py_canoe_log_dir, exist_ok=True)
        self.log.setLevel(logging.DEBUG)
        log_format = logging.Formatter("%(asctime)s [CANOE_LOG] [%(levelname)-5.5s]  %(message)s")
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(log_format)
        self.log.addHandler(ch)
        fh = handlers.RotatingFileHandler(fr'{py_canoe_log_dir}\py_canoe.log', maxBytes=(1024 * 50), backupCount=20)
        fh.setFormatter(log_format)
        self.log.addHandler(fh)

    def __dispatch_canoe(self) -> None:
        if self.__canoe_app_obj is None:
            pythoncom.CoInitialize()
            self.__canoe_app_obj = win32com.client.Dispatch(self.__CANOE_COM_APP_NAME)
            self.log.info('Dispatched CANoe win32com client.')
        else:
            self.log.info('CANoe win32com client already Dispatched')

    def __fetch_canoe_cfg_general_data(self):
        system_namespaces_obj = self.__canoe_app_obj.System.Namespaces
        self.__ui_obj = self.__canoe_app_obj.UI
        # self.__version_obj = self.__canoe_app_obj.Version

        def fetch_variables(namespace_obj, namespace_name):
            variables_obj = namespace_obj.Variables
            for variable_obj in variables_obj:
                variable_name = f"{namespace_name}::{variable_obj.Name}"
                self.__sys_vars_obj_dictionary[variable_name] = variable_obj

        def fetch_namespaces(namespace_obj, obj_name):
            fetch_variables(namespace_obj, obj_name)
            for ns in namespace_obj.Namespaces:
                fetch_namespaces(ns, f'{obj_name}::{ns.Name}')

        for namespace in system_namespaces_obj:
            fetch_namespaces(namespace, namespace.Name)
        for n in self.__canoe_app_obj.Networks:
            self.__networks_obj_dictionary[n.Name] = n
            self.__network_devices_obj_dictionary[n.Name] = {}
            for d in n.Devices:
                self.__network_devices_obj_dictionary[n.Name][d.Name] = d
                try:
                    self.__diag_ecu_qualifiers_dictionary[d.Name] = d.Diagnostic
                except pythoncom.com_error:
                    pass
        for rb in self.__canoe_app_obj.Bus.ReplayCollection:
            self.__replay_blocks_obj_dictionary[rb.Name] = rb
        for sn in self.__canoe_app_obj.Configuration.SimulationSetup.Nodes:
            self.__simulation_nodes_obj_dictionary[sn.Name] = sn

    def open(self, canoe_cfg: str, visible=True, auto_save=False, prompt_user=False) -> None:
        r"""Loads CANoe configuration.

        Args:
            canoe_cfg (str): The complete path for the CANoe configuration.
            visible (bool): True if you want to see CANoe UI. Defaults to True.
            auto_save (bool, optional): A boolean value that indicates whether the active configuration should be saved if it has been changed. Defaults to False.
            prompt_user (bool, optional): A boolean value that indicates whether the user should intervene in error situations. Defaults to False.
        
        Examples:
            >>> # The following example opens a configuration
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
        """
        if os.path.isfile(canoe_cfg):
            self.log.info(f'CANoe cfg "{canoe_cfg}" found.')
            self.__dispatch_canoe()
            self.__canoe_app_obj.Visible = visible
            self.__canoe_app_obj.Open(canoe_cfg, auto_save, prompt_user)
            self.log.info(f'loaded CANoe config "{canoe_cfg}"')
            self.__fetch_canoe_cfg_general_data()
            self.log.info('Fetched CANoe System Variables.')
        else:
            self.log.info(f'CANoe cfg "{canoe_cfg}" not found.')

    def new(self, auto_save=False, prompt_user=False) -> None:
        """Creates a new configuration.

        Args:
            auto_save (bool, optional): A boolean value that indicates whether the active configuration should be saved if it has been changed. Defaults to False.
            prompt_user (bool, optional): A boolean value that indicates whether the user should intervene in error situations. Defaults to False.
        
        Examples:
            >>> # The following example creates a new configuration
            >>> canoe_inst = CANoe()
            >>> canoe_inst.new()
        """
        self.__dispatch_canoe()
        self.__canoe_app_obj.New(auto_save, prompt_user)
        self.log.info('created a new configuration')

    def quit(self) -> None:
        r"""Quits CANoe without saving changes in the configuration.
        
        Examples:
            >>> # The following example quits CANoe
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.quit()
        """
        if self.__canoe_app_obj.Measurement.Running:
            self.stop_measurement()
        self.__canoe_app_obj.Configuration.Modified = False
        self.__canoe_app_obj.Quit()
        self.log.info('CANoe Closed without saving.')

    def start_measurement_in_animation_mode(self, animation_delay=100) -> None:
        r"""Starts the measurement in Animation mode.

        Args:
            animation_delay (int): The animation delay during the measurement in Offline Mode.

        Examples:
            >>> # The following example starts the measurement in Animation mode
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement_in_animation_mode()
        """
        if not self.__canoe_app_obj.Measurement.Running:
            self.__canoe_app_obj.Measurement.AnimationDelay = animation_delay
            self.__canoe_app_obj.Measurement.Animate()
            self.log.info(f'Started the measurement in Animation mode with animation delay = {animation_delay}.')

    def break_measurement_in_offline_mode(self) -> None:
        r"""Interrupts the playback in Offline mode.

        Examples:
            >>> # The following example interrupts the playback in Offline mode
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.break_measurement_in_offline_mode()
        """
        if self.__canoe_app_obj.Measurement.Running:
            self.__canoe_app_obj.Measurement.Break()
            self.log.info('Interrupted the playback in Offline mode.')

    def reset_measurement_in_offline_mode(self) -> None:
        r"""Resets the measurement in Offline mode.

        Examples:
            >>> # The following example resets the measurement in Offline mode
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.reset_measurement_in_offline_mode()
        """
        self.__canoe_app_obj.Measurement.Reset()
        self.log.info('resetted measurement in offline mode.')

    def start_measurement(self) -> bool:
        r"""Starts the measurement.

        Returns:
            True if measurement started. else Flase.

        Examples:
            >>> # The following example starts the measurement
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
        """
        if not self.__canoe_app_obj.Measurement.Running:
            self.__canoe_app_obj.Measurement.Start()
            if not self.__canoe_app_obj.Measurement.Running:
                self.log.info(f'waiting({self.APP_DELAY}s) for measurement to start running.')
                wait(self.APP_DELAY)
            self.log.info(f'CANoe Measurement Running Status: {self.__canoe_app_obj.Measurement.Running}')
        return self.__canoe_app_obj.Measurement.Running

    def step_measurement_event_in_single_step(self) -> None:
        r"""Processes a measurement event in single step.

        Examples:
            >>> # The following example processes a measurement event in single step
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.step_measurement_event_in_single_step()
        """
        if not self.__canoe_app_obj.Measurement.Running:
            self.__canoe_app_obj.Measurement.Step()
            self.log.info('processed a measurement event in single step')

    def stop_measurement(self) -> bool:
        r"""Stops the measurement.

        Returns:
            True if measurement stopped. else Flase.

        Examples:
            >>> # The following example stops the measurement
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.stop_measurement()
        """
        if self.__canoe_app_obj.Measurement.Running:
            self.__canoe_app_obj.Measurement.Stop()
            for i in range(5):
                if self.__canoe_app_obj.Measurement.Running:
                    self.log.info(f'CANoe Simulation still running. waiting for {self.APP_DELAY} seconds.')
                    wait(self.APP_DELAY)
                else:
                    break
        self.log.info(f'Triggered stop measurement. Measurement running status = {self.__canoe_app_obj.Measurement.Running}')
        return not self.__canoe_app_obj.Measurement.Running

    def reset_measurement(self) -> bool:
        r"""reset the measurement.

        Returns:
            Measurement running status(True/False).

        Examples:
            >>> # The following example resets the measurement
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.reset_measurement()
        """
        if self.__canoe_app_obj.Measurement.Running:
            self.stop_measurement()
        self.start_measurement()
        self.log.info(f'Resetted measurement. Measurement running status = {self.__canoe_app_obj.Measurement.Running}')
        return self.__canoe_app_obj.Measurement.Running

    def stop_ex_measurement(self) -> None:
        r"""StopEx repairs differences in the behavior of the Stop method on deferred stops concerning simulated and real mode in CANoe.

        Examples:
            >>> # The following example full stops the measurement
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.stop_ex_measurement()
        """
        if self.__canoe_app_obj.Measurement.Running:
            self.__canoe_app_obj.Measurement.StopEx()
            self.log.info(f'Stopped measurement. Measurement running status = {self.__canoe_app_obj.Measurement.Running}')

    def get_measurement_index(self) -> int:
        r"""gets the measurement index for the next measurement.

        Returns:
            Measurement Index.

        Examples:
            >>> # The following example gets the measurement index measurement
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.stop_measurement()
            >>> canoe_inst.get_measurement_index()
        """
        return self.__canoe_app_obj.Measurement.MeasurementIndex

    def set_measurement_index(self, index: int) -> int:
        r"""sets the measurement index for the next measurement.

        Args:
            index (int): index value to set.

        Returns:
            Measurement Index value.

        Examples:
            >>> # The following example sets the measurement index for the next measurement to 15
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.stop_measurement()
            >>> canoe_inst.set_measurement_index(15)
        """
        self.__canoe_app_obj.Measurement.MeasurementIndex = index
        self.log.info(f'CANoe measurement index set to {index}')
        return self.__canoe_app_obj.Measurement.MeasurementIndex

    def get_measurement_running_status(self) -> bool:
        r"""Returns the running state of the measurement.

        Returns:
            True if The measurement is running.
            False if The measurement is not running.

        Examples:
            >>> # The following example returns measurement running status (True/False)
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.get_measurement_running_status()
        """
        self.log.info(f'CANoe Measurement Running Status = {self.__canoe_app_obj.Measurement.Running}')
        return self.__canoe_app_obj.Measurement.Running

    def save_configuration(self) -> bool:
        r"""Saves the configuration.

        Returns:
            True if configuration saved. else False.

        Examples:
            >>> # The following example saves the configuration if necessary
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.save_configuration()
        """
        if not self.__canoe_app_obj.Configuration.Saved:
            self.__canoe_app_obj.Configuration.Save()
            self.log.info('CANoe Configuration saved.')
        return self.__canoe_app_obj.Configuration.Saved

    def save_configuration_as(self, path: str, major: int, minor: int) -> bool:
        r"""Saves the configuration as a different CANoe version.

        Args:
            path (str): The complete file name.
            major (int): The major version number of the target version.
            minor (int): The minor version number of the target version.

        Returns:
            True if configuration saved. else False.

        Examples:
            >>> # The following example saves the configuration as a CANoe 10.0 version
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.save_configuration_as(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo_v12.cfg', 10, 0)"""
        if not self.__canoe_app_obj.Configuration.Saved:
            self.__canoe_app_obj.Configuration.Save()
        self.__canoe_app_obj.Configuration.SaveAs(path, major, minor)
        self.log.info(f'CANoe Configuration saved as {path}.')
        return self.__canoe_app_obj.Configuration.Saved

    def get_signal_value(self, bus: str, channel: int, message: str, signal: str, raw_value=False) -> Union[float, int]:
        r"""get_signal_value Returns a Signal value.

        Args:
            bus (str): The Bus(CAN, LIN, FlexRay, MOST, AFDX, Ethernet)(CAN, LIN, FlexRay, MOST, AFDX, Ethernet) on which the signal is sent.
            channel (int): The channel on which the signal is sent.
            message (str): The name of the message to which the signal belongs.
            signal (str): The name of the signal.
            raw_value (bool): return raw value of the signal if true. Default(False) is physical value.

        Returns:
            signal vaue.

        Examples:
            >>> # The following example gets signal value
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> sig_val = canoe_inst.get_signal_value('CAN', 1, 'LightState', 'FlashLight')
            >>> print(sig_val)
        """
        signal_obj = self.__canoe_app_obj.GetBus(bus).GetSignal(channel, message, signal)
        signal_value = signal_obj.RawValue if raw_value else signal_obj.Value
        self.log.info(f'value of signal({bus}{channel}.{message}.{signal})={signal_value}.')
        return signal_value

    def set_signal_value(self, bus: str, channel: int, message: str, signal: str, value: Union[float, int], raw_value=False) -> None:
        r"""set_signal_value sets a value to Signal. Works only when messages are sent using CANoe IL.  

        Args:
            bus (str): The Bus(CAN, LIN, FlexRay, MOST, AFDX, Ethernet) on which the signal is sent.
            channel (int): The channel on which the signal is sent.
            message (str): The name of the message to which the signal belongs.
            signal (str): The name of the signal.
            value (Union[float, int]): signal value.
            raw_value (bool): return raw value of the signal if true. Default(False) is physical value.

        Examples:
            >>> # The following example sets signal value to 1
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.set_signal_value('CAN', 1, 'LightState', 'FlashLight', 1)
        """
        signal_obj = self.__canoe_app_obj.GetBus(bus).GetSignal(channel, message, signal)
        if raw_value:
            signal_obj.RawValue = value
        else:
            signal_obj.Value = value
        self.log.info(f'signal({bus}{channel}.{message}.{signal}) value set to {value}.')

    def check_signal_online(self, bus: str, channel: int, message: str, signal: str) -> bool:
        r"""Checks whether the measurement is running and the signal has been received.

        Args:
            bus (str): The Bus(CAN, LIN, FlexRay, MOST, AFDX, Ethernet) on which the signal is sent.
            channel (int): The channel on which the signal is sent.
            message (str): The name of the message to which the signal belongs.
            signal (str): The name of the signal.

        Returns:
            TRUE if the measurement is running and the signal has been received. FALSE if not.
        
        Examples:
            >>> # The following example checks signal is online.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.check_signal_online('CAN', 1, 'LightState', 'FlashLight')
        """
        sig_online_status = self.__canoe_app_obj.GetBus(bus).GetSignal(channel, message, signal).IsOnline
        self.log.info(f'signal({bus}{channel}.{message}.{signal}) online status = {sig_online_status}.')
        return sig_online_status

    def check_signal_state(self, bus: str, channel: int, message: str, signal: str) -> int:
        r"""Checks whether the measurement is running and the signal has been received.

        Args:
            bus (str): The Bus(CAN, LIN, FlexRay, MOST, AFDX, Ethernet) on which the signal is sent.
            channel (int): The channel on which the signal is sent.
            message (str): The name of the message to which the signal belongs.
            signal (str): The name of the signal.

        Returns:
            State of the signal.
            0 The default value of the signal is returned.
            1 The measurement is not running; the value set by the application is returned.
            2 The measurement is not running; the value of the last measurement is returned.
            3 The signal has been received in the current measurement; the current value is returned.

        Examples:
            >>> # The following example checks signal state.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.check_signal_state('CAN', 1, 'LightState', 'FlashLight')
        """
        sig_state = self.__canoe_app_obj.GetBus(bus).GetSignal(channel, message, signal).State
        self.log.info(f'signal({bus}{channel}.{message}.{signal}) state = {sig_state}.')
        return sig_state

    def get_j1939_signal_value(self, bus: str, channel: int, message: str, signal: str, source_addr: int, dest_addr: int,
                               raw_value=False) -> Union[float, int]:
        r"""get_j1939_signal Returns a Signal object.

        Args:
            bus (str): The Bus(CAN, LIN, FlexRay, MOST, AFDX, Ethernet) on which the signal is sent.
            channel (int): The channel on which the signal is sent.
            message (str): The name of the message to which the signal belongs.
            signal (str): The name of the signal.
            source_addr (int): The source address of the ECU that sends the message.
            dest_addr (int): The destination address of the ECU that receives the message.
            raw_value (bool): return raw value of the signal if true. Default(False) is physical value.

        Returns:
            signal vaue.

        Examples:
            >>> # The following example gets j1939 signal value
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> sig_val = canoe_inst.get_j1939_signal_value('CAN', 1, 'LightState', 'FlashLight', 0, 1)
            >>> print(sig_val)
        """
        signal_obj = self.__canoe_app_obj.GetBus(bus).GetJ1939Signal(channel, message, signal, source_addr, dest_addr)
        signal_value = signal_obj.RawValue if raw_value else signal_obj.Value
        self.log.info(f'value of signal({bus}{channel}.{message}.{signal})={signal_value}.')
        return signal_value

    def set_j1939_signal_value(self, bus: str, channel: int, message: str, signal: str, source_addr: int, dest_addr: int, value: Union[float, int],
                               raw_value=False) -> None:
        r"""get_j1939_signal Returns a Signal object.

        Args:
            bus (str): The Bus(CAN, LIN, FlexRay, MOST, AFDX, Ethernet) on which the signal is sent.
            channel (int): The channel on which the signal is sent.
            message (str): The name of the message to which the signal belongs.
            signal (str): The name of the signal.
            source_addr (int): The source address of the ECU that sends the message.
            dest_addr (int): The destination address of the ECU that receives the message.
            value (Union[float, int]): signal value.
            raw_value (bool): return raw value of the signal if true. Default(False) is physical value.

        Returns:
            signal vaue.

        Examples:
            >>> # The following example gets j1939 signal value
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.set_j1939_signal_value('CAN', 1, 'LightState', 'FlashLight', 0, 1, 1)
        """
        signal_obj = self.__canoe_app_obj.GetBus(bus).GetJ1939Signal(channel, message, signal, source_addr, dest_addr)
        if raw_value:
            signal_obj.RawValue = value
        else:
            signal_obj.Value = value
        self.log.info(f'signal({bus}{channel}.{message}.{signal}) value set to {value}.')

    def get_system_variable_value(self, sys_var_name: str) -> Union[int, float, str]:
        r"""get_system_variable_value Returns a system variable value.

        Args:
            sys_var_name (str): The name of the system variable. Ex- "sys_var_demo::speed"

        Returns:
            System Variable value.

        Examples:
            >>> # The following example gets system variable value
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> sys_var_val = canoe_inst.get_system_variable_value('sys_var_demo::speed')
            >>>print(sys_var_val)
        """
        variable_value = None
        if sys_var_name in self.__sys_vars_obj_dictionary.keys():
            variable_value = self.__sys_vars_obj_dictionary[sys_var_name].Value
            self.log.info(f'system variable({sys_var_name}) value = {variable_value}.')
        else:
            self.log.warning(f'system variable({sys_var_name}) not available in loaded CANoe config.')
        return variable_value

    def set_system_variable_value(self, sys_var_name: str, value: Union[int, float, str]) -> None:
        r"""set_system_variable_value sets a value to system variable.

        Args:
            sys_var_name (str): The name of the system variable. Ex- "sys_var_demo::speed"
            value (Union[int, float, str]): variable value.

        Examples:
            >>> # The following example sets system variable value to 1
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.set_system_variable_value('sys_var_demo::speed', 1)
        """
        if sys_var_name in self.__sys_vars_obj_dictionary.keys():
            self.__sys_vars_obj_dictionary[sys_var_name].Value = value
            self.log.info(f'system variable({sys_var_name}) value set to {value}.')
        else:
            self.log.warning(f'system variable({sys_var_name}) not available in loaded CANoe config.')

    def send_diag_request(self, diag_ecu_qualifier_name: str, request: str, request_in_bytes=True) -> str:
        r"""The send_diag_request method represents the query of a diagnostic tester (client) to an ECU (server) in CANoe.

        Args:
            diag_ecu_qualifier_name (str): Diagnostic Node ECU Qualifier Name configured in "Diagnostic/ISO TP Configuration".
            request (str): Diagnostic request in bytes or diagnostic node qualifier name.
            request_in_bytes: True if Diagnostic request is bytes. False if you are using Qualifier name. Default is True.

        Returns:
            diagnostic response stream. Ex- "50 01 00 00 00 00"

        Examples:
            >>> # Example 1 - The following example sends diagnostic request "10 01"
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> wait(1)
            >>> resp = canoe_inst.send_diag_request('Door', '10 01')
            >>> print(resp)
            >>> canoe_inst.stop_measurement()
            >>> # Example 2 - The following example sends diagnostic request "DefaultSession_Start"
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(canoe_cfg=r'C:\Users\Public\Documents\Vector\CANoe\Sample Configurations 11.0.81\.\CAN\Diagnostics\UDSBasic\UDSBasic.cfg')
            >>> canoe_inst.start_measurement()
            >>> wait(1)
            >>> resp = canoe_inst.send_diag_request('Door', 'DefaultSession_Start', False)
            >>> print(resp)
            >>> canoe_inst.stop_measurement()
        """
        diag_response_data = ""
        if diag_ecu_qualifier_name in self.__diag_ecu_qualifiers_dictionary.keys():
            self.log.info(f'Diag Req --> {request}')
            if request_in_bytes:
                diag_req_in_bytes = bytearray()
                request = ''.join(request.split(' '))
                for i in range(0, len(request), 2):
                    diag_req_in_bytes.append(int(request[i:i + 2], 16))
                diag_req = self.__diag_ecu_qualifiers_dictionary[diag_ecu_qualifier_name].CreateRequestFromStream(diag_req_in_bytes)
            else:
                diag_req = self.__diag_ecu_qualifiers_dictionary[diag_ecu_qualifier_name].CreateRequest(request)
            diag_req.Send()
            while diag_req.Pending:
                wait(0.1)
            if diag_req.Responses.Count == 0:
                self.log.info("Diagnostic Response Not Received.")
            else:
                for k in range(1, diag_req.Responses.Count + 1):
                    diag_res = diag_req.Responses(k)
                    if diag_res.Positive:
                        self.log.info(f"+ve response received.")
                    else:
                        self.log.info(f"-ve response received.")
                    diag_response_data = " ".join(f"{d:02X}" for d in diag_res.Stream).upper()
                self.log.info(f'Diag Res --> {diag_response_data}')
        else:
            self.log.info(f'Diag ECU qualifier({diag_ecu_qualifier_name}) not available in loaded CANoe config.')
        return diag_response_data

    def ui_activate_desktop(self, name: str) -> None:
        r"""Activates the desktop with the given name.

        Args:
            name (str): The name of the desktop to be activated.

        Examples:
            >>> # The following example switches to the desktop with the name "Configuration"
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.ui_activate_desktop("Configuration")
        """
        self.__canoe_app_obj.UI.ActivateDesktop(name)
        self.log.info(f'Activated / switched to "{name}" Desktop')

    def ui_open_baudrate_dialog(self) -> None:
        r"""opens the dialog for configuring the bus parameters. Make sure Measurement stopped when using this method.

        Examples:
            >>> # The following example opens the dialog for configuring the bus parameters
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.stop_measurement()
            >>> canoe_inst.ui_open_baudrate_dialog()
        """
        self.log.info('opened the dialog for configuring the bus parameters')
        self.__canoe_app_obj.UI.OpenBaudrateDialog()

    def write_text_in_write_window(self, text: str) -> None:
        r"""Outputs a line of text in the Write Window.
        Args:
            text (str): The text.

        Examples:
            >>> # The following example Outputs a line of text in the Write Window.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> wait(1)
            >>> canoe_inst.write_text_in_write_window("hello from python!")
            >>> wait(1)
            >>> print(canoe_inst.read_text_from_write_window())
        """
        self.__canoe_app_obj.UI.Write.Output(text)
        self.log.info(f'written "{text}" to Write Window')

    def read_text_from_write_window(self) -> str:
        r"""read the text contents from Write Window.

        Returns:
            The text content.

        Examples:
            >>> # The following example reads text from Write Window.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> wait(1)
            >>> canoe_inst.write_text_in_write_window("hello from python!")
            >>> wait(1)
            >>> print(canoe_inst.read_text_from_write_window())
        """
        return self.__canoe_app_obj.UI.Write.Text

    def clear_write_window_content(self) -> None:
        r"""Clears the contents of the Write Window.

        Examples:
            >>> # The following example clears content from Write Window.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.start_measurement()
            >>> wait(1)
            >>> canoe_inst.write_text_in_write_window("hello from python!")
            >>> wait(1)
            >>> canoe_inst.clear_write_window_content()
        """
        self.__canoe_app_obj.UI.Write.Clear()
        self.log.info(f'Cleared Write Window Content.')

    def enable_write_window_output_file(self, output_file: str) -> None:
        r"""Enables logging of all outputs of the Write Window in the output file.

        Args:
            output_file (str): The complete path of the output file.

        Examples:
            >>> # The following example Enables logging of all outputs of the Write Window in the output file.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.enable_write_window_output_file(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\write_out.txt')
            >>> canoe_inst.start_measurement()
            >>> wait(1)
            >>> canoe_inst.write_text_in_write_window("hello from python!")
            >>> wait(1)
            >>> canoe_inst.stop_measurement()
        """
        self.__canoe_app_obj.UI.Write.EnableOutputFile(output_file)
        self.log.info(f'Enabled Write Window logging. file path --> {output_file}')

    def disable_write_window_output_file(self) -> None:
        r"""Disables logging of all outputs of the Write Window.

        Examples:
            >>> # The following example Disables logging of all outputs of the Write Window.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.disable_write_window_output_file()
        """
        self.__canoe_app_obj.UI.Write.DisableOutputFile()
        self.log.info(f'Enabled Write Window logging.')

    def set_replay_block_file(self, block_name: str, recording_file_path: str) -> None:
        r"""Method for setting CANoe replay block file.

        Args:
            block_name: CANoe replay block name
            recording_file_path: CANoe replay recording file including path.

        Examples:
            >>> # The following example sets replay block file
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.set_replay_block_file(block_name='replay block name', recording_file_path='replay file including path')
            >>> canoe_inst.start_measurement()
        """
        if block_name in self.__replay_blocks_obj_dictionary.keys():
            self.__replay_blocks_obj_dictionary[block_name].Path = recording_file_path
            self.log.info(f'Replay block "{block_name}" updated with "{recording_file_path}" path.')
        else:
            self.log.warning(f'Replay block "{block_name}" not available.')

    def control_replay_block(self, block_name: str, start_stop: bool) -> None:
        r"""Method for setting CANoe replay block file.

        Args:
            block_name (str): CANoe replay block name
            start_stop (bool): True to start replay block. False to Stop.

        Examples:
            >>> # The following example starts replay block
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_inst.set_replay_block_file(block_name='replay block name', recording_file_path='replay file including path')
            >>> canoe_inst.start_measurement()
            >>> canoe_inst.control_replay_block('replay block name', True)
        """
        if block_name in self.__replay_blocks_obj_dictionary.keys():
            if start_stop:
                self.__replay_blocks_obj_dictionary[block_name].Start()
            else:
                self.__replay_blocks_obj_dictionary[block_name].Stop()
            self.log.info(f'Replay block "{block_name}" {"Started" if start_stop else "Stopped"}.')
        else:
            self.log.warning(f'Replay block "{block_name}" not available.')

    def get_can_bus_statistics(self, channel: int) -> dict:
        r"""Returns CAN Bus Statistics.

        Args:
            channel (int): The channel of the statistic that is to be returned.

        Returns:
            CAN bus statistics.

        Examples:
            >>> # The following example prints CAN channel 1 statistics
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> print(canoe_inst.get_can_bus_statistics(channel=1))
        """
        bus_statistics_obj = self.__canoe_app_obj.Configuration.OnlineSetup.BusStatistics.BusStatistic(self.__BUS_TYPES['CAN'], channel)
        statistics_info = {
            # The bus load
            'bus_load': bus_statistics_obj.BusLoad,
            # The controller status
            'chip_state': bus_statistics_obj.ChipState,
            # The number of Error Frames per second
            'error': bus_statistics_obj.Error,
            # The total number of Error Frames
            'error_total': bus_statistics_obj.ErrorTotal,
            # The number of messages with extended identifier per second
            'extended': bus_statistics_obj.Extended,
            # The number of remote messages with extended identifier per second
            'extended_remote': bus_statistics_obj.ExtendedRemote,
            # The total number of remote messages with extended identifier
            'extended_remote_total': bus_statistics_obj.ExtendedRemoteTotal,
            # The number of overload frames per second
            'overload': bus_statistics_obj.Overload,
            # The total number of overload frames
            'overload_total': bus_statistics_obj.OverloadTotal,
            # The maximum bus load in 0.01 %
            'peak_load': bus_statistics_obj.PeakLoad,
            # Returns the current number of the Rx error counter
            'rx_error_count': bus_statistics_obj.RxErrorCount,
            # The number of messages with standard identifier per second
            'standard': bus_statistics_obj.Standard,
            # The total number of remote messages with standard identifier
            'standard_total': bus_statistics_obj.StandardTotal,
            # The number of remote messages with standard identifier per second
            'standard_remote': bus_statistics_obj.StandardRemote,
            # The total number of remote messages with standard identifier
            'standard_remote_total': bus_statistics_obj.StandardRemoteTotal,
            # The current number of the Tx error counter
            'tx_error_count': bus_statistics_obj.TxErrorCount,
        }
        return statistics_info

    def get_canoe_configuration_details(self) -> dict:
        r"""Returns Loaded CANoe configuration details.

        Returns:
            Returns Loaded CANoe configuration details.

        Examples:
            >>> # The following example returns CANoe application version relevant information.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_version_info = canoe_inst.get_canoe_configuration_details()
            >>> print(canoe_version_info)
        """
        configuration_details = {
            'canoe_app_full_name': self.__canoe_app_obj.Application.Version.FullName,
            'canoe_app_full_name_with_sp': self.__canoe_app_obj.Application.Version.Name,
            # The complete path to the currently loaded configuration
            'canoe_cfg': self.__canoe_app_obj.Configuration.FullName,
            # CANoe Mode(online/offline)
            'canoe_mode': 'online' if self.__canoe_app_obj.Configuration.Mode == 0 else 'offline',
            # Configuration ReadOnly ?
            'cfg_read_only': self.__canoe_app_obj.Configuration.ReadOnly,
            # CANoe configuration Networks count and Names List
            'networks_count': len(self.__networks_obj_dictionary.keys()),
            'networks_list': list(self.__networks_obj_dictionary.keys()),
            # CANoe Simulation Setup Nodes count and Names List
            'simulation_setup_nodes_count': len(self.__simulation_nodes_obj_dictionary.keys()),
            'simulation_setup_nodes_list': list(self.__simulation_nodes_obj_dictionary.keys()),
            # CANoe Replay Blocks count and Names List
            'simulation_setup_replay_blocks_count': len(self.__replay_blocks_obj_dictionary.keys()),
            'simulation_setup_replay_blocks_list': list(self.__replay_blocks_obj_dictionary.keys()),
            # The number of buses count
            'simulation_setup_buses_count': self.__canoe_app_obj.Configuration.SimulationSetup.Buses.Count,
            # The number of generators contained
            'simulation_setup_generators_count': self.__canoe_app_obj.Configuration.SimulationSetup.Generators.Count,
            # The number of interactive generators contained
            'simulation_setup_interactive_generators_count': self.__canoe_app_obj.Configuration.SimulationSetup.InteractiveGenerators.Count,
        }
        self.log.info('> CANoe Configuration Details <'.center(100, '='))
        for k, v in configuration_details.items():
            self.log.info(f'{k:<50}: {v}')
        self.log.info(''.center(100, '='))
        return configuration_details

    def get_canoe_version_info(self) -> dict:
        r"""The Version class represents the version of the CANoe application.

        Returns:
            "full_name" - The complete CANoe version.
            "name" - The CANoe version.
            "build" - The build number of the CANoe application.
            "major" - The major version number of the CANoe application.
            "minor" - The minor version number of the CANoe application.
            "patch" - The patch number of the CANoe application.

        Examples:
            >>> # The following example returns CANoe application version relevant information.
            >>> canoe_inst = CANoe()
            >>> canoe_inst.open(r'D:\_kms_local\vector_canoe\py_canoe\demo_cfg\demo.cfg')
            >>> canoe_version_info = canoe_inst.get_canoe_version_info()
            >>> print(canoe_version_info)
        """
        version_info = {'full_name': self.__canoe_app_obj.Application.Version.FullName,
                        'name': self.__canoe_app_obj.Application.Version.Name,
                        'build': self.__canoe_app_obj.Application.Version.Build,
                        'major': self.__canoe_app_obj.Application.Version.Major,
                        'minor': self.__canoe_app_obj.Application.Version.Minor,
                        'patch': self.__canoe_app_obj.Application.Version.Patch}
        self.write_text_in_write_window('> CANoe Application.Version <'.center(100, '='))
        for k, v in version_info.items():
            self.write_text_in_write_window(f'{k:<10}: {v}')
        self.write_text_in_write_window(''.center(100, '='))
        return version_info
    
    def print_in_py_canoe(self, txt) -> None:#print in C:\.py_canoe
        return self.log.info(txt)
    
    def read_sw_verssion(self, sw_verssion):
        self.sw_ver = sw_verssion
        # create function to read sw_verssion
        return self.write_text_in_write_window(f'> SW Verssion {self.sw_ver} <'.center(100, '='))
           
    def read_hw_verssion(self, hw_verssion):
        self.hw_ver = hw_verssion
        # create function to read hw_verssion
        self.write_text_in_write_window(f'> HW Verssion {self.hw_ver} <'.center(100, '='))
                
    def get_username(self) -> str:
        # Gives user's home directory
        userhome = os.path.expanduser('~')          
        return self.write_text_in_write_window(f"Executed by: {userhome}\n")
   
    def test_case(self, test_case_name):
        self.write_text_in_write_window(f'\n')      
        self.test_case_name = test_case_name          
        return self.write_text_in_write_window(f"Test Case: {self.test_case_name}")
        
    def test_step(self, test_step_name):
        self.test_step_name = test_step_name 
        # self.log.info(f'\n')
        return self.write_text_in_write_window(f"Test Step: {self.test_step_name}")
        
    def step_ok(self):
        return self.write_text_in_write_window('TestStepResult: OK\n')
        
    def step_nok(self):
        return self.write_text_in_write_window('TestStepResult: NOK\n')
                        
    def check_sw_hw_verssions(self):
    
        master = Tk()

        Label(master, text='Type SW version').grid(row=0)
        Label(master, text='Type HW version').grid(row=1)

        e1 = Entry(master)
        e2 = Entry(master)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        # Function to get the values
        def get_values():
            
            expected_sw_verssion = e1.get()
            expected_hw_verssion = e2.get()
                      
            # Read and check SW and HW verssions
            sw_verssion = "xx"
            hw_verssion = "xx"
            
            self.test_case("Read and check SW and HW versions")
            self.test_step("SW version")
            self.requirement("12346")
            self.write_text_in_write_window(f"SW version Expected: {expected_sw_verssion}; Real: {sw_verssion}")
            if sw_verssion == expected_sw_verssion:
                self.step_ok()
            else:
                self.step_nok()
                self.modify_list()
                print(self.failed_reqs)
            #self.write_text_in_write_window(f''.center(50, '='))
            
            self.test_step("HW verssion")
            self.requirement("12347")
            self.write_text_in_write_window(f"HW verssion Expected: {expected_hw_verssion}; Real: {hw_verssion}")
            if hw_verssion == expected_hw_verssion:
                self.step_ok()
            else:
                self.step_nok()
            #self.write_text_in_write_window(f''.center(50, '='))
            
        # Button to retrieve the values
        button = Button(master, text="Get Values", command=get_values)
        button.grid(row=2, column=0, columnspan=2)

        mainloop()
        
    def check_value(self, var_name, var_value, expected_value):
        self.var_name = var_name
        self.var_value = var_value
        self.expected_value = expected_value
  
        self.expected_value = hex(int(self.expected_value, 16))
        if self.var_value == self.expected_value:
            self.write_text_in_write_window(f"{self.var_name }:Real value = {self.var_value}; expected value = {self.expected_value}")
            self.step_ok()
        else:
            self.write_text_in_write_window(f"{self.var_name }:Real value = {self.var_value}; expected value = {self.expected_value}")
            self.step_nok()  

    def modify_list(self, value):
        self.failed_reqs.append(value)
        
    def test_author(self):
        return self.write_text_in_write_window("Test Author:Dimitar Angelov Email:dimitar.angelov@mercedes-benz.com")
    
    def requirement(self, requirement_id) -> str:
        self.requirement_id = requirement_id
        return self.write_text_in_write_window(f">req.{requirement_id}<")

    def send_sync_fup_eth(self, loops, seq_id_loop, network):
        self.loops = loops
        self.seq_id_loop = seq_id_loop
        self.network = network
        
        if self.network == "ETH":
            for loop in range(self.loops):
                for seq_id in range(self.seq_id_loop):
                    
                    self.sequence_id = str(hex(seq_id)).upper()
                    self.sequence_id = self.sequence_id[2:]

                    if len(self.sequence_id) == 1:
                        self.sequence_id = "000" + self.sequence_id
                    elif len(self.sequence_id) == 2:
                        self.sequence_id = "00" + self.sequence_id
                    elif len(self.sequence_id) == 3:
                        self.sequence_id = "0" + self.sequence_id

                    
                    self.gts_sync_message = self.destination_mac + self.source_mac + self.tpi + self.tci + self.ether_type + self.message_type_sync\
                   + self.version_ptp + self.message_length_sync + self.domain_number + self.reserved_1byte + self.flags_sync + self.correctionfield\
                   + self.reserved_4bytes + self.sourceportidentity + self.sequence_id + self.control_sync + self.logmessageinterval + self.reserved_10bytes
                    self.sync_fup_data["sync"].append(self.gts_sync_message)
                    wait(0.040)

                    if seq_id % 2 == 0:
                        self.prec_ori_time_s = ""
                        self.prec_ori_time_ns = ""
                        self.temp_sec = hex(self.sec).upper()
                        self.temp_sec = self.temp_sec[2:]
                   
                        if len(self.temp_sec) < 12:
                            for idx in range(12 - len(self.temp_sec), 0, -1):
                                self.prec_ori_time_s = self.prec_ori_time_s + "0"

                        self.prec_ori_time_s = self.prec_ori_time_s + self.temp_sec
                        self.prec_ori_time_ns = "00000000"
                        self.sec = self.sec + 1
                    else:
                        self.prec_ori_time_ns = "1DCD6500"

                    self.prec_ori_time = self.prec_ori_time_s + self.prec_ori_time_ns
                    if len(self.prec_ori_time) < 20:
                        temp = 20 - len(self.prec_ori_time)
                        self.prec_ori_time = temp * "0" + self.prec_ori_time
                            
                    #AUTOSAR TLV Sub-TLV:Time Secured
                    self.prec_origin_timestamp_1 = int(self.prec_ori_time[0:2], 16)
                    self.prec_origin_timestamp_2 = int(self.prec_ori_time[2:4], 16)
                    self.prec_origin_timestamp_3 = int(self.prec_ori_time[4:6], 16)
                    self.prec_origin_timestamp_4 = int(self.prec_ori_time[6:8], 16)
                    self.prec_origin_timestamp_5 = int(self.prec_ori_time[8:10], 16)
                    self.prec_origin_timestamp_6 = int(self.prec_ori_time[10:12], 16)
                    self.prec_origin_timestamp_7 = int(self.prec_ori_time[12:14], 16)
                    self.prec_origin_timestamp_8 = int(self.prec_ori_time[14:16], 16)
                    self.prec_origin_timestamp_9 = int(self.prec_ori_time[16:18], 16)
                    self.prec_origin_timestamp_10 = int(self.prec_ori_time[18:20], 16)
                    self.data_id = self.ETHDataId[int(self.domain_number)][(int(self.sequence_id, 16)) % 16]
        
                    self.data =[int(self.crc_time_flags, 16), int(self.domain_number), self.prec_origin_timestamp_1, self.prec_origin_timestamp_2, self.prec_origin_timestamp_3, self.prec_origin_timestamp_4,
                                            self.prec_origin_timestamp_5, self.prec_origin_timestamp_6, self.prec_origin_timestamp_7, self.prec_origin_timestamp_8, self.prec_origin_timestamp_9, self.prec_origin_timestamp_10, self.data_id] #CRC_Time_0
       
                    crc = 0xFF  # init value
                    for value in self.data:
                        crc = self.crc8x_table[value ^ crc]
                    self.crc_time_0 = hex(crc^0xff)[2:].upper()
                    if len(self.crc_time_0) < 2:
                        self.crc_time_0 = "0" + self.crc_time_0
        
                    self.gts_fup_message = self.destination_mac + self.source_mac + self.tpi + self.tci + self.ether_type + self.message_type_fup + self.version_ptp + self.message_length_fup + self.domain_number + self.reserved_1byte\
                        + self.flags_fup + self.correctionfield + self.reserved_4bytes + self.sourceportidentity + self.sequence_id + self.control_fup + self.logmessageinterval + self.prec_ori_time\
                        + self.tlv_type1 + self.length_field1 + self.organization_id1 + self.organization_sub_type1 + self.cumulative_scaled_rate_offset + self.gm_time_base_indicator + self.last_gm_phase_change + self.caled_last_gm_freq_change\
                        + self.tlv_type2 + self.length_field2 + self.organization_id2 + self.organization_sub_type2\
                        + self.type_time_secured + self.length_time_secured + self.crc_time_flags + str(self.crc_time_0) + str(self.crc_time_1)\
                        + self.type_status_secured + self.length_status_secured + self.status + self.crc_status\
                        + self.type_user_data_secured + self.length + self.user_data_length + self.user_byte_0 + self.user_byte_1 + self.user_byte_2 + self.crc_user_data

                    self.sync_fup_data["fup"].append(self.gts_fup_message)
        
        return self.sync_fup_data
       
    def check_sync_fup_SC(self, result):
        self.test_case("Correct sequence of SC in SYNC and FU")
        self.requirement("CTP-10844")
        
        self.result = result
        
        for idx in range(len(self.result['sync'])):
            self.test_step("SC of both SYNC and FUP should become 0x0000 after reaching 0xffff and again starts increasing from 0 by value 1")
            self.test_step("For each SYNC message there should be a corresponding FUP frame.Check sequence caounter incremented by 1 and Sync SC== Fup SC")
            self.requirement("CTP-10864")
            self.requirement("CTP-10862")
            self.write_text_in_write_window(f"gts_sync_message {self.result['sync'][idx]}")
            self.write_text_in_write_window(f"gts_fup_message {self.result['fup'][idx]}")
            sc_sync = self.result["sync"][idx][96:100]
            sc_fup = self.result["fup"][idx][96:100]
           
            if sc_sync == sc_fup:
                self.write_text_in_write_window(f"SC Sync: {sc_sync}; SC Fup: {sc_fup}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"sc_sync = {sc_sync} != sc_fup = {sc_fup}")
                self.step_nok()
    
    def check_vlan_priority(self, result):
        self.test_case("VLAN and Priority field correctly set")
        self.requirement("CTP-10857")

        self.result = result
        for idx in range(len(self.result['sync'])):
            self.test_step("Tag control information should be 0xE07F")
            self.requirement("CTP-12474")
            self.write_text_in_write_window(f"gts_sync_message {self.result['sync'][idx]}")
            self.write_text_in_write_window(f"gts_fup_message {self.result['fup'][idx]}")
            vlan_priority_sync = self.result["sync"][idx][28:32]
            vlan_priority_fup = self.result["fup"][idx][28:32]
           
            if vlan_priority_sync == vlan_priority_fup == "E07F":
                self.write_text_in_write_window(f"SC vlan_priority_sync: 0x{vlan_priority_sync}; SC Fup: 0x{vlan_priority_fup}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:vlan_priority_fup = 0xE07F; Real: vlan_priority_sync = 0x{vlan_priority_sync};vlan_priority_fup = 0x{vlan_priority_fup}")
                self.step_nok()
            
    def check_frame_format_of_sync(self, result):
        self.test_case("Correct frame format of SYNC")
        self.requirement("CTP-10845")

        self.result = result
        for idx in range(len(self.result['sync'])):
            self.test_step("The received SYNC frame should have following fields")
            self.requirement("CTP-12475")
            self.write_text_in_write_window(f"gts_sync_message {self.result['sync'][idx]}")
            message_type = self.result["sync"][idx][36:38]
            version_ptp = self.result["sync"][idx][38:40]
            mes_length = self.result["sync"][idx][40:44]
            mes_length_real = len(self.result["sync"][idx][36:])
            domain_number = self.result["sync"][idx][44:46]
            reserved_2 = self.result["sync"][idx][46:48]
            flags = self.result["sync"][idx][48:52]
            correction_field = self.result["sync"][idx][52:68]
            reserved_3 = self.result["sync"][idx][68:76]
            source_port_identity = self.result["sync"][idx][76:96]
            #sequenceId  is checked by function check_sync_fup_SC
            control = self.result["sync"][idx][100:102]
            log_mes_interval = self.result["sync"][idx][102:104]
            reserved_4 = self.result["sync"][idx][104:124]

                       
            if message_type == "10":
                self.write_text_in_write_window(f"Transport specific: {message_type}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:Transport specific = 10; Real: Transport specific = {message_type}")
                self.step_nok()

            if version_ptp == "02":
                self.write_text_in_write_window(f"version_ptp: {version_ptp}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:version_ptp = 0; Real: version_ptp = {version_ptp}")
                self.step_nok()

            if (mes_length == "002C") and (mes_length_real == 44 * 2):
                self.write_text_in_write_window(f"mes_length: {mes_length}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:mes_length = 002C; Real: mes_length = {mes_length}")
                self.step_nok()

            if domain_number == "00":
                self.write_text_in_write_window(f"domain_number: {domain_number}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:domain_number = 00; Real: domain_number = {domain_number}")
                self.step_nok()

            if reserved_2 == "00":
                self.write_text_in_write_window(f"reserved_2: {reserved_2}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:reserved_2 = 00; Real: reserved_2 = {reserved_2}")
                self.step_nok()

            if flags == "0208":
                self.write_text_in_write_window(f"flags: {flags}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:flags = 0208; Real: flags = {flags}")
                self.step_nok()

            if correction_field == "0000000000000000":
                self.write_text_in_write_window(f"correction_field: {correction_field}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:correction_field = 0000000000000000; Real: correction_field = {correction_field}")
                self.step_nok()

            if reserved_3 == "00000000":
                self.write_text_in_write_window(f"reserved_3: {reserved_3}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:reserved_3 = 00000000; Real: reserved_3 = {reserved_3}")
                self.step_nok()

            if source_port_identity == "3CCE15FFFE0000050001":
                self.write_text_in_write_window(f"source_port_identity: {source_port_identity}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:source_port_identity = 3CCE15FFFE0000050001; Real: source_port_identity = {source_port_identity}")
                self.step_nok()

            if control == "00":
                self.write_text_in_write_window(f"control: {control}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:control = 00; Real: control = {control}")
                self.step_nok()

            if log_mes_interval == "FF":
                self.write_text_in_write_window(f"log_mes_interval: {log_mes_interval}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:log_mes_interval = 00; Real: log_mes_interval = {log_mes_interval}")
                self.step_nok()

            if reserved_4 == "00000000000000000000":
                self.write_text_in_write_window(f"reserved_4: {reserved_4}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:reserved_4 = 00000000000000000000; Real: reserved_4 = {reserved_4}")
                self.step_nok()

    def check_frame_format_of_fup(self, result):
        self.test_case("Correct frame format of FUP")
        self.requirement("CTP-10845")
        sec = 10
        self.result = result
        for idx in range(len(self.result['fup'])):
            self.test_step("The received SYNC frame should have following fields")
            self.requirement("CTP-12475")
            self.write_text_in_write_window(f"gts_fup_message {self.result['fup'][idx]}")
            message_type = self.result["fup"][idx][36:38]
            version_ptp = self.result["fup"][idx][38:40]
            mes_length = self.result["fup"][idx][40:44]
            mes_length_real = len(self.result["fup"][idx][36:])
            domain_number = self.result["fup"][idx][44:46]
            reserved_2 = self.result["fup"][idx][46:48]
            flags = self.result["fup"][idx][48:52]
            correction_field = self.result["fup"][idx][52:68]
            reserved_3 = self.result["fup"][idx][68:76]
            source_port_identity = self.result["fup"][idx][76:96]
            sequenceId  = int(self.result["fup"][idx][96:100])
            control = self.result["fup"][idx][100:102]
            log_mes_interval = self.result["fup"][idx][102:104]
            recived_prec_ori_time = self.result["fup"][idx][104:124]
            if sequenceId % 2 == 0:
                prec_ori_time_s = ""
                prec_ori_time_ns = ""
                temp_sec = hex(sec).upper()
                temp_sec = temp_sec[2:]
                   
                if len(temp_sec) < 12:
                    for idx in range(12 - len(temp_sec), 0, -1):
                        prec_ori_time_s = prec_ori_time_s + "0"

                prec_ori_time_s = prec_ori_time_s + temp_sec
                prec_ori_time_ns = "00000000"
                sec = sec + 1
            else:
                prec_ori_time_ns = "1DCD6500"

            prec_ori_time = prec_ori_time_s + prec_ori_time_ns
            if len(prec_ori_time) < 20:
                temp = 20 - len(prec_ori_time)
                prec_ori_time = temp * "0" + prec_ori_time
            
            print("\n")
            print(prec_ori_time)

                       
            if message_type == "18":
                self.write_text_in_write_window(f"message_type: {message_type}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:message_type = 0x18; Real: message_type = {message_type}")
                self.step_nok()

            if version_ptp == "02":
                self.write_text_in_write_window(f"reserved_1: {version_ptp}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:version_ptp = 02; Real: version_ptp = {version_ptp}")
                self.step_nok()

            if (mes_length == "0066") and (mes_length_real == 102 * 2):
                self.write_text_in_write_window(f"Emes_length: {mes_length_real}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:mes_length = 0x0066; Real: mes_length = {mes_length_real}")
                self.step_nok()

            if domain_number == "00":
                self.write_text_in_write_window(f"domain_number: {domain_number}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:domain_number = 00; Real: domain_number = {domain_number}")
                self.step_nok()

            if reserved_2 == "00":
                self.write_text_in_write_window(f"reserved_2: {reserved_2}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:reserved_2 = 00; Real: reserved_2 = {reserved_2}")
                self.step_nok()

            if flags == "0008":
                self.write_text_in_write_window(f"flags: {flags}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:flags = 0008; Real: flags = {flags}")
                self.step_nok()

            if correction_field == "0000000000000000":
                self.write_text_in_write_window(f"correction_field: {correction_field}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:correction_field = 0000000000000000; Real: correction_field = {correction_field}")
                self.step_nok()

            if reserved_3 == "00000000":
                self.write_text_in_write_window(f"reserved_3: {reserved_3}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:reserved_3 = 00000000; Real: reserved_3 = {reserved_3}")
                self.step_nok()

            if source_port_identity == "3CCE15FFFE0000050001":
                self.write_text_in_write_window(f"source_port_identity: {source_port_identity}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:source_port_identity = 3CCE15FFFE0000050001; Real: source_port_identity = {source_port_identity}")
                self.step_nok()

            if control == "02":
                self.write_text_in_write_window(f"control: {control}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:control = 02; Real: control = {control}")
                self.step_nok()

            if log_mes_interval == "FF":
                self.write_text_in_write_window(f"log_mes_interval: {log_mes_interval}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:log_mes_interval = 00; Real: log_mes_interval = {log_mes_interval}")
                self.step_nok()
            
            if prec_ori_time == recived_prec_ori_time:
                self.write_text_in_write_window(f"prec_ori_time: {prec_ori_time}")
                self.step_ok()
            else:
                self.write_text_in_write_window(f"Expected:prec_ori_time = {recived_prec_ori_time}; Real: prec_ori_time = {prec_ori_time}")
                self.step_nok()

    def calculate_crc8x_fast(self, network, crc, result):
        self.test_case("Check CRCs status")

        self.network = network
        self.result = result
        self.crc = crc
        
        if self.network == "ETH":
            self.test_step("Check Eth CRC_Time_0")
            self.requirement("12349")
            for idx in range(len(self.result['sync'])):
                self.write_text_in_write_window(f"gts_sync_message {self.result['sync'][idx]}")
                self.write_text_in_write_window(f"gts_fup_message {self.result['fup'][idx]}")
                                
                self.crc_time_flags = int(self.result["fup"][idx][212:214], 16)
                self.domain_number = int(self.result["fup"][idx][44:46], 16)
                self.timestamp_1 = int(self.result["fup"][idx][104:106], 16)
                self.timestamp_2 = int(self.result["fup"][idx][106:108], 16)
                self.timestamp_3 = int(self.result["fup"][idx][108:110], 16)
                self.timestamp_4 = int(self.result["fup"][idx][110:112], 16)
                self.timestamp_5 = int(self.result["fup"][idx][112:114], 16)
                self.timestamp_6 = int(self.result["fup"][idx][114:116], 16)
                self.timestamp_7 = int(self.result["fup"][idx][116:118], 16)
                self.timestamp_8 = int(self.result["fup"][idx][118:120], 16)
                self.timestamp_9 = int(self.result["fup"][idx][120:122], 16)
                self.timestamp_10 = int(self.result["fup"][idx][122:124], 16)
                self.preciseOriginTimestamp = self.result["fup"][idx][104:124]
                self.sequence_id = int(self.result["fup"][idx][96:100], 16)                
                self.data_id = self.ETHDataId[int(self.domain_number)][(int(self.sequence_id)) % 16]
                self.CRC_Time_0 = int(self.result["fup"][idx][214:216], 16)

                if self.crc == "CRC_Time_0":               
                    self.data = [self.crc_time_flags, self.domain_number, self.timestamp_1, self.timestamp_2, self.timestamp_3, self.timestamp_4,
                                self.timestamp_5, self.timestamp_6, self.timestamp_7, self.timestamp_8, self.timestamp_9, self.timestamp_10, self.data_id] #CRC_Time_0
                    
                    #self.data = [55, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 3] #CRC_Time_0
                    #self.data = [self.crc_time_flags, 102, 6, 13] #CRC_Time_1
                    #self.data = [0, 13] #CRC_Status
                    #self.data = [1, 32, 0, 0, 13]  #CRC_UserData
                    
                    crc = 0xFF  # init value
                    for value in self.data:
                        crc = self.crc8x_table[value ^ crc]
                    
                    self.write_text_in_write_window(f"CRC_Time_Flags:{self.crc_time_flags}; domainNumber: {self.domain_number}; preciseOriginTimestamp {self.preciseOriginTimestamp}; DataID:{self.data_id}")
                        
                    if crc^0xff == self.CRC_Time_0:
                        self.write_text_in_write_window(f"Expected CRC_Time_0: {self.CRC_Time_0}; Calculated CRC_Time_0: {crc^0xff}")
                        self.step_ok()
                    else:
                        self.write_text_in_write_window(f"Expected CRC_Time_0: {self.CRC_Time_0}; Calculated CRC_Time_0: {crc^0xff}")
                        self.step_nok()
                    print(f"Full Crc = 0x{crc^0xff:x}, dec = {crc^0xff}")
        
                #if self.crc == "CRC_Time_1":               
                #    self.data = [self.crc_time_flags, int(self.message_length), self.timestamp_1, self.timestamp_2, self.timestamp_3, self.timestamp_4,
                #                self.timestamp_5, self.timestamp_6, self.timestamp_7, self.timestamp_8, self.timestamp_9, self.timestamp_10, self.data_id] #CRC_Time_0
                    
                #    #self.data = [55, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 3] #CRC_Time_0
                #    #self.data = [self.crc_time_flags, 102, 6, 13] #CRC_Time_1
                #    #self.data = [0, 13] #CRC_Status
                #    #self.data = [1, 32, 0, 0, 13]  #CRC_UserData
                    
                #    crc = 0xFF  # init value
                #    for value in self.data:
                #        crc = self.crc8x_table[value ^ crc]
                    
                #    self.write_text_in_write_window(f"CRC_Time_Flags:{self.crc_time_flags}; domainNumber: {self.domain_number}; preciseOriginTimestamp {self.preciseOriginTimestamp}; DataID:{self.data_id}")
                        
                #    if crc^0xff == self.CRC_Time_0:
                #        self.write_text_in_write_window(f"Expected CRC_Time_0: {self.CRC_Time_0}; Calculated CRC_Time_0: {crc^0xff}")
                #        self.step_ok()
                #    else:
                #        self.write_text_in_write_window(f"Expected CRC_Time_0: {self.CRC_Time_0}; Calculated CRC_Time_0: {crc^0xff}")
                #        self.step_nok()
                #    print(f"Full Crc = 0x{crc^0xff:x}, dec = {crc^0xff}")

    def get_decimal_value(self, text):
        self.text =text
        match = re.search(r'\.(\d+)', self.text)
        if match:
            return match.group(1)
        else:
            return None