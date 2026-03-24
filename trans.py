import whisper

model = whisper.load_model("base")
result = model.transcribe("AUD-20250626-WA0040.m4a") 
 # Make sure to replace "AUD-20250626-WA0040.m4a" with the path to your audio file
#the audio file should be in the same directory as this script or provide the correct path to the audio file

print(result["text"])
