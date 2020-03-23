

print("Välkommen till gympass-skaparen. Nedan kan du skriva vad du har för krav på passet jag ska göra åt dig.")
a = input("Vilka kroppsdelar vill du fokusera på?") #använd contain för att kolla svar?
b = input("Hur många pass vill du att jag ska göra?")
if int(b)==1:
    c = input("Hur hårt ska passet vara?")
elif int(b)>1:
    d = input("Hur hårda ska passen vara?")
    e = input("Ska jag göra ett veckoschema för passen?")
