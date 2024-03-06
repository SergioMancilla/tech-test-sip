import { Form, Input, Method, SubmitAction  } from './Form.js'

export class FormFactory {
    static createForm(inputs: Input[], method: Method, action: string, onSubmit: SubmitAction, title?: string): Form {
        return new Form(inputs, method, action, onSubmit, title)
    }
}