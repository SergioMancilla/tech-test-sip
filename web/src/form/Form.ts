export interface Input {
    type: string
    name: string
    label: string
    placeholder?: string
    title?: string
    value?: string
    validators: Validator[]
}

type InputForValidate = Required<Pick<Input, 'value' | 'validators'>>

type Validator = (value: string) => boolean
export type SubmitAction = () => void
export type Method = 'GET' | 'POST'

export class Form {
    #inputs: Input[]
    #method: Method
    #action: string
    #onSubmit: SubmitAction
    
    constructor (inputs: Input[], method: Method, action: string, onSubmit: SubmitAction) {
        this.#inputs = inputs
        this.#method = method
        this.#action = action
        this.#onSubmit = onSubmit
    }

    validateForm (newInputs: InputForValidate[]): boolean {
        return newInputs.every(({ value, validators }) => {
            validators.every((validator) => validator(value))
        })
    }

    getInputs (): Input[] {
        return this.#inputs
    }

    getMethod (): Method {
        return this.#method
    }

    getAction (): string {
        return this.#action
    }

    getSubitAction (): SubmitAction {
        return this.#onSubmit
    }
}
