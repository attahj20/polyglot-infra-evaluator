const net = require("net");
const PORT = 9999;
const HOST = "127.0.0.1";
console.log("=== PROJECT 2: MULTI-AGENT PROTOCOL RIGGING MATRIX ===");
const receiverAgent = net.createServer((socket) => {
    socket.on("data", (data) => {
        const frame = JSON.parse(data.toString());
        if (frame.step === 1) {
            socket.write(JSON.stringify({ step: 2, action: "SYN-ACK" }));
        } else if (frame.step === 3) {
            socket.write(JSON.stringify({ step: 4, action: "FIN" }));
            socket.end();
        }
    });
});
receiverAgent.listen(PORT, HOST, () => {
    console.log(`[System] Receiver Agent Online at ${HOST}:${PORT}`);
    const initiatorAgent = new net.Socket();
    initiatorAgent.connect(PORT, HOST, () => {
        initiatorAgent.write(JSON.stringify({ step: 1, action: "SYN" }));
    });
    initiatorAgent.on("data", (data) => {
        const frame = JSON.parse(data.toString());
        if (frame.step === 2) {
            initiatorAgent.write(JSON.stringify({ step: 3, action: "DATA-TX" }));
        } else if (frame.step === 4) {
            console.log("[Initiator Agent] Target state reached. Closing connections.");
            initiatorAgent.destroy();
            receiverAgent.close();
        }
    });
});
