import { FormFactory } from './FormFactory.js';
import { FormController } from './FormController.js';
import { FormRenderer } from './FormRenderer.js';
import { validators } from '../utils/validators.js';
export const studentFormInputs = [
    {
        id: 'name-input',
        type: 'text',
        name: 'fullname',
        label: 'Full name',
        placeholder: 'George',
        validators: [validators.required],
        value: ''
    },
    {
        id: 'lastname-input',
        type: 'text',
        name: 'lastnames',
        label: 'Last names',
        placeholder: 'Washington',
        validators: [validators.required],
        value: ''
    },
    {
        id: 'date-input',
        type: 'date',
        name: 'birth_date',
        label: 'Birth date',
        validators: [validators.required, validators.beforeToday],
        value: ''
    },
    {
        id: 'id_number-input',
        type: 'text',
        name: 'id_number',
        label: 'Id number',
        placeholder: '123456789',
        validators: [validators.required],
        value: ''
    },
    {
        id: 'phone-input',
        type: 'text',
        name: 'phone',
        label: 'Phone number',
        placeholder: '123456789',
        validators: [validators.required, validators.phone],
        value: ''
    },
];
export function makeRegisterStudentsForm() {
    const url = '';
    const form = FormFactory.createForm(studentFormInputs, 'POST', url, FormController.submitForm, 'Register student');
    FormRenderer.renderForm(form, 'form-container');
}
makeRegisterStudentsForm();
