package com.company;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class Hacker1 {
    Hacker1() {
        try {
            Socket clientSocket = new Socket("localhost", 7777);
            new BufferedReader(new InputStreamReader(System.in));
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            BufferedWriter out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
            String request = (new TCP()).with_source_port(6661).with_destination_port(7777).with_syn(1).get_String();
            out.write(request + "\n");
            out.flush();
            String message = in.readLine();
            System.out.println(message);
            TCP responce = TCP.from_string(message);
            System.out.println(responce.ack);
        } catch (Exception var8) {
            var8.printStackTrace();
        }

    }
}

