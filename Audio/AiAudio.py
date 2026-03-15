import azure.cognitiveservices.speech as speech

subscription_key = "40a3fc8e6f304d148c05aca4475ddf23"
service_region="eastus"

speech_config = speech.SpeechConfig(
    subscription = subscription_key,
    region = service_region)

audio_file_path = "./Input.wav"

audio_config = speech.audio.AudioConfig(
    filename=audio_file_path)

speech_recognizer = speech.SpeechRecognizer(
    speech_config = speech_config,
    audio_config = audio_config
)

result = speech_recognizer.recognize_once()

print(result.text)