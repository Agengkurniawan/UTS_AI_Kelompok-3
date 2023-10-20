import pywhatkit as kit
import datetime
import speech_recognition as sr
from gtts import gTTS
import pyttsx3

# Daftar nomor WhatsApp tujuan
target_numbers = ["+6282112220904"]

# Inisialisasi recognizer
recognizer = sr.Recognizer()
  
# Inisialisasi text-to-speech engine
engine = pyttsx3.init()

# Fungsi untuk mendengarkan ucapan dan mengirim pesan
def listen_and_send_message():
    with sr.Microphone() as source:
        print("Hallo, My Name is AgeeChatBot")
        engine.say("Hallo, My Name is AgeeChatBot")
        print("Silakan ucapkan pesan Anda, dan saya akan mengirimkan ke Whatsapp...")
        engine.say("Silakan ucapkan pesan Anda dan saya akan mengirimkan ke Whatsapp.")
        engine.runAndWait()

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="id-ID")  # Ganti dengan kode bahasa yang sesuai
            print("Anda mengatakan:", text)

            engine.say("Anda mengatakan: " + text)
            engine.runAndWait()

            # Kirim pesan menggunakan teks hasil pengenalan
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute + 1  # Kirim pesan 1 menit dari sekarang
            
            # Kirim pesan ke semua nomor target
            for target_number in target_numbers:
                kit.sendwhatmsg(target_number, text, hour, minute)

            engine.say("Pesan telah dikirim ke semua nomor target.")
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Maaf, saya tidak dapat mengenali ucapan Anda.")
            engine.say("Maaf, saya tidak dapat mengenali ucapan Anda.")
            engine.runAndWait()
        except sr.RequestError as e:
            print("Terjadi kesalahan saat mengakses layanan Google Speech Recognition:", str(e))
            engine.say("Terjadi kesalahan saat mengakses layanan Google Speech Recognition.")
            engine.runAndWait()

# Panggil fungsi untuk mendengarkan dan mengirim pesan
listen_and_send_message()
