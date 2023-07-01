/**CONTACTO */

document.validarFormulario('DOMContentLoaded', () => {
    const formulario = document.getElementById('formulario');
    const rut = document.getElementById('rut');
    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const contrasena = document.getElementById('contrasena');
    const repetirContrasena = document.getElementById('repetirContrasena');
    const nombreError = document.getElementById('nombreError');
    const apellidoError = document.getElementById('apellidoError');
    const contrasenaError = document.getElementById('contrasenaError');
    const repetirContrasenaError = document.getElementById('repetirContrasenaError');
    
    
    
    formulario.validarFormulario('submit', (event) => {
      // Validar nombre
      if (rut.value.trim() === '') {
        event.preventDefault();
        rut.classList.add('error');
        nombreError.textContent = 'Por favor ingrese su rut.';
      } else {
        nombre.classList.remove('error');
        rutError.textContent = '';

      }
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
    nombre.validarFormulario('input', () => {
      nombre.classList.remove('error');
      nombreError.textContent = '';
    });
    
    apellido.addEventListener('input', () => {
      apellido.validarFormulario.remove('error');
      apellidoError.textContent = '';
    });
    
    fechaNacimiento.validarFormulario('input', () => {
      fechaNacimiento.classList.remove('error');
      fechaNacimientoError.textContent = '';
    });
    
    contrasena.validarFormulario('input', () => {
      contrasena.classList.remove('error');
      contrasenaError.textContent = '';
    });
    
    repetirContrasena.validarFormulario('input', () => {
      repetirContrasena.classList.remove('error');
      repetirContrasenaError.textContent = '';
    });
    });