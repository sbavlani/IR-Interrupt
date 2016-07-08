int i,ilast,jlast;
int k=0;
int j=0;
void setup() 
{
 Serial.begin(115200);   
pinMode(9,OUTPUT);      
pinMode(10,OUTPUT);
pinMode(5,INPUT);
 ilast=digitalRead(5);
}

void loop() 
{
 
  analogWrite(9,100);   // Rotate the DC motor
  analogWrite(10,0);
 
  i=digitalRead(5);
  
  if(i!=ilast)  // To chexk whether the moor has rotated
  {
    if(i==1)  // Condition when receiver receives signal from transitter
    {
      j++;
     }
      delay(10);
   }
   ilast=i;
  
   if(j!=jlast){
     Serial.print(j);
  
     if(j%17==0 && j!=0)   // Number of steps for full rotation (17 steps)
     {   
        k++;
        Serial.println("");
        Serial.print(k);
        Serial.println(" rotation/s complete! ");
        }
    }
    jlast=j;
  
}
