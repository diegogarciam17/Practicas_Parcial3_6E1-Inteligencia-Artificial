# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Proyecto IA
Deep learning y Redes Neuronales
"""

#Para este proyecto usaremos el programa siguiente para  para predecir el consumo energético de un 
#edificio en base a distintas características como:
#-el tamaño
#-número de pisos 
#-tipo de material de construcción
#-ubicación
# Y al ejecutarlo en la consola estimara el consumo de energia en kwh

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

# Generar datos de ejemplo
# Suponemos que tenemos 4 características: tamaño (pies cuadrados), número de pisos, tipo de material (1 a 3), y ubicación (1 a 5)
np.random.seed(42)
X = np.random.rand(1000, 4) * [5000, 10, 3, 5]  # 1000 muestras con 4 características
y = (X[:, 0] * 0.8 + X[:, 1] * 2000 + X[:, 2] * 1500 + X[:, 3] * 1000).reshape(-1, 1)  # Consumo energético en base a una fórmula hipotética

# Convertir datos a tensores de PyTorch
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)

# Definir el modelo de red neuronal en PyTorch
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(4, 64)
        self.layer2 = nn.Linear(64, 64)
        self.output = nn.Linear(64, 1)
        
    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.output(x)
        return x

model = NeuralNetwork()

# Definir el optimizador y la función de pérdida
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()

# Entrenamiento del modelo
num_epochs = 50
batch_size = 32
history = {'loss': [], 'val_loss': []}

for epoch in range(num_epochs):
    model.train()
    permutation = torch.randperm(X_tensor.size()[0])
    
    for i in range(0, X_tensor.size()[0], batch_size):
        optimizer.zero_grad()
        indices = permutation[i:i + batch_size]
        batch_x, batch_y = X_tensor[indices], y_tensor[indices]
        
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    
    history['loss'].append(loss.item())
    
    # Evaluación en datos de validación (usando 20% de los datos)
    model.eval()
    with torch.no_grad():
        val_loss = criterion(model(X_tensor), y_tensor).item()
        history['val_loss'].append(val_loss)
    
    print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}, Val Loss: {val_loss:.4f}")

# Visualización del proceso de entrenamiento
plt.figure(figsize=(12, 6))

# Gráfico de la pérdida de entrenamiento y validación
plt.plot(history['loss'], label='Pérdida de entrenamiento')
plt.plot(history['val_loss'], label='Pérdida de validación')
plt.title('Pérdida durante el entrenamiento')
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.legend()
plt.grid(True)
plt.show()

# Predicción de consumo energético con nuevos datos
nuevos_datos = np.array([[3000, 5, 2, 3]])  # Tamaño, número de pisos, tipo de material y ubicación
nuevos_datos_tensor = torch.tensor(nuevos_datos, dtype=torch.float32)
prediccion_consumo = model(nuevos_datos_tensor).item()
print(f'Predicción del consumo energético del edificio: {prediccion_consumo:.2f} kWh')

