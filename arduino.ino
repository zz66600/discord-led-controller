int ledPin = 13; // LED no pino 13 (pode ser outro pino)

void setup() {
  pinMode(ledPin, OUTPUT);   // Define o pino do LED como saída
  digitalWrite(ledPin, LOW); // Inicialmente, o LED está desligado
  Serial.begin(9600);        // Inicia a comunicação serial a 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Lê o comando recebido
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Liga o LED
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);   // Desliga o LED
    }
  }
}
