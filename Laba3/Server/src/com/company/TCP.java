package com.company;

public class TCP {
    int source_port = 0;
    int destination_port = 0;
    private int sequence_number = 0;
    private int acknowledgment_number = 0;
    private int urg = 0;
    private int ack = 0;
    private int psh = 0;
    private int rst = 0;
    private int syn = 0;
    private int fin = 0;
    private String data = "test";

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
        String array = this.source_port + " " + this.destination_port + " " + this.sequence_number + " " + this.acknowledgment_number + " " + this.urg + " " + this.ack + " " + this.psh + " " + this.rst + " " + this.syn + " " + this.fin + " " + this.data;
        return array;
    }

    static TCP from_string(String s) {
        TCP obj = new TCP();
        return obj.with_source_port(Integer.parseInt(s.split(" ")[0], 10)).with_destination_port(Integer.parseInt(s.split(" ")[1], 10)).with_sequence_number(Integer.parseInt(s.split(" ")[2], 10)).with_acknowledgment_number(Integer.parseInt(s.split(" ")[3], 10)).with_urg(s.split(" ")[4].charAt(0) - 48).with_ack(s.split(" ")[5].charAt(0) - 48).with_psh(s.split(" ")[6].charAt(0) - 48).with_rst(s.split(" ")[7].charAt(0) - 48).with_syn(s.split(" ")[8].charAt(0) - 48).with_fin(s.split(" ")[9].charAt(0) - 48).with_data(s.split(" ")[10]);
    }
}

