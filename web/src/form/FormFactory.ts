import { Form, Input, Method, SubmitAction  } from './Form'

export class FormFactory {
    static createForm(inputs: Input[], method: Method, action: string, onSubmit: SubmitAction): Form {
        return new Form(inputs, method, action, onSubmit)
    }
}