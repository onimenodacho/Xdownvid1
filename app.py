import streamlit as st

st.title("Descargador de Videos")

# Pantalla de inicio
url = st.text_input("Pega aquí la URL del video")

if st.button("Analizar"):
    # Simulación de análisis de video
    video_info = {
        'titulo': 'Ejemplo de Video',
        'duracion': '3:45',
        'miniatura': 'https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg',
        'formatos': [
            'MP4 720p',
            'MP4 480p',
            'MP3 (audio)'
        ]
    }
    st.image(video_info['miniatura'], width=300)
    st.write(f"**Título:** {video_info['titulo']}")
    st.write(f"**Duración:** {video_info['duracion']}")
    st.write("**Formatos disponibles:**")
    for formato in video_info['formatos']:
        if st.button(f"Descargar {formato}"):
            st.success(f"Descarga simulada de {formato} iniciada.")
