/**CONTACTO */

document.addEventListener('DOMContentLoaded', () => {
    const formulario = document.getElementById('formulario');
    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const correo =document.getElementById('correo')
    const contrasena = document.getElementById('contrasena');
    const repetirContrasena = document.getElementById('repetirContrasena');
    const nombreError = document.getElementById('nombreError');
    const apellidoError = document.getElementById('apellidoError');
    const correoError = document.getElementById('correoError');
    const contrasenaError = document.getElementById('contrasenaError');
    const repetirContrasenaError = document.getElementById('repetirContrasenaError');
    
    
    
    formulario.addEventListener('submit', (event) => {
      // Validar nombre
      if (nombre.value.trim() === '') {
        event.preventDefault();
        nombre.classList.add('error');
        nombreError.textContent = 'Por favor ingrese su nombre.';
      } else {
        nombre.classList.remove('error');
        nombreError.textContent = '';
      }
    
      // Validar apellido
      if (apellido.value.trim() === '') {
        event.preventDefault();
        apellido.classList.add('error');
        apellidoError.textContent = 'Por favor ingrese su apellido.';
      } else {
        apellido.classList.remove('error');
        apellidoError.textContent = '';
      }
    
      // Validar Correo
      if (correo.value.trim() === '') {
        event.preventDefault();
        correo.classList.add('error');
        correoError.textContent = 'Por favor ingrese su Correo.';
      } else {
        correo.classList.remove('error');
        correoError.textContent = '';
      }
    
      // Validar contraseña
      if (contrasena.value.trim() === '') {
        event.preventDefault();
        contrasena.classList.add('error');
        contrasenaError.textContent = 'Por favor ingrese su contraseña.';
      } else {
        contrasena.classList.remove('error');
        contrasenaError.textContent = '';
      }
    
      // Validar repetir contraseña
      if (repetirContrasena.value.trim() === '') {
        event.preventDefault();
        repetirContrasena.classList.add('error');
        repetirContrasenaError.textContent = 'Por favor repita su contraseña.';
      } else if (repetirContrasena.value !== contrasena.value) {
        event.preventDefault();
        repetirContrasena.classList.add('error');
        repetirContrasenaError.textContent = 'Las contraseñas no coinciden.';
      } else {
        repetirContrasena.classList.remove('error');
        repetirContrasenaError.textContent = '';
      }
    });
    
    // Limpiar errores al cambiar el contenido de los campos
    nombre.addEventListener('input', () => {
      nombre.classList.remove('error');
      nombreError.textContent = '';
    });
    
    apellido.addEventListener('input', () => {
      apellido.classList.remove('error');
      apellidoError.textContent = '';
    });
    
    correo.addEventListener('input', () => {
      correo.classList.remove('error');
      correoError.textContent = '';
    });
    
    contrasena.addEventListener('input', () => {
      contrasena.classList.remove('error');
      contrasenaError.textContent = '';
    });
    
    repetirContrasena.addEventListener('input', () => {
      repetirContrasena.classList.remove('error');
      repetirContrasenaError.textContent = '';
    });
    });