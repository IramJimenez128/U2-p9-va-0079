import matplotlib.pyplot as plt

materias = ["Ciencias naturales", "Matematicas", "Lengua y comunicacion", "Vision Artificial", "Machine Learning"]
califas = [100, 50, 70, 90, 100]

plt.pie(califas, labels = materias, autopct="%1.1f%%")
plt.title("Calificaciones de materias 0079")
plt.show()