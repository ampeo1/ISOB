package com.company;

public class TCP {
    int source_port = 0;
    int destination_port = 0;
    int sequence_number = 0;
    int acknowledgment_number = 0;
    int urg = 0;
    int ack = 0;
    int psh = 0;
    int rst = 0;
    int syn = 0;
    int fin = 0;
    String data = "test";

    public TCP() {
    }

    TCP with_source_port(int val) {
        this.source_port = val;
        return this;
    }

    TCP with_destination_port(int val) {
        this.destination_port = val;
        return this;
    }

    TCP with_sequence_number(int val) {
        this.sequence_number = val;
        return this;
    }

    TCP with_acknowledgment_number(int val) {
        this.acknowledgment_number = val;
        return this;
    }

    TCP with_urg(int val) {
        this.urg = val;
        return this;
    }

    TCP with_ack(int val) {
        this.ack = val;
        return this;
    }

    TCP with_psh(int val) {
        this.psh = val;
        return this;
    }

    TCP with_rst(int val) {
        this.rst = val;
        return this;
    }

    TCP with_syn(int val) {
        this.syn = val;
        return this;
    }

    TCP with_fin(int val) {
        this.fin = val;
        return this;
    }

    TCP with_data(String val) {
        this.data = val;
        return this;
    }

    String get_String() {
        int var10000 = this.source_port;
        String array = var10000 + " " + this.destination_port + " " + this.sequence_number + " " + this.acknowledgment_number + " " + this.urg + " " + this.ack + " " + this.psh + " " + this.rst + " " + this.syn + " " + this.fin + " " + text2bin(this.data);
        return array;
    }

    static TCP from_string(String s) {
        TCP obj = new TCP();
        return obj.with_source_port(Integer.parseInt(s.split(" ")[0], 10)).with_destination_port(Integer.parseInt(s.split(" ")[1], 10)).with_sequence_number(Integer.parseInt(s.split(" ")[2], 10)).with_acknowledgment_number(Integer.parseInt(s.split(" ")[3], 10)).with_urg(s.split(" ")[4].charAt(0) - 48).with_ack(s.split(" ")[5].charAt(0) - 48).with_psh(s.split(" ")[6].charAt(0) - 48).with_rst(s.split(" ")[7].charAt(0) - 48).with_syn(s.split(" ")[8].charAt(0) - 48).with_fin(s.split(" ")[9].charAt(0) - 48).with_data(bin2text(s.split(" ")[10]));
    }

    static String text2bin(String s) {
        byte[] bytes = s.getBytes();
        StringBuilder binary = new StringBuilder();
        byte[] var3 = bytes;
        int var4 = bytes.length;

        for(int var5 = 0; var5 < var4; ++var5) {
            byte b = var3[var5];
            int val = b;

            for(int i = 0; i < 8; ++i) {
                binary.append((val & 128) == 0 ? 0 : 1);
                val <<= 1;
            }
        }

        return binary.toString();
    }

    static String bin2text(String s) {
        StringBuilder text = new StringBuilder();

        for(int i = 0; i <= s.length() - 8; i += 8) {
            text.append((char)Integer.parseInt(s.substring(i, i + 8), 2));
        }

        return text.toString();
    }
}
