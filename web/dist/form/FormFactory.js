import { Form } from './Form';
export class FormFactory {
    static createForm(inputs, method, action, onSubmit) {
        return new Form(inputs, method, action, onSubmit);
    }
}
