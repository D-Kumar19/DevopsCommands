FROM maven:3.9.6-eclipse-temurin-17-alpine

RUN apk add --no-cache git \
    openjdk17-jre \
    libxext-dev \
    libxrender-dev \
    libxtst-dev \
    libxi-dev \
    libxrandr-dev \
    fontconfig \
    mesa-gl \
    mesa-dri-gallium

WORKDIR /app

RUN git clone https://github.com/D-Kumar19/Tic-Tac-Toe-using-MVC.git

WORKDIR /app/Tic-Tac-Toe-using-MVC

RUN mvn clean package

CMD ["java", "-cp", "target/Tic-Tac-Toe-Game-1.0.jar", "TicTacToeGame.JavaFX.Main"]
