import { serverUrl } from '../config.js';
export class FormRepository {
    static registerStudent(formDTO) {
        fetch(`${serverUrl}/sip_students/default/api_get_user_email`, {
            method: 'GET',
            // body: JSON.stringify(formDTO),
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'no-cors'
        })
            .then(response => {
            if (!response) {
                throw new Error('La solicitud no fue exitosa');
            }
            return response.json(); // Convertir la respuesta a JSON
        })
            .then(data => {
            console.log(data); // Imprimir los datos en la consola
        })
            .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
    }
}
