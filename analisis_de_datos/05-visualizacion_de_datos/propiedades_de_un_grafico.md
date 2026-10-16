# PROPIEDADES BÁSICAS

# 1. `title` (TÍTULO)

```python
plt.title('Promedio de notas según curso')
```

---

# 2. `xlabel` y `ylabel`

```python
plt.xlabel('Curso')
plt.ylabel('Promedio')
```

---

## Qué hacen

👉 Nombran los ejes

---

# 3. `figsize` (TAMAÑO)

```python
.plot(figsize=(8,5))
```

## Qué hace

👉 Cambia el tamaño del gráfico

- 8 → ancho
- 5 → alto

---

# 4. `grid=True` (CUADRÍCULA)

```python
.plot(grid=True)
```

---

## Qué hace

👉 Agrega líneas de referencia

---

## 5. `color`

```python
.plot(kind='bar', color='skyblue')
```

---

## Qué hace

👉 Cambia el color

# 6. `alpha` (TRANSPARENCIA)

```python
.plot(kind='hist', alpha=0.5)
```

---

## Qué hace

👉 Hace el gráfico semi-transparente

---

# 7. `legend` (LEYENDA)

```python
plt.legend(['Con curso', 'Sin curso'])
```

---

## Qué hace

👉 Explica qué representa cada color

---

# 8. `bins` (HISTOGRAMAS)

```python
.plot(kind='hist', bins=5)
```

---

## Qué hace

👉 Define cuántos grupos se crean

---

# 9. `rot` (ROTACIÓN DE TEXTO)

```python
.plot(kind='bar', rot=45)
```

---

## Qué hace

👉 Rota etiquetas del eje X

---

# 10. `subplots` y `layout`

```python
.plot(subplots=True, layout=(1,2))
```

---

## Qué hace

👉 organiza múltiples gráficos

---

---

# EJEMPLO

```python
df_no_uni.groupby('test preparation course')['average score'].mean().plot(
    kind='bar',
    figsize=(8,5),
    color='skyblue',
    grid=True,
    rot=0
)

plt.title('Promedio según curso de preparación')
plt.xlabel('Curso')
plt.ylabel('Promedio')
plt.show()
```
