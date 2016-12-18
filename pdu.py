

class PDU(object):
    """
        Pdu class format
    """

    def hex_to_num(self, hexinfo):
        return int(hexinfo, 16)

    def semi_octet_to_string(self, hexinfo):

        out = ""
        for i in range(0, len(hexinfo)-1, 2):
            temp = hexinfo[i: i+2]
            out += temp[1] + temp[0]

        return out


    def dcs_bits(self, tp_dcs):
        alphabet_size = 7
        pomdcs = self.hex_to_num(tp_dcs)

        if pomdcs & 192 == 0:

            if (pomdcs & 12) == 4:
                alphabet_size = 8
            if (pomdcs & 12) == 8:
                alphabet_size = 16

        if pomdcs & 192 == 192:
            if (pomdcs & 0x30) == 0x20:
                alphabet_size = 16

            if (pomdcs & 0x30) == 0x30:
                if (pomdcs & 0x4) is False:
                    alphabet_size = 8

        return alphabet_size

    def get_meta_info(self, metainfo):
        """
            GET class metainfo
        """

        smsc_length_info = self.hex_to_num(metainfo[:2])
        smsc_info = metainfo[2 : 2+(smsc_length_info*2)]
        smsc_type_address = smsc_info[0:2]
        smsc_number = smsc_info[2 : 2+(smsc_length_info*2)]

        if smsc_length_info == 0:
            return

        smsc_number = self.semi_octet_to_string(smsc_number)

        if smsc_number[-1:].upper() == "F":
            smsc_number = smsc_number[:-1]

        start_sms_delivery = (smsc_length_info *2)+2
        start = start_sms_delivery

        first_octet_smsdeliver = metainfo[start:start + 2]
        start = start + 2


        if (self.hex_to_num(first_octet_smsdeliver) & 0x03) == 0:
            print "Receiver"
            senderinfo = metainfo[start:]

            sender_address_length = self.hex_to_num(senderinfo[0:2])
            if sender_address_length % 2 != 0:
                sender_address_length += 1

            sender_type_address = senderinfo[2:4]
            sender_info = senderinfo[4 : 4 + sender_address_length]
            sender_number = self.semi_octet_to_string(sender_info)

            if sender_number[-1:].upper() == "F":
                sender_number = sender_number[:-1]

            tp_dcs = senderinfo[sender_address_length+6 : sender_address_length+8]

            timeStamp = senderinfo[sender_address_length+8 : sender_address_length+20]

            timeStamp = self.semi_octet_to_string(timeStamp)
            year = timeStamp[0:2]
            month = timeStamp[2:4]
            day = timeStamp[4:6]
            hours = timeStamp[6:8]
            minutes = timeStamp[8:10]
            seconds = timeStamp[10:12]

            print day + "/" + month + "/" + year + " " + hours + ":" + minutes + ":" + seconds

            print self.dcs_bits(tp_dcs)



        if (self.hex_to_num(first_octet_smsdeliver) & 0x03) == 1:
            print "Transmit"

        
metainfoReceiver = "07911326040000F0040B911346610089F60004608062917314080CC8F71D14969741F977FD07B"
metainfoTransmit = "07911356131313F311000A9260214365870000AA0CC8F71D14969741F977FD07"
pdu = PDU()
pdu.get_meta_info(metainfoReceiver)

