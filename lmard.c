float temp;
int tempPin = 0;


void setup()
{
	Serial.begin(9600);
}

void loop()
{
	temp = analogRead(tempPin);
	temp = temp * 0.48828125;
	Serial.print(temp);
	delay(10000);
}