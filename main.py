import pyttsx3
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Add the path to the Job Description file in Docx format
job_description = docx2txt.process("../Job_Description.docx")
# Add the path to your Resume file in Docx format
resume = docx2txt.process("../Resume.docx")

content = [job_description, resume]
cv = CountVectorizer()
matrix = cv.fit_transform(content)
similarity_matrix = cosine_similarity(matrix)
print(similarity_matrix)

print('The percentage of correct match is: ' + str(similarity_matrix[1][0] * 100) + '%')
speak('The percentage of correct match is: ' + str(similarity_matrix[1][0] * 100) + '%')
