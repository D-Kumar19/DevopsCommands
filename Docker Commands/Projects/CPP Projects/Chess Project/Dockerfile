FROM gcc:14.1.0

WORKDIR /app

RUN git clone https://github.com/D-Kumar19/Regal-Rumble-The-Compact-Chess.git

WORKDIR /app/Regal-Rumble-The-Compact-Chess/Chess\ Game/

RUN g++ -o ChessGame ./MainProgram.cpp

CMD ["./ChessGame"]
