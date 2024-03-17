import { FormFactory } from './factory/FormFactory.js';
import { FormController } from './controllers/FormController.js';
import { FormRenderer } from './renderer/FormRenderer.js';
import { validators } from './utils/validators.js';
export const studentFormInputs = [
    {
        id: 'name-input',
        type: 'text',
        name: 'fullname',
        label: 'Full name',
        placeholder: 'George',
        validators: [validators.required]
    },
    {
        id: 'lastname-input',
        type: 'text',
        name: 'lastnames',
        label: 'Last names',
        placeholder: 'Washington',
        validators: [validators.required]
    },
    {
        id: 'date-input',
        type: 'date',
        name: 'birth_date',
        label: 'Birth date',
        validators: [validators.required, validators.beforeToday]
    },
    {
        id: 'id_number-input',
        type: 'text',
        name: 'id_number',
        label: 'Id number',
        placeholder: '123456789',
        validators: [validators.required]
    },
    {
        id: 'phone-input',
        type: 'text',
        name: 'phone',
        label: 'Phone number',
        placeholder: '123456789',
        validators: [validators.required, validators.phone]
    },
];
export function makeRegisterStudentsForm() {
    const url = '';
    const form = FormFactory.createForm(studentFormInputs, 'POST', url, FormController.submitForm, 'Register student');
    FormRenderer.renderForm(form, 'form-container');
}
makeRegisterStudentsForm();
