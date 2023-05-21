import signal
import sys

def prevents_unexpected_closures(server):
    
    # Registrar o sinal de interrupção (Ctrl+C)
    def signal_handler(signal, frame):
        server.close_connection()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    # Registrar o manipulador para o evento de fechamento do terminal
    sys.exitfunc = server.close_connection