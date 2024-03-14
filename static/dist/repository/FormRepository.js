import { serverUrl } from '../config.js';
export class FormRepository {
    static registerStudent(formDTO) {
        return new Promise((resolve, reject) => {
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
                if (data['status'] === 'success') {
                    resolve(true);
                }
                else {
                    resolve(false);
                }
            })
                .catch(error => {
                console.error('Error al obtener los datos:');
                console.log(error);
                reject(error);
            });
        });
    }
}
