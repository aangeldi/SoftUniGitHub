crc8x_table = [
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

 #@ETHDataId = ([204,214,224,234,244,3,13,23,33,43,53,63,73,83,93,103], 											# [CC,D6,E0,EA,F4,03,0D,17,21,2B,35,3F,49,53,5D,67]	time domain 0
	#					undef,	# time domain 1
	#					undef,	# time domain 2
	#					undef,	# time domain 3
	#					[0x1A,0x96,0x17,0x93,0x14,0x90,0x11,0x8D,0x0E,0x8A,0x0B,0x87,0x08,0x84,0x05,0x81],		# [1A,96,17,93,14,90,11,8D,0E,8A,0B,87,08,84,05,81]	time domain 4
	#					[0x71,0x66,0x5B,0x50,0x45,0x3A,0x2F,0x24,0x19,0x0E,0x03,0xF3,0xE8,0xDD,0xD2,0xC7],		# [71,66,5B,50,45,3A,2F,24,19,0E,03,F3,E8,DD,D2,C7]	time domain 5
	#					[0xA0,0x19,0x8D,0x06,0x7A,0xEE,0x67,0xDB,0x54,0xC8,0x41,0xB5,0x2E,0xA2,0x1B,0x8F],		# [A0,19,8D,06,7A,EE,67,DB,54,C8,41,B5,2E,A2,1B,8F]	time domain 6
	#					[0x12,0xFC,0xEB,0xDA,0xC9,0xB8,0xA7,0x96,0x85,0x74,0x63,0x52,0x41,0x30,0x1F,0x0E],		# [12,FC,EB,DA,C9,B8,A7,96,85,74,63,52,41,30,1F,0E]	time domain 7
	#					[0x41,0x0D,0xD4,0xA0,0x6C,0x38,0x04,0xCB,0x97,0x63,0x2F,0xF6,0xC2,0x8E,0x5A,0x26],		# [41,0D,D4,A0,6C,38,04,CB,97,63,2F,F6,C2,8E,5A,26]	time domain 8
	#					[0x09,0x6D,0xD1,0x3A,0x9E,0x07,0x6B,0xCF,0x38,0x9C,0x05,0x69,0xCD,0x36,0x9A,0x03],		# [09,6D,D1,3A,9E,07,6B,CF,38,9C,05,69,CD,36,9A,03]	time domain 9
	#					[0xDA,0x4E,0xBD,0x31,0xA0,0x14,0x83,0xF2,0x66,0xD5,0x49,0xB8,0x2C,0x9B,0x0F,0x7E],		# [DA,4E,BD,31,A0,14,83,F2,66,D5,49,B8,2C,9B,0F,7E]	time domain 10
	#					[0xA1,0x40,0xDA,0x79,0x18,0xB2,0x51,0xEB,0x8A,0x29,0xC3,0x62,0xFC,0x9B,0x3A,0xD4],		# [A1,40,DA,79,18,B2,51,EB,8A,29,C3,62,FC,9B,3A,D4]	time domain 11
	#					[0xFA,0x8B,0x1C,0xA8,0x39,0xC5,0x56,0xE2,0x73,0x04,0x90,0x21,0xAD,0x3E,0xCA,0x5B],		# [FA,8B,1C,A8,39,C5,56,E2,73,04,90,21,AD,3E,CA,5B]	time domain 12
	#					[0x6C,0x8D,0xAE,0xCF,0xF0,0x16,0x37,0x58,0x79,0x9A,0xBB,0xDC,0xFD,0x23,0x44,0x65],		# [6C,8D,AE,CF,F0,16,37,58,79,9A,BB,DC,FD,23,44,65]	time domain 13
	#					[0xFB,0x24,0x48,0x6C,0x90,0xB4,0xD8,0xFC,0x25,0x49,0x6D,0x91,0xB5,0xD9,0xFD,0x26],		# [FB,24,48,6C,90,B4,D8,FC,25,49,6D,91,B5,D9,FD,26]	time domain 14
	#					[0x1B,0x0E,0xFC,0xEF,0xE2,0xD5,0xC8,0xBB,0xAE,0xA1,0x94,0x87,0x7A,0x6D,0x60,0x53],		# [1B,0E,FC,EF,E2,D5,C8,BB,AE,A1,94,87,7A,6D,60,53]	time domain 15
	#				  );


def calculate_crc8x_fast(data):
    crc = 0xFF  # init value
    for value in data:
        crc = crc8x_table[value ^ crc]

    return crc ^ 0xff

 


#for data_id in range(0xFF):
#data = [55, 0, 0, 0, 0, 0, 0, 10, 29, 205, 101, 0, 204] #CRC_Time_0
#data = [55, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 53] #CRC_Time_0
#ata = [55, 102, 11, 63] #CRC_Time_1
data = [0x37,0x00, 0x66,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x19,0x2B] #CRC_Time_1
#data = [0, 13] #CRC_Status
#data = [1, 32, 0, 0, 13] #CRC_Time_1 #CRC_Status
    #data.append(data_id)
    #print(data)

crc = calculate_crc8x_fast(data)
print(f"Full Crc = 0x{crc:x}, dec = {crc}")
#if crc == 0x84:
#    break
