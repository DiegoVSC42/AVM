from moviepy.editor import AudioFileClip

# abre o arquivo original
audio = AudioFileClip("a.mp3")

# corta os primeiros 10 segundos
corte = audio.subclip(0, 10)

# exporta como mp3
corte.write_audiofile("b.mp3")

print("Arquivo 'b.mp3' criado com 10 segundos de duração.")
