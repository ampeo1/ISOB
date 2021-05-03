package com.company;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.Iterator;

class Server {
    private int PORT = 7777;
    private ArrayList<Integer> SYNReceivedList = new ArrayList();
    private ArrayList<Integer> CONNECTED = new ArrayList();
    private final int SYN_RECEIVED_MAXSIZE = 7;
    private final int CONNECTED_MAXSIZE = 7;
    private static Socket clientSocket;
    private static ServerSocket server;
    private static BufferedReader in;
    private static BufferedWriter out;

    private void addToSynReceived(TCP request, Socket clientSocket) throws Exception {
        TCP response = (new TCP()).with_source_port(this.PORT).with_destination_port(request.destination_port).with_syn(1);
        out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
        out.write(response.get_String() + "\n");
        out.flush();
        this.SYNReceivedList.add(request.source_port);
        System.out.println("NEW SYN HAS BEEN RECEIVED.");
        System.out.print("SYN_RECEIVED: ");
        Iterator var4 = this.SYNReceivedList.iterator();

        Integer i;
        while(var4.hasNext()) {
            i = (Integer)var4.next();
            System.out.print(i + " ");
        }

        System.out.print("\nCONNECTED.");
        var4 = this.CONNECTED.iterator();

        while(var4.hasNext()) {
            i = (Integer)var4.next();
            System.out.print(i + " ");
        }

        System.out.println("");
        if (this.SYNReceivedList.size() > 7) {
            System.out.println("TOO MUCH SYN...");
            throw new Exception("SYN IS OVERLOAD!");
        }
    }

    void addToConnected(TCP request) throws Exception {
        this.SYNReceivedList.remove(this.SYNReceivedList.indexOf(request.source_port));
        this.CONNECTED.add(request.source_port);
        System.out.println("NEW CLIENT HAS BEEN CONNECTED.");
        System.out.print("SYN_RECEIVED:");
        Iterator var2 = this.SYNReceivedList.iterator();

        Integer i;
        while(var2.hasNext()) {
            i = (Integer)var2.next();
            System.out.print(i + " ");
        }

        System.out.print("\nCONNECTED:");
        var2 = this.CONNECTED.iterator();

        while(var2.hasNext()) {
            i = (Integer)var2.next();
            System.out.print(i + " ");
        }

        System.out.println("");
        if (this.CONNECTED.size() > 7) {
            System.out.println("TOO MUCH CONNECTIONS...");
            throw new Exception("SERVER IS OVERLOAD!");
        }
    }

    Server() throws Exception {
        try {
            try {
                server = new ServerSocket(this.PORT);
                System.out.println("*********************SERVER*********************");
                System.out.println("SERVER IS WORKING...");
                System.out.println("------------------------------------------------");
                System.out.println("WAIT PLEASE...");
                System.out.println("------------------------------------------------");
                clientSocket = server.accept();
                System.out.println("SOME CLIENT IS CONNECTED");

                try {
                    in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));

                    while(true) {
                        while(true) {
                            String word = in.readLine();
                            System.out.println("MESSAGE: " + word.replaceAll(" ", ""));
                            System.out.println("------------------------------------------------");
                            TCP request = TCP.from_string(word);
                            if (request.destination_port == this.PORT && !this.CONNECTED.contains(request.source_port)) {
                                if (this.SYNReceivedList.contains(request.source_port)) {
                                    this.addToConnected(request);
                                } else {
                                    this.addToSynReceived(request, clientSocket);
                                }
                            }
                        }
                    }
                } catch (SocketException var15) {
                    System.out.println("------------------------------------------------");
                    System.out.println("CLIENT DIED!");
                } catch (Exception var16) {
                    System.out.println("------------------------------------------------");
                    System.out.println("ERROR! Something wrong...");
                    var16.printStackTrace();
                } finally {
                    System.out.println("------------------------------------------------");
                    System.out.println("SOCKET CLOSING...");
                    clientSocket.close();
                    in.close();
                    out.close();
                }
            } finally {
                System.out.println("SERVER IS DOWN");
                server.close();
            }
        } catch (IOException var19) {
            System.err.println(var19);
        }

    }
}
