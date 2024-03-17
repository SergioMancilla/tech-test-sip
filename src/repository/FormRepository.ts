import { serverUrl } from '../config.js'

export class FormRepository {
    static registerStudent (formDTO: { [key: string]: string }): Promise<{success: boolean, msg: string}> {

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
                    throw new Error('The request was not successfull');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                if (data['status']  === 'success') {
                    resolve({success: true, msg: data['msg']})
                } else {
                    resolve({success: false, msg: data['msg']})
                }
            })
            .catch(error => {
                console.error('Error al obtener los datos:');
                console.log(error)
                reject(error)
            });

        })
    }
}