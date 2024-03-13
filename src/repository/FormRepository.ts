import { serverUrl } from '../config.js'

export class FormRepository {
    static registerStudent (formDTO: { [key: string]: string }) {

        fetch(`${serverUrl}/sip_students/students/save_student`, {
            method: 'POST',
            body: JSON.stringify(formDTO),
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'no-cors'
        })
        .then(response => {
            if (!response) {
                throw new Error('La solicitud no fue exitosa');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.log(error)
            console.error('Error al obtener los datos:');
        });

    }
}