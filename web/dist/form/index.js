import { FormFactory } from './FormFactory';
import { FormController } from './FormController';
import { FormRenderer } from './FormRenderer';
import { validators } from '@utils/validators';
const formInputs = [
    {
        type: 'text',
        name: 'fullname',
        label: 'Full name',
        placeholder: 'George',
        validators: [validators.required]
    },
    {
        type: 'text',
        name: 'lastnames',
        label: 'Last names',
        placeholder: 'Washington',
        validators: [validators.required]
    },
    {
        type: 'date',
        name: 'birth_date',
        label: 'Birth date',
        validators: [validators.required]
    },
    {
        type: 'text',
        name: 'id_number',
        label: 'Id number',
        placeholder: '123456789',
        validators: [validators.required]
    },
    {
        type: 'text',
        name: 'phone',
        label: 'Phone number',
        placeholder: '123456789',
        validators: [validators.phone]
    },
];
const url = '';
const form = FormFactory.createForm(formInputs, 'POST', url, FormController.submitForm);
FormRenderer.renderForm(form, 'form-container');
