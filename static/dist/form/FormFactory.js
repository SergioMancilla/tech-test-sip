import { Form } from './Form.js';
export class FormFactory {
    static createForm(inputs, method, action, onSubmit, title) {
        return new Form(inputs, method, action, onSubmit, title);
    }
}
