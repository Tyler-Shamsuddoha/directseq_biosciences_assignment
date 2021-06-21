# Interview Question for DirectSeq Biosciences

This repository contains the files needed to answer the following interview question:


<b>Interview question:</b>

Please use Python3 to implement a network system; it consists of two parts, the client and the server, both running on the console(terminal). The server runs on the local port 9999 and receives data (a list of floats) from clients. It analyzes the floats, finds all the basecallings, and return them to the client. The client receives user input (comma-separated floats) from the console and sends it to the server. If it gets the data responded from the server, it will print the data onto the console. Definitions: basecalling: if the difference between two floats, floatv and floatu, approximately equals any value of the dict { &#39;A&#39;: 329.0525, &#39;C&#39;: 305.0413, &#39;G&#39;: 345.0474, &#39;U&#39;: 306.0253}, it is called a basecalling, denoted as a tuple (floatv, floatu, base). Where base is ‘A’, ‘C’, ‘G’, or ‘U’. Approximately equal: if |floatm – floatn| <= 1E-6 , then we say that floatm approximately equals floatn.
