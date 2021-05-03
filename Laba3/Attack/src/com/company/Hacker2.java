package com.company;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class Hacker2 {
    Hacker2() {
        try {
            Socket clientSocket = new Socket("localhost", 7777);
            new BufferedReader(new InputStreamReader(System.in));
            new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            BufferedWriter out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));

            for(int i = 0; i < 10; ++i) {
                String request = (new TCP()).with_source_port(1488 + i).with_destination_port(7777).with_syn(1).get_String();
                out.write(request + "\n");
                out.flush();
            }
        } catch (Exception var7) {
            var7.printStackTrace();
        }

    }
}