#Part of the Model
import ffmpeg
import os
from os import path
from pydub import AudioSegment

class AudioHandler:
    def __init__(self, file_path):
        self.file_name = path.splitext(file_path)[0]
        self.file_type = path.splitext(file_path)[1]
        self.sound = self.to_wav(file_path)
    @staticmethod
    def to_wav(file_path):
        file_type = path.splitext(file_path)[1]
        accepted_file_types = {".wav", ".raw", ".mp3", ".m4a"}
        if file_type in accepted_file_types:
            return AudioSegment.from_file(file_path)

    @staticmethod
    def audio_file_holder_path():
        # Returns the proper filepath for Audio_File_Holder directory
        cwd = os.getcwd()
        return path.join(cwd, "Audio_File_Holder")


    def export(self):
        # Exports the audio into the Audio_File_Holder directory
        output_dir = self.audio_file_holder_path()
        output_path = path.join(output_dir, self.file_name + ".wav")
        self.sound.export(output_path, format="wav")
        return output_path